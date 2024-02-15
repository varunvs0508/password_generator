import random
import string

def generate_password(length=12):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))
        
    if num_passwords <= 0 or password_length <= 0:
        print("Please enter valid positive integers for number of passwords and password length.")     
    passwords = [generate_password(password_length) for _ in range(num_passwords)]
        
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)
except ValueError:
    print("Invalid input. Please enter valid integers for number of passwords and password length.")
