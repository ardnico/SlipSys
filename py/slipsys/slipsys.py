
import os
import _config as cfg
import subprocess
from multiprocessing import Process

class slipsys:
    config = cfg.config()
    def __init__(self) -> None:
        pass
    
    def run_server(self):
        os.chdir(r"C:\work_space\SlipSys\py\slipsys\django")
        subprocess.run(["python","manage.py","runserver","127.0.0.1:8000"])
    
    def process_run_server(self):
        process = Process(target=self.run_server ,args=())
        process.start()
        return process
    
    def launch_browser(self):
        subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe",r"http://127.0.0.1:8000"])
    
    def process_launch_browser(self):
        process = Process(target=self.launch_browser ,args=())
        process.start()
        return process
    
    def launch_webbrowser(self):
        pass
    
    def main(self):
        print('comming soon ...')        

if __name__ == "__main__":
    instance = slipsys()
    instance.main()
    serverprocess = instance.process_run_server()
    browserprocess = instance.process_launch_browser()

    
