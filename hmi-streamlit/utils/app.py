import streamlit as st
from utils.config import Config
from utils.api_client import APIClient
from utils.initial_page import InitialPage
from utils.irrigation_control_page import IrrigationControlPage
from utils.ambient_temp_control_page import AmbientTempControlPage
from utils.sunlight_control_page import SunlightControlPage
from utils.pest_control_page import PestControlPage

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
            page_title='HMI Plantação em Estufa',
            layout='wide'
        )

        # Barra lateral com um combobox para selecionar a tela do sensor
        option = st.sidebar.selectbox(
            "Selecione a Página:",
            [
                "Página inicial",
                "Controle de Irrigação (Umidade %)",
                "Controle de Temperatura Ambiente (°C)",
                "Controle de Iluminação Solar (W/m²)",
                "Controle de Pragas (Binário)",
                "Controle de Nutrientes do Solo (ppm de Nitrogênio)"
            ]
        )

        # Cria um container principal para o conteúdo da página
        page_container = st.empty()

        # Alterna para a tela correspondente ao sensor selecionado
        if option == "Página inicial":
            page_container.empty()
            page = InitialPage()
            page.show()
        elif option == "Controle de Irrigação (Umidade %)":
            page_container.empty()
            IrrigationControlPage(self._conf.irrigation_control_page, self._api_client).show()
        elif option == "Controle de Temperatura Ambiente (°C)":
            page_container.empty()
            AmbientTempControlPage(self._conf.ambient_temp_control_page, self._api_client).show()
        elif option == "Controle de Iluminação Solar (W/m²)":
            page_container.empty()
            SunlightControlPage(self._conf.sunlight_control_page, self._api_client).show()
        elif option == "Controle de Pragas (Binário)":
            page_container.empty()
            PestControlPage(self._conf.pest_control_page, self._api_client).show()
        elif option == "Controle de Nutrientes do Solo (ppm de Nitrogênio)":
            pass
