from ftplib import FTP


class client:
    def __init__(self,hostname:str,username:str,password:str):
        self.hostname = hostname
        self.username = username
        self.password = password