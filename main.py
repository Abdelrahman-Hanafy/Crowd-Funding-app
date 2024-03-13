from Account import auth
from Project import manage

from getpass import getpass


def show_log_menu():
    print(50*"=")
    print("""
    Do you want to:
        1. Register
        2. LogIn
        0. Exit
    """)
    print(50*"=")


def show_main_menu():
    print(50*"=")
    print("""
    Do you want to:
        1. View All projects
        2. Edit your Projects
        3. Delete from your Project
        4. Search with date
        5. Create Project
        0. LogOut
    """)
    print(50*"=")


def main() -> bool:

    logged_id: str = None

    while not logged_id:
        show_log_menu()
        choice = input("your choice: ")

        if choice == '0':
            return False

        elif choice == '1':  # reg
            name = input("Enter your name [first last]: ").split(" ")
            email = input("Email: ")
            phone = input("Mobile phone: ")
            while True:
                password = getpass("Choose a password: ")
                confirm_pass = getpass("Enter your password again: ")

                if password != confirm_pass:
                    print("Passwords should match!!")
                    continue
                break

            try:
                logged_id = auth.register(first_name=name[0], last_name=name[1], password=password,
                                          email=email, mobile_phone=phone)
            except Exception as e:
                print(e)

        elif choice == '2':  # login
            email = input("Email: ")
            password = getpass("Passowrd: ")
            try:
                logged_id = auth.login(email=email, password=password)
            except Exception as e:
                print(e)

        else:
            print("Please choose from menu items [1, 2, 0]")
            continue

    if not logged_id:
        return True

    while logged_id:
        show_main_menu()
        choice = input("your choice: ")

        if choice == '0':  # log out
            logged_id = None

        elif choice == '1':  # view
            manage.show_projects()

        elif choice == '2':  # edit
            my_projects = manage.get_by_auther(id=logged_id)
            manage.show_projects_list(my_projects)
            to_edit = int(input("Which one you want to edit: "))
            if to_edit == 0:
                continue
            print("Leave empty if you do not want to edit!!")
            title = input("Enter project title: ")
            description = input("Enter project description: ")
            target = input("Enter project target Amount: ")
            start_date = input("Enter project Start date [YYYY-MM-DD]: ")
            end_date = input("Enter project End date [YYYY-MM-DD]: ")

            pro_to_edit = my_projects[to_edit-1]

            manage.edit_item(pro_to_edit, title, description,
                             target, start_date, end_date)

        elif choice == '3':  # delete
            my_projects = manage.get_by_auther(id=logged_id)
            manage.show_projects_list(my_projects)
            to_delete = int(input("Which one you want to delete: "))
            if to_delete == 0:
                continue
            try:
                manage.remove_item(my_projects[to_delete-1])
            except IndexError:
                print(f"Please choose Number between 1-{len(my_projects)}")
            except ValueError:
                print("Error while deleting this object...")

        elif choice == '4':  # search
            year = int(input("Enter the year: "))
            month = input("Enter Month or leave blank [1-12]: ")
            month = int(month) if month else None
            projects = manage.get_by_date(year, month)
            manage.show_projects_list(projects)
            to_view = int(input("More details for: "))
            if to_view == 0:
                continue
            try:
                print(projects[to_view-1])
            except IndexError:
                print(f"Please choose Number between 1-{len(projects)}")

        elif choice == '5':
            title = input("Enter project title: ")
            description = input("Enter project description: ")
            target = input("Enter project target Amount: ")
            start_date = input("Enter project Start date [YYYY-MM-DD]: ")
            end_date = input("Enter project End date [YYYY-MM-DD]: ")
            try:
                manage.create_project(auth_id=logged_id, title=title, description=description,
                                      target=target, start_date=start_date, end_date=end_date)
            except Exception as e:
                print(e)

        else:
            print("Please choose from menu items [1, 2, 3, 4, 0]")
            continue
    return True


if __name__ == "__main__":
    auth.generate_demo_accounts()
    manage.generate_demo_projects(auth.accounts)

    while main():
        pass
