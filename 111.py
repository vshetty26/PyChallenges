import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters."
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    all_chars = letters + digits + special_chars
    password += random.choices(all_chars, k=length - 3)
    
    random.shuffle(password)
    
    return ''.join(password)

length = int(input("Enter the desired password length: "))
password = generate_password(length)
print("Generated Password:", password)
