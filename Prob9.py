import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError(
            "Password length should be at least 4 characters to include all types of characters."
        )
    uppercase_letter = string.ascii_uppercase
    lowercase_letter = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    password = [
        random.choice(uppercase_letter),
        random.choice(lowercase_letter),
        random.choice(digits),
        random.choice(special_characters),
    ]
    all_char = uppercase_letter + lowercase_letter + digits + special_characters
    password += [random.choice(all_char) for _ in range(length - 4)]
    random.shuffle(password)
    return "".join(password)


password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print(f"Generated password: {password}")
