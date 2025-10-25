    cd /d "%~dp0db"
    start db.exe
    timeout /t 15 /nobreak > nul
    cd /d "%~dp0auth"
    start game.exe
    timeout /t 4 /nobreak > nul
    cd /d "%~dp0ch1\processor"
    start game.exe
    timeout /t 10 /nobreak > nul
    cd /d "%~dp0ch1\core1"
    start game.exe
REM    timeout /t 4 /nobreak > nul
REM    cd /d D:\Games\Metin2\Aeldra\WServer_Windows\Server\ch99
REM    start game.exe