import hmac
import base64
import hashlib
import time
import requests
from requests import Response
# from requests.exceptions import ConnectionError
from urllib.parse import urlencode


class BitgetAuth:
    """
    Handles authentication for the Bitget API.

    Methods:
    - __init__(self, api_key, api_secret, api_passphrase) -> None
    - get_timestamp() -> int
    - ping() -> bool
    - _pre_hash(timestamp, method, endpoint, params=None, body=None) -> str
    - sign(timestamp, method, endpoint, params=None, body=None) -> bytes
    - _headers(signature, timestamp) -> dict
    - get_headers(method, endpoint, params=None, body=None) -> dict
    - get(endpoint, params=None, body=None) -> Response

    Fields:
    - api_key: The API key provided during initialization.
    - api_secret: The API secret provided during initialization.
    - api_passphrase: The API passphrase provided during initialization.
    - is_connected: A boolean indicating whether the instance
        is connected to the Bitget API.
    - HOST: The base URL of the Bitget API.
    """

    api_key: str
    api_secret: str
    api_passphrase: str
    is_connected: bool
    HOST = "https://api.bitget.com"

    def __init__(self, api_key, api_secret, api_passphrase) -> None:
        """
        Initializes the BitgetAuth instance.

        Args:
        - api_key (str): The API key.
        - api_secret (str): The API secret.
        - api_passphrase (str): The API passphrase.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.is_connected = self.ping()

    @staticmethod
    def get_timestamp() -> int:
        """
        Returns the current timestamp in milliseconds.

        Returns:
        - int: The current timestamp in milliseconds.
        """
        return int(time.time() * 1000)

    def ping(self) -> bool:
        """
        Checks the connection to the Bitget API.

        Returns:
        - bool: True if the connection is successful, False otherwise.
        """
        res = requests.get(
            self.HOST + "/api/v2/public/time"
        )
        if res.status_code == 200 and (
            "code" in res.json() and res.json()["code"] == 0
        ):
            return True

        return False

    @staticmethod
    def _pre_hash(timestamp, method,
                  endpoint, params=None, body=None) -> str:
        """
        Prepares the data for hashing.

        Args:
        - timestamp (int): The timestamp in milliseconds.
        - method (str): The HTTP method.
        - endpoint (str): The API endpoint.
        - params (dict, optional): The query parameters. Defaults to None.
        - body (str, optional): The request body. Defaults to None.

        Returns:
        - str: The pre-hashed data.
        """
        param_str = ("?" + urlencode(params)) if params else ''
        body_str = body if body else ''
        return (str(timestamp) + str.upper(method) + endpoint
                + param_str + body_str)

    def sign(self, timestamp, method,
             endpoint, params=None, body=None) -> bytes:
        """
        Signs the request.

        Args:
        - timestamp (int): The timestamp in milliseconds.
        - method (str): The HTTP method.
        - endpoint (str): The API endpoint.
        - params (dict, optional): The query parameters. Defaults to None.
        - body (str, optional): The request body. Defaults to None.

        Returns:
        - bytes: The base64-encoded signature.
        """
        pre_hash = self._pre_hash(
            timestamp, method, endpoint,
            params, body
        ).encode()
        mac = hmac.new(self.api_secret.encode(), pre_hash, hashlib.sha256)
        return base64.b64encode(mac.digest())

    def _headers(self, signature, timestamp) -> dict:
        """
        Returns the headers for a request.

        Args:
        - signature (bytes): The base64-encoded signature.
        - timestamp (int): The timestamp in milliseconds.

        Returns:
        - dict: The headers template.
        """
        return {
            'ACCESS-KEY': self.api_key,
            'ACCESS-SIGN': signature,
            'ACCESS-PASSPHRASE': self.api_passphrase,
            'ACCESS-TIMESTAMP': str(timestamp),
            'Content-Type': 'application/json'
        }

    def get_headers(self, method, endpoint, params=None, body=None) -> dict:
        """
        Returns the headers for a request.

        Args:
        - method (str): The HTTP method.
        - endpoint (str): The API endpoint.
        - params (dict, optional): The query parameters. Defaults to None.
        - body (str, optional): The request body. Defaults to None.

        Returns:
        - dict: The headers for the request.
        """
        timestamp = self.get_timestamp()
        signature = self.sign(timestamp, method, endpoint, params, body)
        return self._headers(signature, timestamp)

    def get(self, endpoint, params=None, body=None) -> Response:
        """
        Makes a GET request to the Bitget API.

        Args:
        - endpoint (str): The API endpoint.
        - params (dict, optional): The query parameters. Defaults to None.
        - body (str, optional): The request body. Defaults to None.

        Returns:
        - Response
        """
        url = self.HOST + endpoint
        response = requests.get(
            url,
            headers=self.get_headers(
                "GET", endpoint, params, body
            ),
            params=params
        )
        return response

    def post(self, endpoint, params=None, body=None) -> Response:
        """
        Makes a POST request to the Bitget API.

        Args:
        - endpoint (str): The API endpoint.
        - params (dict, optional): The query parameters. Defaults to None.
        - body (str, optional): The request body. Defaults to None.

        Returns:
        - Response
        """
        url = self.HOST + endpoint
        response = requests.post(
            url,
            headers=self.get_headers(
                "POST", endpoint, params, body
            ),
            params=params
        )
        return response
