import random
import string

print("=" * 40)
print("      PYTHON PASSWORD GENERATOR")
print("=" * 40)

while True:

    try:
        length = int(input("\nEnter password length (4-50): "))

        if length < 4 or length > 50:
            print("Password length must be between 4 and 50.")
            continue

        characters = ""

        uppercase = input("Include uppercase letters? (y/n): ").lower()
        if uppercase == "y":
            characters += string.ascii_uppercase

        lowercase = input("Include lowercase letters? (y/n): ").lower()
        if lowercase == "y":
            characters += string.ascii_lowercase

        numbers = input("Include numbers? (y/n): ").lower()
        if numbers == "y":
            characters += string.digits

        symbols = input("Include symbols? (y/n): ").lower()
        if symbols == "y":
            characters += string.punctuation

        if characters == "":
            print("\nYou must choose at least one character type.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

        with open("passwords.txt", "a") as file:
            file.write(password + "\n")

        print("Password saved to passwords.txt")

    except ValueError:
        print("Please enter a valid number.")

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("\nProgram closed.")
        break
