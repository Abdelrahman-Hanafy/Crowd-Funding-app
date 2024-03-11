"""
TODO: 
    1- store password as hash value not plain text
    2- move the accounts list to Account class and impl the find by email thier
    3- create custom Exception calsses to better handel them
"""
import rstr
from .account import Account
from .utils import generate_id, validate_email
from faker import Faker  # A library for generating fake data

accounts: list[Account] = []


def valid_reg_data(keys) -> bool:
    required_keys = {"first_name", "last_name",
                     "password", "email", "mobile_phone"}

    return all(key in required_keys for key in keys)


def valid_login_data(keys) -> bool:
    required_keys = {"password", "email"}

    return all(key in required_keys for key in keys)


def register(**kwargs):
    """
    Parameters:
    - **kwargs: Additional keyword arguments.
        Suggested keys: "first_name", "last_name","password", "email", "mobile_phone".
    """
    if not valid_reg_data(kwargs.keys()):
        raise Exception("Please provide the full data to register")

    uid = generate_id()
    acc = Account(uid, kwargs["first_name"], kwargs["last_name"], kwargs["password"],
                  kwargs["email"], kwargs["mobile_phone"])
    accounts.append(acc)
    return acc._uid


def login(**kwagrs):
    if not valid_login_data(kwagrs.keys()):
        raise Exception("Please provide the full data to login")

    if not validate_email(kwagrs["email"]):
        raise Exception("Wrong email format please [example@co.domain]")

    filtered_accs = [
        account for account in accounts if account.email == kwagrs["email"]]

    for acc in filtered_accs:
        if acc.password == kwagrs["password"]:
            return acc._uid
    else:
        raise Exception("Username or Password is wrong!!")

def generate_demo_accounts():
    def generate_demo_account():
        fake = Faker()
        uid = generate_id()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = fake.password(length=10)
        email = fake.email()
        mobile_phone = rstr.xeger(r"^(?:\+20|0)?1[0-9]{9}$")

        return Account(uid, first_name, last_name, password, email, mobile_phone)

    with open("demo_data.txt","w") as f:
        for _ in range(5):
            acc = generate_demo_account()
            accounts.append(acc)
            f.write(str(acc))