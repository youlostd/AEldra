    cd /d E:\Aeldra\WServer_Windows\Server\db
    start db.exe
    timeout /t 15 /nobreak > nul
    cd /d E:\Aeldra\WServer_Windows\Server\auth
    start game.exe
    timeout /t 4 /nobreak > nul
    cd /d E:\Aeldra\WServer_Windows\Server\ch1\processor
    start game.exe
    timeout /t 10 /nobreak > nul
    cd /d E:\Aeldra\WServer_Windows\Server\ch1\core1
    start game.exe
REM    timeout /t 4 /nobreak > nul
REM    cd /d E:\Aeldra\WServer_Windows\Server\ch99
REM    start game.exe