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
