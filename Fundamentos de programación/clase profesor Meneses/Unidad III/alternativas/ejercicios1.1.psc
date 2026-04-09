// Algoritmo que pida dos números e indique 
// si el primero es mayor que el segundo o no.
// Análisis: encontrar el mayor de dos números
// Entrada: num1 (Entero) num2 (Entero)
// Salida: saber cuál es el número mayo
// Variable: num1 (Entero), num2 (Entero)

// Diseño:
// 1. Leer los dos números
// 2. Escribir si el primero el número es
// 		mayor que el segundo y viceversa
Proceso mayor_dos_numero
	Definir num1, num2 Como Entero;
	Escribir "Ingrese el primer número";
	Leer num1;
	Escribir "Ingrese el segundo número";
	Leer num2;	
	Si num1 > num2  Entonces
		Escribir num1, " es mayor que ", num2;
	SiNo
		Si num1 < num2 Entonces
			Escribir num2, " es mayor que ", num1;
		SiNo
			Escribir  "Ambos números son iguales";
		FinSi
	FinSi
FinProceso
