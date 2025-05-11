@echo off
setlocal ENABLEDELAYEDEXPANSION

REM === Vérification de Python ===
where python >nul 2>&1
if %errorlevel% NEQ 0 (
    echo ❌ Python non détecté. Installe-le depuis https://www.python.org/
    pause
    exit /b
)

REM Vérification de la version de Python
python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo ❌ Python semble installé, mais il ne fonctionne pas correctement.
    pause
    exit /b
)

REM === Installation des dépendances ===
set "DEPENDANCES=pyperclip pywin32"

for %%d in (%DEPENDANCES%) do (
    python -m pip show %%d >nul 2>&1
    if !errorlevel! NEQ 0 (
        echo ⏳ Installation de %%d...
        python -m pip install %%d
        if !errorlevel! NEQ 0 (
            echo ❌ Échec de l'installation de %%d !
            pause
            exit /b
        )
    )
)

REM === Exécution du script Python ===
start "" pythonw.exe "%~dp0main.py"

endlocal
pause