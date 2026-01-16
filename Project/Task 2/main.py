# main.py
# Task 2: Password Verification and File Processing Program

import random
import sys

def password_check():
    """
    Function to verify user's password.
    Password must be at least 9 characters.
    Performs 3 random letter checks.
    """
    password = input("Enter your password: ")

    # Check if password length is sufficient
    if len(password) < 9:
        print("Password too short.")
        sys.exit()  # Exit program immediately

    print("Password length OK.")

    total_checks = 3  # Number of letters to check

    # Perform 3 random letter checks
    for i in range(total_checks):
        position = random.randint(1, len(password))  # Random position (1-based)
        user_input = input(f"Enter letter at position {position}: ")

        if user_input == password[position - 1]:  # Python is 0-indexed
            print("Correct")
        else:
            print("Security check failed.")
            sys.exit()  # Exit immediately on wrong input

    print("Security check passed.\n")

def file_processing(filename):
    """
    Function to read a file and output line, word, and character counts.
    """
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit()

    lines = contents.splitlines()
    words = contents.split()
    chars = len(contents)

    print(f"File: {filename}")
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {chars}\n")

def main():
    # Step 1: Password verification
    password_check()

    # Step 2: Check for command-line argument (filename)
    if len(sys.argv) < 2:
        print("Please provide a filename as a command-line argument.")
        print("Usage: python main.py sample_input.txt")
        sys.exit()

    filename = sys.argv[1]

    # Step 3: File processing
    file_processing(filename)

if __name__ == "__main__":
    main()
