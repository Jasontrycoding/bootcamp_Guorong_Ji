from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

def get_key(name, default=None):
    return os.getenv(name, default)

if __name__ == "__main__":
    load_env()
    print("API_KEY:", get_key("API_KEY"))
    print("DATA_DIR:", get_key("DATA_DIR"))
