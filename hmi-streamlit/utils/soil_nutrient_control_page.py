# soil_nutrient_control_page.py
import streamlit as st
import plotly.graph_objects as go
from time import sleep
from utils.api_client import APIClient
from utils.get_base64_image import get_base64_image

class SoilNutrientControlPage:
    def __init__(self, update_interval: int, api_client: APIClient):
        """
        :param update_interval: Intervalo de atualização em segundos.
        :param api_client: Instância da classe APIClient para comunicação com a API.
        """
        self._update_interval = update_interval
        self._api_client = api_client

    def show(self):
        # --- Limpa a tela --- #
        st.empty()

        st.header('HMI Estufa - Controle de Nutrientes do Solo (ppm de Nitrogênio)', divider='green')
        
        # --- Leitura do valor atual do sensor (sensor_id = 7) --- #
        try:
            data = self._api_client.read_sensor(sensor_id=7)
            reading_value = data.get("reading_value", "N/A")
        except Exception as e:
            reading_value = f"Erro: {e}"
        
        st.write(f"Concentração de Nitrogênio atual: {reading_value} ppm")
        
        # Converte o valor para numérico
        try:
            value_numeric = float(reading_value)
        except:
            value_numeric = 0
        
        # --- Criação do gauge para Nitrogênio ---
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value_numeric,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Nitrogênio (ppm)"},
            gauge={
                'axis': {'range': [0, 100]},  # Ajuste o range conforme necessário
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, 20], 'color': "lightsalmon"},
                    {'range': [20, 100], 'color': "lightblue"}
                ],
                'threshold': {
                    'line': {'color': "orange", 'width': 4},
                    'thickness': 0.75,
                    'value': value_numeric
                }
            }
        ))
        
        # --- Divisão da tela em duas colunas ---
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(gauge_fig, use_container_width=True)
        
        # --- Gráfico do histórico de Nitrogênio ---
        try:
            historical_data = self._api_client.get_readings(sensor_id=7)
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
            name='Nitrogênio'
        ))
        hist_fig.update_layout(
            title='Histórico de Nitrogênio no Solo',
            xaxis_title='Data/Hora',
            yaxis_title='Nitrogênio (ppm)'
        )
        
        with col2:
            st.plotly_chart(hist_fig, use_container_width=True)
        
        # --- Lógica de automação e exibição da imagem ---
        if value_numeric < 20:
            fertilizer_image_path = "images/nutritionON.png"
            caption = "Aplicação automática de fertilizante ativada"
        else:
            fertilizer_image_path = "images/nutritionOFF.png"
            caption = "Sistema de controle de nutrientes inativo"
        
        img_base64 = get_base64_image(fertilizer_image_path)
        image_html = f"""
            <div style="text-align: center; margin-top: 20px;">
                <img src="data:image/png;base64,{img_base64}" width="150px">
                <p>{caption}</p>
            </div>
        """
        st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
        st.sidebar.markdown(image_html, unsafe_allow_html=True)
        
        # --- Atualização periódica ---
        sleep(self._update_interval)
        st.rerun()
