@echo off
rmdir /s "C:/Users/%USERNAME%/aem"
if not exist "C:/Users/%USERNAME%/aem" mkdir "C:/Users/%USERNAME%/aem"
xcopy /s /i /Y /C "%cd%\aem\*.*"  "C:/Users/%USERNAME%/aem"