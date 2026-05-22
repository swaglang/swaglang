@echo off
if "%~2"=="" (
    for %%F in (%1) do python "%~dp0main.py" %1 --out "%%~nF.exe"
) else (
    python "%~dp0main.py" %1 --out %2
)
