import random

class MyVirtualSensors:
    """
    # MyVirtualSensors
    Classe que implementa a leitura de sensores virtuais para simulação de um sistema de automação agrícola.
    """
    def __init__(self, floating_point: bool = False):
        # --- Se o valor vai ser de ponto flutuante --- #
        self._floating_point = floating_point
        # --- --- #

        # --- Sensores --- #
        self._sensor_ambient_temperature = 0
        self._sensor_irrigation_level = 0
        self._sensor_solar_radiation_index = 0
        self._sensor_wind_speed = 0
        self._sensor_soil_moisture = 0
        self._sensor_soil_ph = 0
        self._sensor_soil_temperature = 0
        self._sensor_soil_nitrogen_concentration = 0
        self._sensor_pest_presence = False
        # --- --- #
    
    @property
    def sensor_ambient_temperature(self):
        return self._sensor_ambient_temperature
    
    @property
    def sensor_irrigation_level(self):
        return self._sensor_irrigation_level
    
    @property
    def sensor_solar_radiation_index(self):
        return self._sensor_solar_radiation_index
    
    @property
    def sensor_wind_speed(self):
        return self._sensor_wind_speed
    
    @property
    def sensor_soil_moisture(self):
        return self._sensor_soil_moisture
    
    @property
    def sensor_soil_ph(self):
        return self._sensor_soil_ph
    
    @property
    def sensor_soil_temperature(self):
        return self._sensor_soil_temperature
    
    @property
    def sensor_soil_nitrogen_concentration(self):
        return self._sensor_soil_nitrogen_concentration
    
    @property
    def sensor_pest_presence(self):
        return self._sensor_pest_presence

    def get_one_sensor(self, sensor: int):
        """
        # get_one_sensor
        Metodo para obter a leitura de um sensor especifico.
        """
        match sensor:
            case 0:
                self._get_ambient_temperature()
            case 1:
                self._get_irrigation_level()
            case 2:
                self._get_solar_radiation_index()
            case 3:
                self._get_wind_speed()
            case 4:
                self._get_soil_moisture()
            case 5:
                self._get_soil_ph()
            case 6:
                self._get_soil_temperature()
            case 7:
                self._get_soil_nitrogen_concentration()
            case 8:
                self._get_pest_presence()
            case _:
                pass
    
    def get_all_sensors(self):
        """
        # get_all_sensors
        Metodo para obter a leitura de todos os sensores.
        """
        self._get_ambient_temperature()
        self._get_irrigation_level()
        self._get_solar_radiation_index()
        self._get_wind_speed()
        self._get_soil_moisture()
        self._get_soil_ph()
        self._get_soil_temperature()
        self._get_soil_nitrogen_concentration()
        self._get_pest_presence()

    def _get_ambient_temperature(self):
        """
        # _get_ambient_temperature
        Temperatura Ambiente (°C)
        """
        self._sensor_ambient_temperature = random.uniform(20, 35)
        if not self._floating_point:
            self._sensor_ambient_temperature = int(self._sensor_ambient_temperature)
    
    def _get_irrigation_level(self):
        """
        # _get_irrigation_level
        Nível de Irrigação (Litros/Hora)
        """
        self._sensor_irrigation_level = random.uniform(0, 100)
        if not self._floating_point:
            self._sensor_irrigation_level = int(self._sensor_irrigation_level)
    
    def _get_solar_radiation_index(self):
        """
        # _get_solar_radiation_index
        Índice de Radiação Solar (W/m²)
        """
        self._sensor_solar_radiation_index = random.uniform(0, 1000)
        if not self._floating_point:
            self._sensor_solar_radiation_index = int(self._sensor_solar_radiation_index)
    
    def _get_wind_speed(self):
        """
        # _get_wind_speed
        Velocidade do Vento (m/s)
        """
        self._sensor_wind_speed = random.uniform(0, 10)
        if not self._floating_point:
            self._sensor_wind_speed = int(self._sensor_wind_speed)
    
    def _get_soil_moisture(self):
        """
        # _get_soil_moisture
        Umidade do Solo (%)
        """
        self._sensor_soil_moisture = random.uniform(0, 100)
        if not self._floating_point:
            self._sensor_soil_moisture = int(self._sensor_soil_moisture)
    
    def _get_soil_ph(self):
        """
        # _get_soil_ph
        pH do Solo
        """
        self._sensor_soil_ph = random.uniform(0, 14)
        if not self._floating_point:
            self._sensor_soil_ph = int(self._sensor_soil_ph)
    
    def _get_soil_temperature(self):
        """
        # _get_soil_temperature
        Temperatura do Solo (°C)
        """
        self._sensor_soil_temperature = random.uniform(20, 40)
        if not self._floating_point:
            self._sensor_soil_temperature = int(self._sensor_soil_temperature)
    
    def _get_soil_nitrogen_concentration(self):
        """
        # _get_soil_nitrogen_concentration
        Concentração de Nitrogenio no Solo (ppm de Nitrogenio)
        """
        self._sensor_soil_nitrogen_concentration = random.uniform(0, 100)
        if not self._floating_point:
            self._sensor_soil_nitrogen_concentration = int(self._sensor_soil_nitrogen_concentration)
    
    def _get_pest_presence(self):
        """
        # _get_pest_presence
        Presença de Pragas (0/1) (deteccao binaria: Sim/Nao)
        """
        self._sensor_pest_presence = random.choice([True, False])

# if __name__ == "__main__":
#     sensors = MyVirtualSensors()
#     sensors.get_all_sensors()
#     print(f"Temperatura Ambiente: {sensors.sensor_ambient_temperature}°C")
#     print(f"Nível de Irrigação: {sensors.sensor_irrigation_level} Litros/Hora")
#     print(f"Índice de Radiação Solar: {sensors.sensor_solar_radiation_index} W/m²")
#     print(f"Velocidade do Vento: {sensors.sensor_wind_speed} m/s")
#     print(f"Umidade do Solo: {sensors.sensor_soil_moisture}%")
#     print(f"pH do Solo: {sensors.sensor_soil_ph}")
#     print(f"Temperatura do Solo: {sensors.sensor_soil_temperature}°C")
#     print(f"Concentração de Nitrogenio no Solo: {sensors.sensor_soil_nitrogen_concentration} ppm de Nitrogenio")
#     print(f"Presença de Pragas: {'Sim' if sensors.sensor_pest_presence else 'Não'}")
