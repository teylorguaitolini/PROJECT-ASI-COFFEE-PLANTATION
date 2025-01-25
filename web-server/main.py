from utils.config import Config
from utils.api import API

if __name__ == "__main__":
    try:
        # --- Leitura do arquivo de configuracao --- #
        conf = Config()
        conf.load()
        # --- --- #

        # --- Inicializacao do Web Server --- #
        api = API(conf.web_server_host, conf.web_server_port, conf.modbus_server_host, conf.modbus_server_port)
        api.run()
        # --- --- #
    except KeyboardInterrupt:
        print("Encerrando o Web Server...")