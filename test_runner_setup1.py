# import shutil
# import subprocess
# import argparse
# import sys
# import os
#
# # Append the parent directory to sys.path
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)
#
# from Util_Factory.find_base_dir import find_base_dir
#
# # Argument parser for command-line arguments
# parser = argparse.ArgumentParser(description='Run Behave tests with optional feature file paths and tags.')
# parser.add_argument('params', type=str, nargs='*', help='Feature file paths and/or tags.')
# args, unknown_args = parser.parse_known_args()
#
# # Separate feature file paths and tags
# feature_paths = []
# tags = []
#
# for param in args.params:
#     if param.startswith('@'):
#         tags.append(param)
#     else:
#         feature_paths.append(param)
#
# # Default to 'features' directory if no feature paths are provided
# if not feature_paths:
#     feature_paths.append('features')
#
# # Define base paths
# base_dir = find_base_dir()
# # print("Base Directory:", base_dir)
# features_dir = os.path.join(base_dir, 'features')
# # print("Features Directory:", features_dir)  # Print the features directory for debugging
# util_factory_dir = os.path.join(base_dir, 'Util_Factory')
# # print("Util_Factory Directory:", util_factory_dir)  # Print the util_factory directory for debugging
# steps_dir = os.path.join(base_dir, 'steps')
#
# environment_file = os.path.join(util_factory_dir, 'environment.py')
# temporary_environment_file = os.path.join(features_dir, 'environment.py')
# temporary_steps_dir = os.path.join(features_dir, 'steps')
#
# # Ensure the features directory exists
# if not os.path.exists(features_dir):
#     os.makedirs(features_dir)
#
# # Copy environment.py to the features directory
# shutil.copy(environment_file, temporary_environment_file)
#
# # Copy the steps directory to the temporary steps directory within the features directory
# if os.path.exists(steps_dir):
#     if not os.path.exists(temporary_steps_dir):
#         shutil.copytree(steps_dir, temporary_steps_dir)
#
# os.environ['PYTHONPATH'] = f"{base_dir};{util_factory_dir};{steps_dir}"
#
# # Construct the Behave command
# behave_command = ['behave']
# behave_command.extend(['-f', 'allure_behave.formatter:AllureFormatter', '-o', f'{base_dir}/test-results/allure-report'
#                                                                               f'-json/'])
#
# if feature_paths:
#     behave_command.extend(feature_paths)
# if tags:
#     behave_command.append('--tags')
#     behave_command.append(' , '.join(tags))
#
# # Add any additional unknown arguments (such as formatter and output directory)
# behave_command.extend(unknown_args)
# print("Executing Behave command:", behave_command)
#
# # Run Behave
# result = subprocess.run(behave_command, cwd=base_dir)
#
# # Clean up temporary files
# if os.path.exists(temporary_environment_file):
#     os.remove(temporary_environment_file)
#
# if os.path.exists(temporary_steps_dir):
#     shutil.rmtree(temporary_steps_dir)
#
# # Exit with the same code as the Behave command
# sys.exit(result.returncode)
