//################################################################################
//Diseñar un algoritmo que nos diga el dinero que tenemos (en córdobas y centavos) 
//después de pedirnos cuantas monedas tenemos (de C$ 5, C$ 1, 50 centavos, 25 centavos 
//o 10 centavos).
//################################################################################
//Análisis
//Se piden la cantidad de monedas que tenemos (de C$ 5, C$ 1, 50 centavos, 25 centavos 
//o 10 centavos) y calculamos el dinero que tenemos (córdobas y centavos)
//Datos de entrada: monedas de 5 córdobas, 1 córdoba, 50 centavos, 25 centavos o 10 centavos) (entero).
//Información de salida: total de dinero: córdobas y centavos (enteros)
//Variables: cord_5,cord_1,cent_50,cent_25, cent_10, total_cordobas, total_centavos (entero)
//################################################################################
//Diseño
//1. Leer el monedas de cord_5,cord_1,cent_50,cent_25, cent_10.
//2. Calcular Córdobas (sumar monedas de 5 córdobas * 5 + monedas de 1 córdoba)
//3. Calcular centavos 
//	monedas de 50 centavos * 50 + monedas de 25 centavos * 25 + moneda de 10 centavos * 10 
//4. Convertir centavos a córdobas (división entera entre 100)
//5. Mostrar córdobas y centavos totales
//################################################################################

Proceso CalcularDinero
	Definir cord_5,cord_1,cent_50,cent_25, cent_10, total_cordobas, total_centavos como Entero;
	Escribir Sin Saltar "Monedas de 5 córdobas:";
	Leer cord_5;
	Escribir Sin Saltar "Monedas de 1 córdoba:";
	Leer cord_1;
	Escribir Sin Saltar "Monedas de 50 centavos:";
	Leer cent_50;
	Escribir Sin Saltar "Monedas de 25 centavos:";
	Leer cent_25;
	Escribir Sin Saltar "Monedas de 10 centavos:";
	Leer cent_10;
	//2. Calcular Córdobas (sumar monedas de 5 córdobas * 5 + monedas de 1 córdoba)
	total_cordobas <- cord_5 * 5 + cord_1;
	//3. Calcular centavos 
	//	monedas de 50 centavos * 50 + monedas de 25 centavos * 25 + moneda de 10 centavos * 10
	total_centavos <- cent_50 * 50 + cent_25 * 25 + cent_10 * 10;
	//4. Convertir centavos a córdobas (división entera entre 100)
	total_cordobas <- total_cordobas + trunc(total_centavos / 100);
	total_centavos <- total_centavos % 100;
	Escribir total_cordobas," córdobas y ",total_centavos," centavos.";
FinProceso

