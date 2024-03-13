"""
TODO: 
    1- Add a user id for the project 
    2- Add project creation option
"""
from .project import Project
import lorem  # A library for generating random Lorem Ipsum text
import random
from datetime import datetime, timedelta

projects: list[Project] = []


def generate_demo_projects(accs: list[object]):
    def generate_demo_project():
        auth_id = random.choice(accs)._uid
        title = lorem.sentence()
        description = lorem.paragraph()
        target = random.randint(1000, 10000)  # Random target value
        start_date = datetime.now() - timedelta(days=random.randint(1, 365)
                                                )  # Random start date within the last year
        # Random end date after the start date
        end_date = start_date + timedelta(days=random.randint(1, 365))

        return Project(auth_id, title, description, target, start_date, end_date)

    for _ in range(5):
        projects.append(generate_demo_project())


def show_projects(id: str | None = None):
    if id is not None:
        pros = get_by_auther(id)
    else:
        pros = projects

    for project in pros:
        print(project)


def get_by_auther(id: str) -> list[Project]:
    def check(project: Project) -> bool:
        return project.auth_id == id
    filtered_by_id = [project for project in projects if check(project)]
    return filtered_by_id


def show_projects_list(pros: list[Project]):
    print("="*50)
    for i, p in enumerate(pros):
        print(f"{i+1}. {p.title}")
    print("0. Go Back")
    print("="*50)


def remove_item(pro: Project):
    global projects
    try:
        projects.remove(pro)
    except ValueError as e:
        raise e
