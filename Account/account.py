from .utils import validate_email, validate_phone_number

class Account():
    
    def __init__(self,first_name,last_name,password,email,mobile_phone) -> None:
        self.first_name = first_name
        self.last_name =last_name
        self.password = password

        self.email = email
        self.mobile_phone = mobile_phone

    @property
    def email(self): 
        return self.__email
    
    @email.setter
    def email(self, email):
        if not validate_email(email):
            raise Exception("Wrong email format please [example@co.domain]")
        self.__email = email

    @property
    def mobile_phone(self): 
        return self.__mobile_phone 
    
    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if not validate_phone_number(mobile_phone):
            raise Exception("Not an Egyption Number")
        self.__mobile_phone = mobile_phone
    