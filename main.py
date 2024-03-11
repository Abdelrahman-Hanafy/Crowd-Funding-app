from Account import auth
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
    
def main():
    logged_id:str = None

    while not logged_id:
        show_log_menu()
        choice  = input("your choice: ")
        
        if choice == '0':
            break
        
        elif choice == '1': #reg
            pass
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
    
if __name__ == "__main__":
    main()