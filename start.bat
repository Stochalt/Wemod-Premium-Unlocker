@echo off
cls

title WeMod Pro Unlocker - Automated Installer

color 0A

echo ##########################################################
echo #                                                        #
echo #                      AUTO SETUP                        #
echo #                                                        #
echo #                       By Hira                          #
echo ##########################################################
echo.
call :wait

echo Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python is not installed. Please install Python and try again.
    echo ==========================================================
    call :wait
    exit /b
)

color 0B
echo.
echo [INFO] Preparing to install required Python modules...
echo ==========================================================
call :wait

echo [INFO] Upgrading pip to the latest version...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to upgrade pip. Please check your internet connection or pip installation.
    echo ==========================================================
    call :wait
    exit /b
)

echo.
echo [INFO] Installing required Python modules:
echo          - colorama
echo          - tqdm
echo          - yaspin
echo          - rich
echo ==========================================================
python -m pip install colorama tqdm yaspin rich
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to install Python modules. Please check your pip configuration or internet connection.
    echo ==========================================================
    call :wait
    exit /b
)

color 0A
echo.
echo [SUCCESS] Required Python modules have been successfully installed!
echo ==========================================================
call :wait

if not exist Wemod_ProUnlocker.py (
    color 0C
    echo [ERROR] Wemod_ProUnlocker.py n'a pas été trouvé dans le répertoire actuel.
    echo ==========================================================
    call :wait
    exit /b
)

color 0E
echo.
echo [INFO] All necessary modules are installed and up to date.
echo Preparing to launch WeMod Pro Unlocker...
echo ==========================================================
call :wait

cls
echo Launching WeMod Pro Unlocker...
python Wemod_ProUnlocker.py
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to launch WeMod Pro Unlocker.
    echo ==========================================================
    call :wait
    exit /b
)

color 0A
echo.
echo [SUCCESS] WeMod Pro Unlocker completed successfully!
echo ==========================================================
call :wait
echo.
echo [INFO] Press any key to close this window...
pause >nul
exit /b

:wait
ping 127.0.0.1 -n 3 >nul
goto :eof
