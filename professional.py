'''
Password Generator
Generate a cryptographically secure random password
'''
import string
import secrets
MIN_LENGTH = 8
CHAR_POOL = string.ascii_letters + string.digits + string.punctuation

def password_length(min_length: int) -> int:
    '''Prompt user until valid password length is entered'''
    while True:
        try:
            length = int(input("Enter the length of password: "))
            if length < min_length:
                raise ValueError (f"Length of password can't be lessthan {min_length}.")
            return length
        except ValueError as e:
            print(f"Invalid input: {e}. Try again\n")

def generate_password(length: int) -> str:
    '''Generate a cryptographically secure password'''
    return "".join(secrets.choice(CHAR_POOL) for _ in range(length))

def display_password(password: str) -> None:
    '''Display generated password'''
    print(f"Generated password is: {password}")

def main() -> None:
    '''Entry point'''
    length = password_length(MIN_LENGTH)
    password = generate_password(length)
    display_password(password)

if __name__ == "__main__":
    main()