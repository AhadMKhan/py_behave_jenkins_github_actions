# import subprocess
# import logging
# from concurrent.futures import ThreadPoolExecutor
#
# logger = logging.getLogger(__name__)
#
#
# def run_behave_command(behave_command, base_dir):
#     """
#     Executes the Behave command in a subprocess.
#     Args:
#         behave_command (list): The Behave command to execute.
#         base_dir (str): The base directory from which to execute the command.
#     Returns:
#         int: The return code of the subprocess.
#     """
#     logger.info("Executing Behave command: %s", behave_command)
#     result = subprocess.run(behave_command, cwd=base_dir)
#     return result.returncode
#
#
# def run_behave_parallel(behave_command, base_dir, num_threads):
#     """
#     Executes Behave tests in parallel using ThreadPoolExecutor.
#     Args:
#         behave_command (list): The Behave command to execute.
#         base_dir (str): The base directory from which to execute the command.
#         num_threads (int): Number of threads to use for parallel execution.
#     Returns:
#         int: The return code of the Behave command with the highest return code.
#     """
#     with ThreadPoolExecutor(max_workers=num_threads) as executor:
#         futures = [executor.submit(run_behave_command, behave_command, base_dir) for _ in range(num_threads)]
#
#         # Wait for all tasks to complete
#         results = [future.result() for future in futures]
#
#         return max(results)
