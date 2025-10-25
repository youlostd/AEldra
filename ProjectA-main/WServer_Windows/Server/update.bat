@echo off
@echo Windows Server
@echo Deletando logs...

@echo off
@echo Updating Cores...
echo f | xcopy /f /y E:\Aeldra\WServer_Windows\Server\ch1\core1\game.exe E:\Aeldra\WServer_Windows\Server\auth\game.exe
echo f | xcopy /f /y E:\Aeldra\WServer_Windows\Server\ch1\core1\game.exe E:\Aeldra\WServer_Windows\Server\ch1\processor\game.exe
REM echo f | xcopy /f /y E:\Aeldra\WServer_Windows\Server\ch1\core1\game.exe E:\Aeldra\WServer_Windows\Server\ch1\core2\game.exe
REM echo f | xcopy /f /y E:\Aeldra\WServer_Windows\Server\ch1\core1\game.exe E:\Aeldra\WServer_Windows\Server\ch99\game.exe

pause
exit
