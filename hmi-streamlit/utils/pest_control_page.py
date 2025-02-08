# pest_control_page.py
import streamlit as st
import plotly.graph_objects as go
from time import sleep
from utils.api_client import APIClient
from utils.get_base64_image import get_base64_image

class PestControlPage:
    def __init__(self, update_interval: int, api_client: APIClient):
        """
        :param update_interval: Intervalo de atualização em segundos.
        :param api_client: Instância da classe APIClient para comunicação com a API.
        """
        self._update_interval = update_interval  # em segundos
        self._api_client = api_client

    def show(self):
        st.header('HMI Estufa - Controle de Pragas (Binário)', divider='green')
        
        # --- Leitura do valor atual do sensor (sensor_id = 8) --- #
        try:
            data = self._api_client.read_sensor(sensor_id=8)
            reading_value = data.get("reading_value", "N/A")
        except Exception as e:
            reading_value = f"Erro: {e}"
        
        # Interpreta o valor lido como binário (1/True = Detectado)
        if reading_value in [1, "1", True, "True"]:
            st.error("Alerta: Pragas detectadas! Aplicação automática de pesticida ativada!")
            pest_status = "Ativo"
        else:
            st.success("Nenhuma praga detectada. Sistema normal.")
            pest_status = "Inativo"
        
        st.write(f"Status atual do sensor de pragas: {pest_status}")
        
        # --- Gráfico histórico ---
        try:
            historical_data = self._api_client.get_readings(sensor_id=8)
            readings_list = historical_data.get("readings", [])
        except Exception as e:
            readings_list = []
            st.error(f"Erro ao obter histórico: {e}")
        
        times = []
        values = []
        for reading in readings_list:
            times.append(reading.get("reading_datetime", ""))
            # Converte para inteiro (0 ou 1)
            try:
                val = int(reading.get("reading_value", 0))
            except:
                val = 1 if str(reading.get("reading_value", "")).lower() == "true" else 0
            values.append(val)
        
        hist_fig = go.Figure()
        hist_fig.add_trace(go.Scatter(
            x=times,
            y=values,
            mode='lines+markers',
            name='Presença de Pragas'
        ))
        hist_fig.update_layout(
            title='Histórico de Presença de Pragas',
            xaxis_title='Data/Hora',
            yaxis=dict(
                title='Presença (1 = Detectado, 0 = Não Detectado)',
                tickvals=[0, 1],
                ticktext=["Não Detectado", "Detectado"]
            )
        )
        st.plotly_chart(hist_fig, use_container_width=True)
        
        # --- Exibe imagem na sidebar com base no status ---
        if pest_status == "Ativo":
            pest_image_path = "images/pestON.png"  # imagem indicando que a aplicação de pesticida está ativa
            caption = "Aplicação automática de pesticida ativada"
        else:
            pest_image_path = "images/pestOFF.png"  # imagem indicando que o sistema está inativo
            caption = "Sistema de controle de pragas desativado"
        
        img_base64 = get_base64_image(pest_image_path)
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
