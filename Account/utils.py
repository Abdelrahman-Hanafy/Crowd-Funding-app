import re
import uuid


def generate_id() -> str:
    return str(uuid.uuid1())


def get_match(data: str, regex: str) -> str:
    pattern = re.compile(regex)
    return pattern.fullmatch(data)


def validate_email(email: str) -> bool:
    # Regular expression pattern for a valid email address
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    return True if get_match(regex=email_regex, data=email) else False


def validate_phone_number(phone_number: str) -> bool:
    # Regular expression pattern for Egypt phone numbers
    phone_regex = r"^(?:\+20|0)?1[0-9]{9}$"

    return True if get_match(regex=phone_regex, data=phone_number) else False
