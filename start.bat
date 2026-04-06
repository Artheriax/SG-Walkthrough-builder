@echo off
setlocal

cd /d "%~dp0"

python app.py
if errorlevel 1 (
	echo.
	echo Python was not found on PATH. Trying the Python launcher...
	py app.py
)

endlocal