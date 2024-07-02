import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Calculate the score based on the criteria met
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "digit_criteria": digit_criteria,
        "special_char_criteria": special_char_criteria,
        "strength": strength
    }

    return feedback

def main():
    password = input("Enter a password to check its strength: ")
    feedback = check_password_strength(password)

    print(f"Password Strength: {feedback['strength']}")
    print("Criteria met:")
    print(f" - Length >= 8: {'Yes' if feedback['length_criteria'] else 'No'}")
    print(f" - Contains uppercase letter: {'Yes' if feedback['uppercase_criteria'] else 'No'}")
    print(f" - Contains lowercase letter: {'Yes' if feedback['lowercase_criteria'] else 'No'}")
    print(f" - Contains digit: {'Yes' if feedback['digit_criteria'] else 'No'}")
    print(f" - Contains special character (@$!%*?&): {'Yes' if feedback['special_char_criteria'] else 'No'}")

if __name__ == "__main__":
    main()