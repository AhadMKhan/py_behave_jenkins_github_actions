import shutil
import subprocess
import argparse
import sys
import os
import logging
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add parent directory to sys.path

from dir_configurations.setup_directories import setup_directories, validate_feature_paths, cleanup, find_base_dir
from Util_Factory.readers import get_yaml_property

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_behave_command(behave_command, base_dir):
    """
    Executes the Behave command in a subprocess.
    Args:
        behave_command (list): The Behave command to execute.
        base_dir (str): The base directory from which to execute the command.
    Returns:
        int: The return code of the subprocess.
    """
    logger.info("Executing Behave command: %s", behave_command)
    result = subprocess.run(behave_command, cwd=base_dir)
    return result.returncode


def test_runner_setup():
    """
    Sets up and runs Behave tests, either sequentially or in parallel based on configuration.
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Argument parser for command-line arguments
    parser = argparse.ArgumentParser(description='Run Behave tests with optional feature file paths and tags.')
    parser.add_argument('params', type=str, nargs='*', help='Feature file paths and/or tags.')
    args, unknown_args = parser.parse_known_args()

    # Separate feature file paths and tags
    feature_paths = []
    tags = []

    for param in args.params:
        if param.startswith('@'):
            tags.append(param)
        else:
            feature_paths.append(param)

    # Default to 'features' directory if no feature paths are provided
    if not feature_paths:
        feature_paths.append('features')

    # Define base path using the current directory
    base_dir = find_base_dir(current_dir)
    util_factory_dir = os.path.join(base_dir, 'Util_Factory')
    steps_dir = os.path.join(base_dir, 'steps')

    # Validate feature paths
    validate_feature_paths(feature_paths, base_dir)

    # Setup directories
    temporary_environment_file, temporary_steps_dir = setup_directories(base_dir, util_factory_dir, steps_dir)

    os.environ['PYTHONPATH'] = f"{base_dir}{os.pathsep}{util_factory_dir}{os.pathsep}{steps_dir}"

    # Read parallel property from env.yaml
    environment_file_path = "../configuration/environment_config.yaml"
    parallel = get_yaml_property(environment_file_path, "parallel")
    if parallel is None:
        parallel = False  # Set default value if not provided

    if parallel:
        # Determine the number of threads to use (dynamic)
        num_threads = os.cpu_count() or 1  # Default to 1 if CPU count cannot be determined

        # Construct the Behave command
        behave_command = ['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o',
                          f'{base_dir}/test-results/allure-report-json/']
        if feature_paths:
            behave_command.extend(feature_paths)
        if tags:
            behave_command.append('--tags')
            behave_command.append(' , '.join(tags))

        # Add any additional unknown arguments (such as formatter and output directory)
        behave_command.extend(unknown_args)

        # Run Behave in parallel
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for _ in range(num_threads):
                future = executor.submit(run_behave_command, behave_command, base_dir)
                futures.append(future)

            # Wait for all tasks to complete
            results = [future.result() for future in futures]

            # Clean up temporary files
            cleanup(temporary_environment_file, temporary_steps_dir)

            # Exit with the same code as the Behave command with the highest return code
            sys.exit(max(results))
    else:
        # Construct the Behave command
        behave_command = ['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o',
                          f'{base_dir}/test-results/allure-report-json/']
        if feature_paths:
            behave_command.extend(feature_paths)
        if tags:
            behave_command.append('--tags')
            behave_command.append(' , '.join(tags))

        # Add any additional unknown arguments (such as formatter and output directory)
        behave_command.extend(unknown_args)

        # Run Behave sequentially
        result = subprocess.run(behave_command, cwd=base_dir)

        # Clean up temporary files
        cleanup(temporary_environment_file, temporary_steps_dir)

        # Exit with the same code as the Behave command
        sys.exit(result.returncode)


if __name__ == "__main__":
    test_runner_setup()