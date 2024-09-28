import json
from functools import cache
from json.decoder import JSONDecodeError

from typing_extensions import Any, Dict


@cache
def get_courses() -> Dict[str, Any]:
    try:
        with open("app/configs/courses.json", "r") as f:
            courses = json.load(f)
        return courses
    except (JSONDecodeError, FileNotFoundError) as e:
        raise Exception(f"Error reading courses.json: {e}")
