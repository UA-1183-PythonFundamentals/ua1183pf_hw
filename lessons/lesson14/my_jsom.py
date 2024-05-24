import json
from user import User

json_str_user = """
    {
        "user_id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 28,
        "country": "United States"
    }
"""

user = json.loads(json_str_user)
print(user)
print(user.get("email"))

json_str_user = """[
    {
        "user_id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 28,
        "country": "United States"
    },
    {
        "user_id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "age": 34,
        "country": "Canada"
    },
    {
        "user_id": 3,
        "name": "Bob Johnson",
        "email": "bobjohnson@example.com",
        "age": 45,
        "country": "United Kingdom"
    }
]

"""

user = json.loads(json_str_user)
print(user)
print(user[0].get("email"))



if __name__ == "__main__":
    
    USERS = []
    with open('data.txt') as file:
        colum_names = file.readline()
        for row in file:
            user = User(*(row.split(",")))
            USERS.append(user)

    with open("users.json", "w") as write_file:
        users = [user.to_dict() for user in USERS]
        json.dump(users, write_file)
