SET startup_dile_dir="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\update_slipsys.bat"
SET desktop_bat=%USERPROFILE%\DeskTop\StartApp.bat

ECHO mkdir C:\work_space > %startup_dile_dir%
ECHO cd C:\work_space >> %startup_dile_dir%
ECHO if exist C:\work_space\SlipSys ( >> %startup_dile_dir%
ECHO     cd SlipSys >> %startup_dile_dir%
ECHO     git pull >> %startup_dile_dir%
ECHO ) else ( >> %startup_dile_dir%
ECHO     git clone https://github.com/ardnico/SlipSys >> %startup_dile_dir%
ECHO ) >> %startup_dile_dir%
ECHO ECHO cd C:\work_space\SlipSys\py\slipsys ^> %USERPROFILE%\DeskTop\start_app.bat  >> %startup_dile_dir%
ECHO ECHO python slipsys.py ^>^> %USERPROFILE%\DeskTop\start_app.bat  >> %startup_dile_dir%
ECHO CALL C:\work_space\lib_installer.bat >> %startup_dile_dir%

ECHO pip install pandas >> C:\work_space\lib_installer.bat
ECHO pip install openpyxl >> C:\work_space\lib_installer.bat
ECHO pip install xlrd >> C:\work_space\lib_installer.bat

CALL %startup_dile_dir%

ECHO . > C:\work_space\lib_installer.bat

CD C:\work_space
CD SlipSys\py\slipsys
python SlipSys.py
