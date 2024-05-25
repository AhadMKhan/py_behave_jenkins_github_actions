@echo off

cd ..
REM Clean the Allure reports directory
if exist test-results rmdir /S /Q test-results

cd test_runners
REM Check if any arguments are provided
set "ARGS=%*"
if "%ARGS%"=="" (
    REM No arguments provided, run Behave with default options
    python test_runner_setup.py
) else (
    REM Arguments provided, pass them to run_behave.py
    python test_runner_setup.py %ARGS%
)

REM Generate the HTML report
cd ..
.\allure-2.29.0\bin\allure generate test-results/allure-report-json/ -o test-results/allure-report/ --report-name "cTest Result" --clean