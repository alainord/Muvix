import json
import os
import hashlib

class UserManager:
    def __init__(self, filename="users_db.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def _load_users(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_users(self, users):
        with open(self.filename, "w") as f:
            json.dump(users, f, indent=4)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def username_exists(self, username):
        users = self._load_users()
        for user in users:
            if user["username"] == username:
                return True
        return False

    def register_user(self, full_name, username, password):
        if self.username_exists(username):
            return False, "Username already exists"

        users = self._load_users()
        new_user = {
            "full_name": full_name,
            "username": username,
            "password": self._hash_password(password)
        }

        users.append(new_user)
        self._save_users(users)
        
        return True, "User registered successfully"

    # --- NEW METHOD FOR LOGIN ---
    def login_user(self, username, password):
        """
        Verify credentials.
        Returns: (Success, User data or Error message)
        """
        users = self._load_users()
        hashed_pw = self._hash_password(password)

        for user in users:
            # Compare username and the hashed password
            if user["username"] == username and user["password"] == hashed_pw:
                return True, user # Correct login
        
        return False, "Invalid username or password"