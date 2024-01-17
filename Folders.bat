@echo off
setlocal

REM Set the directory where the script is executed as the current directory
cd /d "%~dp0"

REM Set the output file name and path
set "outputFile=%~dp0folder_names.csv"

REM List all the folders in the current directory and save them to the CSV file
dir /ad /b > "%outputFile%"

echo CSV file created: "%outputFile%"

endlocal
