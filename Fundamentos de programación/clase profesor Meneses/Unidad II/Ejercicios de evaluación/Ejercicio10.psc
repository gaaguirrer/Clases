// Tres personas deciden invertir su dinero para fundar 
// una empresa.  Cada una de ellas invierte una cantidad 
// distinta.  Obtener el porcentaje que cada quien 
// invierte con respecto a la cantidad total invertida.
Proceso Inversion
	Definir cantidad1, cantidad2, cantidad3, cantidad_total Como Real;
	Definir porcentaje1, porcentaje2, porcentaje3 Como Real;
	Escribir "Ingrese la cantidad que invierte la primera persona";
	Leer cantidad1;
	Escribir "Ingrese la cantidad que invierte la segunda persona";
	Leer cantidad2;
	Escribir "Ingrese la cantidad que invierte la tercera persona";
	Leer cantidad3;	
	cantidad_total <- cantidad1 + cantidad2 + cantidad3;
    porcentaje1 <- cantidad1 * 100/ cantidad_total;
    porcentaje2 <- cantidad2 * 100/ cantidad_total;
    porcentaje3 <- cantidad3 * 100/ cantidad_total;
    Escribir "La inversión de la primera persona es: ", porcentaje1, "%";
	Escribir "La inversión de la segunda persona es: ", porcentaje2, "%";
	Escribir "La inversión de la tercera persona es: ", porcentaje3, "%";
FinProceso
