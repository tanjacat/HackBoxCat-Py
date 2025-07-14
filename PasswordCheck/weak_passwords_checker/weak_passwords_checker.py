def load_weak_passwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        weak_passwords = set(line.strip() for line in file)
    return weak_passwords

def is_weak_password(password, weak_passwords):
    return password in weak_passwords

def main():
    weak_passwords = load_weak_passwords('weak_passwords.txt')
    password = input("Enter the password to check: ")
    if is_weak_password(password, weak_passwords):
        print("The password is weak! Please choose a stronger one.")
    else:
        print("The password was not found in the weak list. But it might still be unsafe.")

if __name__ == "__main__":
    main()
