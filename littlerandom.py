import random
import string

def generate_password():
    lower = ''.join(random.choices(string.ascii_lowercase, k=4))
    digits = ''.join(random.choices(string.digits, k=4))
    upper = ''.join(random.choices(string.ascii_uppercase, k=4))
    return f"{lower}-{digits}${upper}"

print(generate_password())