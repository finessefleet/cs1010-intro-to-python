import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(length))
