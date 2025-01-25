import sqlite3
from typing import Optional, List, Tuple

class ReadingDAO:
    """
    Classe DAO para a tabela 'sensor_readings'.
    Fornece métodos de CRUD (Create, Read, Update, Delete).
    """

    def __init__(self, db_file="sensors.db"):
        """
        :param db_file: Caminho/arquivo do banco de dados SQLite.
        """
        self.db_file = db_file

    def create_reading(self, sensor_id: int, reading_value: int, reading_datetime: Optional[str] = None) -> None:
        """
        Insere uma nova leitura na tabela 'sensor_readings'.
        :param sensor_id: ID do sensor (deve existir na tabela 'sensors').
        :param reading_value: Valor lido do sensor (inteiro).
        :param reading_datetime: Data/hora da leitura (string "YYYY-MM-DD HH:MM:SS"). 
                                 Se None, usará datetime('now','localtime') por padrão.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            with conn:
                if reading_datetime:
                    conn.execute(
                        """
                        INSERT INTO sensor_readings (sensor_id, reading_value, reading_datetime)
                        VALUES (?, ?, ?);
                        """,
                        (sensor_id, reading_value, reading_datetime)
                    )
                else:
                    # Se não for passada data/hora, o DEFAULT do banco assume datetime('now','localtime')
                    conn.execute(
                        """
                        INSERT INTO sensor_readings (sensor_id, reading_value)
                        VALUES (?, ?);
                        """,
                        (sensor_id, reading_value)
                    )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir leitura para o sensor (ID={sensor_id}): {e}")
        finally:
            conn.close()

    def get_reading_by_id(self, reading_id: int) -> Optional[tuple]:
        """
        Retorna uma leitura com base no ID da leitura.
        :param reading_id: ID da leitura.
        :return: Tupla (reading_id, sensor_id, reading_value, reading_datetime) ou None se não existir.
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT reading_id, sensor_id, reading_value, reading_datetime
                FROM sensor_readings
                WHERE reading_id = ?;
                """,
                (reading_id,)
            )
            return cursor.fetchone()
        finally:
            conn.close()

    def get_readings_by_sensor(self, sensor_id: int) -> List[tuple]:
        """
        Retorna todas as leituras associadas a um sensor específico.
        :param sensor_id: ID do sensor a filtrar.
        :return: Lista de tuplas (reading_id, sensor_id, reading_value, reading_datetime).
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT reading_id, sensor_id, reading_value, reading_datetime
                FROM sensor_readings
                WHERE sensor_id = ?
                ORDER BY reading_datetime DESC;
                """,
                (sensor_id,)
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def get_all_readings(self) -> List[tuple]:
        """
        Retorna todas as leituras registradas.
        :return: Lista de tuplas (reading_id, sensor_id, reading_value, reading_datetime).
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT reading_id, sensor_id, reading_value, reading_datetime
                FROM sensor_readings
                ORDER BY reading_datetime DESC;
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def update_reading(self, reading_id: int, reading_value: int, reading_datetime: str) -> None:
        """
        Atualiza uma leitura existente (valor e data/hora).
        :param reading_id: ID da leitura.
        :param reading_value: Novo valor de leitura.
        :param reading_datetime: Nova data/hora da leitura.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            with conn:
                conn.execute(
                    """
                    UPDATE sensor_readings
                    SET reading_value = ?, reading_datetime = ?
                    WHERE reading_id = ?;
                    """,
                    (reading_value, reading_datetime, reading_id)
                )
        finally:
            conn.close()

    def delete_reading(self, reading_id: int) -> None:
        """
        Remove uma leitura da tabela.
        :param reading_id: ID da leitura a ser removida.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            with conn:
                conn.execute(
                    """
                    DELETE FROM sensor_readings
                    WHERE reading_id = ?;
                    """,
                    (reading_id,)
                )
        finally:
            conn.close()
