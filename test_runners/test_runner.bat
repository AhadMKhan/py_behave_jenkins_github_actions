@echo off

REM Get the directory of the current script
set "SCRIPT_DIR=%~dp0"

REM Get the directory of the current script
set "SCRIPT_DIR=%~dp0"

REM Debugging: Print the resolved base directory and script paths
echo SCRIPT_DIR=%SCRIPT_DIR%
echo Calling: %SCRIPT_DIR%\pre_test_runner.bat %*

REM Call the pre_test_runner.bat script using the dynamic base directory
call "%SCRIPT_DIR%\pre_test_runner.bat" %*

REM Check if index.html exists before renaming
if exist "test-results\allure-report\index.html" (
    ren "test-results\allure-report\index.html" "Automation Test Execution Report.html"
)

REM Prompt user to press any key before exiting
cd test_runners
echo Allure report generation completed. Press any key to exit.