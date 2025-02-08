import streamlit as st
import plotly.graph_objects as go
from time import sleep
from utils.api_client import APIClient
from utils.get_base64_image import get_base64_image

class AmbientTempControlPage:
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
        
        st.header('HMI Plantação em Esufa - Controle de Temperatura Ambiente (°C)', divider='green')
        
        # --- Leitura do valor atual do sensor --- #
        try:
            data = self._api_client.read_sensor(sensor_id=0)
            reading_value = data.get("reading_value", "N/A")
        except Exception as e:
            reading_value = f"Erro: {e}"
        
        st.write(f"Temperatura atual: {reading_value} °C")
        
        # Converte o valor para numérico (para uso no gauge)
        try:
            value_numeric = float(reading_value)
        except:
            value_numeric = 0

        # --- Criação do gauge (termômetro) --- #
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value_numeric,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Temperatura (°C)"},
            gauge={
                'axis': {'range': [20, 40]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [20, 30], 'color': "lightblue"},
                    {'range': [30, 35], 'color': "lightgreen"},
                    {'range': [35, 40], 'color': "lightsalmon"}
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
        
        # --- Gráfico do histórico de temperatura (na coluna 2) --- #
        try:
            historical_data = self._api_client.get_readings(sensor_id=0)
            readings_list = historical_data.get("readings", [])
        except Exception as e:
            readings_list = []
            st.error(f"Erro ao obter histórico: {e}")
        
        # Extrai datas e valores do histórico
        times = []
        values = []
        for reading in readings_list:
            times.append(reading.get("reading_datetime", ""))
            try:
                val = float(reading.get("reading_value", 0))
            except:
                val = 0
            values.append(val)
        
        # Cria o gráfico de linha para o histórico de temperatura
        hist_fig = go.Figure()
        hist_fig.add_trace(go.Scatter(
            x=times,
            y=values,
            mode='lines+markers',
            name='Temperatura'
        ))
        hist_fig.update_layout(
            title='Histórico de Temperatura',
            xaxis_title='Data/Hora',
            yaxis_title='Temperatura (°C)'
        )
        
        with col2:
            st.plotly_chart(hist_fig, use_container_width=True)
        
        # --- Exibe imagem do ventilador na sidebar, abaixo do combobox --- #
        # Se a temperatura for maior que 35°C, exibe imagem do ventilador ligado; senão, desligado.
        if value_numeric > 35:
            fan_image_path = "images/fanON.png"
            caption = "Ventilador de Nebulização Ligado"
        else:
            fan_image_path = "images/fanOFF.png"
            caption = "Ventilador de Nebulização Desligado"
        
        img_base64 = get_base64_image(fan_image_path)
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
