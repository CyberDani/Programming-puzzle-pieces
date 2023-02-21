@echo off
set "command=notfound"
WHERE py
IF %ERRORLEVEL% EQU 0 > nul 2>&1 (
	set "command=py"
)
WHERE python
IF %ERRORLEVEL% EQU 0 > nul 2>&1 (
	set "command=python"
)
IF "%command%" == "notfound" (
	@echo on
	echo error:python command not found
) Else (
	@echo on
	echo Start http local server
	"%command%" -m http.server 9499
)