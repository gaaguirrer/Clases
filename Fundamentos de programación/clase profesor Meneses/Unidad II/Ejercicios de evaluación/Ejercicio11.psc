// Escribir un programa que calcule el salario de un 
// trabajador de la manera siguiente. El trabajador 
// cobra un precio fijo por hora y se le descuenta el 10% 
// en concepto de impuesto sobre la renta. El programa 
// debe pedir el nombre del trabajador, las horas 
// trabajadas y el precio que cobra por hora. Como salida 
// debe imprimir el sueldo bruto, el descuento de renta y 
// el salario a pagar.
Proceso SalarioTrabajador
	Definir nombre_trabajador Como Caracter;
	Definir horas_trabajadas Como Entero;
	Definir precio_x_hora, salario_bruto Como Real;
	Definir descuento_renta, salario_pagar Como Real;
	Escribir "Ingrese el nombre del trabajador";
	Leer nombre_trabajador;
	Escribir  "Ingrese las horas trabajadas";
	Leer horas_trabajadas;
	Escribir "Ingrese el precio por hora";
	Leer precio_x_hora;
	salario_bruto <- precio_x_hora * horas_trabajadas;
    descuento_renta <- salario_bruto * 0.10;
    salario_pagar <- salario_bruto - descuento_renta;
    Escribir  "El salario bruto es: ", salario_bruto;
	Escribir  "El descuento de renta es: ", descuento_renta;
	Escribir "El salario a pagar es: ", salario_pagar;
FinProceso
