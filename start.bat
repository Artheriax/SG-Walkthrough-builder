@echo off
setlocal EnableExtensions

cd /d "%~dp0"

set "VENV_DIR=.venv"
set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

if not exist "%VENV_PY%" (
	echo Creating virtual environment in "%VENV_DIR%"...

	where py >nul 2>&1
	if not errorlevel 1 (
		set "BASE_PYTHON=py -3"
	) else (
		where python >nul 2>&1
		if not errorlevel 1 (
			set "BASE_PYTHON=python"
		) else (
			echo.
			echo Could not find Python. Install Python 3 and ensure "py" or "python" is on PATH.
			exit /b 1
		)
	)

	%BASE_PYTHON% -m venv "%VENV_DIR%"
	if errorlevel 1 (
		echo.
		echo Failed to create virtual environment.
		exit /b 1
	)
)

if not exist "%VENV_PY%" (
	echo.
	echo Virtual environment python not found at "%VENV_PY%".
	exit /b 1
)

echo Installing dependencies...
"%VENV_PY%" -m pip install --upgrade pip
if errorlevel 1 (
	echo.
	echo Failed to upgrade pip.
	exit /b 1
)

if exist "requirements.txt" (
	"%VENV_PY%" -m pip install -r requirements.txt
	if errorlevel 1 (
		echo.
		echo Failed to install requirements.
		exit /b 1
	)
) else (
	echo requirements.txt not found. Skipping dependency install.
)

echo Starting Walkthrough Builder...
"%VENV_PY%" app.py
if errorlevel 1 (
	echo.
	echo App exited with an error.
	exit /b 1
)

endlocal