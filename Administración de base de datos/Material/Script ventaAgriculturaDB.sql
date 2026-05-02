-- =====================================================================
-- Script: VentasAgricolasDB
-- Contexto: pequeña empresa agrícola nicaragüense.
-- =====================================================================

-- 1. Creación segura de la base de datos
IF DB_ID('VentasAgricolasDB') IS NOT NULL
    DROP DATABASE VentasAgricolasDB;
GO

CREATE DATABASE VentasAgricolasDB
    COLLATE Modern_Spanish_CI_AS;   -- soporte para tildes, ñ y ordenación en español
GO

USE VentasAgricolasDB;
GO

-- 2. Tabla de Clientes
CREATE TABLE Clientes (
    ID_Cliente  INT             NOT NULL IDENTITY(1,1)
        CONSTRAINT PK_Clientes PRIMARY KEY,
    Nombre      VARCHAR(15)     NOT NULL,
    Apellido    VARCHAR(15)     NOT NULL,
    Direccion   VARCHAR(50)    NULL,
    Telefono    VARCHAR(15)     NULL,
    Correo      VARCHAR(18)    NOT NULL
        CONSTRAINT UQ_Clientes_Correo UNIQUE,   -- evita duplicados en el contacto principal
    Estado      CHAR(8)         NOT NULL DEFAULT 'Activo'
        CONSTRAINT CK_Clientes_Estado CHECK (Estado IN ('Activo', 'Inactivo'))
);
GO

-- 3. Tabla de Productos
CREATE TABLE Productos (
    ID_Producto INT             NOT NULL IDENTITY(1,1)
        CONSTRAINT PK_Productos PRIMARY KEY,
    Nombre      VARCHAR(25)    NOT NULL,
    Descripcion VARCHAR(100)    NULL,
    Precio      DECIMAL(12,2)   NOT NULL
        CONSTRAINT CK_Productos_Precio CHECK (Precio > 0),
    Stock       INT             NOT NULL DEFAULT 0
);
GO

-- 4. Tabla de Ventas 
CREATE TABLE Ventas (
    ID_Venta    INT             NOT NULL IDENTITY(1,1)
        CONSTRAINT PK_Ventas PRIMARY KEY,
    ID_Cliente  INT             NOT NULL
        CONSTRAINT FK_Ventas_Cliente FOREIGN KEY REFERENCES Clientes(ID_Cliente)
        ON DELETE NO ACTION,
    ID_Producto INT             NOT NULL
        CONSTRAINT FK_Ventas_Producto FOREIGN KEY REFERENCES Productos(ID_Producto)
        ON DELETE NO ACTION,
    Fecha       DATETIME        NOT NULL DEFAULT GETDATE(),
    Cantidad    INT             NOT NULL
        CONSTRAINT CK_Ventas_Cantidad CHECK (Cantidad > 0)
);
GO

-- 5. Índices no agrupados para las consultas más frecuentes
CREATE NONCLUSTERED INDEX IX_Ventas_Fecha      ON Ventas(Fecha);
CREATE NONCLUSTERED INDEX IX_Ventas_ID_Cliente ON Ventas(ID_Cliente);
CREATE NONCLUSTERED INDEX IX_Ventas_ID_Producto ON Ventas(ID_Producto);
GO

-- 6. Datos de ejemplo
INSERT INTO Clientes (Nombre, Apellido, Direccion, Telefono, Correo)
VALUES 
    ('Juan',   'Pérez',  'Managua, Centro',      '505-8888-0001', 'juan.perez@email.com'),
    ('María',  'López',  'León, Calle Real',     '505-8888-0002', 'maria.lopez@email.com');

INSERT INTO Productos (Nombre, Descripcion, Precio, Stock)
VALUES 
    ('Frijol rojo', 'Saco de 50 kg', 750.00, 100),
    ('Maíz blanco', 'Quintal',       320.00, 200),
    ('Café molido', 'Bolsa de 1 kg', 180.00,  50);

INSERT INTO Ventas (ID_Cliente, ID_Producto, Fecha, Cantidad)
VALUES 
    (1, 1, '2024-12-01 10:30', 2),
    (2, 3, '2024-12-02 11:00', 5),
    (1, 2, '2024-12-03 09:15', 10);
GO

-- 7. Vista para consultas con el total calculado
CREATE VIEW vw_VentasConTotal
AS
SELECT v.ID_Venta, c.Nombre AS Cliente, p.Nombre AS Producto,
       v.Fecha, v.Cantidad, p.Precio,
       v.Cantidad * p.Precio AS Total
FROM Ventas v
JOIN Clientes c ON v.ID_Cliente = c.ID_Cliente
JOIN Productos p ON v.ID_Producto = p.ID_Producto;
GO

-- 8. Verificación
SELECT 'Base de datos VentasAgricolasDB creada con diseño profesional.' AS Mensaje;
SELECT * FROM Clientes;
SELECT * FROM Productos;
SELECT * FROM vw_VentasConTotal;