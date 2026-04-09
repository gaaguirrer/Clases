// Un maestro desea saber qué porcentaje de hombres 
//y qué porcentaje de mujeres hay en un grupo de alumnos.
Proceso PocentajeClase
	Definir hombres, mujeres, total_clase Como Entero;
	Escribir "Ingrese la cantidad de hombres";
	Leer hombres;
	Escribir "Ingrese la cantidad de mujeres";
	Leer mujeres;
	total_clase <- hombres + mujeres;
	Escribir "El porcentaje de hombres es: ", hombres / total_clase * 100, '%';
	Escribir "El porcentaje de mujeres es: ", mujeres / total_clase * 100, '%';
FinProceso
