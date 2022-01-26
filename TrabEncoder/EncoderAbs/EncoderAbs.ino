//Sensores Digitais//
int sensor_0 = 8;
int sensor_1 = 12;
int sensor_2 = 11;

uint8_t array_sensores = 0;

int leitura0;
int leitura1;
int leitura2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  leitura0 = !digitalRead(sensor_0);
  leitura1 = !digitalRead(sensor_1);
  leitura2 = !digitalRead(sensor_2);

  Serial.print("(");
  Serial.print(leitura0);
  Serial.print(",");
  Serial.print(leitura1);
  Serial.print(",");
  Serial.print(leitura2);
  Serial.print(",");
  Serial.print(")");
  Serial.println();
  delay(1000);
}
