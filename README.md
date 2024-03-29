# 15_palos
El juego de los quince palos. Propuesta de IA para competir con Don Rogelio.

El sistema de IA está basado en aprendizaje por refuerzo, en el que el sistema no conoce ninguna regla específica del juego más allá de que no puede realizar movimientos ilegales. Aprende jugando contra sí mismo.

## Requisitos

- python
- numpy
- pygame
- LibSDL dev (ttf, image, ...)

## Ejecución

El sistema se puede poner en marcha a traves de conda
```
conda env create -f 15palos.yml
```

Para entrenar el modelo ejecutar en una terminal
 
```python 15_palos_train.py```

Para jugar contra el modelo entrenado

```python 15_palos.py```

## Notas de juego
Seleccionar los palos a retirar con el mouse y presionar la tecla enter. Al finalizar la partira presionar y / n para continuar o finalizar el juego, para cada nueva partida el jugador inicial va rotando.

[Demo playing in twitter] (https://twitter.com/lgazpio/status/1194299484940963840)

## Versión alpha
Si detectas cualquier bug comunícalo a inigo.lopezgazpio@deusto.es
