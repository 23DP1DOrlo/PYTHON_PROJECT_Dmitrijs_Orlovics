import json

class AuthManager:
    def __init__(self, filepath="Data/users.json"):
        self.filepath = filepath
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filepath, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_users(self):
        with open(self.filepath, "w") as file:
            json.dump(self.users, file, indent=4)

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return True, f"Login successful as {username}."
        return False, "Invalid username or password."

    def sign_up(self, username, password):
        for user in self.users:
            if user["username"] == username:
                return False, "Username already exists."
        self.users.append({"username": username, "password": password})
        self.save_users()
        return True, f"User {username} successfully registered."
