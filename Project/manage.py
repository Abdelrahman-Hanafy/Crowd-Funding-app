from .project import Project
import lorem  # A library for generating random Lorem Ipsum text
import random
from datetime import datetime, timedelta

projects : list[Project] = []



def generate_demo_projects():
    def generate_demo_project():
        title = lorem.sentence()
        description = lorem.paragraph()
        target = random.randint(1000, 10000)  # Random target value
        start_date = datetime.now() - timedelta(days=random.randint(1, 365))  # Random start date within the last year
        end_date = start_date + timedelta(days=random.randint(1, 365))  # Random end date after the start date

        return Project(title, description, target, start_date, end_date)
    
    for _ in range(5):
        projects.append(generate_demo_project())

def show_all():
    for project in projects:
        print(project)