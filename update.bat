@echo off
rmdir /s /q "C:/Users/%USERNAME%/aem/modules" > nul
rmdir /s /q "C:/Users/%USERNAME%/aem/templates" > nul
set cwd=%cd%
if not exist "%cwd%\aem\modules" mkdir "C:\Users\%USERNAME%\aem\modules"
if not exist "%cwd%\aem\templates" mkdir "C:\Users\%USERNAME%\aem\templates"
xcopy /s /i /Y "%cwd%\templates\*.*"  "C:\Users\%USERNAME%\aem\templates" > nul
xcopy /s /i /Y "%cwd%\modules\*.*"  "C:\Users\%USERNAME%\aem\modules" > nul