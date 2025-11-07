-- Usar la base de datos creada
USE citas_db;


-- Insertar estados de cita
INSERT INTO estados_cita (nombre_estado) VALUES
('Pendiente'),
('Confirmada'),
('Cancelada'),
('Completada');


-- Insertar citas de ejemplo
INSERT INTO citas (barbero_id, cliente_id, fecha, hora, estado_id, notas) VALUES
(1, 2, '2025-10-22', '10:00:00', 1, 'Corte de cabello'),
(3, 2, '2025-10-23', '11:30:00', 2, 'Coloración de cabello'),
(2, 1, '2025-10-24', '09:00:00', 3, 'Cancelada por el cliente'),
(4, 3, '2025-10-25', '14:00:00', 4, 'Cita completada con éxito');
