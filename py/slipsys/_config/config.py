import os
from tkinter import filedialog

class config:
    def __init__(self):
        default_data_dir = fr"{os.getcwd()}\data"
        path_setting = fr"{default_data_dir}\path_setting.data"
        os.makedirs(default_data_dir,exist_ok=True)
        if os.path.exists(path_setting):
            with open(path_setting,"r",encoding="shift_jis") as f:
                self.setting_path = f.read()
        else:
            user_desktop = os.environ["USERPROFILE"]
            user_desktop = fr"{user_desktop}\Desktop"
            if os.path.exists(user_desktop)==False:
                user_desktop = os.environ["USERPROFILE"]
                user_desktop = fr"{user_desktop}\Onedrive\Desktop"            
            with open(path_setting,"w") as f:
                fld = filedialog.askdirectory(initialdir = user_desktop)
                f.write(fld)
            self.setting_path = fld
            starter_txt = f"""cd {default_data_dir}
cd SlipSys\py\slipsys
python SlipSys.py
"""
            with open(fr"{user_desktop}\start_app.bat","w",encoding="shift_jis") as f:
                f.write(starter_txt)