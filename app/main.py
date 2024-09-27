import logging

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from utils.constants import ANSI, ENDPOINTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Code Caloy",
    description="An API for testing C code",
    version="1.0.0",
)


@app.get("/", response_class=PlainTextResponse)
def root() -> str:
    margin = max(len(endpoint) for endpoint in ENDPOINTS.keys()) + 2

    output = [
        f"{ANSI['BOLD']}{ANSI['UNDERLINE']}Usage:{ANSI['RESET']} curl <endpoint>\n\n",
        f"{ANSI['BOLD']}{ANSI['UNDERLINE']}Endpoints:{ANSI['RESET']}\n",
    ]

    for endpoint, description in ENDPOINTS.items():
        output.append(f"{endpoint:<{margin}}{description}\n")

    return "".join(output)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )
