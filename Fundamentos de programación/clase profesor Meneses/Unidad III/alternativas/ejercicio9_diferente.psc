Proceso ordena_numeros
	Definir num1, num2, num3 Como Entero;
	Escribir "Introduzca el primer número";
	Leer num1;
	Escribir "Introduzca el segundo número";
	Leer num2;
	Escribir "Introduzca el tercer número";
	Leer num3;
	
	Si num1 > num2 Entonces
		Si num2 > num3 Entonces
			Escribir num1,'-',num2,'-', num3;
		SiNo
			Si num3 > num1 Entonces
				Escribir num3,'-',num1,'-', num2;
			SiNo
				Escribir num1,'-',num3,'-', num2;
			FinSi
		FinSi
	SiNo
		Si num2 > num3 Entonces
			Si num3 > num1 Entonces
				Escribir num2,'-',num3,'-', num1;
			SiNo
				Escribir num2,'-',num1,'-', num3;
			FinSi
		SiNo
			Escribir num3,'-',num2,'-', num1;
		FinSi
	FinSi
FinProceso
