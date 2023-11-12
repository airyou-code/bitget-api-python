"""
Basic building blocks for Clients classes
"""


class AccountMixin:
    """
    Account metods
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
