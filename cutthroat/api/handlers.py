import uuid

from tornado_json.requesthandlers import APIHandler
from tornado_json.utils import io_schema


class CreateGame(APIHandler):
    apid = {}
    apid["post"] = {
        "input_schema": {
            "type": "object",
            "properties": {
                "player_names": {"type": "array"},
                "nbpp": {"type": "number"},
                "password": {"type": "string"}
            },
            "required": ["player_names", "nbpp"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "game_id": {"type": "string"}
            }
        },
        "doc": ""
    }

    @io_schema
    def post(self, body):
        """POST RequestHandler"""
        game_id = str(uuid.uuid4())
        return {"game_id": game_id}
