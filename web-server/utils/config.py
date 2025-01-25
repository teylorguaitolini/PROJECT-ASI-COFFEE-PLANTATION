from configparser import ConfigParser
from os import path
from sys import path as sys_path

class Config:
    """
    # Config
    Classe para leitura do arquivo de configuração.
    """
    def __init__(self):
        # --- Inicializacao do caminho do arquivo de configuracao --- #
        self._file_path = path.join(sys_path[0], "utils", "config.ini")
        # --- --- #

        # --- Inicializacao do parser de configuracao --- #
        self._config = ConfigParser()
        # --- --- #

        # --- Inicializacao dos atributos de configuracao --- #
        # [Modbus-Server]
        self._modbus_server_host = ""
        self._modbus_server_port = 0
        # [Web-Server]
        self._web_server_host = ""
        self._web_server_port = 0
        # --- --- #
    
    # [Modbus-Server]
    @property
    def modbus_server_host(self):
        return self._modbus_server_host
    
    @property
    def modbus_server_port(self):
        return self._modbus_server_port
    
    # [Web-Server]
    @property
    def web_server_host(self):
        return self._web_server_host
    
    @property
    def web_server_port(self):
        return self._web_server_port

    def load(self):
        """
        # load
        Metodo que carrega as configuracoes do arquivo de configuracao.
        """
        self._config.read(self._file_path)

        # [Modbus-Server]
        self._modbus_server_host = self._config.get("Modbus-Server", "host")
        self._modbus_server_port = self._config.getint("Modbus-Server", "port")

        # [Web-Server]
        self._web_server_host = self._config.get("Web-Server", "host")
        self._web_server_port = self._config.getint("Web-Server", "port")
