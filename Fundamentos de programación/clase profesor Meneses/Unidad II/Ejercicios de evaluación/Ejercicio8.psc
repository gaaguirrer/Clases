// El dueño de una tienda compra un artículo a un precio 
// determinado.  Obtener el precio en que lo debe vender 
// para obtener una ganancia del 30%.
Proceso VentaTienda
	Definir precio_art, precio_venta Como Real;
	Escribir 'Ingrese el precio del artículo';
	Leer precio_art;
	precio_venta <- (precio_art * 0.30) + precio_art;
    Escribir "El precio de ventadel artículo es de: ", precio_venta;
FinProceso
