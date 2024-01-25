import random
import string

def generate_password():
    # Get user input for password length
    length = int(input("Enter the password length (8, 10, 12, or 14): "))

    # Get user input for the number of special characters
    special_chars = int(input("Enter the number of special characters (up to 3): "))
    
    # Ensure valid input
    if length not in [8, 10, 12, 14] or special_chars < 0 or special_chars > 3:
        print("Invalid input. Please follow the specified requirements.")
        return None

    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "@!?-%()"

    # Initialize password
    password = []

    # Add characters to password
    for i in range(length - special_chars):
        # Add lowercase letters and digits
        if i % 2 == 0:
            password.append(random.choice(lowercase_letters + digits))
        else:
            # Add uppercase letters
            password.append(random.choice(uppercase_letters))

    # Add special characters
    for _ in range(special_chars):
        password.append(random.choice(special_characters))

    # Shuffle the password to mix characters
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

# Example usage
generated_password = generate_password()

if generated_password:
    print(f"Generated Password: {generated_password}")
