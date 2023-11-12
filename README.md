# bitget-api-python Library

The `bitget-api-python` library is designed for interacting with the API endpoints of the BitGet exchange. It provides an easy-to-use interface for making authenticated requests to the BitGet trading platform.

## Installation

You can install this library using pip:

```bash
pip install git+https://github.com/airyou-code/bitget-api-python.git
```

Uninstall:

```bash
pip uninstall bitget_api_python 
```

## Introduction

BitGet is a cryptocurrency exchange platform that offers a wide range of trading features and services. This library allows you to access and utilize the BitGet API to automate trading operations, retrieve market data, and manage your account.



## Usage

[BitGet Quick Start](https://www.bitget.com/api-doc/common/quick-start)

To use the BitGet API Python client, you need to initialize a `Client` instance with your API credentials. The `Client` class includes mixins for trading and account management

Mixins:
 - `AccountMixin` provides methods for account management, such as getting account information, balances, and transaction history. ([Docs](docs/accountmixin.md))

 - ~~`MarketMixin` provides methods for retrieving market data, such as ticker information, order book, and recent trades.~~ ***not released**

 - ~~`TradeMixin` provides methods for trading operations, such as placing limit and market orders, canceling orders, and getting order status.~~ ***not released**

 <!-- - `BitgetAuth` class is used to sign requests with your API credentials. This class is used internally by the

 - `Client` class, and you do not need to use it directly. -->

## Examples

Here is an example of how to use the `Client` class to get account information:

```python
from bitget_api_python import BitgetAuth, Client

# Initialize the client with your API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'
api_passphrase = 'your_api_passphrase'
client = Client(api_key, api_secret, api_passphrase)

# Account-related methods are now available through the client instance.
# For example, you can get account information like this:
account_info = client.get_account_info()
print(account_info)
```

## License

This library is distributed under the [GNU General Public License (GPL) version 3](LICENSE).
## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or pull requests, please open an issue or submit a pull request on the [GitHub repository](https://github.com/airyou-code/bitget-api-python).

Please note that this is a beta release, and we welcome your feedback and contributions. If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/airyou-code/bitget-api-python/issues) on our GitHub repository.

Thank you for using the BitGet API Python client library!
