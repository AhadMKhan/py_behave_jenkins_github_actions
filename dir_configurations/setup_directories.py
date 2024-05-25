import shutil
import os
import sys
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_base_dir() -> str:
    """
    Finds the base directory of the project by traversing upwards from the current directory.
    Returns the outermost directory with no parent directory.
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        raise FileNotFoundError("The __file__ attribute is not available. Cannot determine the base directory.")

    logger.info("Checking Current directory: %s", current_dir)

    while True:
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            raise FileNotFoundError("Project base directory not found.")
        if os.path.basename(parent_dir) == '':
            return current_dir  # Return the outermost directory
        current_dir = parent_dir
        logger.info("Set to Base directory: %s", current_dir)


def validate_feature_paths(feature_paths: List[str], base_dir: str) -> None:
    """
    Validates the existence of feature paths relative to the base directory.
    Exits the program if any of the paths do not exist.
    """
    invalid_paths = [path for path in feature_paths if not os.path.exists(os.path.join(base_dir, path))]
    if invalid_paths:
        logger.error("The following feature file paths do not exist: %s", ', '.join(invalid_paths))
        sys.exit(1)


def setup_directories(base_dir: str, util_factory_dir: str, steps_dir: str) -> Tuple[str, str]:
    """
    Sets up the necessary directories and copies required files for the test environment.
    Returns the paths of the temporary environment file and steps directory.
    """
    features_dir = os.path.join(base_dir, 'features')
    os.makedirs(features_dir, exist_ok=True)

    environment_file = os.path.join(util_factory_dir, 'environment.py')
    temporary_environment_file = os.path.join(features_dir, 'environment.py')

    try:
        shutil.copy(environment_file, temporary_environment_file)
    except FileNotFoundError:
        logger.error("Environment file not found: %s", environment_file)
        sys.exit(1)
    except IOError as e:
        logger.error("Error copying environment file: %s", e)
        sys.exit(1)

    temporary_steps_dir = os.path.join(features_dir, 'steps')
    if os.path.exists(steps_dir):
        try:
            if not os.path.exists(temporary_steps_dir):
                shutil.copytree(steps_dir, temporary_steps_dir)
        except FileNotFoundError:
            logger.error("Steps directory not found: %s", steps_dir)
            sys.exit(1)
        except IOError as e:
            logger.error("Error copying steps directory: %s", e)
            sys.exit(1)

    return temporary_environment_file, temporary_steps_dir


def cleanup(temporary_environment_file: str, temporary_steps_dir: str) -> None:
    """
    Cleans up the temporary environment file and steps directory.
    """
    try:
        if os.path.exists(temporary_environment_file):
            os.remove(temporary_environment_file)
        if os.path.exists(temporary_steps_dir):
            shutil.rmtree(temporary_steps_dir)
    except IOError as e:
        logger.error("Error during cleanup: %s", e)


# Example usage of functions (uncomment to use in a script)
# base_dir = find_base_dir()
# feature_paths = ['path/to/feature1', 'path/to/feature2']
# validate_feature_paths(feature_paths, base_dir)
# temporary_environment_file, temporary_steps_dir = setup_directories(base_dir, 'path/to/util_factory', 'path/to/steps')
# cleanup(temporary_environment_file, temporary_steps_dir)
