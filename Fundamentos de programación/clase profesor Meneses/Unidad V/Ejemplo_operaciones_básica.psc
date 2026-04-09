Funcion opcion <- menu()
	Definir opcion, operacion Como Entero;
	Escribir "¿Qué operación desea realizar?";
	Escribir "1. Sumar";
	Escribir "2. Restar";
	Escribir "3. Multiplicar";
	Escribir "4. Dividir";
	Leer operacion;
	opcion <- operacion;
FinFuncion

Funcion suma (num1, num2)
	Escribir "La suma es: ", num1 + num2;
FinFuncion

Funcion resta (num1, num2)
	Escribir "La resta es: ", abs(num1 - num2);
FinFuncion

Proceso Operaciones
	Definir num1, num2 Como Real;
	Definir mult, division Como Real;;
	Definir salir Como Caracter;
	Definir operacion Como Entero;
	repetir 
		operacion <- menu();
		Escribir Sin Saltar "Introduzca el primer número: ";
		Leer num1;
		Escribir Sin Saltar "Introduzca el segundo número: ";
		Leer num2;
		Si operacion = 1 Entonces
			suma(num1, num2);
		SiNo
			Si operacion = 2 Entonces
				resta(num1, num2);
			SiNo
				Si operacion = 3 Entonces
					mult <- num1 * num2;
					Escribir "La multiplicacion es: ", mult;
				SiNo
					Si operacion = 4 Entonces
						division <- num1 / num2;
						Escribir "La división es: ", division;
					SiNo
						Escribir "Operación no válida";
					FinSi
				FinSi
			FinSi
		FinSi
		Escribir "¿Desea salir?s/n";
		Leer salir;
	Hasta Que Mayusculas(salir) = "S"; 
FinProceso
