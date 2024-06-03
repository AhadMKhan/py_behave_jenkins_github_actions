import subprocess
import argparse
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Append the parent directory to sys.path
parent_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)  # pylint: disable=W0621
sys.path.append(parent_dir)

# Import necessary functions from dir_configurations.setup_directories
from dir_configurations.setup_directories import (
    SetupDirectories,
)  # pylint: disable=C0413


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run Behave tests with optional feature file paths and tags."
    )
    parser.add_argument(
        "params", type=str, nargs="*", help="Feature file paths and/or tags."
    )
    return parser.parse_known_args()


def setup_environment(current_dir):
    """Setup environment paths and directories."""
    base_dir = SetupDirectories.find_base_dir(current_dir)
    util_factory_dir = os.path.join(base_dir, "Util_Factory")
    steps_dir = os.path.join(base_dir, "steps")
    os.environ["PYTHONPATH"] = (
        f"{base_dir}{os.pathsep}{util_factory_dir}{os.pathsep}{steps_dir}"
    )
    return base_dir, util_factory_dir, steps_dir


def run_behave(base_dir, feature_paths, tags, unknown_args):
    """Run Behave tests with the specified parameters."""
    behave_command = [
        "behave",
        "-f",
        "allure_behave.formatter:AllureFormatter",
        "-o",
        f"{base_dir}/test-results/allure-report-json/",
    ]
    if feature_paths:
        behave_command.extend(feature_paths)
    if tags:
        behave_command.append("--tags")
        behave_command.append(" , ".join(tags))
    behave_command.extend(unknown_args)

    logger.info("Executing Behave command: %s", behave_command)
    result = subprocess.run(
        behave_command, cwd=base_dir, check=True
    )  # Add check=True to handle errors
    return result.returncode


def test_runner_setup():
    # Append the parent directory to sys.path
    sys.path.append(parent_dir)

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Parse arguments
    args, unknown_args = parse_arguments()

    # Separate feature file paths and tags
    feature_paths = [param for param in args.params if not param.startswith("@")]
    tags = [param for param in args.params if param.startswith("@")]

    # Default to 'features' directory if no feature paths are provided
    if not feature_paths:
        feature_paths.append("features")

    # Setup environment
    base_dir, util_factory_dir, steps_dir = setup_environment(current_dir)

    # Validate feature paths
    SetupDirectories.validate_feature_paths(feature_paths, base_dir)

    # Setup directories
    temporary_environment_file, temporary_steps_dir = (
        SetupDirectories.setup_directories(base_dir, util_factory_dir, steps_dir)
    )

    try:
        # Run Behave
        return_code = run_behave(base_dir, feature_paths, tags, unknown_args)
    finally:
        # Clean up temporary files
        SetupDirectories.cleanup(temporary_environment_file, temporary_steps_dir)

    # Exit with the same code as the Behave command
    sys.exit(return_code)


if __name__ == "__main__":
    test_runner_setup()
