# import subprocess
# import argparse
# import sys
# import os
# import logging
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# def test_runner_setup():
#     # Append the parent directory to sys.path
#     parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#     sys.path.append(parent_dir)
#
#     # Import necessary functions from dir_configurations.setup_directories
#     from dir_configurations.setup_directories import setup_directories, validate_feature_paths, cleanup, find_base_dir
#
#     # Get the current directory
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#
#     # Argument parser for command-line arguments
#     parser = argparse.ArgumentParser(description='Run Behave tests with optional feature file paths and tags.')
#     parser.add_argument('params', type=str, nargs='*', help='Feature file paths and/or tags.')
#     args, unknown_args = parser.parse_known_args()
#
#     # Separate feature file paths and tags
#     feature_paths = []
#     tags = []
#
#     for param in args.params:
#         if param.startswith('@'):
#             tags.append(param)
#         else:
#             feature_paths.append(param)
#
#     # Default to 'features' directory if no feature paths are provided
#     if not feature_paths:
#         feature_paths.append('features')
#
#     # Define base path using the current directory
#     base_dir = find_base_dir(current_dir)
#     util_factory_dir = os.path.join(base_dir, 'Util_Factory')
#     steps_dir = os.path.join(base_dir, 'steps')
#
#     # Validate feature paths
#     validate_feature_paths(feature_paths, base_dir)
#
#     # Setup directories
#     temporary_environment_file, temporary_steps_dir = setup_directories(base_dir, util_factory_dir, steps_dir)
#
#     os.environ['PYTHONPATH'] = f"{base_dir}{os.pathsep}{util_factory_dir}{os.pathsep}{steps_dir}"
#
#     # Construct the Behave command
#     behave_command = ['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o',
#                       f'{base_dir}/test-results/allure-report-json/']
#     if feature_paths:
#         behave_command.extend(feature_paths)
#     if tags:
#         behave_command.append('--tags')
#         behave_command.append(' , '.join(tags))
#
#     # Add any additional unknown arguments (such as formatter and output directory)
#     behave_command.extend(unknown_args)
#     logger.info("Executing Behave command: %s", behave_command)
#
#     # Run Behave
#     result = subprocess.run(behave_command, cwd=base_dir)
#
#     # Clean up temporary files
#     cleanup(temporary_environment_file, temporary_steps_dir)
#
#     # Exit with the same code as the Behave command
#     sys.exit(result.returncode)
#
#
# if __name__ == "__main__":
#     test_runner_setup()
