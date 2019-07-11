/*  El servidor de bototo guarda datos en una base de datos.
Este es el script que describe el esquema de la base de datos
para Bototo. */

/* Guarda los datos basicos para identificar un usuario de
telegram */
CREATE TABLE IF NOT EXISTS Usuarios (
    user_id INTEGER PRIMARY KEY,
    telegram_id BIGINT UNSIGNED NOT NULL UNIQUE,
    telegram_name VARCHAR(255),
    creation_datetime DATETIME DEFAULT CURRENT_TIMESTAMP
);

/* Guarda los datos basicos de un evento
El creador de un evento se modela como un participante
imlicito. */
CREATE TABLE IF NOT EXISTS Eventos (
    evento_id INTEGER PRIMARY KEY,
    creador BIGINT UNSIGNED NOT NULL UNIQUE,
    evento_name VARCHAR(255) NOT NULL,
    evento_hora VARCHAR(255) NOT NULL,
    evento_detalle TEXT,
    creation_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(creador) REFERENCES Usuarios(user_id)
);

/* Relaciona un evento y sus participantes */
CREATE TABLE IF NOT EXISTS Asistentes (
    asistente_id INTEGER PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL UNIQUE,
    evento_id BIGINT UNSIGNED NOT NULL UNIQUE,
    creation_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES Usuarios(user_id),
    FOREIGN KEY(evento_id) REFERENCES Eventos(evento_id)
);