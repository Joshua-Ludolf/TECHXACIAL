from flask_login import UserMixin

# In-memory user store to avoid MySQL dependency during development
_users_store = {}
_next_id = 1

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_by_id(user_id):
        for uid, rec in _users_store.items():
            if uid == user_id:
                return User(id=uid, username=rec['username'], password=rec['password'])
        return None

    @staticmethod
    def get_by_username(username):
        for uid, rec in _users_store.items():
            if rec['username'] == username:
                return (uid, rec['username'], rec['password'])
        return 0

    @staticmethod
    def create_user(username, password):
        global _next_id
        # Simple overwrite if username exists
        for uid, rec in _users_store.items():
            if rec['username'] == username:
                _users_store[uid]['password'] = password
                return
        _users_store[_next_id] = {'username': username, 'password': password}
        _next_id += 1

