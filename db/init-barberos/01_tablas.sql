-- Crear base de datos
CREATE DATABASE IF NOT EXISTS barberos_db;
USE barberos_db;


-- Tabla para almacenar la información de los barberos
CREATE TABLE barberos (
    id_barbero INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    edad INT CHECK (edad > 0),
    correo VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);


-- Tabla para registrar los horarios ocupados de los barberos
CREATE TABLE horarios_ocupados (
    id_horario INT PRIMARY KEY AUTO_INCREMENT,
    id_barbero INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cita_id INT NOT NULL,
    FOREIGN KEY (id_barbero) REFERENCES barberos(id_barbero)
);
