// Calcular el nuevo salario de un obrero si obtuvo un 
// incremento del 25% sobre su salario anterior.
Proceso NuevoSalario
	Definir salario, nuevo_salario Como Real;
	Escribir "Ingrese su salario";
	Leer salario;
	nuevo_salario <- (salario * 0.25) + salario;
    Escribir "Su nuevo salario es: ", nuevo_salario;
FinProceso
