@echo off

REM Call the run_test.bat script
call pre_test_runner.bat %*

REM Check if index.html exists before renaming
if exist "test-results\allure-report\index.html" (
    ren "test-results\allure-report\index.html" "Automation Test Execution Report.html"
)

REM Prompt user to press any key before exiting
cd test_runners
echo Allure report generation completed. Press any key to exit.