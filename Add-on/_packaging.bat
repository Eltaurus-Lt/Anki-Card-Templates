@echo off

set zipped="temp.zip"
set "script_name=%~nx0"
set "script_path=%~dp0"

:: remove garbage
if exist "__pycache__" rd /s /q "__pycache__"
REM if exist "meta.json" del /f /q "meta.json"
if exist "%zipped%" del /f /q "%zipped%"
if exist "%~dp0*.ankiaddon" del "%~dp0*.ankiaddon" /q

dir /b "%script_path%" | findstr /v /i "%script_name% __pycache__ meta.json %zipped%"' | tar -caf %zipped% --files-from -

python -c "import os, sys; script_path = sys.argv[1].strip('\"'); os.rename(os.path.join(script_path, 'temp.zip'), os.path.join(script_path, 'temp.ankiaddon'))" "%script_path%"