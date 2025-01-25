from pyModbusTCP.server import DataBank
from utils.MyVirtualSensors import MyVirtualSensors

class MyDataBank(DataBank):
    """
    # MyDataBank
    Classe que herda de DataBank e implementa uma personalização do metodo get_holding_registers.
    \n
    Este servidor Modbus terá a seguinte estrutura de registradores:
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
    def __init__(self):
        super().__init__()

        # --- Inicializacao dos sensores virtuais --- #
        self._sensors = MyVirtualSensors()
        # --- --- #

    def get_holding_registers(self, address, number=1, srv_info=None):
        """
        # get_holding_registers
        Metodo que retorna o valor dos registradores de holding. 
        """
        try:
            result = []
            for i in range(address, address + number):
                value = self._sensors.get_sensor_data(i)
                self._h_regs[i] = value
                result.append(value)
            return result
        except KeyError:        
            return
        