from configparser import ConfigParser
from os import path
from sys import path as sys_path

class Config:
    def __init__(self):
        self._file_path = path.join(sys_path[0], "config.ini")
        self._config = ConfigParser()

        self._host = ""
        self._port = 0
        self._data_points = {}
    
    @property
    def host(self):
        return self._host
    
    @property
    def port(self):
        return self._port
    
    @property
    def data_points(self):
        return self._data_points

    def load(self):
        self._config.read(self._file_path)

        self._host = self._config.get("Server", "host")
        self._port = self._config.getint("Server", "port")

        if "DataPoints" in self._config:
            for key, value in self._config["DataPoints"].items():
                self._data_points[int(key)] = value