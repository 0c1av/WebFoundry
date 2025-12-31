from foundry.project_setup import run as run_project_setup
from foundry.basic_functions import get_projects_list
from foundry.project_dev import run as run_project_dev

import os
import json

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def run():
    for i in range(3):
        # Prompt user to continue or start new project
        start_option = input(f"{YELLOW}[*]{RESET} Continue or start new project? (c/n): ").strip().lower()
        if start_option == 'c' or start_option == 'n':
           break
        else:
            print(f"{RED}[!]{RESET} Invalid option. Please enter 'c' or 'n'.")
        print()
            



    if start_option == 'c':
        projects = get_projects_list()
        if not projects:
            print(f"{RED}[!]{RESET} No existing projects found. Please start a new project.")
            return
        
        print(f"{YELLOW}[*]{RESET} Existing projects:")
        for idx, project in enumerate(projects, start=1):
            print(f"    {idx}. {project}")
        print()

        selected_project = None
        for i in range(3):
            project_choice = input(f"{YELLOW}[*]{RESET} Select a project by number (1-{len(projects)}): ").strip()
            if not project_choice.isdigit() or not (1 <= int(project_choice) <= len(projects)):
                print(f"{RED}[!]{RESET} Invalid selection. Please choose a valid project number.")
            else:
                selected_project = projects[int(project_choice) - 1]
                break
        if selected_project:
            run_project_dev(selected_project)
        return




    elif start_option == 'n':
        project_name = run_project_setup()
        run_project_dev(project_name)

    return 