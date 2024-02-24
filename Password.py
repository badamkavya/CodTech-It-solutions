import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Invalid configuration. Please include at least one type of character."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 5
complexity = {'include_letters': True, 'include_numbers': True, 'include_symbols': True}
generated_password = generate_password(password_length, **complexity)
print(generated_password)
