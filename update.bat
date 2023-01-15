@echo off
rmdir "C:/Users/%USERNAME%/aem"
xcopy /s /i /Y /C "%cd%\aem"  "C:/Users/%USERNAME%/aem"