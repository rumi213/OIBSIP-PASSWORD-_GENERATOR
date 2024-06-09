import string
import random

def generate_password(length, use_symbols=False, use_numbers=False):
    all_characters = string.ascii_letters
    if use_symbols:
        all_characters += string.punctuation
    if use_numbers:
        all_characters += string.digits
    

    if length < 8:
        print("For security reasons, consider using a password length of at least 8 characters.")

    return ''.join(random.choice(all_characters) for i in range(length))

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_symbols = input("Use symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").lower() == 'y'


    print(f"Generated password: {generate_password(length, use_symbols, use_numbers)}")
