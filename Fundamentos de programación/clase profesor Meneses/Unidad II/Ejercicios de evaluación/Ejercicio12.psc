// Dada una medida de tiempo expresada en horas, minutos 
// y segundos con valores arbitrarios, elabore un programa 
// que transforme dicha medida en una expresión correcta. 
// Por ejemplo, dada la medida 3h 118m 195s, el programa 
// deberá obtener como resultado 5h 1m 15s.
Proceso HorasMinutosSegundos
	Definir cant_horas, cant_minutos, cant_segundos Como Entero;
	Definir total_segundos, hh, mn, seg Como Entero;
	Escribir "Ingrese la cantidad de horas";
	Leer cant_horas;
	Escribir "Ingrese la cantidad de minutos";
	Leer cant_minutos;
	Escribir "Ingrese la cantidad de segundos";
	Leer cant_segundos;
	total_segundos <- (cant_horas * 3600) + (cant_minutos * 60) + cant_segundos;
    hh <- trunc(total_segundos / 3600);
    seg <- total_segundos MOD 3600;
    mn <- trunc(seg / 60);
    seg <- trunc(seg MOD 60);
	Escribir hh, ":", mn, ":", seg;
FinProceso
