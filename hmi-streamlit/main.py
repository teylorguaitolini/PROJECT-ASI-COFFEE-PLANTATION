from utils.app import APP
from utils.config import Config

if __name__ == "__main__":
    # --- Leitura do arquivo de configuracao --- #
    conf = Config()
    conf.load()
    # --- --- #

    # --- Iniciar o aplicativo --- #
    app = APP(conf)
    app.run()
    # --- --- #