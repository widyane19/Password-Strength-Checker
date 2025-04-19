import re

def check_password_strength(password):
    strength_criteria = {
        "Length (8+ chars)": len(password) >= 8,
        "Uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"[0-9]", password)),
        "Special character": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    passed = [key for key, passed in strength_criteria.items() if passed]
    failed = [key for key, passed in strength_criteria.items() if not passed]

    print(f"\n🔍 Password: {password}")
    print("✅ Passed:")
    for p in passed:
        print(f"  - {p}")
    print("❌ Missing:")
    for f in failed:
        print(f"  - {f}")

    if not failed:
        print("🎉 This password is strong!")
    else:
        print("⚠️ This password needs improvement.")

# Example: test a single password
if __name__ == "__main__":
    user_input = input("Enter a password to check: ")
    check_password_strength(user_input)
