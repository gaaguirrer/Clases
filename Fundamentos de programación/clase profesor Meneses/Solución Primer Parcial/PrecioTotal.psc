Proceso PrecioTotal
	Definir precio_basico, impuesto, total Como Real;
	Escribir "Ingrese el precio básico";
	Leer precio_basico;
	Si precio_basico > 500 Entonces
		impuesto <- 20 * 0.30 + (precio_basico - 40) * 0.50;
	SiNo
		Si precio_basico > 40 Entonces
			impuesto <- 20 * 0.30 + (precio_basico - 20) * 0.40;
		SiNo
			Si precio_basico > 20 Entonces
				impuesto <- (precio_basico - 20) * 0.30;
			SiNo
				impuesto <- 0;
			FinSi
		FinSi
	FinSi
	total <- precio_basico + impuesto;
	Escribir "Impuesto: ", impuesto;
	Escribir "Total a pagar: ", total;
FinProceso
