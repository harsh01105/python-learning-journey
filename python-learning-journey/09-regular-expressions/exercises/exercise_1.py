import re

text = "Call me at 987-654-3210 or my office at 123-456-7890."

pattern = r"\d{3}-\d{3}-\d{4}"
phone_numbers = re.findall(pattern, text)

print(f"Found phone numbers: {phone_numbers}")