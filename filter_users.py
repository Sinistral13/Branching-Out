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
        print(f"No users with name {name}  found.")
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

    filtered_users = [user for user in users if user["age"] == int(age)]

    if not filtered_users:
        print(f"No users with name {age}  found.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_email(email):
    """
    Filter users in a .json file by email.
    Print found users.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    if not filtered_users:
        print(f"No users with name {email}  found.")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
