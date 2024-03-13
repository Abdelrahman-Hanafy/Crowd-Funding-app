"""
TODO: 
    1- Add project creation option
"""
from .project import Project
import lorem  # A library for generating random Lorem Ipsum text
import random
from datetime import datetime, timedelta

projects: list[Project] = []


def generate_demo_projects(accs: list[object]):
    global projects

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


def is_valid_project(keys: list[str]) -> bool:
    required = {"auth_id", "title", "description",
                "target", "start_date", "end_date"}
    return all(key in required for key in keys)


def make_date(data: str) -> datetime:
    date_data = list(map(int, data.split("-")))
    date = datetime(date_data[0], date_data[1], date_data[2])
    return date


def create_project(**kwargs: str):
    global projects
    if not is_valid_project(kwargs.keys()):
        raise Exception("Provide the full project data")

    st_date = make_date(kwargs["start_date"])
    end_date = make_date(kwargs["end_date"])

    if st_date > end_date:
        raise Exception("End date should be after the start date")

    pro = Project(kwargs["auth_id"], kwargs["title"], kwargs["description"],
                  int(kwargs["target"]), st_date, end_date)
    projects.append(pro)


def show_projects():
    for project in projects:
        print(project)


def get_filtered(check: callable) -> list[Project]:
    filtered = [project for project in projects if check(project)]
    return filtered


def get_by_auther(id: str) -> list[Project]:
    def check(project: Project) -> bool:
        return project.auth_id == id

    return get_filtered(check)


def get_by_date(year: int, month: int | None = None) -> list[Project]:
    def check(project: Project) -> bool:
        return project.start.year == year and (project.start.month == month if month else True)

    return get_filtered(check)


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


def edit_item(pro: Project, title, description,
              target, start_date, end_date):

    pro.title = title if title else pro.title
    pro.description = description if description else pro.description
    pro.traget = target if target else pro.traget
    pro.start = make_date(start_date) if start_date else pro.start
    pro.end = make_date(end_date) if end_date else pro.end
