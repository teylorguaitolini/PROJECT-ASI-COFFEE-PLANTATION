from pyModbusTCP.client import ModbusClient

class MyModbusClient:
    def __init__(self, host: str, port: int):
        # --- Dicionario de sensores do servidor --- #
        self._sensors = {
            0: "Sensor de temperatura ambiente (°C)",
            1: "Sensor de nível de irrigação (Litros/Hora)",
            2: "Sensor de índice de radiação solar (W/m²)",
            3: "Sensor de velocidade do vento (m/s)",
            4: "Sensor de umidade do solo (%)",
            5: "Sensor de pH do solo (pH)",
            6: "Sensor de temperatura do solo (°C)",
            7: "Sensor de concentração de nitrogênio no solo (ppm de Nitrogênio)",
            8: "Sensor de presença de pragas (0/1) (deteccao binaria: Sim/Nao)"
        }
        # --- --- #

        # --- Cliente Modbus --- #
        self._client = ModbusClient(host=host, port=port)
        # --- --- #
    
    def get_sensors_id(self):
        """
        # get_sensors
        Retorna a lista de sensores do servidor
        """
        return list(self._sensors.keys())
    
    def get_sensor_description(self, sensor_id: int):
        """
        # get_sensor_description
        Retorna a descrição do sensor
        """
        return self._sensors.get(sensor_id, None)
    
    def read_sensor_data(self, sensor_id: int):
        """
        # read_sensor_data
        Leitura de dados do sensor
        """
        if self._client.open():
            sensor_value = self._client.read_holding_registers(sensor_id)
            self._client.close()
            return sensor_value
        else:
            return None

# if __name__ == "__main__":
#     client = MyModbusClient("localhost", 5010)
#     for i in client.get_sensors_id():
#         print(f"Sensor ID: {i} -- Descrição: {client.get_sensor_description(i)} -- Valor: {client.read_sensor_data(i)}")
