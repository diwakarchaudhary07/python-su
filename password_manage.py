import json

FILE_NAME = "passwords.json"

# Load existing passwords
def load_passwords():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save passwords
def save_passwords(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add new password
def add_password(data):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data[website] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("✅ Password saved!")

# View passwords
def view_passwords(data):
    if not data:
        print("No passwords saved.")
        return

    for site, info in data.items():
        print(f"\n🌐 {site}")
        print(f"👤 Username: {info['username']}")
        print(f"🔑 Password: {info['password']}")

# Main program
def main():
    data = load_passwords()

    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_password(data)
        elif choice == '2':
            view_passwords(data)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()