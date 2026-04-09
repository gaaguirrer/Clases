Proceso Ejercicio4
	Definir nombre Como Caracter;
	Definir sexo Como Caracter;
	Definir dpto Como Entero;
	Definir edad Como Entero;
	Definir tiempo_trabajar Como Entero;
	Definir ultimo_trabajador Como Caracter; // S o s
	
	// Acumuladores, contadores
	Definir suma_edades_mujeres Como Entero;
	Definir cuenta_mujeres Como Entero;
	Definir suma_ant_mayores_40_edad  Como Entero;
	Definir cuenta_mayores_40_edad Como Entero;
	Definir primera_iteracion Como Logico;
	
	// Salida
	Definir nombre_ant_mayor Como Caracter;
	Definir mayor_ant Como Entero;
	Definir edad_ant_mayor Como Entero;
	Definir cuenta_mujeres_dpto_contabilidad Como Entero;
	
	suma_edades_mujeres <- 0;
	cuenta_mujeres <- 0;
	suma_ant_mayores_40_edad <- 0;
	cuenta_mayores_40_edad <- 0;
	primera_iteracion = Verdadero;
	cuenta_mujeres_dpto_contabilidad <- 0;
	// Ciclo para leer información de los trabajadores
	Repetir
		Escribir "Introduzca el nombre: ";
		Leer nombre;
		// ciclo para garantizar que el usuario
		// escribe M o F
		repetir
			Escribir "Introduzca el sexo: ";
			Leer sexo;
		Hasta Que Mayusculas(sexo) = "M" O Mayusculas(sexo) = "F"
		// Ciclo para verificar que el usuario escribe
		// un valor del 1 al 4 (1= compras, 2= contabilidad, 
		// 3= control de calidad, 4= tecnología
		repetir
			Escribir "Introduzca el dpto (no): ";
			Leer dpto;
		Hasta Que dpto >= 1 Y dpto <= 4
		Escribir "Introduzca la edad: ";
		Leer edad;
		Escribir "Introduzca la antigüedad: ";
		Leer tiempo_trabajar;
		
		Si Mayusculas(sexo) = "F" Entonces
			suma_edades_mujeres <- suma_edades_mujeres + edad;
			cuenta_mujeres = cuenta_mujeres + 1;
			Si dpto = 2 Entonces
				cuenta_mujeres_dpto_contabilidad <- cuenta_mujeres_dpto_contabilidad + 1;
			FinSi
		FinSi
		
		Si edad > 40 Entonces
			suma_ant_mayores_40_edad <- suma_ant_mayores_40_edad + tiempo_trabajar;
			cuenta_mayores_40_edad <- cuenta_mayores_40_edad + 1;
		FinSi
		
		// Determinar mayor antigüedad
		Si primera_iteracion Entonces
			nombre_ant_mayor = nombre;
			edad_ant_mayor = edad;
			mayor_ant = tiempo_trabajar;
			primera_iteracion = Falso;
		SiNo
			Si tiempo_trabajar > mayor_ant Entonces
				nombre_ant_mayor = nombre;
				edad_ant_mayor = edad;
				mayor_ant = tiempo_trabajar;
			FinSi
		FinSi
		
		Escribir "¿Es el último trabajador?s/n";
		Leer ultimo_trabajador;
	Hasta Que Mayusculas(ultimo_trabajador) = "S"
	
	Si cuenta_mujeres = 0 Entonces
		Escribir "No hubo mujeres";
	Sino
		Escribir "Promedio de edad de mujeres: ", suma_edades_mujeres / cuenta_mujeres;
	FinSi
	
	Escribir "Promedio de antigüedad para mayores de 40 años de edad: ", suma_ant_mayores_40_edad / cuenta_mayores_40_edad;
	Escribir "Persona con mayor antigüedad:";
	Escribir "Nombre : ", nombre_ant_mayor;
	Escribir "Edad: ", edad_ant_mayor;
	Escribir "Porcentaje de mujeres en dpto contabilidad: ", trunc(cuenta_mujeres_dpto_contabilidad / cuenta_mujeres * 100);
FinProceso
