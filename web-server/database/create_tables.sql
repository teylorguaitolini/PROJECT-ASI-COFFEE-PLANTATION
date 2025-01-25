-- create_tables.sql

PRAGMA foreign_keys = ON;

-- Criação da tabela sensors
CREATE TABLE IF NOT EXISTS sensors (
    sensor_id INTEGER NOT NULL PRIMARY KEY,
    description TEXT NOT NULL,
    unit_of_measurement TEXT NOT NULL
);

-- Criação da tabela sensor_readings
CREATE TABLE IF NOT EXISTS sensor_readings (
    reading_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER NOT NULL,
    reading_value INTEGER NOT NULL,
    reading_datetime DATETIME NOT NULL DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (sensor_id) REFERENCES sensors (sensor_id)
);

-- Insere os sensores padrão do projeto
INSERT INTO sensors (sensor_id, description, unit_of_measurement) VALUES
(0, 'Sensor de temperatura ambiente', '°C'),
(1, 'Sensor de nível de irrigação', 'Litros/hora'),
(2, 'Sensor de índice de radiação solar', 'W/m²'),
(3, 'Sensor de velocidade do vento', 'm/s'),
(4, 'Sensor de umidade do solo', '%'),
(5, 'Sensor de pH do solo', 'pH'),
(6, 'Sensor de temperatura do solo', '°C'),
(7, 'Sensor de concentração de nitrogênio no solo', 'ppm'),
(8, 'Sensor de presença de pragas', '0/1');
