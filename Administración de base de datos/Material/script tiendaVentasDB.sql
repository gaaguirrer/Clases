-- =====================================================================
-- Script profesional: TiendaVentasDB
-- Contexto: empresa de ventas al por menor (Nicaragua)
-- =====================================================================

-- 1. Creación segura de la base de datos
IF DB_ID('TiendaVentasDB') IS NOT NULL
    DROP DATABASE TiendaVentasDB;
GO

CREATE DATABASE TiendaVentasDB
    COLLATE Modern_Spanish_CI_AS;   -- ordenación y comparación en español
GO

USE TiendaVentasDB;
GO

-- 2. Tabla de Clientes (Clients)
CREATE TABLE Clients (
    ID_Client   INT             NOT NULL IDENTITY(1,1)
        CONSTRAINT PK_Clients PRIMARY KEY,
    FirstName   VARCHAR(15)     NOT NULL,
    LastName    VARCHAR(15)     NOT NULL,
    Address     VARCHAR(50)    NULL,
    Phone       VARCHAR(30)     NULL,
    Email       VARCHAR(25)    NOT NULL
        CONSTRAINT UQ_Clients_Email UNIQUE,      -- evita duplicados en el contacto principal
    Status      CHAR(8)         NOT NULL DEFAULT 'Active'
        CONSTRAINT CK_Clients_Status CHECK (Status IN ('Active', 'Inactive'))
);
GO

-- 3. Tabla de Productos (Products)
CREATE TABLE Products (
    ID_Product  INT             NOT NULL IDENTITY(1,1)
        CONSTRAINT PK_Products PRIMARY KEY,
    Name        VARCHAR(15)    NOT NULL,
    Description VARCHAR(100)    NULL,
    Price       DECIMAL(12,2)   NOT NULL
        CONSTRAINT CK_Products_Price CHECK (Price > 0),
    Stock       INT             NOT NULL DEFAULT 0
);
GO

-- 4. Tabla de Transacciones (Transactions)
CREATE TABLE Transactions (
    ID_Transaction  INT         NOT NULL IDENTITY(1,1)
        CONSTRAINT PK_Transactions PRIMARY KEY,
    ID_Client       INT         NOT NULL
        CONSTRAINT FK_Transactions_Client FOREIGN KEY REFERENCES Clients(ID_Client)
        ON DELETE NO ACTION,
    ID_Product      INT         NOT NULL
        CONSTRAINT FK_Transactions_Product FOREIGN KEY REFERENCES Products(ID_Product)
        ON DELETE NO ACTION,
    TransactionDate DATETIME    NOT NULL DEFAULT GETDATE(),
    Quantity        INT         NOT NULL
        CONSTRAINT CK_Transactions_Quantity CHECK (Quantity > 0)
);
GO

-- 5. Índices para las consultas más frecuentes
CREATE NONCLUSTERED INDEX IX_Transactions_Date   ON Transactions(TransactionDate);
CREATE NONCLUSTERED INDEX IX_Transactions_Client ON Transactions(ID_Client);
CREATE NONCLUSTERED INDEX IX_Transactions_Product ON Transactions(ID_Product);
GO

-- 6. Datos de ejemplo
INSERT INTO Clients (FirstName, LastName, Address, Phone, Email, Status)
VALUES 
    ('Carlos',  'González', 'Managua, Altamira',       '505-8888-1001', 'carlos.gonzalez@email.com', 'Active'),
    ('Ana',     'Martínez', 'León, Centro Histórico',  '505-8888-1002', 'ana.martinez@email.com',    'Active'),
    ('Pedro',   'López',    'Masaya, Monimbó',         '505-8888-1003', 'pedro.lopez@email.com',    'Inactive');

INSERT INTO Products (Name, Description, Price, Stock)
VALUES 
    ('Laptop 15"',        'Laptop de oficina con Windows 11', 850.00, 15),
    ('Mouse inalámbrico', 'Mouse óptico recargable',          25.00,  50),
    ('Teclado mecánico',  'Teclado RGB switches azules',      45.00,  30);

INSERT INTO Transactions (ID_Client, ID_Product, TransactionDate, Quantity)
VALUES 
    (1, 1, '2024-12-01 10:30', 2),
    (2, 3, '2024-12-02 11:00', 5),
    (1, 2, '2024-12-03 09:15', 10),
    (3, 1, '2024-12-04 14:00', 1);
GO

-- 7. Vista para calcular el total de cada transacción de forma segura
CREATE VIEW vw_TransactionsWithTotal
AS
SELECT t.ID_Transaction,
       c.FirstName + ' ' + c.LastName AS ClientName,
       p.Name AS ProductName,
       t.TransactionDate,
       t.Quantity,
       p.Price,
       (t.Quantity * p.Price) AS Total
FROM Transactions t
JOIN Clients c ON t.ID_Client = c.ID_Client
JOIN Products p ON t.ID_Product = p.ID_Product;
GO

-- 8. Verificación
SELECT 'Base de datos TiendaVentasDB creada con diseño profesional.' AS Mensaje;
SELECT * FROM Clients;
SELECT * FROM Products;
SELECT * FROM vw_TransactionsWithTotal;