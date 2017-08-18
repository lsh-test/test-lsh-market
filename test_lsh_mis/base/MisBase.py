import ConfigParser
import os,sys


cf = ConfigParser.ConfigParser()
#cf.read(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]) + "/conf/mis_config.ini")

class MisBase:
    def __init__(self,environment,module,confPath):
        self.environment = environment
        self.module = module
        cf.read(confPath)

    def getEmail(self):
        email = cf.get("mis_user","email")
        return email

    def getPassword(self):
        password = cf.get("mis_user","password")
        return password

    def getHost(self):
        if self.environment == 'qa':
            host = cf.get("mis_host","qa_host")
            return host
        elif self.environment == 'qa2':
            host = cf.get("mis_host", "qa2_host")
            return host
        elif self.environment == 'qa3':
            host = cf.get("mis_host", "qa3_host")
            return host