Proceso Cifras
	Definir digito Como Entero;
	Escribir "Ingrese el número";
	Leer digito;
	Si digito < 10 Y digito > 0 Entonces
		Escribir "Es de 1 cifra";
	SiNo 
		Si digito >= 10 Y digito < 100 Entonces
			Escribir "Es de 2 cifras";
		SiNo
			Si digito >= 100 Y digito < 1000 Entonces
				Escribir "Es de 3 cifras";
			SiNo
				Escribir "Error";
			FinSi
			
		FinSi
	FinSi
FinProceso
