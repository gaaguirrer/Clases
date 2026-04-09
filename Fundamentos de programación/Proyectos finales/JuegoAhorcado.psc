Algoritmo JuegoAhorcado
    // Definir la palabra a adivinar
    Definir palabraSecreta Como Caracter
    palabraSecreta <- "ahorcado"
    
    // Convertir la palabra en una lista de caracteres
    Definir letrasSecretas[Longitud(palabraSecreta)] Como Caracter
    Para i <- 1 Hasta Longitud(palabraSecreta) Hacer
        letrasSecretas[i] <- Subcadena(palabraSecreta, i, 1)
    FinPara
    
    // Definir la cantidad de intentos permitidos
    Definir intentosMaximos Como Entero
    intentosMaximos <- 6
    
    // Definir el contador de intentos
    Definir intentosRealizados Como Entero
    intentosRealizados <- 0
    
    // Definir la lista de letras adivinadas
    Definir letrasAdivinadas[Longitud(palabraSecreta)] Como Caracter
    Para i <- 1 Hasta Longitud(palabraSecreta) Hacer
        letrasAdivinadas[i] <- "_"
    FinPara
    
    // Definir la lista de letras incorrectas
    Definir letrasIncorrectas[26] Como Caracter
    Para i <- 1 Hasta 26 Hacer
        letrasIncorrectas[i] <- ""
    FinPara
    
    // Mostrar el tablero inicial
    Escribir "¡Bienvenido al juego del ahorcado!"
    MostrarTablero(letrasAdivinadas, letrasIncorrectas, intentosRealizados, intentosMaximos)
    
    // Mientras haya intentos y la palabra no esté completa
    Mientras (intentosRealizados < intentosMaximos) Y (ContieneGuionBajo(letrasAdivinadas))
        // Pedir al jugador que ingrese una letra
        Escribir "Ingresa una letra: "
        Leer letra
        
        // Verificar si la letra está en la palabra secreta
        Si (ContieneLetra(letrasSecretas, letra)) Entonces
            Para i <- 1 Hasta Longitud(palabraSecreta) Hacer
                Si (letrasSecretas[i] = letra) Entonces
                    letrasAdivinadas[i] <- letra
                FinSi
            FinPara
        Sino
            // Si la letra no está en la palabra secreta, registrarla como incorrecta
            letrasIncorrectas[intentosRealizados + 1] <- letra
            intentosRealizados <- intentosRealizados + 1
        FinSi
        
        // Mostrar el tablero actualizado
        MostrarTablero(letrasAdivinadas, letrasIncorrectas, intentosRealizados, intentosMaximos)
    FinMientras
    
    // Determinar si el jugador ganó o perdió
    Si (ContieneGuionBajo(letrasAdivinadas)) Entonces
        Escribir "Lo siento, has perdido. La palabra era '", palabraSecreta, "'."
    Sino
        Escribir "¡Felicidades! ¡Has ganado!"
    FinSi
FinAlgoritmo

Funcion ContieneLetra(letras: Arreglo[], letra: Caracter) Como Logico
			// Verificar si la letra está en el arreglo de letras
			Para i <- 1 Hasta Longitud(letras) Hacer
				Si (letras[i] = letra) Entonces
					Devolver Verdadero
				FinSi
			FinPara
			Devolver Falso
FinFuncion

Funcion ContieneGuionBajo(letras: Arreglo[]) Como Logico
		// Verificar si hay algún guion bajo en el arreglo de letras
		Para i <- 1 Hasta Longitud(letras) Hacer
			Si (letras[i] = "_") Entonces
				Devolver Verdadero
			FinSi
		FinPara
		Devolver Falso
FinFuncion

SubProceso MostrarTablero(letrasAdivinadas: Arreglo[], letrasIncorrectas: Arreglo[], intentosRealizados: Entero, intentosMaximos: Entero)
					// Mostrar las letras adivinadas y las incorrectas, así como los intentos restantes
					Escribir ""
					Escribir "Palabra: "
					Para i <- 1 Hasta Longitud(letrasAdivinadas) Hacer
						Escribir letrasAdivinadas[i], " "
					FinPara
					Escribir ""
					Escribir "Letras incorrectas: "
					Para i <- 1 Hasta intentosRealizados Hacer
						Escribir letrasIncorrectas[i], " "
					FinPara
					Escribir ""
					Escribir "Intentos restantes: ", intentosMaximos - intentosRealizados
					Escribir ""
FinSubProceso
