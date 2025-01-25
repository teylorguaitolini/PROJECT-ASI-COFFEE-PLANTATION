import uvicorn
from fastapi import FastAPI
from database.createDB import createDB
from utils.MyModbusClient import MyModbusClient
from utils.sensor_dao import SensorDAO
from utils.reading_dao import ReadingDAO

class API:
    """
    # API
    Classe para inicialização do servidor web
    """

    def __init__(self, web_server_host: str, web_server_port: int, modbus_server_host: str, modbus_server_port: int):
        # --- Configuração do servidor web --- #
        self._web_server_host = web_server_host
        self._web_server_port = web_server_port
        # --- --- #

        # --- Criação do banco de dados --- #
        self._DB_PATH = createDB()
        # --- --- #

        # --- DAO para a tabela 'sensors' --- #
        self._sensor_dao = SensorDAO(self._DB_PATH)
        # --- --- #

        # --- DAO para a tabela 'sensor_readings' --- #
        self._reading_dao = ReadingDAO(self._DB_PATH)
        # --- --- #

        # --- Cliente Modbus --- #
        self._modbus_client = MyModbusClient(modbus_server_host, modbus_server_port)
        # --- --- #

        # --- Objeto FastAPI --- #
        self.app = FastAPI()
        # --- --- #

        # --- Configuração das rotas da API --- #
        self._setup_api_routes()
        # --- --- #

    def run(self):
        uvicorn.run(self.app, host=self._web_server_host, port=self._web_server_port, log_level='info')

    def _setup_api_routes(self):
        """
        Configura as rotas da API.
        """

        @self.app.get('/')
        def default():
            """
            Rota raiz que não faz nada específico.
            """
            return {"msg": "Bem-vindo à API!"}

        @self.app.get('/listar_sensores')
        def list_sensors():
            """
            Retorna todos os sensores cadastrados no banco de dados.
            """
            sensors = self._sensor_dao.get_all_sensors()  # retorna lista de tuplas: (sensor_id, description, unit)
            # Transformando em lista de dicionários para retornar em JSON
            result = [
                {
                    "sensor_id": row[0],
                    "description": row[1],
                    "unit_of_measurement": row[2]
                }
                for row in sensors
            ]
            return {"sensors": result}

        @self.app.get('/ler_sensor/{sensor_id}')
        def read_sensor(sensor_id: int):
            """
            Lê o valor atual de um sensor via Modbus, insere a leitura no banco e retorna o valor lido.
            """
            # Tenta ler do servidor Modbus
            sensor_data = self._modbus_client.read_sensor_data(sensor_id)
            
            # Verificação de retorno
            if not sensor_data:
                return {"error": "Não foi possível ler dados do sensor via Modbus."}
            
            # Insere no banco de dados
            value = sensor_data[0]
            self._reading_dao.create_reading(sensor_id=sensor_id, reading_value=value)
            
            return {
                "sensor_id": sensor_id,
                "reading_value": value,
                "status": "Leitura realizada e inserida no banco."
            }

        @self.app.get('/listar_leituras/{sensor_id}')
        def list_readings(sensor_id: int):
            """
            Retorna todas as leituras registradas para um sensor específico.
            """
            # Busca leituras no banco
            readings = self._reading_dao.get_readings_by_sensor(sensor_id)
            # readings é uma lista de tuplas: (reading_id, sensor_id, reading_value, reading_datetime)

            # Transformando em lista de dicionários
            result = [
                {
                    "reading_id": r[0],
                    "sensor_id": r[1],
                    "reading_value": r[2],
                    "reading_datetime": r[3]
                }
                for r in readings
            ]
            return {"readings": result}   
