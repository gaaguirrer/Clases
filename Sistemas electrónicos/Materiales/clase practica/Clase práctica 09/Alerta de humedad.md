# Guía para el Uso del Sensor de Humedad de Suelo y Activación de un Zumbador

## **Objetivos de la Actividad**
1. **Conexión del Sensor de Humedad de Suelo**: Aprender a conectar correctamente el sensor de humedad de suelo a una placa Arduino.
2. **Determinación de Valores Máximos y Mínimos del Sensor**: Realizar experimentos para determinar los valores máximo y mínimo proporcionados por el sensor bajo diferentes condiciones de humedad del suelo.
3. **Programación de la Activación del Zumbador**: Escribir un código que active un zumbador cuando la humedad del suelo caiga por debajo del 30%.
4. **Interpretación de Datos del Sensor**: Interpretar los datos obtenidos del sensor y ajustar el código según sea necesario para lograr la precisión deseada.

## **Materiales Necesarios**
- Placa Arduino
- Sensor de humedad de suelo
- Zumbador activo
- Cables de conexión
- Protoboard (si es necesario)
- Computadora con el IDE de Arduino instalado

## **Conexión del Sensor de Humedad de Suelo y del Zumbador**
1. **Sensor de Humedad de Suelo**:
   - **VCC**: Conectar el pin VCC del sensor al pin A2 de la placa Arduino.
   - **GND**: Conectar el pin GND del sensor al pin GND de la placa Arduino.
   - **Signal**: Conectar el pin Signal del sensor al pin A0 de la placa Arduino.
2. **Zumbador Activo**:
   - **Positivo (Pin 3)**: Conectar el pin positivo del zumbador al pin 3 de la placa Arduino.
   - **Negativo**: Conectar el pin negativo del zumbador al pin GND de la placa Arduino.

## **Determinación de Valores Máximos y Mínimos del Sensor**
1. **Configuración del Sensor**: Escribir un código que lea los valores del sensor y los imprima en el Monitor Serie.
2. **Experimentos**: Realizar experimentos con el suelo seco y húmedo para determinar los valores máximo y mínimo proporcionados por el sensor.

## **Activación del Zumbador al 30% de Humedad**
1. **Determinación del 30%**: Utilizar los valores máximos y mínimos obtenidos para calcular el valor correspondiente al 30% de humedad.
2. **Código para Activar el Zumbador**: Escribir un código que active el zumbador cuando la humedad caiga por debajo del 30%.

## **Preguntas para Evaluar la Experiencia**
1. ¿Cuál es el valor máximo proporcionado por el sensor de humedad de suelo en condiciones de suelo seco?
2. ¿Cuál es el valor mínimo proporcionado por el sensor de humedad de suelo en condiciones de suelo húmedo?
3. ¿Cómo calculaste el valor correspondiente al 30% de humedad utilizando los valores máximo y mínimo obtenidos?
4. ¿Qué cambios harías en el código si el sensor proporciona valores incorrectos o inestables?
5. ¿Qué otros tipos de sensores podrían ser útiles para monitorear la salud del suelo en un entorno agrícola?

## **Evaluación y Ajustes**
- **Verificación de Conexiones**: Asegurarse de que todas las conexiones estén correctamente realizadas.
- **Monitoreo de Valores**: Comparar los valores obtenidos con los esperados y ajustar el código según sea necesario.
- **Discusión de Resultados**: Discutir en clase los resultados obtenidos y los posibles problemas encontrados durante la actividad.
