
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
    
    def run_by_process(self):
        serverprocess = Process(target=self.run_server ,args=())
        serverprocess.start()
        return serverprocess
    
    def launch_webbrowser(self):
        pass
    
    def main(self):
        self.run_by_process()
        print('comming soon ...')        

if __name__ == "__main__":
    instance = slipsys()
    instance.main()
    # instance.run_server()
