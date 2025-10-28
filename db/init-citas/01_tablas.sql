-- Crear base de datos
CREATE DATABASE IF NOT EXISTS citas_db;
USE citas_db;


-- Crear tabla estados_cita
CREATE TABLE estados_cita (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_estado VARCHAR(50) NOT NULL UNIQUE
);


-- Crear tabla citas
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    notas TEXT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    barbero_id INT NOT NULL,
    estado_id INT NOT NULL DEFAULT 1,

    FOREIGN KEY (estado_id) REFERENCES estados_cita(id)
);