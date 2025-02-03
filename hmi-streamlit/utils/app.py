import streamlit as st
from utils.config import Config
from utils.api_client import APIClient
from utils.initial_page import InitialPage
from utils.sensor_temperature_page import SensorTemperaturePage

class APP:
    def __init__(self, conf: Config):
        # --- Dados de configuração do aplicativo --- #
        self._conf = conf
        # --- --- #

        # --- Inicialização do cliente da API --- #
        self._api_client = APIClient(
            f'http://{self._conf.web_server_host}:{self._conf.web_server_port}'
        )
        # --- --- #

    def run(self):
        """
        # run
        Inicia o aplicativo.
        """
        # Configuração da página principal
        st.set_page_config(
            page_title='HMI Plantação de Café',
            layout='wide'
        )

        # Barra lateral com um combobox para selecionar a tela do sensor
        opcao = st.sidebar.selectbox(
            "Selecione a Página:",
            [
                "Página inicial",
                "Sensor de temperatura ambiente (°C)",
                "Sensor de nível de irrigação (Litros/Hora)",
                "Sensor de índice de radiação solar (W/m²)",
                "Sensor de velocidade do vento (m/s)",
                "Sensor de umidade do solo (%)",
                "Sensor de pH do solo (pH)",
                "Sensor de temperatura do solo (°C)",
                "Sensor de concentração de nitrogênio no solo (ppm de Nitrogênio)",
                "Sensor de presença de pragas (0/1) (deteccao binaria: Sim/Nao)"
            ]
        )

        # espaçamento extra
        st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

        # Alterna para a tela correspondente ao sensor selecionado
        if opcao == "Página inicial":
            pagina = InitialPage()
            pagina.show()
        elif opcao == "Sensor de temperatura ambiente (°C)":
            pagina = SensorTemperaturePage(self._conf.sensor_temperature_page, self._api_client)
            pagina.show()