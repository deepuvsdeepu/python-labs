from configparser import ConfigParser
from pathlib import Path

def loadsecrets(secret_file = 'secrets.ini'):
    return loadConfig(str(Path.home()) + '/.private/'+ secret_file)

def loadConfig(file_name):
    print('loading config from file:' + file_name)
    config = ConfigParser()
    config.read(file_name)
    return config