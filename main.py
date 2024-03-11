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
    
    print(logged_id)
    
if __name__ == "__main__":
    main()