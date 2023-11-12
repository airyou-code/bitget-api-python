# AccountMixin

The `AccountMixin` is a mixin class included in the BitGet API Python client, providing methods related to account endpoints. It simplifies interactions with account-related API calls.

### AccountMixin Methods

- `get_account_info()`: Get account information.
- `get_account_assets(coin=None, asset_type=None)`: Get account assets.
- `get_account_bills(coin=None, group_type=None, business_type=None, start_time=None, end_time=None, limit=100, id_less_than=None)`: Get account bills.
- `transfer_assets(from_type, to_type, amount, coin, symbol=None, client_oid=None)`: Transfer assets between different productType accounts.
- `get_transfer_records(coin, from_type, start_time, end_time, client_oid=None, limit=100, id_less_than=None)`: Get transfer records.
- `withdraw_coins(coin, transfer_type, address, chain=None, inner_to_type=None, area_code=None, tag=None, size, remark=None, client_oid=None)`: Withdraw coins.
- `get_deposit_address(coin, chain=None)`: Get deposit address.
- `get_deposit_records(coin=None, order_id=None, start_time, end_time, id_less_than=None, limit=20)`: Get deposit records.
- `get_withdrawal_records(coin=None, client_oid=None, start_time, end_time, id_less_than=None, order_id=None, limit=20)`: Get withdrawal records.

## Example Usage

```python
from bitget_api_python import BitgetAuth, Client

# Initialize the client with your API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'
api_passphrase = 'your_api_passphrase'
client = Client(api_key, api_secret, api_passphrase)

# Get account information
account_info = client.get_account_info()
print(account_info)

# Get account assets
account_assets = client.get_account_assets()
print(account_assets)

# Get account bills
account_bills = client.get_account_bills(start_time='1690196141868', end_time='1690196141869')
print(account_bills)

# Transfer assets
transfer_response = client.transfer_assets('spot', 'cross_margin', '10', 'BTC')
print(transfer_response)

# Get transfer records
transfer_records = client.get_transfer_records('BTC', 'spot', '1690196141868', '1690196141869')
print(transfer_records)

# Withdraw coins
withdrawal_response = client.withdraw_coins('BTC', 'on_chain', 'your_withdrawal_address', 'btc_chain', size='10')
print(withdrawal_response)

# Get deposit address
deposit_address = client.get_deposit_address('BTC')
print(deposit_address)

# Get deposit records
deposit_records = client.get_deposit_records('BTC', start_time='1690196141868', end_time='1690196141869')
print(deposit_records)

# Get withdrawal records
withdrawal_records = client.get_withdrawal_records('BTC', start_time='1690196141868', end_time='1690196141869')
print(withdrawal_records)
```