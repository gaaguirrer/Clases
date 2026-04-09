Proceso sin_titulo
	Definir precio Como Entero;
	Definir sucursal Como Entero;
	Definir indice_art Como Entero;
	Definir indice_suc Como Entero;
	Definir cant_art_suc_2 Como Entero;
	Definir cant_total_x_art Como Entero;
	Definir recaudacion_x_suc Como Entero;
	Definir recaudacion_empresa Como Entero;
	Definir mayor_rec Como Entero;
	Definir suc_mayor_rec Como Entero;
	
	Dimension precio[5];
	Dimension sucursal[4,5];
	
	cant_art_suc_2 <- 0;
	recaudacion_x_suc <- 0;
	recaudacion_empresa <- 0;
	
	Para indice_art <- 0 Hasta 4 Hacer
		Escribir "Introduzca el precio del artículo: ", indice_art + 1;
		Leer precio[indice_art];
	FinPara
	
	Para indice_suc <- 0 Hasta 3 Hacer
		// Recorrer productos
		Para indice_art <- 0  Hasta 4 Hacer
			Escribir "Introduzca la cantidad vendida en sucursal ", indice_suc + 1 , " producto: ", indice_art + 1;
			Leer sucursal[indice_suc, indice_art];
		FinPara
	FinPara
	
	Para indice_art <- 0 Hasta 4 Hacer
		cant_total_x_art = sucursal[0, indice_art] + sucursal[1, indice_art] + sucursal[2, indice_art] + sucursal[3, indice_art];
		Escribir "Cantidad vendida del pructo: ", indice_art + 1, " es: ", cant_total_x_art;
	FinPara
	
	Para indice_art <- 0 Hasta 4 Hacer
		cant_art_suc_2 =  cant_art_suc_2 + sucursal[1,indice_art];
	FinPara
	Escribir "Cantidad de artículos en la sucuarsal 2: ", cant_art_suc_2;
	
	Escribir "Cantidad de artículo 3 en la sucuarsal 1: ", sucursal[0, 2];
	
	mayor_rec <- 0;
	suc_mayor_rec <- 0;
	
	Para indice_suc <- 0 Hasta 3 Hacer
		Para indice_art <- 0 Hasta 4 Hacer
			recaudacion_x_suc <- recaudacion_x_suc + sucursal[indice_suc, indice_art] * precio[indice_art];
		FinPara
		Escribir "Recaudación de la sucursal #", indice_suc + 1, ":", recaudacion_x_suc;
		
		recaudacion_empresa <- recaudacion_empresa + recaudacion_x_suc;
		
		Si recaudacion_x_suc > mayor_rec Entonces
			mayor_rec <- recaudacion_x_suc;
			suc_mayor_rec <- indice_suc;
		FinSi
		
		recaudacion_x_suc <- 0;
	FinPara
	
	Escribir "La recaudación total de la empresa: ", recaudacion_empresa;
	
	Escribir "Sucursal con mayor recaudación: #", suc_mayor_rec + 1; 
FinProceso
