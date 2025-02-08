import streamlit as st
import plotly.graph_objects as go
from time import sleep
from utils.api_client import APIClient
from utils.get_base64_image import get_base64_image

class IrrigationControlPage:
    def __init__(self, update_interval: int, api_client: APIClient):
        """
        :param update_interval: Intervalo de atualização em segundos.
        :param api_client: Instância da classe APIClient para comunicação com a API.
        """
        self._update_interval = update_interval  # em segundos
        self._api_client = api_client

    def show(self):
        # --- Limpa a tela --- #
        st.empty()
        st.header('HMI Plantação em Esufa - Controle de Irrigação (Umidade do Solo %)', divider='green')
        
        # --- Leitura do valor atual do sensor de umidade (sensor_id = 1) --- #
        try:
            data = self._api_client.read_sensor(sensor_id=1)
            reading_value = data.get("reading_value", "N/A")
        except Exception as e:
            reading_value = f"Erro: {e}"
        
        st.write(f"Umidade do Solo atual: {reading_value} %")
        
        # Converte o valor para numérico para uso nos gráficos e nas condições
        try:
            value_numeric = float(reading_value)
        except:
            value_numeric = 0

        # --- Criação do gauge (indicador) para umidade do solo --- #
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value_numeric,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Umidade do Solo (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "blue"},
                'steps': [
                    {'range': [0, 30], 'color': "lightsalmon"},
                    {'range': [30, 80], 'color': "lightblue"},
                    {'range': [80, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "orange", 'width': 4},
                    'thickness': 0.75,
                    'value': value_numeric
                }
            }
        ))
        
        # --- Divisão da tela em duas colunas --- #
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(gauge_fig, use_container_width=True)
        
        # --- Gráfico do histórico de umidade (na coluna 2) --- #
        try:
            historical_data = self._api_client.get_readings(sensor_id=1)
            readings_list = historical_data.get("readings", [])
        except Exception as e:
            readings_list = []
            st.error(f"Erro ao obter histórico: {e}")
        
        times = []
        values = []
        for reading in readings_list:
            times.append(reading.get("reading_datetime", ""))
            try:
                val = float(reading.get("reading_value", 0))
            except:
                val = 0
            values.append(val)
        
        hist_fig = go.Figure()
        hist_fig.add_trace(go.Scatter(
            x=times,
            y=values,
            mode='lines+markers',
            name='Umidade do Solo'
        ))
        hist_fig.update_layout(
            title='Histórico de Umidade do Solo',
            xaxis_title='Data/Hora',
            yaxis_title='Umidade (%)'
        )
        
        with col2:
            st.plotly_chart(hist_fig, use_container_width=True)
        
        # --- Exibe imagem do sistema de irrigação na sidebar --- #
        # Inicialize o estado se ainda não existir
        if "irrigation_state" not in st.session_state:
            st.session_state.irrigation_state = "off"  # valor inicial

        # Atualiza o estado somente se ultrapassar os limites
        if value_numeric < 30:
            st.session_state.irrigation_state = "on"
        elif value_numeric > 80:
            st.session_state.irrigation_state = "off"

        # Agora, de acordo com o estado armazenado, define a imagem e a legenda
        if st.session_state.irrigation_state == "on":
            irrigation_image_path = "images/irrigationON.png"
            caption = "Sistema de Irrigação Ativado"
        else:
            irrigation_image_path = "images/irrigationOFF.png"
            caption = "Sistema de Irrigação Desativado"
        
        # Converte a imagem para base64 e insere na sidebar com espaçamento e centralização
        img_base64 = get_base64_image(irrigation_image_path)
        image_html = f"""
            <div style="text-align: center; margin-top: 20px;">
                <img src="data:image/png;base64,{img_base64}" width="150px">
                <p>{caption}</p>
            </div>
            """
        st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
        st.sidebar.markdown(image_html, unsafe_allow_html=True)
        
        # --- Atualização periódica --- #
        sleep(self._update_interval)
        st.rerun()
