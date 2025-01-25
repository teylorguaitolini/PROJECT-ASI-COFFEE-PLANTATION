import sqlite3

class SensorDAO:
    """
    Classe DAO para a tabela 'sensors'.
    Fornece métodos de CRUD (Create, Read, Update, Delete).
    """

    def __init__(self, db_file="sensors.db"):
        """
        :param db_file: Caminho/arquivo do banco de dados SQLite.
        """
        self.db_file = db_file
    
    def create_sensor(self, sensor_id: int, description: str, unit_of_measurement: str) -> None:
        """
        Insere um novo sensor na tabela 'sensors'.
        :param sensor_id: ID do sensor (PRIMARY KEY).
        :param description: Descrição do sensor.
        :param unit_of_measurement: Unidade de medida do sensor.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            with conn:
                conn.execute(
                    """
                    INSERT INTO sensors (sensor_id, description, unit_of_measurement)
                    VALUES (?, ?, ?);
                    """,
                    (sensor_id, description, unit_of_measurement)
                )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir sensor (ID={sensor_id}): {e}")
        finally:
            conn.close()

    def get_sensor_by_id(self, sensor_id: int) -> tuple:
        """
        Retorna o sensor com base no ID.
        :param sensor_id: ID do sensor.
        :return: Tupla (sensor_id, description, unit_of_measurement) ou None se não existir.
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT sensor_id, description, unit_of_measurement
                FROM sensors
                WHERE sensor_id = ?;
                """,
                (sensor_id,)
            )
            return cursor.fetchone()  # retorna a primeira linha ou None
        finally:
            conn.close()

    def get_all_sensors(self) -> list:
        """
        Retorna todos os sensores cadastrados.
        :return: Lista de tuplas (sensor_id, description, unit_of_measurement).
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT sensor_id, description, unit_of_measurement FROM sensors;")
            return cursor.fetchall()  # retorna todas as linhas
        finally:
            conn.close()

    def update_sensor(self, sensor_id: int, description: str, unit_of_measurement: str) -> None:
        """
        Atualiza os dados de um sensor.
        :param sensor_id: ID do sensor a ser atualizado.
        :param description: Nova descrição do sensor.
        :param unit_of_measurement: Nova unidade de medida.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            with conn:
                conn.execute(
                    """
                    UPDATE sensors
                    SET description = ?, unit_of_measurement = ?
                    WHERE sensor_id = ?;
                    """,
                    (description, unit_of_measurement, sensor_id)
                )
        finally:
            conn.close()

    def delete_sensor(self, sensor_id: int) -> None:
        """
        Remove um sensor da tabela.
        :param sensor_id: ID do sensor a ser removido.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            with conn:
                conn.execute(
                    """
                    DELETE FROM sensors
                    WHERE sensor_id = ?;
                    """,
                    (sensor_id,)
                )
        finally:
            conn.close()
