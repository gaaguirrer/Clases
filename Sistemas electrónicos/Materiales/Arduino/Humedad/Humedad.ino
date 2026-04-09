int sensorHumedad = A0; // Sensor para lectura
int green = 3, red = 4,alarma = 5; //Salida de Alertas por led y buzzer / piezo
int humedad; // Almacena la lectura de la humedad
float porcentajeHumedad; // Almacena el porcentaje de Humedad
void setup(){
  pinMode(alarma, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  humedad = analogRead(sensorHumedad);
  porcentajeHumedad = map(humedad, 650, 200, 0, 100);
  if(porcentajeHumedad <= 30){
    digitalWrite(red, HIGH);
    digitalWrite(alarma, HIGH);
    digitalWrite(green, LOW);
  }
  else if (porcentajeHumedad >= 80){
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(alarma, LOW);
    }
    Serial.println(porcentajeHumedad);
    delay(2000);
  
}
