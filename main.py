import json
import os

import requests
from dotenv import load_dotenv
from pycognito.utils import RequestsSrpAuth

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

auth = RequestsSrpAuth(
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_pool_id=os.getenv("USER_POOL_ID"),
    client_id=os.getenv("APP_CLIENT_ID"),
    user_pool_region=os.getenv("USER_POOL_REGION"),
)

orion_endpoint = os.getenv("ORION_ENDPOINT")

response = requests.get(orion_endpoint + "/version", auth=auth)
str_json = json.dumps(response.json(), indent=4)
print(str_json)
