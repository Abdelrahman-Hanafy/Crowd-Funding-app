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
        0. Exit
    """)
    print(50*"=")


def main():
    manage.generate_demo_projects()
    logged_id:str = None

    while not logged_id:
        show_log_menu()
        choice  = input("your choice: ")
        
        if choice == '0':
            break
        
        elif choice == '1': #reg
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
                logged_id = auth.register(first_name=name[0],last_name=name[1],password=password,
                                        email=email,mobile_phone=phone)
            except Exception as e:
                print(e)

        elif choice == '2': #login
            email = input("Email: ")
            password = getpass("Passowrd: ")
            try:
                logged_id = auth.login(email=email, password =password)
            except Exception as e:
                print(e)
                
        else:
            print("Please choose from menu items [1, 2, 0]")
            continue

    if not logged_id :
        return
    
    while logged_id:
        show_main_menu()
        choice  = input("your choice: ")

        if choice == '0': #log out
            logged_id = None

        elif choice == '1': #view
            manage.show_all()

        elif choice == '2': #edit
            pass
        elif choice == '3': #delete
            pass
        elif choice == '4': #search
            pass

        else:
            print("Please choose from menu items [1, 2, 3, 4, 0]")
            continue

if __name__ == "__main__":
    while True:
        main()