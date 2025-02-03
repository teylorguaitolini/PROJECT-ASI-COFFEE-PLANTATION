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
        self._sensor_temperature_page = 0
        self._sensor_soil_moisture_page = 0
        self._sensor_irrigation_level_page = 0
        self._sensor_solar_index_page = 0
        self._sensor_wind_speed_page = 0
        self._sensor_soil_ph_page = 0
        self._sensor_nutrient_concentration_page = 0
        self._sensor_pest_detection_page = 0
        self._sensor_biomass_production_page = 0
        self._sensor_soil_temperature_page = 0
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
    def sensor_temperature_page(self):
        return self._sensor_temperature_page

    @property
    def sensor_soil_moisture_page(self):
        return self._sensor_soil_moisture_page

    @property
    def sensor_irrigation_level_page(self):
        return self._sensor_irrigation_level_page

    @property
    def sensor_solar_index_page(self):
        return self._sensor_solar_index_page

    @property
    def sensor_wind_speed_page(self):
        return self._sensor_wind_speed_page

    @property
    def sensor_soil_ph_page(self):
        return self._sensor_soil_ph_page

    @property
    def sensor_nutrient_concentration_page(self):
        return self._sensor_nutrient_concentration_page

    @property
    def sensor_pest_detection_page(self):
        return self._sensor_pest_detection_page

    @property
    def sensor_biomass_production_page(self):
        return self._sensor_biomass_production_page

    @property
    def sensor_soil_temperature_page(self):
        return self._sensor_soil_temperature_page

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
        self._sensor_temperature_page = self._config.getint("Pages-Update-Interval", "sensor_temperature_page")
        self._sensor_soil_moisture_page = self._config.getint("Pages-Update-Interval", "sensor_soil_moisture_page")
        self._sensor_irrigation_level_page = self._config.getint("Pages-Update-Interval", "sensor_irrigation_level_page")
        self._sensor_solar_index_page = self._config.getint("Pages-Update-Interval", "sensor_solar_index_page")
        self._sensor_wind_speed_page = self._config.getint("Pages-Update-Interval", "sensor_wind_speed_page")
        self._sensor_soil_ph_page = self._config.getint("Pages-Update-Interval", "sensor_soil_ph_page")
        self._sensor_nutrient_concentration_page = self._config.getint("Pages-Update-Interval", "sensor_nutrient_concentration_page")
        self._sensor_pest_detection_page = self._config.getint("Pages-Update-Interval", "sensor_pest_detection_page")
        self._sensor_biomass_production_page = self._config.getint("Pages-Update-Interval", "sensor_biomass_production_page")
        self._sensor_soil_temperature_page = self._config.getint("Pages-Update-Interval", "sensor_soil_temperature_page")

