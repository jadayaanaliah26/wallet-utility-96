from enum import Enum, unique

@unique
class ErrorCode(Enum):
    INVALID_ADDRESS = "ERR_001"
    INSUFFICIENT_FUNDS = "ERR_002"
    NETWORK_TIMEOUT = "ERR_003"
    API_LIMIT_EXCEEDED = "ERR_004"
    TRANSACTION_FAILED = "ERR_005"

MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
SUPPORTED_NETWORKS = {"mainnet", "testnet", "devnet"}

MIN_TX_AMOUNT = 1e-18
MAX_TX_AMOUNT = 1e12

ERROR_MESSAGES = {
    ErrorCode.INVALID_ADDRESS: "The provided wallet address format is invalid",
    ErrorCode.INSUFFICIENT_FUNDS: "Account balance is lower than requested amount",
    ErrorCode.NETWORK_TIMEOUT: "Node connection timed out during broadcast",
    ErrorCode.API_LIMIT_EXCEEDED: "Rate limit exceeded for blockchain node RPC",
    ErrorCode.TRANSACTION_FAILED: "Transaction validation failed at the protocol layer"
}