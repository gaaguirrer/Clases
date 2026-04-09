Proceso MinutosAHora
	Definir min, h, m Como Real;
	Escribir "¿Cuántos minutos quiere convertir?";
	Leer min;
	h <- trunc(min /60);
	m <- min % 60;
	Escribir min, " minutos son ", h, " horas y ", m, " minutos";
FinProceso
