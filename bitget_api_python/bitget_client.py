from .bitget_auth import BitgetAuth
from . import mixins


class Client(BitgetAuth, mixins.AccountMixin):
    """
    Bitget API Client.
    """
