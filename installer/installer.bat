whoami /priv | find "SeDebugPrivilege" > nul
if %errorlevel% neq 0 (
　@powershell start-process ”%~0" -verb runas
　echo 管理者権限がありません。管理者権限で実行します
　exit
)

set startup_dile_dir="C:\Users\leafs\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\update_slipsys.bat"
set desktop_bat=%USERPROFILE%\DeskTop\StartApp.bat

echo mkdir C:\work_space > %startup_dile_dir%
echo cd C:\work_space >> %startup_dile_dir%
echo if exist C:\work_space\SlipSys ( >> %startup_dile_dir%
echo     git pull >> %startup_dile_dir%
echo )else( >> %startup_dile_dir%
echo     git clone https://github.com/ardnico/SlipSys >> %startup_dile_dir%
echo ) >> %startup_dile_dir%

%startup_dile_dir%

cd C:\work_space
cd SlipSys\py
python SlipSys.py
