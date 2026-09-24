import re

mobile = "9876543210"
email = "tejas@gmail.com"

password = "Tejas@123"

print(bool(re.fullmatch(r"[6-9]\d{9}", mobile)))
print(bool(re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email)))
print(bool(re.fullmatch(r"(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%]).{8,}", password)))