import os

# Estrutura do repositório
os.makedirs("SmartHome_LED_Controller/src", exist_ok=True)
os.makedirs("SmartHome_LED_Controller/diagrams", exist_ok=True)

# Código-fonte Arduino
arduino_code = """\
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
"""

# README explicativo
readme_text = """\
# SmartHome_LED_Controller

Este projeto simula o controle de um LED representando o ar-condicionado de uma casa inteligente. O LED será ligado ou desligado com base em quatro condições simuladas por botões:

- **manualPin (pino 2)**: controle manual
- **presencaPin (pino 3)**: detecção de presença
- **temperaturaPin (pino 4)**: temperatura abaixo do ideal
- **energiaPin (pino 5)**: energia disponível

## Lógica

O LED será ligado se:
- O botão manual for pressionado (LOW), **ou**
- Houver presença (presencaPin == HIGH), **ou**
- A temperatura estiver baixa (temperaturaPin == LOW), **ou**
- A energia estiver disponível (energiaPin == HIGH)

Caso contrário, o LED será desligado.

## Diagrama de ligação

Veja o arquivo `diagrams/ligacao.txt` para uma descrição textual da ligação dos componentes.
"""

# Diagrama textual
diagram_text = """\
[Arduino UNO]
  ├── Pino 2  ── Botão Manual ── GND
  ├── Pino 3  ── Botão Presença ── GND
  ├── Pino 4  ── Botão Temperatura ── GND
  ├── Pino 5  ── Botão Energia ── GND
  └── Pino 13 ── LED ── Resistor 220Ω ── GND
"""

# Salvar os arquivos com codificação UTF-8
with open("SmartHome_LED_Controller/src/main.ino", "w", encoding="utf-8") as f:
    f.write(arduino_code)

with open("SmartHome_LED_Controller/README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)

with open("SmartHome_LED_Controller/diagrams/ligacao.txt", "w", encoding="utf-8") as f:
    f.write(diagram_text)

# Compactar o repositório
import shutil
shutil.make_archive("SmartHome_LED_Controller", "zip", "SmartHome_LED_Controller")

