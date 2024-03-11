"""
TODO: 
    1- store password as hash value not plain text
    2- move the accounts list to Account class and impl the find by email thier
"""
from .account import Account
from .utils import generate_id, validate_email

accounts: list[Account] = []


def valid_reg_data(keys) -> bool:
    required_keys = {"first_name", "last_name",
                     "password", "email", "mobile_phone"}

    return all(key in required_keys for key in keys)


def valid_login_data(keys) -> bool:
    required_keys = {"password", "email"}

    return all(key in required_keys for key in keys)


def register(**kwargs):
    if not valid_reg_data(kwargs.keys()):
        raise Exception("Please provide the full data to register")

    uid = generate_id()
    acc = Account(uid, kwargs["first_name"], kwargs["last_name"], kwargs["password"],
                  kwargs["email"], kwargs["mobile_phone"])

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
