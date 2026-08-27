import re

def is_valid_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None

emails = ["harsh@gmail.com", "not-an-email", "test.user@college.edu"]

for email in emails:
    result = "Valid" if is_valid_email(email) else "Invalid"
    print(f"{email}: {result}")