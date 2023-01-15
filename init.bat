@echo off
set cwd=%cd%
setlocal EnableExtensions DisableDelayedExpansion
set "UserPath="
for /F "skip=2 tokens=1,2*" %%G in ('%SystemRoot%\System32\reg.exe query "HKCU\Environment" /v "Path" 2^>nul') do if /I "%%G" == "Path" (
    if /I "%%H" == "REG_EXPAND_SZ" (call set "UserPath=%%I") else if /I "%%H" == "REG_SZ" set "UserPath=%%I"
    if defined UserPath goto UserPathRead
)
echo User PATH is not defined or has no string value.
goto EndBatch

:UserPathRead
setlocal EnableDelayedExpansion
if not exist "C:/Users/%USERNAME%/aem" mkdir "C:/Users/%USERNAME%/aem"
if not exist "%cwd%\aem\modules" mkdir "%cwd%\aem\modules"
if not exist "%cwd%\aem\templates" mkdir "%cwd%\aem\templates"
xcopy /s /i /Y "%cwd%\templates\*.*"  "%cwd%\aem\templates"
xcopy /s /i /Y "%cwd%\modules\*.*"  "%cwd%\aem\modules"
xcopy /s /Y "%cwd%\to_user_folder.bat"  "%cwd%\aem\to_user_folder.bat"
xcopy /s /i /Y "%cwd%\aem\*.*"  "C:/Users/%USERNAME%/aem"
aem.exe 2> NUL
set erlev=%ERRORLEVEL%
if %erlev%==9009 setx path "%UserPath%;C:/Users/%USERNAME%/aem"
endlocal
:EndBatch