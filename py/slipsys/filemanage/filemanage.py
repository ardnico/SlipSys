
from glob import glob
import os
import shutil
from datetime import datetime as dt
import sys
sys.path.append('../')
from _config.config import config

class Filemanagaer:
    config = config()
    def __init__(self) -> None:
        self.get_default_files()
    
    def get_default_files(self):
        work_dirs = glob(fr"{self.config.setting_path}\*")
        if len(work_dirs) == 0:
            waiting = input("There is no files")
            raise Exception
        work_dirs = [i for i in work_dirs if i != fr"{self.config.setting_path}\default"]
        for path in work_dirs:
            self.make_tomonth_file(path)
        
    def make_tomonth_file(self,file_path):
        current_year = str(int(dt.now().year))
        current_year_name = self.get_year_name(current_year)
        current_year_name_with_dot = self.get_year_name_with_dot(current_year)
        current_month = str(int(dt.now().month))
        project_name = file_path.split("\\")[-1].replace("データ","")
        new_directory_name = fr"{file_path}\{current_year}_{current_year_name}\{current_year_name_with_dot}_{project_name}-{current_month}"
        os.makedirs(new_directory_name,exist_ok=True)
        default_files = glob(fr"{self.config.setting_path}\default\*")
        for file in default_files:
            new_file_name = file.split("\\")[-1].replace("(ym)",current_year_name)
            new_file_path = fr"{new_directory_name}\{new_file_name}"
            if os.path.exists(new_file_path)==False:
                shutil.copy(file,new_file_path)
        
    
    def get_year_name(self,y):
        y = int(y)
        if y > 2018:
            tmp_y = str(y - 2018)
            return "R" + tmp_y
        elif y > 1989:
            tmp_y = str(y - 1989)
            return "H" + tmp_y
        else:
            return ""
    
    def get_year_name_with_dot(self,y):
        y = int(y)
        if y > 2018:
            tmp_y = str(y - 2018)
            return "R." + tmp_y
        elif y > 1989:
            tmp_y = str(y - 1989)
            return "H." + tmp_y
        else:
            return ""
    