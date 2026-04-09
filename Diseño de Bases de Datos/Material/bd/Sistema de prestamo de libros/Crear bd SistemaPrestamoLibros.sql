-- Crear la base de datos
CREATE DATABASE SistemaPrestamoLibros;
GO

-- Usar la base de datos
USE SistemaPrestamoLibros;
GO

-- Crear la tabla Generos
CREATE TABLE Generos (
    id_genero INT PRIMARY KEY,
    nombre NVARCHAR(50),
    descripcion NVARCHAR(100)
);
GO

-- Crear la tabla Autores
CREATE TABLE Autores (
    id_autor INT PRIMARY KEY,
    nombre NVARCHAR(50),
    apellido NVARCHAR(50)
);
GO

-- Crear la tabla Libros
CREATE TABLE Libros (
    isbn NVARCHAR(20) PRIMARY KEY,
    titulo NVARCHAR(100),
    cnt_paginas INT,
    ubicacion NVARCHAR(100),
    id_genero INT,
    id_autor INT,
    FOREIGN KEY (id_genero) REFERENCES Generos(id_genero),
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor)
);
GO

-- Crear la tabla DetalleLibro
CREATE TABLE DetalleLibro (
    id_genero INT,
    id_libro NVARCHAR(20),
    FOREIGN KEY (id_genero) REFERENCES Generos(id_genero),
    FOREIGN KEY (id_libro) REFERENCES Libros(isbn)
);
GO

-- Crear la tabla Turnos
CREATE TABLE Turnos (
    id_turno INT PRIMARY KEY,
    turno NVARCHAR(50)
);
GO

-- Crear la tabla Bibliotecarios
CREATE TABLE Bibliotecarios (
    dni NVARCHAR(10) PRIMARY KEY,
    nombre NVARCHAR(50),
    apellido NVARCHAR(50),
    telefono NVARCHAR(15),
    e_mail NVARCHAR(100),
    id_turno INT,
    FOREIGN KEY (id_turno) REFERENCES Turnos(id_turno)
);
GO

-- Crear la tabla DetalleTurno
CREATE TABLE DetalleTurno (
    id_turno INT,
    id_bibliotecario NVARCHAR(10),
    FOREIGN KEY (id_turno) REFERENCES Turnos(id_turno),
    FOREIGN KEY (id_bibliotecario) REFERENCES Bibliotecarios(dni)
);
GO

-- Crear la tabla Carreras
CREATE TABLE Carreras (
    id_carrera INT PRIMARY KEY,
    carrera NVARCHAR(100)
);
GO

-- Crear la tabla Estudiantes
CREATE TABLE Estudiantes (
    carnet NVARCHAR(10) PRIMARY KEY,
    nombre NVARCHAR(50),
    apellido NVARCHAR(50),
    direccion NVARCHAR(100),
    telefono NVARCHAR(15),
    e_mail NVARCHAR(100),
    id_carrera INT,
    FOREIGN KEY (id_carrera) REFERENCES Carreras(id_carrera)
);
GO

-- Crear la tabla Prestamos
CREATE TABLE Prestamos (
    id_libro NVARCHAR(20),
    id_bibliotecario NVARCHAR(10),
    id_estudiante NVARCHAR(10),
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY (id_libro) REFERENCES Libros(isbn),
    FOREIGN KEY (id_bibliotecario) REFERENCES Bibliotecarios(dni),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(carnet)
);
GO
