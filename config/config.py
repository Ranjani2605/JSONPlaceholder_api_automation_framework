import os
from dotenv import load_dotenv

load_dotenv()


class config:
    ENV = os.getenv("ENV", "qa")

    BASE_URLS = {
        "qa": "https://jsonplaceholder.typicode.com",
        "dev": "https://jsonplaceholder.tyicode.com",
        "staging": "https://jsonplaceholder.typicode.com",
        "prod": "https://jsonplaceholder.typicode.com"
    }

    TIMEOUT = int(os.getenv("TIMEOUT", 10))

    @classmethod
    def get_base_url(self):
        return cls.BASE_URLS[self.ENV]