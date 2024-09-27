import os
import re
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
        self.connect_switch()

    def connect_switch(self):
        try:
            self.connect = Scrapli(**self.switch)
            self.connect.open()

        except Exception as E:
            print(f"Error connecting to OLT: {E}")

    def mac_address_table_vlan(self, vlanid):
        output = self.connect.send_command("show mac address-table | exclude te").result
        rez = re.findall(f'^\s+{vlanid}\s+(\S+)\s+(\S+)',output,re.MULTILINE)
        return rez
    def send_command(self, command):
        output = self.connect.send_command(command).result
        return output

    def close_switch(self):
        self.connect.close()



if __name__ == '__main__':
    load_dotenv()
    eltex = EltexSW(username=os.getenv('USERNAME'), password= os.getenv('PASSWORD'), host='10.35.8.62')
    output = eltex.mac_address_table_vlan('6')
    for i in output:
        print(i,f'//SIGA-KORP4-P3-SW0 - {eltex.host} - {i[1]}')
    eltex.close_switch()