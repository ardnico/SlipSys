
# library import
import subprocess

try:
    import django
except:
    subprocess.run(["pip","install","django"])
subprocess.run(["pip","install","django-bootstrap5"])


from slipsys_handler import slipsys
from filemanage import filemanage


if __name__ == "__main__":
    fm = filemanage.Filemanagaer()
    
    # instance = slipsys()
    # instance.main()
    # serverprocess = instance.process_run_server()
    # browserprocess = instance.process_launch_browser()

    
