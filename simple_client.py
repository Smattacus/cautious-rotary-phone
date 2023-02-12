import requests
import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnvVars:
    ENDPOINT = "APP_ENDPOINT"
    PROTOCOL = "APP_PROTOCOL"

class APIConfig:

    def __init__(self):
        self._endpoint = os.environ.get(EnvVars.ENDPOINT, "localhost:8000")
        self._protocol = os.environ.get(EnvVars.PROTOCOL, "http")

    def __str__(self):
        return f"{self._protocol}://{self._endpoint}/"

newline = '\n'

config = APIConfig()

for i in range(5):
    logger.info(f"Sending request to {config}")
    r = requests.get(f"bad_endpoint")
    logging.info(f"Request returned! Result: {r}: {r.text.rstrip(newline)}")
