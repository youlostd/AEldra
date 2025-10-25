cd /D "%~dp0"

cd auth
mklink /D data ..\share\data
mklink /D locale ..\share\locale
mklink /D log ..\logs\auth
mklink /D mark ..\share\mark
mklink /D package ..\share\package
mklink /D public ..\share\public

cd ../db
mklink /D log ..\logs\db
mklink /D locale ..\share\locale

cd ../ch1/core1
mklink /D data ..\..\share\data
mklink /D locale ..\..\share\locale
mklink /D log ..\..\logs\ch1\core1
mklink /D mark ..\..\share\mark
mklink /D package ..\..\share\package
mklink /D public ..\..\share\public

cd ../core2
mklink /D data ..\..\share\data
mklink /D locale ..\..\share\locale
mklink /D log ..\..\logs\ch1\core2
mklink /D mark ..\..\share\mark
mklink /D package ..\..\share\package

cd ../core3
mklink /D data ..\..\share\data
mklink /D locale ..\..\share\locale
mklink /D log ..\..\logs\ch1\core3
mklink /D mark ..\..\share\mark
mklink /D package ..\..\share\package

cd ../processor
mklink /D data ..\..\share\data
mklink /D locale ..\..\share\locale
mklink /D log ..\..\logs\ch1\processor
mklink /D mark ..\..\share\mark
mklink /D package ..\..\share\package

cd ../../ch99
mklink /D data ..\share\data
mklink /D locale ..\share\locale
mklink /D log ..\logs\ch99
mklink /D mark ..\share\mark
mklink /D package ..\share\package

pause