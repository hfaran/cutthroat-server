from tornado_json.utils import io_schema, APIError

from cutthroat.handlers import APIHandler


class Login(APIHandler):

    """Handle authentication"""

    apid = {}
    apid["post"] = {
        "input_schema": {
            "required": ["username", "password"],
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "password": {"type": "string"},
            },
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "username": {"type": "string"}
            }
        },
        "doc": """
POST the required credentials to get back a cookie

* `username`: Username
* `password`: Password
"""
    }
    apid["get"] = {
        "input_schema": None,
        "output_schema": {"type": "string"},
        "doc": """
GET to check if authenticated. Should be obvious from status code (403 vs. 200).
"""
    }

    @io_schema
    def post(self, body):
        player_name = body["username"]
        password = body["password"]

        if self.db_conn.auth_user(player_name, password):
            self.set_secure_cookie("user", player_name)
            return {"username": player_name}
        else:
            raise APIError(
                400,
                log_message="Bad username/password combo"
            )

    @io_schema
    def get(self, body):
        if not self.get_current_user():
            raise APIError(
                403,
                log_message="Please post to {} to get a cookie".format(
                    "/api/auth/login")
            )
        else:
            return "You are already logged in."