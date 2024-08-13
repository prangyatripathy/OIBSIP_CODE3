import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

def user_input():
    len = int(input("Enter the desired password length: "))
    include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
    return len, include_letters, include_numbers, include_symbols

def validate_input(include_letters, include_numbers, include_symbols):
    if not (include_letters or include_numbers or include_symbols):
        raise ValueError("At least one character type must be selected!")

def generate_password(len, include_letters, include_numbers, include_symbols):
    character_pool = ''
    if include_letters:
        character_pool += letters
    if include_numbers:
        character_pool += numbers
    if include_symbols:
        character_pool += symbols
    password = ''.join(random.choice(character_pool) for _ in range(len))
    return password

def main():
    try:
        len, include_letters, include_numbers, include_symbols = user_input()
        validate_input(include_letters, include_numbers, include_symbols)
        password = generate_password(len, include_letters, include_numbers, include_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
