from config import Config
from pyModbusTCP.server import ModbusServer
from MyDataBank import MyDataBank

if __name__ == "__main__":
    try:
        # --- Leitura do arquivo de configuracao --- #
        conf = Config()
        conf.load()
        # --- --- #

        # --- Inicializacao do servidor Modbus --- #
        modbus_server = ModbusServer(host=conf.host, port=conf.port, data_bank=MyDataBank())
        modbus_server.start()
        # --- --- #
    except KeyboardInterrupt:
        print("Encerrando o Modbus Server...")
        modbus_server.stop()