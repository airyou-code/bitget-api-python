"""
Basic building blocks for Clients classes
"""


class MarketMixin:
    """
    Market methods

    Methods:
        - get_symbol_info -> Response
        - get_ticker_info -> Response
        - get_merge_depth -> Response
        - get_orderbook_depth -> Response
        - get_candlestick_data -> Response
    """

    def get_symbol_info(self, symbol=None):
        """
        Get spot trading pair information, supporting both individual and full queries.

        docs:
            - https://www.bitget.com/api-doc/spot/public/symbols
        HTTP Request:
            GET /api/v2/spot/public/symbols

        Parameters:
            - symbol (str, optional): Trading pair name, e.g. BTCUSDT.
              If omitted, returns information for all trading pairs.

        Returns:
            A dictionary with trading pair information.

        Returns example:
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
        """
        endpoint = "/api/v2/spot/public/symbols"
        params = {}
        if symbol:
            params["symbol"] = symbol

        return self.get(endpoint, params=params)

    def get_ticker_info(self, symbol=None):
        """
        Get ticker information, supporting both single and batch queries.

        docs:
            - https://www.bitget.com/api-doc/spot/market/tickers
        HTTP Request:
            GET /api/v2/spot/market/tickers

        Parameters:
            - symbol (str, optional): Trading pair name, e.g. BTCUSDT.
              If omitted, returns ticker information for all trading pairs.

        Returns:
            A dictionary with ticker information.

        Returns example:
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
        """
        endpoint = "/api/v2/spot/market/tickers"
        params = {}
        if symbol:
            params["symbol"] = symbol

        return self.get(endpoint, params=params)

    def get_merge_depth(self, symbol, precision="scale0", limit="100"):
        """
        Get merge depth.

        docs:
            - https://www.bitget.com/api-doc/spot/market/merge-depth
        HTTP Request:
            GET /api/v2/spot/market/merge-depth

        Parameters:
            - symbol (str, required): Trading pair, e.g. BTCUSDT.
            - precision (str, optional): Price precision for cumulative depth.
              Options: scale0, scale1, scale2, scale3. Default is "scale0" (without merging).
            - limit (str, optional): Limit parameter. Default is "100". Options include: 1, 5, 15, 50, max.

        Returns:
            A dictionary with merge depth data.

        Returns example:
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
        """
        endpoint = "/api/v2/spot/market/merge-depth"
        params = {"symbol": symbol, "precision": precision, "limit": limit}
        return self.get(endpoint, params=params)

    def get_orderbook_depth(self, symbol, type="step0", limit="150"):
        """
        Get order book depth.

        docs:
            - https://www.bitget.com/api-doc/spot/market/orderbook
        HTTP Request:
            GET /api/v2/spot/market/orderbook

        Parameters:
            - symbol (str, required): Trading pair, e.g. BTCUSDT.
            - type (str, optional): Type of depth. Default is "step0".
              Options: step0, step1, step2, step3, step4, step5.
            - limit (str, optional): Number of entries to return.
              Default is "150" (maximum 150).

        Returns:
            A dictionary with order book depth data.

        Returns example:
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
        """
        endpoint = "/api/v2/spot/market/orderbook"
        params = {"symbol": symbol, "type": type, "limit": limit}
        return self.get(endpoint, params=params)

    def get_candlestick_data(
        self, symbol, granularity, startTime=None, endTime=None, limit="100"
    ):
        """
        Get candlestick data.

        docs:
            - https://www.bitget.com/api-doc/spot/market/candles
        HTTP Request:
            GET /api/v2/spot/market/candles

        Parameters:
            - symbol (str, required): Trading pair, e.g. BTCUSDT.
            - granularity (str, required): Time interval for candlesticks.
              Examples: 1min, 3min, 5min, 15min, 30min, 1h, 4h, 6h, 12h, 1day, 3day, 1week, 1M, etc.
            - startTime (str, optional): Start time of the interval (Unix timestamp in milliseconds).
            - endTime (str, optional): End time of the interval (Unix timestamp in milliseconds).
            - limit (str, optional): Number of data entries to return. Default "100", maximum "1000".

        Returns:
            A dictionary containing candlestick data as a list of lists.
            Each nested list contains:
                [timestamp, open, high, low, close, base volume, USDT volume, quote volume]

        Example return value:
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
        """
        endpoint = "/api/v2/spot/market/candles"
        params = {"symbol": symbol, "granularity": granularity, "limit": limit}
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        return self.get(endpoint, params=params)

    def get_history_candlestick_data(self, symbol, granularity, endTime, limit="100"):
        """
        Get historical candlestick data.

        Docs:
            - https://www.bitget.com/api-doc/spot/market/history-candles
        HTTP Request:
            GET /api/v2/spot/market/history-candles

        Parameters:
            symbol (str): Trading pair, e.g. "BTCUSDT".
            granularity (str): Time interval for candlesticks. Examples: "1min", "3min", "5min", "15min", "30min", "1h", etc.
            endTime (str): End time for the candlestick data (Unix timestamp in milliseconds).
            limit (str, optional): Number of data points to return. Default is "100", maximum is "200".

        Returns:
            dict: A dictionary containing historical candlestick data as a list of lists.
                Each inner list includes:
                [timestamp, open, high, low, close, base volume, USDT volume, quote volume].

        Example return:
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
                    // ... more candlesticks
                ]
            }
        """
        endpoint = "/api/v2/spot/market/history-candles"
        params = {
            "symbol": symbol,
            "granularity": granularity,
            "endTime": endTime,
            "limit": limit
        }
        return self.get(endpoint, params=params)
    
    def get_recent_trades(self, symbol, limit="100"):
        """
        Get recent trades.

        Docs:
            - https://www.bitget.com/api-doc/spot/market/fills
        HTTP Request:
            GET /api/v2/spot/market/fills

        Parameters:
            symbol (str): Trading pair name, e.g. "BTCUSDT".
            limit (str, optional): Number of trades to return. Default is "100", maximum is "500".

        Returns:
            dict: A dictionary containing recent trades data.
                Each trade includes:
                - symbol (str): Trading pair.
                - tradeId (str): Order ID.
                - side (str): Direction ("buy" or "sell").
                - price (str): Order price.
                - size (str): Filled quantity.
                - ts (str): Transaction time (Unix timestamp in milliseconds).

        Example return:
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
        """
        endpoint = "/api/v2/spot/market/fills"
        params = {
            "symbol": symbol,
            "limit": limit
        }
        return self.get(endpoint, params=params)

    def get_market_trades(self, symbol, limit="500", idLessThan=None, startTime=None, endTime=None):
        """
        Get market trades.

        Docs:
            - https://www.bitget.com/api-doc/spot/market/fills-history
        HTTP Request:
            GET /api/v2/spot/market/fills-history

        Parameters:
            symbol (str): Trading pair name, e.g. "BTCUSDT".
            limit (str, optional): Number of data returned. Default is "500", maximum is "1000".
            idLessThan (str, optional): Order ID; returns records with tradeId less than the specified value.
            startTime (str, optional): Start time (Unix millisecond timestamp, e.g. "1690196141868").
            endTime (str, optional): End time (Unix millisecond timestamp, e.g. "1690196141868"). 
                                    startTime and endTime should be within 7 days.

        Returns:
            dict: A dictionary containing market trades data.
                Each trade includes:
                    - symbol (str): Trading pair.
                    - tradeId (str): Order ID.
                    - side (str): Direction ("buy" or "sell").
                    - price (str): Order price.
                    - size (str): Filled quantity.
                    - ts (str): Transaction time (Unix millisecond timestamp).

        Example return:
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
        """
        endpoint = "/api/v2/spot/market/fills-history"
        params = {
            "symbol": symbol,
            "limit": limit
        }
        if idLessThan:
            params["idLessThan"] = idLessThan
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        return self.get(endpoint, params=params)


class AccountMixin:
    """
    Account metods

    Methods:
        - get_account_info -> Response
        - get_account_assets -> Response
        - get_account_bills -> Response
        - transfer_assets -> Response
        - get_transfer_records -> Response
        - withdraw_coins -> Response
        - get_deposit_address -> Response
        - get_deposit_records -> Response
        - get_withdrawal_records -> Response
    """
    def get_account_info(self):
        """
        Get account information.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Get-Account-Info
        HTTP Request:
        GET /api/v2/spot/account/info

        Parameters:
        N/A

        Returns:
        A dictionary containing account information.
        """
        endpoint = "/api/v2/spot/account/info"
        return self.get(endpoint)

    def get_account_assets(self, coin=None, asset_type="hold_only"):
        """
        Get account assets.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Get-Account-Assets

        HTTP Request:
        GET /api/v2/spot/account/assets

        Parameters:
        - coin (str, optional):
            Token name, e.g. USDT.
            Used for querying the positions of a single coin.
        - asset_type (str, optional): Asset type. Default is "hold_only".
            - "hold_only": Position coin
            - "all": All coins

        Returns:
        A list of dictionaries containing account assets information.
        """
        endpoint = "/api/v2/spot/account/assets"
        params = {}
        if coin:
            params["coin"] = coin
        params["assetType"] = asset_type

        return self.get(endpoint, params=params)

    def get_account_bills(
        self,
        coin=None,
        group_type=None,
        business_type=None,
        start_time=None,
        end_time=None,
        limit=100,
        id_less_than=None,
    ):
        """
        Get account bills.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Get-Account-Bills

        HTTP Request:
        GET /api/v2/spot/account/bills

        Parameters:
        - coin (str, optional): Token name, e.g. USDT.
        - group_type (str, optional): Billing type.
        - business_type (str, optional): Business type of billing.
        - start_time (str, optional): The start time of the billing history.
        - end_time (str, optional): The end time of the billing history.
        - limit (int, optional):
            Number of results returned. Default is 100, maximum is 500.
        - id_less_than (str, optional):
            Requests the content on the page before this ID (older data).

        Returns:
        A list of dictionaries containing account bills information.
        """
        endpoint = "/api/v2/spot/account/bills"
        params = {}
        if coin:
            params["coin"] = coin
        if group_type:
            params["groupType"] = group_type
        if business_type:
            params["businessType"] = business_type
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        if limit:
            params["limit"] = limit
        if id_less_than:
            params["idLessThan"] = id_less_than

        return self.get(endpoint, params=params)

    def transfer_assets(self, from_type, to_type, amount, coin,
                        symbol=None, client_oid=None):
        """
        Transfer assets between different productType accounts.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Wallet-Transfer

        HTTP Request:
        POST /api/v2/spot/wallet/transfer

        Parameters:
        - from_type (str): Account type to transfer from.
        - to_type (str): Account type to transfer to.
        - amount (str): Amount to transfer.
        - coin (str): Currency of transfer.
        - symbol (str, optional):
            Required when transferring to or from
            a leveraged position-by-position account.
        - client_oid (str, optional): Custom order ID.

        Returns:
        A dictionary containing the transfer information.
        """
        endpoint = "/api/v2/spot/wallet/transfer"
        data = {
            "fromType": from_type,
            "toType": to_type,
            "amount": amount,
            "coin": coin,
        }
        if symbol:
            data["symbol"] = symbol
        if client_oid:
            data["clientOid"] = client_oid

        return self.post(endpoint, body=data)

    def get_transfer_records(
        self,
        coin,
        from_type,
        start_time=None,
        end_time=None,
        client_oid=None,
        limit=100,
        id_less_than=None,
    ):
        """
        Get transfer records.

        docs:
        https://www.bitget.com/api-doc/spot/account/Get-Account-TransferRecords

        HTTP Request:
        GET /api/v2/spot/account/transferRecords

        Parameters:
        - coin (str): Token name.
        - from_type (str): Account type to transfer from.
        - start_time (str, optional): The start time of the transfer history.
        - end_time (str, optional): The end time of the transfer history.
        - client_oid (str, optional): Order ID customized by user.
        - limit (int, optional):
            Number of results returned. Default is 100, maximum is 500.
        - id_less_than (str, optional):
            Requests the content on the page before this ID (older data).

        Returns:
        A list of dictionaries containing transfer records information.
        """
        endpoint = "/api/v2/spot/account/transferRecords"
        params = {
            "coin": coin,
            "fromType": from_type,
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        if client_oid:
            params["clientOid"] = client_oid
        if limit:
            params["limit"] = limit
        if id_less_than:
            params["idLessThan"] = id_less_than

        return self.get(endpoint, params=params)

    def withdraw_coins(
        self,
        coin,
        transfer_type,
        address,
        size,
        chain=None,
        inner_to_type=None,
        area_code=None,
        tag=None,
        remark=None,
        client_oid=None,
    ):
        """
        Withdraw coins, including on-chain withdrawals and internal transfers.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Wallet-Withdrawal

        HTTP Request:
        POST /api/v2/spot/wallet/withdrawal

        Parameters:
        - coin (str): Coin to withdraw.
        - transfer_type (str): Withdrawal type (on_chain or internal_transfer).
        - address (str): Holder address.
        - chain (str, optional):
            Blockchain network (e.g., erc20, trc20)
            required for on-chain withdrawals.
        - inner_to_type (str, optional):
            Type of address for internal withdrawals (email, mobile, uid).
        - area_code (str, optional): Required when the address type is mobile.
        - tag (str, optional): Address tag.
        - size (str): Amount to withdraw.
        - remark (str, optional): Note.
        - client_oid (str, optional): Custom order ID.

        Returns:
        A dictionary containing the withdrawal information.
        """
        endpoint = "/api/v2/spot/wallet/withdrawal"
        data = {
            "coin": coin,
            "transferType": transfer_type,
            "address": address,
            "size": size,
        }
        if chain:
            data["chain"] = chain
        if inner_to_type:
            data["innerToType"] = inner_to_type
        if area_code:
            data["areaCode"] = area_code
        if tag:
            data["tag"] = tag
        if remark:
            data["remark"] = remark
        if client_oid:
            data["clientOid"] = client_oid

        return self.post(endpoint, data=data)

    def get_deposit_address(self, coin, chain=None):
        """
        Get deposit address.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Get-Deposit-Address

        HTTP Request:
        GET /api/v2/spot/wallet/deposit-address

        Parameters:
        - coin (str): Coin name (e.g., USDT).
        - chain (str, optional): Chain name (e.g., trc20).

        Returns:
        A dictionary containing deposit address information.
        """
        endpoint = "/api/v2/spot/wallet/deposit-address"
        params = {"coin": coin}
        if chain:
            params["chain"] = chain

        return self.get(endpoint, params=params)

    def get_deposit_records(self, start_time, end_time,
                            coin=None, order_id=None,
                            id_less_than=None, limit=20):
        """
        Get deposit records.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Get-Deposit-Record

        HTTP Request:
        GET /api/v2/spot/wallet/deposit-records

        Parameters:
        - coin (str, optional): Coin name (e.g., USDT).
        - order_id (str, optional): The response orderId.
        - start_time (str):
            The record start time for the query (Unix millisecond timestamp).
        - end_time (str):
            The end time of the record for the query
            (Unix millisecond timestamp).
        - id_less_than (str, optional):
            Requests the content on the page before this ID (older data).
        - limit (int, optional):
            Number of entries per page (default: 20, maximum: 100).

        Returns:
        A list of deposit records.
        """
        endpoint = "/api/v2/spot/wallet/deposit-records"
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
        }
        if coin:
            params["coin"] = coin
        if order_id:
            params["orderId"] = order_id
        if id_less_than:
            params["idLessThan"] = id_less_than

        return self.get(endpoint, params=params)

    def get_withdrawal_records(self, start_time, end_time,
                               coin=None, client_oid=None,
                               id_less_than=None, order_id=None, limit=20):
        """
        Get withdrawal records.

        docs:
            - https://www.bitget.com/api-doc/spot/account/Get-Withdraw-Record

        HTTP Request:
        GET /api/v2/spot/wallet/withdrawal-records

        Parameters:
        - coin (str, optional): Coin name (e.g., USDT).
        - client_oid (str, optional): Client customized ID.
        - start_time (str):
            The record start time for the query
            (Unix millisecond timestamp).
        - end_time (str):
            The end time of the record for the query
            (Unix millisecond timestamp).
        - id_less_than (str, optional):
            Requests the content on the page before this ID (older data).
        - order_id (str, optional): The response orderId.
        - limit (int, optional):
            Number of entries per page (default: 20, maximum: 100).

        Returns:
        A list of withdrawal records.
        """
        endpoint = "/api/v2/spot/wallet/withdrawal-records"
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
        }
        if coin:
            params["coin"] = coin
        if client_oid:
            params["clientOid"] = client_oid
        if id_less_than:
            params["idLessThan"] = id_less_than
        if order_id:
            params["orderId"] = order_id

        return self.get(endpoint, params=params)
