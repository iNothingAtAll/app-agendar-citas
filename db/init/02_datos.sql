-- Usar la base de datos creada
USE citas_db;


-- Insertar roles
INSERT INTO roles (nombre) VALUES
('cliente'),
('peluquero');


-- Insertar estados de cita
INSERT INTO estados_cita (nombre_estado) VALUES
('pendiente'),
('confirmada'),
('cancelada'),
('completada');


-- Insertar usuarios (peluqueros)
INSERT INTO usuarios (nombre, email, telefono, rol_id) VALUES
('Dr. Juan Pérez', 'juan.perez@clinic.com', '555-1234', 2),
('Dra. Ana Torres', 'ana.torres@clinic.com', '555-5678', 2);


-- Insertar usuarios (clientes)
INSERT INTO usuarios (nombre, email, telefono, rol_id) VALUES
('Carlos Gómez', 'carlos.gomez@mail.com', '555-1111', 1),
('Lucía Martínez', 'lucia.martinez@mail.com', '555-2222', 1),
('Pedro Rojas', 'pedro.rojas@mail.com', '555-3333', 1);


-- Insertar citas de ejemplo
INSERT INTO citas (paciente_id, doctor_id, fecha, hora, estado_id, notas) VALUES
(3, 1, '2025-10-22', '10:00:00', 1, 'Corte de cabello'),
(4, 2, '2025-10-23', '11:30:00', 2, 'Coloración de cabello'),
(5, 2, '2025-10-24', '09:00:00', 3, 'Cancelada por el cliente'),
(3, 1, '2025-10-25', '14:00:00', 4, 'Cita completada con éxito');