class Account():
    
    def __init__(self,first_name,last_name,password,email,mobile_phone) -> None:
        self.first_name = first_name
        self.last_name =last_name
        self.password = password

        self.email = email
        self.mobile_phone = mobile_phone

    @property
    def email(self): 
        return self.__email or "NO EMAIL"
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def mobile_phone(self): 
        return self.__mobile_phone or "NO Mobile Phone"
    
    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        self.__mobile_phone = mobile_phone
    