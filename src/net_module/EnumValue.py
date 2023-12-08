from enum import Enum
class ConnectionState(Enum):
    NONE=0
    CONNECTING=1
    DISCONNECTION=2

class MessageType(Enum):
    CIPHER=0
    PG=1
    PUBKEY=2
    