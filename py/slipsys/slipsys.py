
# library import
import subprocess

subprocess.run(["pip","install","django-bootstrap5"])


from slipsys_handler import slipsys

if __name__ == "__main__":
    instance = slipsys()
    instance.main()
    serverprocess = instance.process_run_server()
    browserprocess = instance.process_launch_browser()

    
