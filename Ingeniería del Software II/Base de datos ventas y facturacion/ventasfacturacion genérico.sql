-- Creación de la base de datos llamada 'ventas_facturacion'
CREATE DATABASE ventas_facturacion;

-- Nos aseguramos de usar la base de datos creada
USE ventas_facturacion;

-- ============================================
-- 1. Tabla de Clientes
-- ============================================
-- Tabla para almacenar la información de los clientes
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY, -- Identificador único de cada cliente
    name VARCHAR(100) NOT NULL, -- Nombre del cliente
    email VARCHAR(100) UNIQUE NOT NULL, -- Correo único del cliente
    phone VARCHAR(20), -- Número de teléfono del cliente
    address VARCHAR(255), -- Dirección del cliente
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro
);

-- ============================================
-- 2. Tabla de Productos
-- ============================================
-- Tabla para almacenar los productos disponibles para la venta
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Identificador único del producto
    name VARCHAR(100) NOT NULL, -- Nombre del producto
    description TEXT, -- Descripción del producto
    price DECIMAL(10, 2) NOT NULL, -- Precio del producto
    stock INT NOT NULL, -- Cantidad de producto en inventario
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro
);

-- ============================================
-- 3. Tabla de Estatus de Pago
-- ============================================
-- Tabla que contiene los diferentes estatus de los pagos
CREATE TABLE payment_status (
    payment_status_id SERIAL PRIMARY KEY, -- Identificador único del estatus
    status VARCHAR(50) NOT NULL -- Descripción del estatus (Ej: 'paid', 'pending', 'canceled')
);

-- ============================================
-- 4. Tabla de Ventas
-- ============================================
-- Tabla para registrar las ventas realizadas
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY, -- Identificador único de la venta
    customer_id INT REFERENCES customers(customer_id), -- Clave foránea que enlaza con el cliente
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha en la que se realiza la venta
    total_amount DECIMAL(10, 2) NOT NULL, -- Monto total de la venta
    payment_status_id INT REFERENCES payment_status(payment_status_id), -- Estatus de pago (Ej. pagado o pendiente)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro
);

-- ============================================
-- 5. Tabla de Detalles de la Venta
-- ============================================
-- Tabla que almacena los detalles de los productos vendidos en cada venta
CREATE TABLE sale_details (
    sale_detail_id SERIAL PRIMARY KEY, -- Identificador único del detalle de venta
    sale_id INT REFERENCES sales(sale_id) ON DELETE CASCADE, -- Clave foránea que enlaza con la venta (si se elimina la venta, se eliminan sus detalles)
    product_id INT REFERENCES products(product_id), -- Clave foránea que enlaza con el producto
    quantity INT NOT NULL, -- Cantidad de productos vendidos
    unit_price DECIMAL(10, 2) NOT NULL, -- Precio unitario del producto
    total_price DECIMAL(10, 2) AS (quantity * unit_price) STORED -- Total por línea (calculado como cantidad * precio unitario)
);

-- ============================================
-- 6. Tabla de Facturas
-- ============================================
-- Tabla que almacena las facturas generadas para cada venta
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY, -- Identificador único de la factura
    sale_id INT REFERENCES sales(sale_id), -- Clave foránea que enlaza con la venta correspondiente
    invoice_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha de creación de la factura
    invoice_number VARCHAR(50) UNIQUE NOT NULL, -- Número único de factura
    due_date TIMESTAMP, -- Fecha de vencimiento de la factura (si aplica)
    total_amount DECIMAL(10, 2) NOT NULL, -- Monto total de la factura
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro
);

-- ============================================
-- 7. Tabla de Métodos de Pago
-- ============================================
-- Tabla para almacenar los métodos de pago disponibles
CREATE TABLE payment_methods (
    payment_method_id SERIAL PRIMARY KEY, -- Identificador único del método de pago
    method VARCHAR(50) NOT NULL -- Descripción del método de pago (Ej. 'cash', 'credit card', 'transfer')
);

-- ============================================
-- 8. Tabla de Pagos
-- ============================================
-- Tabla para registrar los pagos realizados por los clientes
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY, -- Identificador único del pago
    sale_id INT REFERENCES sales(sale_id), -- Clave foránea que enlaza con la venta correspondiente
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha en la que se realiza el pago
    payment_method_id INT REFERENCES payment_methods(payment_method_id), -- Método de pago utilizado
    amount_paid DECIMAL(10, 2) NOT NULL, -- Monto pagado
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro
);

-- ============================================
-- 9. Tabla de Roles de Usuario
-- ============================================
-- Tabla que almacena los diferentes roles de los usuarios del sistema
CREATE TABLE user_roles (
    role_id SERIAL PRIMARY KEY, -- Identificador único del rol
    role_name VARCHAR(50) NOT NULL -- Descripción del rol (Ej. 'admin', 'seller')
);

-- ============================================
-- 10. Tabla de Usuarios
-- ============================================
-- Tabla que almacena los usuarios del sistema
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Identificador único del usuario
    username VARCHAR(50) UNIQUE NOT NULL, -- Nombre de usuario único
    password_hash VARCHAR(255) NOT NULL, -- Hash de la contraseña (por seguridad)
    role_id INT REFERENCES user_roles(role_id), -- Rol asignado al usuario
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha de creación del registro
);

-- ============================================
-- Inserciones de datos iniciales para estatus de pago y métodos de pago
-- ============================================
-- Insertar valores iniciales en la tabla de estatus de pago
INSERT INTO payment_status (status) VALUES ('pending'), ('paid'), ('canceled');

-- Insertar valores iniciales en la tabla de métodos de pago
INSERT INTO payment_methods (method) VALUES ('cash'), ('credit card'), ('transfer');

-- Insertar valores iniciales en la tabla de roles de usuario
INSERT INTO user_roles (role_name) VALUES ('admin'), ('seller');

-- ============================================
-- Fin del script de creación de la base de datos
-- ============================================
