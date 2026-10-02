import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class WalletSession:
    address: str
    network: str
    active: bool = True

class WalletHandler:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.sessions: Dict[str, WalletSession] = {}

    def create_session(self, address: str, network: str = 'mainnet') -> str:
        if not address.startswith('0x'):
            raise ValueError('Invalid address format')
        session_id = f'sess_{address[-8:]}'
        self.sessions[session_id] = WalletSession(address, network)
        self.logger.info(f'session created for {address}')
        return session_id

    def terminate_session(self, session_id: str) -> bool:
        if session_id in self.sessions:
            del self.sessions[session_id]
            self.logger.info(f'terminated session {session_id}')
            return True
        return False

    def get_status(self, session_id: str) -> Optional[Dict[str, Any]]:
        session = self.sessions.get(session_id)
        if not session:
            return None
        return {'address': session.address, 'network': session.network}
