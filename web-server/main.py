from config import Config
from api import API

if __name__ == "__main__":
    try:
        # --- Leitura do arquivo de configuracao --- #
        conf = Config()
        conf.load()
        # --- --- #

        api = API(conf.host, conf.port)
    except KeyboardInterrupt:
        print("Encerrando o Web Server...")