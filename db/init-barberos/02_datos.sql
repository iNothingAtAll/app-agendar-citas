-- Usar la base de datos creada
USE barberos_db;


-- Datos iniciales para la tabla de barberos
INSERT INTO barberos (nombre, edad, correo, telefono, contrasenya) VALUES
('Carlos Ramírez', 30, 'carlos.ramirez@barberia.com', '555-1234', "12345"),
('Juan Torres', 27, 'juan.torres@barberia.com', '555-5678', "12345"),
('Luis Gómez', 35, 'luis.gomez@barberia.com', '555-9012', "12345"),
('Miguel López', 29, 'miguel.lopez@barberia.com', '555-3456', "12345");


-- Datos iniciales para la tabla de clientes
INSERT INTO cliente (nombre, correo, telefono) VALUES
('Ana Martínez', 'ana.algo@algo.com', '555-7890'),
('Beatriz Sánchez', 'sanchez.algo@algo.com', '555-2345'),
('Carla Fernández', 'carla.algo@algo.com', '555-6789');


-- Ejemplo de horarios ocupados
INSERT INTO cronograma (id_barbero, fecha, hora, cita_id) VALUES
(1, '2025-10-28', '09:00:00', 1),
(1, '2025-10-28', '11:00:00', 4),
(2, '2025-10-28', '10:30:00', 2),
(2, '2025-10-29', '14:00:00', 3);
