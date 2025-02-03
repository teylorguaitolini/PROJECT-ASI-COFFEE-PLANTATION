import requests

class APIClient:
    """
    Classe para comunicação com a API.
    """

    def __init__(self, base_url: str):
        """
        Inicializa o cliente da API.
        
        :param base_url: URL base da API (ex: "http://127.0.0.1:8000")
        """
        self.base_url = base_url.rstrip("/")  # Remove a barra final, se houver

    def get_sensors(self) -> dict:
        """
        Obtém a lista de sensores cadastrados.
        """
        url = f"{self.base_url}/listar_sensores"
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção se houver erro
        return response.json()

    def read_sensor(self, sensor_id: int) -> dict:
        """
        Lê o valor atual de um sensor via API.
        :param sensor_id: ID do sensor a ser lido
        """
        url = f"{self.base_url}/ler_sensor/{sensor_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_readings(self, sensor_id: int) -> dict:
        """
        Retorna as leituras de um sensor específico.
        :param sensor_id: ID do sensor
        """
        url = f"{self.base_url}/listar_leituras/{sensor_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
