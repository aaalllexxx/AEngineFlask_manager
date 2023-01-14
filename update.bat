@echo off
xcopy /s /i /Y /C "%cd%\aem\*.*"  "C:/Users/%USERNAME%/aem"
echo updated.