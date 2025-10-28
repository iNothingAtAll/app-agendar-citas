-- Usar la base de datos creada
USE barberos_db;


-- Datos iniciales para la tabla de barberos
INSERT INTO barberos (nombre, edad, correo, telefono) VALUES
('Carlos Ramírez', 30, 'carlos.ramirez@barberia.com', '555-1234'),
('Juan Torres', 27, 'juan.torres@barberia.com', '555-5678'),
('Luis Gómez', 35, 'luis.gomez@barberia.com', '555-9012'),
('Miguel López', 29, 'miguel.lopez@barberia.com', '555-3456');


-- Ejemplo de horarios ocupados
INSERT INTO horarios_ocupados (id_barbero, fecha, hora, cita_id) VALUES
(1, '2025-10-28', '09:00:00', 1),
(1, '2025-10-28', '11:00:00', 4),
(2, '2025-10-28', '10:30:00', 2),
(2, '2025-10-29', '14:00:00', 3),
