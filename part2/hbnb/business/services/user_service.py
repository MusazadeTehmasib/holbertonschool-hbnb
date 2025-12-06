class UserService:
    def __init__(self, repository):
        self._repo = repository
        self._model_name = "User"

    def create_user(self, payload):
        # basic validation
        if not payload.get("username"):
            raise ValueError("username is required")
        if not payload.get("email"):
            raise ValueError("email is required")

        # prepare data (strip unexpected keys)
        data = {"username": payload["username"], "email": payload["email"]}
        created = self._repo.create(self._model_name, data)
        return created

    def get_user(self, user_id):
        return self._repo.get(self._model_name, user_id)

    def list_users(self):
        return self._repo.list(self._model_name)
