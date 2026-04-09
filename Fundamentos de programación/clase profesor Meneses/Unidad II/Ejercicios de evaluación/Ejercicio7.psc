// En un hospital existen tres áreas: Ginecología, 
// Pediatría, Traumatología. El presupuesto anual del 
// hospital se reparte conforme a la sig. tabla:
// Área:       		% del presupuesto:
// Ginecología       40%
// Traumatología     30%
// Pediatría         30%
// Obtener la cantidad de dinero que recibirá cada área, 
// para cualquier monto presupuestal.
Proceso DineroPorArea
	Definir presupuesto, gin, tra, ped Como Real;
	Escribir "Escriba el monto presupuestal";
	Leer presupuesto;
	gin <- presupuesto * 0.40;
    tra <- presupuesto * 0.30;
    ped <- presupuesto * 0.30;
    Escribir "Ginecología recibe: ", gin;
	Escribir "Traumatología recibe: ", tra;
	Escribir "Pediatría recibe: ", ped;
FinProceso
