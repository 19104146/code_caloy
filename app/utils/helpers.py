import json
from functools import cache
from json.decoder import JSONDecodeError

from typing_extensions import Any, Dict


@cache
def get_routes() -> Dict[str, Any]:
    try:
        with open("routes.json", "r") as f:
            routes = json.load(f)
        return routes
    except (JSONDecodeError, FileNotFoundError) as e:
        raise Exception(f"Error reading routes.json: {e}")
