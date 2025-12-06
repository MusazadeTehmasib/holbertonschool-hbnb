class User:
    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}
