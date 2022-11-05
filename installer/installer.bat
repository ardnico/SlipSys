set startup_dile_dir="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\update_slipsys.bat"
set desktop_bat=%USERPROFILE%\DeskTop\StartApp.bat

echo mkdir C:\work_space > %startup_dile_dir%
echo cd C:\work_space >> %startup_dile_dir%
echo if exist C:\work_space\SlipSys ( >> %startup_dile_dir%
echo     cd SlipSys >> %startup_dile_dir%
echo     git pull >> %startup_dile_dir%
echo ) else ( >> %startup_dile_dir%
echo     git clone https://github.com/ardnico/SlipSys >> %startup_dile_dir%
echo ) >> %startup_dile_dir%

%startup_dile_dir%

cd C:\work_space
cd SlipSys\py\slipsys
python SlipSys.py
