-- Crear base de datos
CREATE DATABASE IF NOT EXISTS citas_db;
USE citas_db;


-- Tabla: Roles de usuario
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);


-- Tabla: Usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    rol_id INT NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);


-- Tabla: Estados de la cita
CREATE TABLE estados_cita (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_estado VARCHAR(50) NOT NULL UNIQUE
);


-- Tabla: Citas
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    notas TEXT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    paciente_id INT NOT NULL,
    doctor_id INT NOT NULL,
    estado_id INT NOT NULL DEFAULT 1,

    FOREIGN KEY (paciente_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES usuarios(id) ON DELETE CASCADE,    
    FOREIGN KEY (estado_id) REFERENCES estados_cita(id)
);