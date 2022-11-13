import os
from tkinter import filedialog

class config:
    __default_data_dir = fr"{os.getcwd()}\data"
    __path_setting = fr"{os.getcwd()}\data\path_setting.data"
    __startup_file = os.environ["APPDATA"] + r"\Microsoft\Windows\Start Menu\Programs\Startup\update_slipsys.bat"
    def __init__(self) -> None:
        self.__make_work_dir()
        self.__make_start_file()
        text = f"""
cd {os.getcwd()}
python file_mk.py
"""
        self.__add_startup_file(text)
    
    def __set_work_dir(self) -> None:
        user_desktop = self.__get_userdesktop()
        with open(self.__path_setting,"w") as f:
            fld = filedialog.askdirectory(initialdir = user_desktop)
            f.write(fld)
        self.setting_path = fld
    
    def __make_work_dir(self) -> None:
        os.makedirs(self.__default_data_dir,exist_ok=True)
        if os.path.exists(self.__path_setting):
            with open(self.__path_setting,"r",encoding="shift_jis") as f:
                self.setting_path = f.read()
        else:
            self.__set_work_dir()
    
    def __get_userdesktop(self) -> str:
        user_desktop = os.environ["USERPROFILE"] + "\\Desktop"
        if os.path.exists(user_desktop)==False:
            user_desktop = os.environ["USERPROFILE"] + "\\Onedrive\\Desktop"
        return user_desktop
    
    def __make_start_file(self) -> None:
        user_desktop = self.__get_userdesktop()
        starter_txt = f"""cd {os.getcwd()}
python SlipSys.py
"""
        with open(fr"{user_desktop}\start_app.bat","w",encoding="shift_jis") as f:
            f.write(starter_txt)
    
    def __add_startup_file(self,text) -> None:
        with open(self.__startup_file,"r",encoding="shift_jis") as f:
            tmp_txt = f.read()
        
        if tmp_txt.find(text) != -1:
            return
        # add text
        with open(self.__startup_file,"a",encoding="shift_jis") as f:
            f.write(f"{text}\n")
