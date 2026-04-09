// Escribir un programa que calcule el salario de un 
// trabajador de la manera siguiente. El trabajador 
// cobra un precio fijo por hora y se le descuenta el 10% 
// en concepto de impuesto sobre la renta. El programa 
// debe pedir el nombre del trabajador, las horas 
// trabajadas y el precio que cobra por hora. Como salida 
// debe imprimir el sueldo bruto, el descuento de renta y 
// el salario a pagar.

// Análisis
// A partir de horas trabajadas y el precio por hora, calcular el 
// salario bruto, el descuento de renta y total a pagar
// Salida: sueldo_bruto, descuento_renta, salario_pagar (Real) 
// Entrada: nombre_trabajador (cadena), horas_trabajadas (Entero), precio_x_hora (Real)
// Variables: sueldo_bruto (Real), descuento_renta (Real)
//            salario_pagar (Real), nombre_trabajador (cadena),
//            horas_trabajadas (Entero), precio_x_hora (Real)
// Diseño
// 1. Leer nombre_trabajador (cadena), horas_trabajadas (Entero), precio_x_hora (Real)
// 2. Calcular el salario bruto
// 3. Calcular descuento_renta
// 4. Calcula total_pagar
// 5. Escribir salario_bruto, descuento_renta, total_pagar
Proceso CalculaSalario
	Definir sueldo_bruto, descuento_renta, total_pagar, precio_x_hora Como Real;
	Definir nombre_trabajador Como Cadena;
	Definir horas_trabajadas Como Entero;
	Escribir "Ingrese su nombre";
	Leer nombre_trabajador;
	Escribir  "Ingrese las horas trabajadas";
	Leer horas_trabajadas;
	Escribir "Ingrese el precio fijo por hora";
	Leer precio_x_hora;
	sueldo_bruto = horas_trabajadas * precio_x_hora;
	descuento_renta = sueldo_bruto * 0.10;
	total_pagar <- sueldo_bruto - descuento_renta;
	Escribir "-----", nombre_trabajador, ": --------------";
	Escribir "Sueldo bruto: C$", sueldo_bruto;
	Escribir "Renta: C$", descuento_renta;
	Escribir  "Total a pagar: C$", total_pagar;
FinProceso
