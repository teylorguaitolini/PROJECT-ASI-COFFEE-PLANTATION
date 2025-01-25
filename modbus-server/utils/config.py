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
        self._host = ""
        self._port = 0
        # --- --- #
    
    @property
    def host(self):
        return self._host
    
    @property
    def port(self):
        return self._port

    def load(self):
        """
        # load
        Metodo que carrega as configuracoes do arquivo de configuracao.
        """
        self._config.read(self._file_path)
        self._host = self._config.get("Server", "host")
        self._port = self._config.getint("Server", "port")
