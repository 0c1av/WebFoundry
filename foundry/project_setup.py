import os
import json
import shutil

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def run():
    # Logic to start new project
    print(f"{YELLOW}[*]{RESET} Enter some details about your project. You can modify them later")
    required_fields = ["name", "type", "description", "primary_color", "secondary_color", "font", "page_structure"]
    print(f"{YELLOW}[*]{RESET} Required fields:")
    for field in required_fields:
        print(f"    - {field}")
    print()

    for i in range(3):
        new_project_name = input("[STEP 1] Enter new project name: ").strip()
        new_project_path = f"./projects/{new_project_name}"
        if os.path.exists(new_project_path):
                print(f"{RED}[!]{RESET}Project '{new_project_name}' already exists. Please choose a different name.")
        elif not new_project_name:
            print(f"{RED}[!]{RESET} Project name cannot be empty.")
        else:
            break
    print()


    for i in range(3):
        new_project_type = input("[STEP 2] Select project type: (1)Personal blog, (2)Portfolio, (3)Business website, (4)E-commerce site, (5)Other: ").strip().lower()
        if new_project_type not in ['1', '2', '3', '4', '5']:
            print(f"{RED}[!]{RESET} Invalid option. Please select a valid project type.")
        else:
            break
    print()


    new_project_description = input("[STEP 3] Enter small project description: ").strip()
    print()


    for i in range(3):
        new_project_primary_color = input("[STEP 4] Enter primary color (e.g., #ff5733): ").strip()
        new_project_secondary_color = input("[STEP 4] Enter secondary color (e.g., #33c1ff): ").strip()
        if not (new_project_primary_color.startswith('#') and len(new_project_primary_color) == 7 and
                new_project_secondary_color.startswith('#') and len(new_project_secondary_color) == 7):
            print(f"{RED}[!]{RESET} Invalid color format. Please enter colors in hex format (e.g., #ff5733).")
        else:
            break
    print()




    for i in range(3):
        new_project_font = input("[STEP 5] Enter font (e.g., Arial, Helvetica): ").strip()
        if new_project_font not in ["Arial", "Helvetica", "Times New Roman", "Georgia", "Courier New", "Verdana", "Trebuchet MS"]:
            print(f"{RED}[!]{RESET} Unsupported font. Please choose from the common web fonts.")
        else:
            break
    print()



    '''
    new_project_favicon_path = input("[STEP 6] Enter path to favicon file (e.g., ./path/to/favicon.ico) or leave blank if no favicon needed: ").strip()
    if not new_project_favicon_path:
        new_project_favicon_path = False
    else:
        if not os.path.isfile(new_project_favicon_path):
            print(f"{RED}[!]{RESET} Favicon file not found. Proceeding without favicon.")
            new_project_favicon_path = False
    print()
    '''





    for i in range(3):
        new_project_page_structure = input("[STEP 6] Single-page or multi-page site? (s/m): ").strip().lower()
        if new_project_page_structure not in ['s', 'm']:
            print(f"{RED}[!]{RESET} Invalid option. Please enter 's' for single-page or 'm' for multi-page.")
        else:
            break
    print()


    if new_project_page_structure == 'm':
        new_project_nav_bar_option = input("[STEP 7] Include navigation bar on each page? (y/n): ").strip().lower()
        if new_project_nav_bar_option == 'y':
            new_project_nav_bar = True
        else:
            new_project_nav_bar = False
    else:
        new_project_nav_bar = False
    print()




    new_project_media = {
        "mail": None,
        "instagram": None,
        "twitter": None,
        "facebook": None,
        "linkedin": None,
        "spotify": None
    }
    new_project_media_option = input("[STEP 8] Would you like to add media links now? (y/n): ").strip().lower()
    if new_project_media_option == 'y':
        for media in new_project_media.keys():
            media_link = input(f"[STEP 8] Enter {media} link or leave blank to skip: ").strip()
            if media_link:
                new_project_media[media] = media_link
    print()

    
    

    metadata = {
        "name": new_project_name,
        "path": new_project_path,
        "type": new_project_type,
        "description": new_project_description,
        "primary_color": new_project_primary_color,
        "secondary_color": new_project_secondary_color,
        "font": new_project_font,
        "page_structure": "single-page" if new_project_page_structure == 's' else "multi-page",
        "navigation_bar": new_project_nav_bar,
        "media": {
            "mail": new_project_media["mail"],
            "instagram": new_project_media["instagram"],
            "twitter": new_project_media["twitter"],
            "facebook": new_project_media["facebook"],
            "linkedin": new_project_media["linkedin"],
            "spotify": new_project_media["spotify"]
        }
    }

    exit_option = False
    for field in required_fields:
        if not metadata[field]:
            print(f"{RED}[!]{RESET} Missing required field: {field}. Project setup aborted.")
            exit_option = True
    if exit_option:
        exit(1)


    # Create project structure
    os.makedirs(new_project_path)
    os.makedirs(os.path.join(new_project_path, "project_data"))
    os.makedirs(os.path.join(new_project_path, "static"))
    os.makedirs(os.path.join(new_project_path, "templates"))
    os.makedirs(os.path.join(new_project_path, "static", "css"))
    os.makedirs(os.path.join(new_project_path, "static", "js"))
    os.makedirs(os.path.join(new_project_path, "static", "images"))

    metadata_file_path = os.path.join(f"{new_project_path}/project_data", "metadata.json")
    with open(metadata_file_path, 'w') as f:
        json.dump(metadata, f, indent=4)


    shutil.copyfile("./foundry/templates/acc_log.json", new_project_path + "/project_data/acc_log.json")
    def update_acc_log(update_place, file_path, details):
        acc_log_path = os.path.join(new_project_path, "project_data", "acc_log.json")
        with open(acc_log_path, 'r') as f:
            acc_log = json.load(f)
        acc_log[update_place][file_path] = details
        with open(acc_log_path, 'w') as f:
            json.dump(acc_log, f, indent=4)

        
    update_acc_log("project-structure", "project_data", "Directory for project data files.")
    update_acc_log("project-structure", "project_data/metadata.json", "Contains all the metadata information about the project.")
    update_acc_log("project-structure", "project_data/acc_log.json", "Log file to track the file structure and the status of created project files.")
    update_acc_log("project-structure", "static/", "Directory for static files like CSS, JS, and images.")
    update_acc_log("project-structure", "templates/", "Directory for HTML template files.")
    update_acc_log("project-structure", "static/css/", "Directory for CSS files.")
    update_acc_log("project-structure", "static/js/", "Directory for JavaScript files.")
    update_acc_log("project-structure", "static/images/", "Directory for image files.")
    

            


    shutil.copyfile("./foundry/templates/flask_main.py", f"{new_project_path}/flask_main.py")
    update_acc_log("created-project-files-status", f"{new_project_path}/flask_main.py", "PARTIAL")
    update_acc_log("project-structure", "flask_main.py", "Runs the Flask application. Contains route definitions and server configurations.")

    shutil.copyfile("./foundry/templates/home.html", f"{new_project_path}/templates/home.html")
    update_acc_log("created-project-files-status", f"{new_project_path}/templates/home.html", "EMPTY")
    update_acc_log("project-structure", "templates/home.html", "Main HTML template for the homepage.")

    shutil.copyfile("./foundry/templates/style.css", f"{new_project_path}/static/css/style.css")
    update_acc_log("created-project-files-status", f"{new_project_path}/static/css/style.css", "EMPTY")
    update_acc_log("project-structure", "static/css/style.css", "CSS file for styling the web pages.")

    shutil.copyfile("./foundry/templates/home.js", f"{new_project_path}/static/js/home.js")
    update_acc_log("created-project-files-status", f"{new_project_path}/static/js/home.js", "EMPTY")
    update_acc_log("project-structure", "static/js/home.js", "JavaScript file for homepage interactivity.")


    print(f"{GREEN}[+]{RESET} {new_project_name} has successfully been set up and is created at {new_project_path}.")
    return new_project_name