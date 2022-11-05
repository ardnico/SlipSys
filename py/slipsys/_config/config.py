import os
from tkinter import filedialog

class config:
    def __init__(self):
        default_data_dir = fr"{os.getcwd()}\data"
        path_setting = fr"{default_data_dir}\path_setting.data"
        os.makedirs(default_data_dir,exist_ok=True)
        self.startup_file = os.environ["APPDATA"] + r"\Microsoft\Windows\Start Menu\Programs\Startup\update_slipsys.bat"
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
            starter_txt = f"""cd {os.getcwd()}
python SlipSys.py
"""
            with open(fr"{user_desktop}\start_app.bat","w",encoding="shift_jis") as f:
                f.write(starter_txt)
        rewrite_file = fr"{default_data_dir}\rewrite_file.csv"
        if os.path.exists(rewrite_file):
            with open(rewrite_file,"r",encoding="shift_jis") as f:
                rewrite_txt = f.read().split("\n")
            for line in rewrite_txt:
                tmp_line = line.split(",")
                if len(tmp_line) != 2:
                    continue
                self.rewrite_startup_file(tmp_line[0],int(tmp_line[1]))
        else:
            with open(rewrite_file,"w",encoding="shift_jis") as f:
                f.write("")
    
    def rewrite_startup_file(self,text,mode=0):
        with open(self.startup_file,"r",encoding="shift_jis") as f:
            tmp_txt = f.read()
        if mode == 0:
            # add text
            with open(self.startup_file,"a",encoding="shift_jis") as f:
                f.write(text)
        elif mode == 1:
            # remove text
            tmp_txt = tmp_txt.split("\n")
            tmp_txt = [i for i in tmp_txt if i != text]
            tmp_txt = "\n".join(tmp_txt)
            with open(self.startup_file,"w",encoding="shift_jis") as f:
                f.write(tmp_txt)