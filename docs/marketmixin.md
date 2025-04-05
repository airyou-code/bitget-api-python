# MarketMixin

The `MarketMixin` is a mixin class included in the BitGet API Python client, providing methods related to market endpoints. It simplifies interactions with market-related API calls.

### MarketMixin Methods

- **`get_symbol_info(symbol=None)`**:  
  Retrieves spot trading pair information.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695808949356,
      "data": [
          {
              "symbol": "BTCUSDT",
              "baseCoin": "BTC",
              "quoteCoin": "USDT",
              "minTradeAmount": "0.0001",
              "maxTradeAmount": "10000",
              "takerFeeRate": "0.001",
              "makerFeeRate": "0.001",
              "pricePrecision": "4",
              "quantityPrecision": "8",
              "quotePrecision": "4",
              "minTradeUSDT": "5",
              "status": "online",
              "buyLimitPriceRatio": "0.05",
              "sellLimitPriceRatio": "0.05",
              "orderQuantity": "100",
              "areaSymbol": "no"
          }
      ]
  }
  ```

- **`get_ticker_info(symbol=None)`**:  
  Retrieves ticker information, supporting both single and batch queries.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695808949356,
      "data": [
          {
              "symbol": "BTCUSDT",
              "high24h": "37775.65",
              "open": "35134.2",
              "low24h": "34413.1",
              "lastPr": "34413.1",
              "quoteVolume": "0",
              "baseVolume": "0",
              "usdtVolume": "0",
              "bidPr": "0",
              "askPr": "0",
              "bidSz": "0.0663",
              "askSz": "0.0119",
              "openUtc": "23856.72",
              "ts": "1625125755277",
              "changeUtc24h": "0.00301",
              "change24h": "0.00069"
          }
      ]
  }
  ```

- **`get_merge_depth(symbol, precision="scale0", limit="100")`**:  
  Retrieves merge depth data for a trading pair with specified price precision and limit parameters.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695808949356,
      "data": {
          "asks": [
              ["38084.5", "0.0039"],
              ["38085.7", "0.0018"],
              ["38086.7", "0.0310"],
              ["38088.2", "0.5303"]
          ],
          "bids": [
              ["38073.7", "0.4993"],
              ["38073.4", "0.4500"],
              ["38073.3", "0.1179"],
              ["38071.5", "0.2162"]
          ],
          "ts": "1622102974025",
          "scale": "0.1",
          "precision": "scale0",
          "isMaxPrecision": "YES"
      }
  }
  ```

- **`get_orderbook_depth(symbol, type="step0", limit="150")`**:  
  Retrieves order book depth data for a trading pair with specified depth type and limit parameters.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1698303884579,
      "data": {
          "asks": [
              ["34567.15", "0.0131"],
              ["34567.25", "0.0144"]
          ],
          "bids": [
              ["34567", "0.2917"],
              ["34566.85", "0.0145"]
          ],
          "ts": "1698303884584"
      }
  }
  ```

- **`get_candlestick_data(symbol, granularity, startTime=None, endTime=None, limit="100")`**:  
  Retrieves candlestick data for a trading pair over a specified time interval.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695800278693,
      "data": [
          [
              "1656604800000",
              "37834.5",
              "37849.5",
              "37773.5",
              "37773.5",
              "428.3462",
              "16198849.1079",
              "16198849.1079"
          ],
          [
              "1656604860000",
              "37834.5",
              "37850.0",
              "37775.0",
              "37780.0",
              "430.0000",
              "16200000.0000",
              "16200000.0000"
          ]
      ]
  }
  ```

- **`get_history_candlestick_data(symbol, granularity, endTime, limit="100")`**:  
  Retrieves historical candlestick data for a trading pair up to a specified end time.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695799900330,
      "data": [
          [
              "1646064000000",
              "43500.8",
              "48207.2",
              "38516",
              "46451.9",
              "2581.4668",
              "118062073.82644",
              "118062073.82644"
          ],
          [
              "1648742400000",
              "46451.9",
              "55199.6",
              "15522.1",
              "38892.5",
              "42331329.5473",
              "1726993402150.991724",
              "1726993402150.991724"
          ]
          // ... more candlestick entries
      ]
  }
  ```

- **`get_recent_trades(symbol, limit="100")`**:  
  Retrieves recent trades for a specified trading pair.  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695808949356,
      "data": [
          {
              "symbol": "BFTUSDT",
              "tradeId": "1",
              "side": "buy",
              "price": "2.38735",
              "size": "2470.6224",
              "ts": "1622097282536"
          },
          {
              "symbol": "BFTUSDT",
              "tradeId": "2",
              "side": "sell",
              "price": "2.38649",
              "size": "3239.7976",
              "ts": "1622097280642"
          }
      ]
  }
  ```

- **`get_market_trades(symbol, limit="500", idLessThan=None, startTime=None, endTime=None)`**:  
  Retrieves market trades data for a specified trading pair within a given time period (up to 7 days).  
  *Example Return*:  
  ```json
  {
      "code": "00000",
      "msg": "success",
      "requestTime": 1695808949356,
      "data": [
          {
              "symbol": "BTCUSDT",
              "tradeId": "1",
              "side": "buy",
              "price": "2.38735",
              "size": "2470.6224",
              "ts": "1622097282536"
          },
          {
              "symbol": "BFTUSDT",
              "tradeId": "2",
              "side": "sell",
              "price": "2.38649",
              "size": "3239.7976",
              "ts": "1622097280642"
          }
      ]
  }
  ```

## Example Usage

```python
from bitget_api_python import BitgetAuth, Client

# Initialize the client with your API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'
api_passphrase = 'your_api_passphrase'
client = Client(api_key, api_secret, api_passphrase)

# Get trading pair information
symbol_info = client.get_symbol_info()
print(symbol_info)

# Get ticker information for a specific trading pair
ticker_info = client.get_ticker_info("BTCUSDT")
print(ticker_info)

# Get merge depth data for a trading pair
merge_depth = client.get_merge_depth("BTCUSDT", precision="scale1", limit="50")
print(merge_depth)

# Get order book depth for a trading pair
orderbook_depth = client.get_orderbook_depth("BTCUSDT", type="step0", limit="150")
print(orderbook_depth)

# Get candlestick data for a trading pair
candlestick_data = client.get_candlestick_data("BTCUSDT", "1min", startTime="1659076670000", endTime="1659080270000")
print(candlestick_data)

# Get historical candlestick data for a trading pair
history_candles = client.get_history_candlestick_data("BTCUSDT", "1min", endTime="1659080270000", limit="100")
print(history_candles)

# Get recent trades for a trading pair
recent_trades = client.get_recent_trades("BTCUSDT", limit="100")
print(recent_trades)

# Get market trades for a trading pair within a specific time period
market_trades = client.get_market_trades("BTCUSDT", limit="20", startTime="1678965010861", endTime="1678965910861")
print(market_trades)
```
