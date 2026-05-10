import json

def filter_users_by_name(name):
    """
    Filter users in a .json file by name.
    Print found users.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if not filtered_users:
        print(f'No users with name "{name}" found.')
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_age(age):
    """
    Filter users in a .json file by age.
    Print found users.
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    try:    #not needed in this structure, added for scaling
        filtered_users = [user for user in users if user["age"] == int(age)]
        if not filtered_users:
            print(f'No users with age "{age}" found.')
        else:
            for user in filtered_users:
                print(user)
    except ValueError:
        print(f'"{age}" is not a number.')


def filter_users_by_email(email):
    """
    Filter users in a .json file by email.
    Print found users.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    if not filtered_users:
        print(f'No users with email "{email}" found.')
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = input('What would you like to filter by?' 
                    '(Currently, "name", "age" and "email" are supported\n').strip().lower()

    if filter_option == "name":
        while True:
            name_to_search = input("Enter a name to filter users: ").strip()

            if name_to_search:
                break

            print("Name is required for filtering. Please try again.")
    
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        while True:
            age_to_search = input("Enter an age to filter users: ").strip()

            try:
                age_to_search = int(age_to_search)
                break
            except ValueError:
                print(f'"{age_to_search}" is not a valid number.')

        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()

            if email_to_search:
                break

            print("Email is required for filtering. Please try again.")
    
        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
