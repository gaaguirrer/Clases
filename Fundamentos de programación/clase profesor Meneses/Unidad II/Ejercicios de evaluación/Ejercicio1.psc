// Suponga que un individuo desea invertir su capital 
//en un banco y desea saber cuánto dinero ganará 
//después de un mes si el banco paga a razón de 2% mensual.
Proceso InversionCapital
	Definir cap_inv, ganancia Como Real;
	Escribir "¿Cuánto capital desea invertir?";
	Leer cap_inv;
	ganancia <- cap_inv * 0.02;
	Escribir "La ganancia por su inversión en un mes es de: ", ganancia;
FinProceso
