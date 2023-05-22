from typing import Dict, List, Union

from pydantic import BaseModel

from ...core.base import Invoice, P2SHScript


class PayResponse(BaseModel):
    amount: int
    fee: int
    amount_with_fee: int
    initial_balance: int
    balance: int


class InvoiceResponse(BaseModel):
    amount: int
    invoice: Union[Invoice, None] = None
    hash: Union[str, None] = None
    initial_balance: int
    balance: int


class BalanceResponse(BaseModel):
    balance: int
    keysets: Union[Dict, None] = None
    mints: Union[Dict, None] = None


class SendResponse(BaseModel):
    balance: int
    token: str
    npub: Union[str, None] = None


class ReceiveResponse(BaseModel):
    initial_balance: int
    balance: int


class BurnResponse(BaseModel):
    balance: int


class PendingResponse(BaseModel):
    pending_token: Dict


class LockResponse(BaseModel):
    P2SH: Union[str, None]


class LocksResponse(BaseModel):
    locks: List[P2SHScript]


class InvoicesResponse(BaseModel):
    invoices: List[Invoice]


class WalletsResponse(BaseModel):
    wallets: Dict


class InfoResponse(BaseModel):
    version: str
    wallet: str
    debug: bool
    cashu_dir: str
    mint_url: str
    settings: Union[str, None]
    tor: bool
    nostr_public_key: Union[str, None] = None
    nostr_relays: List[str] = []
    socks_proxy: Union[str, None] = None
