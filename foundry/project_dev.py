import json
import shutil
import subprocess
import sys
import os
import time


GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def run(project_name):
    project_dir = f"./projects/{project_name}"
    

    print("\n\n\n")
    print(f"{GREEN}[+][+][+][+][+]{RESET}  {project_name} Development Environment  {GREEN}[+][+][+][+][+]{RESET}")
    

    subprocess.run(["pkill", "-f", f"{project_dir}/flask_main.py"])
    flask_process = subprocess.Popen([
        "gnome-terminal",
        "--",
        "bash", "-c",
        f'echo "{GREEN}[+]{RESET} In this flask server you can see the server\'s activity.\n{YELLOW}[*]{RESET} This is an execution of {project_dir}/flask_main.py\n"; sleep 0.1; {sys.executable} flask_main.py; exec bash'
    ],
    cwd=project_dir)

    print(f"{GREEN}[+]{RESET} Flask server started in new terminal.")

    