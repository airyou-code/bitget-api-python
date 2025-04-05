from .bitget_auth import BitgetAuth
from . import mixins


class Client(BitgetAuth, mixins.AccountMixin, mixins.MarketMixin):
    """
    Bitget API Client.
    """
