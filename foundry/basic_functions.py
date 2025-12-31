from pathlib import Path


def get_projects_list():
    directory = Path("./projects")
    projects = [f.name for f in directory.iterdir() if f.is_dir()]
    return projects