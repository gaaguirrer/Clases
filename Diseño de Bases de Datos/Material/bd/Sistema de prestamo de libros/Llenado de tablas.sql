-- Insertar datos en la tabla Generos
INSERT INTO Generos (id_genero, nombre, descripcion)
VALUES
  (1, 'Ciencia Ficción', 'Libros de ciencia ficción y fantasía'),
  (2, 'Romance', 'Novelas románticas'),
  (3, 'Misterio', 'Libros de misterio y suspense');

-- Insertar datos en la tabla Autores
INSERT INTO Autores (id_autor, nombre, apellido)
VALUES
  (1, 'Isaac', 'Asimov'),
  (2, 'J.K.', 'Rowling'),
  (3, 'Agatha', 'Christie');

-- Insertar datos en la tabla Libros
INSERT INTO Libros (isbn, titulo, cnt_paginas, ubicacion, id_genero, id_autor)
VALUES
  ('9780553803700', 'Fundación', 300, 'Estantería A1', 1, 1),
  ('9780545010221', 'Harry Potter y la Piedra Filosofal', 400, 'Estantería B2', 2, 2),
  ('9780062073488', 'Asesinato en el Orient Express', 250, 'Estantería C3', 3, 3),
  ('9788498389399', 'Cien años de soledad', 432, 'Estantería D4', 1, 4),
  ('9788420471839', 'El código Da Vinci', 560, 'Estantería E5', 3, 5),
  -- Agrega los otros 25 libros aquí
  ('9788408161315', 'El principito', 96, 'Estantería F6', 1, 6),
  ('9789876120010', 'Rayuela', 700, 'Estantería G7', 2, 7),
  ('9788467025676', 'Los juegos del hambre', 400, 'Estantería H8', 2, 8);

-- Insertar datos en la tabla DetalleLibro
INSERT INTO DetalleLibro (id_genero, id_libro)
VALUES
  (1, '9780553803700'),
  (2, '9780545010221'),
  (3, '9780062073488'),
  (1, '9788498389399'),
  (3, '9788420471839'),
  -- Agrega los otros libros aquí
  (1, '9788408161315'),
  (2, '9789876120010'),
  (2, '9788467025676');

-- Insertar datos en la tabla Turnos
INSERT INTO Turnos (id_turno, turno)
VALUES
  (1, 'Mañana'),
  (2, 'Tarde'),
  (3, 'Noche');

-- Insertar datos en la tabla Bibliotecarios
INSERT INTO Bibliotecarios (dni, nombre, apellido, telefono, e_mail, id_turno)
VALUES
  ('12345678', 'Juan', 'Pérez', '123456789', 'juan.perez@example.com', 1),
  ('23456789', 'María', 'López', '987654321', 'maria.lopez@example.com', 2),
  ('34567890', 'Pedro', 'González', '456789012', 'pedro.gonzalez@example.com', 3),
  ('45678901', 'Ana', 'Martínez', '654321098', 'ana.martinez@example.com', 1),
  ('56789012', 'Carlos', 'Rodríguez', '321098765', 'carlos.rodriguez@example.com', 2);

-- Insertar datos en la tabla DetalleTurno
INSERT INTO DetalleTurno (id_turno, id_bibliotecario)
VALUES
  (1, '12345678'),
  (2, '23456789'),
  (3, '34567890'),
  (1, '45678901'),
  (2, '56789012');

-- Insertar datos en la tabla Carreras
INSERT INTO Carreras (id_carrera, carrera)
VALUES
  (1, 'Ingeniería de Sistemas'),
  (2, 'Medicina'),
  (3, 'Arquitectura');

-- Insertar datos en la tabla Estudiantes
INSERT INTO Estudiantes (carnet, nombre, apellido, direccion, telefono, e_mail, id_carrera)
VALUES
  ('20210001', 'Luis', 'García', 'Calle 123', '987654321', 'luis.garcia@example.com', 1),
  ('20210002', 'Laura', 'Hernández', 'Avenida 456', '123456789', 'laura.hernandez@example.com', 2),
  ('20210003', 'Carlos', 'Pérez', 'Carrera 789', '654321098', 'carlos.perez@example.com', 3),
  ('20210004', 'Ana', 'Sánchez', 'Calle 321', '456789012', 'ana.sanchez@example.com', 1),
  ('20210005', 'Juan', 'López', 'Avenida 654', '321098765', 'juan.lopez@example.com', 2);
