from flask_restx import Namespace, Resource, fields
from hbnb.business.facade import HBnBFacade

api_namespace = Namespace("hbnb", description="HBnB API namespace")

# Simple DTO model for users
user_model = api_namespace.model(
    "User",
    {
        "id": fields.String(readonly=True, description="User identifier"),
        "username": fields.String(required=True, description="Username"),
        "email": fields.String(required=True, description="User email"),
    },
)

# facade instance (singleton for simplicity)
_facade = HBnBFacade()

@api_namespace.route("/users")
class UsersList(Resource):
    @api_namespace.expect(user_model, validate=True)
    @api_namespace.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        payload = api_namespace.payload
        created = _facade.create_user(payload)
        return created, 201

    def get(self):
        """List all users"""
        return _facade.list_users(), 200

@api_namespace.route("/users/<string:user_id>")
class UserItem(Resource):
    @api_namespace.marshal_with(user_model)
    def get(self, user_id):
        """Get a user by id"""
        user = _facade.get_user(user_id)
        if not user:
            api_namespace.abort(404, "User not found")
        return user
