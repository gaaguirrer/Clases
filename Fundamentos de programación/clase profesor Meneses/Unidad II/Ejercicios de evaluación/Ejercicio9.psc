// Todos los lunes, miércoles y viernes, una persona 
// corre la misma ruta y cronometra los tiempos obtenidos.  
// Determinar el tiempo promedio que la persona tarda en 
// recorrer la ruta en una semana cualquiera.
Proceso TiempoRecorridoRuta
	Definir tiempo_lunes, tiempo_martes Como Real; 
	Definir tiempo_miercoles, tiempo_promedio Como Real;
	Escribir "Escriba el tiempo cronometrado el lunes";
	Leer tiempo_lunes;
	Escribir "Escriba el tiempo cronometrado el martes";
	Leer tiempo_martes;
	Escribir "Escriba el tiempo cronometrado el miércoles";
	Leer tiempo_miercoles;	
	tiempo_promedio <- (tiempo_lunes + tiempo_martes + tiempo_miercoles) / 3;
    Escribir "El tiempo promedio recorrido es de: ", tiempo_promedio;
FinProceso
