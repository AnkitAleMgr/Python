from urllib import response
import requests, os, traceback
from dotenv import load_dotenv

load_dotenv() # <-- creating object name load_dotenv() to acess .env file data

# Access token imported from .env file
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# url/ Link
BASE_URL = os.getenv("BASE_URL")


def main_operation():
    
    # header for
    post_header = dict()
    






def main():
    main_operation()

if __name__ == "__main__":
    main()