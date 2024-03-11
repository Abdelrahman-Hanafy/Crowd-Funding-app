from .project import Project

projects : list[Project] = None

def generate_demo_projects():
    pass

def show_all():
    for project in projects:
        print(project)