import requests

from config import config
from utils.logger import get_logger


class BaseClient:

    def __init__(self):
        self.base_url = config.Config.get_base_url()
        self.timeout = config.Config.TIMEOUT
        self.logger = get_logger(self.__class__.__name__)


    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"GET Request URL: {url}")
        self.logger.info(f"Query Params: {params}")

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=self.timeout
        )

    def post(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"POST Request URL: {url}")
        self.logger.info(f"Request payload: {payload}")

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response



    def put(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.infp(f"PUT Request URL: {url}")
        self.logger.info(f"Request payload: {payload}")

        response = requests.put(
            url,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response

    def patch(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"PATCH Request URL: {url}")
        self.logger.info(f"Request payload: {payload}")

        response = requests.patch(
            url,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response


    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE Request URL: {url}")

        response = requests.delete(
            url,
            headers=headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response

    def _log_response(self, response):
        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")





