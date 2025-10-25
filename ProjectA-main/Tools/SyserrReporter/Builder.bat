set PYTHONOPTIMIZE=1
pyinstaller ^
	    --onefile ^
	    --name=SyserrReporter ^
		--noconfirm ^
SyserrReporter.spec
