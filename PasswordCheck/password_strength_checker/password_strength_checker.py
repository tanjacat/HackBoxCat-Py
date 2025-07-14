import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make the password longer (at least 8 characters).")

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # Digits
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include numbers (0-9).")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Include special characters (!@#$%^&* etc.).")

    # Evaluation
    print(f"\nPassword: {password}")
    print(f"Strength score: {score}/6")

    if score == 6:
        print("✅ Strong password!")
    elif score >= 4:
        print("⚠️  Moderate password.")
    else:
        print("❌ Weak password!")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print(f" - {s}")

# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)
