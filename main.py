from scrapli import Scrapli
from dotenv import load_dotenv

class EltexSW:
    def __init__(self, username, password, host):
        self.username = username
        self.password = password
        self.host = host
        self.switch = {
            "host": self.host,
            "auth_username": self.username,
            "auth_password": self.password,
            "auth_strict_key": False,
            "ssh_config_file": True,
            "channel_log": True,
            "platform": "eltex_esr",
            "timeout_ops": 65,
            "timeout_transport": 65,
            "timeout_socket": 65,
        }

