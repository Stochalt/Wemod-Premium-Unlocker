@echo off
cls


title WeMod Pro Unlocker - Automated Installer


color 0A


echo ==========================================================
echo              WeMod Pro Unlocker - Automated Setup
echo                          By Hira
echo ==========================================================
echo.
ping 127.0.0.1 -n 3 >nul

echo Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python is not installed. Please install Python and try again.
    echo ==========================================================
    ping 127.0.0.1 -n 3 >nul
    exit /b
)


color 0B
echo [INFO] Preparing to install required Python modules...
echo ==========================================================
ping 127.0.0.1 -n 3 >nul


echo [INFO] Upgrading pip to the latest version...
python -m pip install --upgrade pip >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to upgrade pip. Please check your internet connection or pip installation.
    echo ==========================================================
    ping 127.0.0.1 -n 3 >nul
    exit /b
)


echo [INFO] Installing required Python modules: colorama, tqdm, yaspin, and rich...
python -m pip install colorama tqdm yaspin rich >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to install Python modules. Please check your pip configuration or internet connection.
    echo ==========================================================
    ping 127.0.0.1 -n 3 >nul
    exit /b
)


color 0A
echo [SUCCESS] Required Python modules have been successfully installed!
echo ==========================================================
ping 127.0.0.1 -n 3 >nul


color 0E
echo [INFO] All necessary modules are installed and up to date.
echo Preparing to launch WeMod Pro Unlocker...
echo ==========================================================
ping 127.0.0.1 -n 3 >nul


cls
echo Launching WeMod Pro Unlocker...
python Wemod_ProUnlocker.py


if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to launch WeMod Pro Unlocker.
    echo ==========================================================
    ping 127.0.0.1 -n 3 >nul
    exit /b
)


color 0A
echo [SUCCESS] WeMod Pro Unlocker completed successfully!
echo ==========================================================
ping 127.0.0.1 -n 3 >nul
echo.
echo [INFO] Press any key to close this window...
pause >nul
