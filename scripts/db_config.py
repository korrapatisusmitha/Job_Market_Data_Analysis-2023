import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('config')/'.env'
load_dotenv(dotenv_path=env_path)  # This reads .env and loads values into os.environ

'''
user = os.getenv("DB_USER")
print(user)  # → your_username (from .env)
'''

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# print("success👍")