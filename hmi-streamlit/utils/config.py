from configparser import ConfigParser
from os import path
from os import getcwd

class Config:
    """
    # Config
    Classe para leitura do arquivo de configuração.
    """
    def __init__(self):
        # --- Inicializacao do caminho do arquivo de configuracao --- #
        self._file_path = path.join(getcwd(), "hmi-streamlit", "utils", "config.ini")
        # --- --- #

        # --- Inicializacao do parser de configuracao --- #
        self._config = ConfigParser()
        # --- --- #

        # --- Inicializacao dos atributos de configuracao --- #
        # [Web-Server]
        self._web_server_host = ""
        self._web_server_port = 0

        # [Pages-Update-Interval]
        self._irrigation_control_page = 0
        self._ambient_temp_control_page = 0
        self._sunlight_control_page = 0
        self._pest_control_page = 0
        self._soil_nutrient_control_page = 0
        # --- --- #

    # [Web-Server]
    @property
    def web_server_host(self):
        return self._web_server_host

    @property
    def web_server_port(self):
        return self._web_server_port

    # [Pages-Update-Interval]
    @property
    def irrigation_control_page(self):
        return self._irrigation_control_page

    @property
    def ambient_temp_control_page(self):
        return self._ambient_temp_control_page
    
    @property
    def sunlight_control_page(self):
        return self._sunlight_control_page
    
    @property
    def pest_control_page(self):
        return self._pest_control_page
    
    @property
    def soil_nutrient_control_page(self):
        return self._soil_nutrient_control_page

    def load(self):
        """
        # load
        Metodo que carrega as configuracoes do arquivo de configuracao.
        """
        self._config.read(self._file_path)

        # [Web-Server]
        self._web_server_host = self._config.get("Web-Server", "host")
        self._web_server_port = self._config.getint("Web-Server", "port")

        # [Pages-Update-Interval]
        self._irrigation_control_page = self._config.getint("Pages-Update-Interval", "irrigation_control_page")
        self._ambient_temp_control_page = self._config.getint("Pages-Update-Interval", "ambient_temp_control_page")
        self._sunlight_control_page = self._config.getint("Pages-Update-Interval", "sunlight_control_page")
        self._pest_control_page = self._config.getint("Pages-Update-Interval", "pest_control_page")
        self._soil_nutrient_control_page = self._config.getint("Pages-Update-Interval", "soil_nutrient_control_page")
