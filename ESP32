const int ledPin = 18;
const int phototransistorPin = 35;

const int pwmChannel = 0;
const int resolution = 8;
const int pwmFrequency = 60;
const int duty = 127;

const int numLecturas = 1000;
const int intervaloLectura = 1;

void setup() {
  Serial.begin(115200);
  ledcSetup(pwmChannel, pwmFrequency, resolution);
  ledcAttachPin(ledPin, pwmChannel);
  ledcWrite(pwmChannel, duty);
  delay(0);
}

void loop() {
  for (int i = 0; i < numLecturas; i++) {
    unsigned long tiempo = millis();
    int lectura = analogRead(phototransistorPin);
    Serial.print(tiempo);
    Serial.print(", ");
    Serial.println(lectura);
    delay(intervaloLectura);
  }
}
