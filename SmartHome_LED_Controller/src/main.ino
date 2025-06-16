const int led = 13;
const int manualPin = 2;
const int presencaPin = 3;
const int temperaturaPin = 4;
const int energiaPin = 5;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(manualPin, INPUT_PULLUP);
  pinMode(presencaPin, INPUT_PULLUP);
  pinMode(temperaturaPin, INPUT_PULLUP);
  pinMode(energiaPin, INPUT_PULLUP);
}

void loop() {
  int manual = digitalRead(manualPin);
  int presenca = digitalRead(presencaPin);
  int temperatura = digitalRead(temperaturaPin);
  int energia = digitalRead(energiaPin);

  // Corrigindo a lógica: os botões estão em INPUT_PULLUP, então LOW significa "ativado"
  if (manual == LOW || (presenca == HIGH) || (temperatura == LOW) || (energia == HIGH)) {
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }
}
