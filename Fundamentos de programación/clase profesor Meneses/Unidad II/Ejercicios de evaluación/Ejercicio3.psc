// Dada un cantidad en pesos, obtener la equivalencia 
// en dólares, asumiendo que la unidad cambiaria es un 
// dato desconocido.
Proceso PesosADolares
	Definir unidad_cambiaria, cant_pesos, cambio Como Real;
	Escribir "Ingrese la unidad cambiaria";
	Leer unidad_cambiaria;
	Escribir "Ingrese la cantidad de pesos";
	Leer cant_pesos;
	cambio <- cant_pesos / unidad_cambiaria;
    Escribir cant_pesos, " pesos equivalen a ", cambio, " dólares";
FinProceso
