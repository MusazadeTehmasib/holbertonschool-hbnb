from hbnb.persistence.in_memory.repository import InMemoryRepository
from hbnb.business.services.user_service import UserService

class HBnBFacade:
    def __init__(self):
        # In a real app you'd inject a repo instance (for testing, etc.)
        self._repo = InMemoryRepository()
        self.users = UserService(self._repo)

    # convenience methods used by the presentation layer
    def create_user(self, data):
        return self.users.create_user(data)

    def get_user(self, user_id):
        return self.users.get_user(user_id)

    def list_users(self):
        return self.users.list_users()
