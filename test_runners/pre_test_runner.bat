@echo off

cd ..
REM Clean the Allure reports directory
if exist test-results rmdir /S /Q test-results

cd test_runners
REM Check if any arguments are provided
set "ARGS=%*"
if "%ARGS%"=="" (
    REM Get the directory of the current script
    set "SCRIPT_DIR=%~dp0"

    REM Debugging: Print the resolved base directory and script paths
    echo SCRIPT_DIR=%SCRIPT_DIR%

    REM No arguments provided, run Behave with default options
    python "%SCRIPT_DIR%\test_runner_setup.py"
) else (
    REM Arguments provided, pass them to run_behave.py
    python "%SCRIPT_DIR%\test_runner_setup.py" %ARGS%
)

REM Generate the HTML report
cd ..
allure generate test-results/allure-report-json/ -o test-results/allure-report/ --report-name "cTest Result" --clean