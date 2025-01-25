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

    def get_sensor_data(self, sensor: int):
        """
        # get_sensor_data
        Metodo para obter a leitura de um sensor especifico.
        \n
        - 0: Sensor de temperatura ambiente
        - 1: Sensor de nível de irrigação
        - 2: Sensor de índice de radiação solar
        - 3: Sensor de velocidade do vento
        - 4: Sensor de umidade do solo
        - 5: Sensor de pH do solo
        - 6: Sensor de temperatura do solo
        - 7: Sensor de concentração de nitrogênio no solo
        - 8: Sensor de presença de pragas
        """
        value = None

        match sensor:
            case 0:
                value = self._get_ambient_temperature()
            case 1:
                value = self._get_irrigation_level()
            case 2:
                value = self._get_solar_radiation_index()
            case 3:
                value = self._get_wind_speed()
            case 4:
                value = self._get_soil_moisture()
            case 5:
                value = self._get_soil_ph()
            case 6:
                value = self._get_soil_temperature()
            case 7:
                value = self._get_soil_nitrogen_concentration()
            case 8:
                value = self._get_pest_presence()
            case _:
                pass
        
        return value

    def _get_ambient_temperature(self):
        """
        # _get_ambient_temperature
        Temperatura Ambiente (°C)
        """
        sensor_ambient_temperature = random.uniform(20, 35)
        if not self._floating_point:
            sensor_ambient_temperature = int(sensor_ambient_temperature)
        return sensor_ambient_temperature
    
    def _get_irrigation_level(self):
        """
        # _get_irrigation_level
        Nível de Irrigação (Litros/Hora)
        """
        sensor_irrigation_level = random.uniform(0, 100)
        if not self._floating_point:
            sensor_irrigation_level = int(sensor_irrigation_level)
        return sensor_irrigation_level
    
    def _get_solar_radiation_index(self):
        """
        # _get_solar_radiation_index
        Índice de Radiação Solar (W/m²)
        """
        sensor_solar_radiation_index = random.uniform(0, 1000)
        if not self._floating_point:
            sensor_solar_radiation_index = int(sensor_solar_radiation_index)
        return sensor_solar_radiation_index
    
    def _get_wind_speed(self):
        """
        # _get_wind_speed
        Velocidade do Vento (m/s)
        """
        sensor_wind_speed = random.uniform(0, 10)
        if not self._floating_point:
            sensor_wind_speed = int(sensor_wind_speed)
        return sensor_wind_speed
    
    def _get_soil_moisture(self):
        """
        # _get_soil_moisture
        Umidade do Solo (%)
        """
        sensor_soil_moisture = random.uniform(0, 100)
        if not self._floating_point:
            sensor_soil_moisture = int(sensor_soil_moisture)
        return sensor_soil_moisture
    
    def _get_soil_ph(self):
        """
        # _get_soil_ph
        pH do Solo
        """
        sensor_soil_ph = random.uniform(0, 14)
        if not self._floating_point:
            sensor_soil_ph = int(sensor_soil_ph)
        return sensor_soil_ph
    
    def _get_soil_temperature(self):
        """
        # _get_soil_temperature
        Temperatura do Solo (°C)
        """
        sensor_soil_temperature = random.uniform(20, 40)
        if not self._floating_point:
            sensor_soil_temperature = int(sensor_soil_temperature)
        return sensor_soil_temperature
    
    def _get_soil_nitrogen_concentration(self):
        """
        # _get_soil_nitrogen_concentration
        Concentração de Nitrogenio no Solo (ppm de Nitrogenio)
        """
        sensor_soil_nitrogen_concentration = random.uniform(0, 100)
        if not self._floating_point:
            sensor_soil_nitrogen_concentration = int(sensor_soil_nitrogen_concentration)
        return sensor_soil_nitrogen_concentration
    
    def _get_pest_presence(self):
        """
        # _get_pest_presence
        Presença de Pragas (0/1) (deteccao binaria: Sim/Nao)
        """
        if random.choice([True, False]):
            sensor_pest_presence = 1
        else:
            sensor_pest_presence = 0
        return sensor_pest_presence

# if __name__ == "__main__":
#     sensors = MyVirtualSensors()
#     for i in range(9):
#         print(f"{i}: {sensors.get_sensor_data(i)}")

