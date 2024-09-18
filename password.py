"""
TASK 3
create a password generator application using python, allowing users to 
specify the lenght and complexity of the password.
User input: Prompt the user to specify the desired lenght of the password.
Generate Password: Use a combination of random characters to generate a password of specified length.
Display the password: Print the generated password on the screen.
"""
import random
import string

# Function to generate a password
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define the character pool based on user preferences
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure the password includes at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password with random characters
    password += random.choices(characters, k=length - len(password))
    
    # Shuffle to ensure randomness and return as a string
    random.shuffle(password)
    return ''.join(password)

# Main function
def main():
    print(".... Password Generator!....")
    
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4 characters): "))
            if length >= 4:
                break
            else:
                print("Password length should be at least 4 characters.")
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user for password complexity preferences
    use_uppercase = input(" Do you want to Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Do you want to Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Do you want to Include symbols? (yes/no): ").lower() == 'yes'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    
    # Display the generated password
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()