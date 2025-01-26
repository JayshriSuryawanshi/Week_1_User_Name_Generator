import random
import string


adjectives = [
    "Brave", "Royal", "Golden", "Sacred", "Mystic", "Fiery",
    "Serene", "Vibrant", "Divine", "Majestic", "Noble", "Mighty",
    "Radiant", "Wise", "Loyal", "Bold", "Sacred", "Blissful",
    "Gallant", "Bright", "Courageous", "Heroic", "Glorious",
    "Powerful", "Charming", "Ethereal", "Graceful", "Ancient", "Resilient"
]

nouns = ["Tiger", "Dragon", "Eagle", "Lion", "Panda", "Fox", "Wolf"]


def generate_username(include_numbers=False, include_special_chars=False, length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Add numbers if required
    if include_numbers:
        username += str(random.randint(0, 99))


    if include_special_chars:
        username += random.choice(string.punctuation)

    if length and len(username) < length:
        username += ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(username)))
    elif length and len(username) > length:
        username = username[:length]

    return username



def save_usernames_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            file.write("\n".join(usernames))
        print(f"Usernames saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")


def main():
    print("Welcome to the Random Username Generator!")
    usernames = []

    while True:
        print("\nOptions:")
        print("1. Generate a Username")
        print("2. Save Usernames to File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
            include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            length = input("Enter desired length (or press Enter for default): ").strip()
            length = int(length) if length.isdigit() else None

            username = generate_username(include_numbers, include_special_chars, length)
            usernames.append(username)
            print(f"Generated Username: {username}")

        elif choice == "2":
            if usernames:
                save_usernames_to_file(usernames)
            else:
                print("No usernames to save!")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
