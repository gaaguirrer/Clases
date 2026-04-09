// Calcular el número de pulsaciones que una persona 
// debe tener por cada 10 segundos de ejercicio, si 
// la fórmula es:   num. pulsaciones = (220 - edad)/10
Proceso Pulsaciones
	Definir edad, num_pulsaciones Como Entero;
	Escribir "Ingrese su edad";
	Leer edad;
	// Se usa la función de redondeo lo cual es opcional
    num_pulsaciones <- redon((220 - edad)/10);
    Escribir "Cada diez segundo, usted debe tener ", num_pulsaciones, " pulsaciones";
FinProceso
