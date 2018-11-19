# 15_palos
El juego de los quince palos. Propuesta de IA para competir con Don Rogelio.

El sistema de IA está basado en aprendizaje por refuerzo, en el que el sistema no conoce ninguna regla específica del juego más allá de que no puede realizar movimientos ilegales. Aprende jugando contra sí mismo.

## Requisitos

- python 3.6
- numpy

## Ejecución

En un terminal de python lanzar el comando
 
```python 15_palos.py```

Esto entrenará el modelo de IA durante 30000 iteraciones (unos 20 segundos dependiendo de la máquina).

La partida empieza automáticamente una vez terminado el entrenamiento. En la primera partida empieza la IA y va rotando sucesivamente.

## Jugar contra la IA

El movimiento se especifica por teclado mediante dos números separados por un espacio.
El primer número hace referencia al nivel [0, 1, 2] y el segundo número hace referencia al número de fichas que se desea extraer de ese nivel.

### Ejemplos

Ejemplo de una partida sin empezar

```
Starting round 0
-------------
[ 7 ]        (Nivel 2)
-------------
[ 5 ]        (Nivel 1)
-------------
[ 3 ]        (Nivel 0)
-------------
```

Ejemplo de un movimiento de la IA 
```

-------------
[ 6 ]        (Nivel 2)
-------------
[ 4 ]        (Nivel 1)
-------------
[ 3 ]        (Nivel 0)
-------------
===========
IA Movement
(0, 1), value 0.6261976348634948    (Retira una ficha del nivel 0
===========
-------------
[ 6 ]
-------------
[ 4 ]
-------------
[ 2 ]
-------------
```

Ejemplo de un movimiento de un jugador

```

-------------
[ 6 ]
-------------
[ 4 ]
-------------
[ 2 ]
-------------

Enter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): 0 1
-------------
[ 6 ]
-------------
[ 4 ]
-------------
[ 1 ]
-------------

```

### Ejemplo completo
```
python 15_palos.py 
=================
Starting training
=================
0
5000
10000
15000
20000
25000
============
End training
============
Starting round 0
-------------
[ 7 ]
-------------
[ 5 ]
-------------
[ 3 ]
-------------
===========
IA Movement
(1, 1), value 0.6023400386049069
===========
-------------
[ 7 ]
-------------
[ 4 ]
-------------
[ 3 ]
-------------

Enter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): 2 1
-------------
[ 6 ]
-------------
[ 4 ]
-------------
[ 3 ]
-------------
===========
IA Movement
(0, 1), value 0.6261976348634948
===========
-------------
[ 6 ]
-------------
[ 4 ]
-------------
[ 2 ]
-------------

Enter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): 0 1
-------------
[ 6 ]
-------------
[ 4 ]
-------------
[ 1 ]
-------------
===========
IA Movement
(2, 1), value 0.7265792565695163
===========
-------------
[ 5 ]
-------------
[ 4 ]
-------------
[ 1 ]
-------------

Enter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): 1 1
-------------
[ 5 ]
-------------
[ 3 ]
-------------
[ 1 ]
-------------
===========
IA Movement
(2, 3), value 0.8283691012574238
===========
-------------
[ 2 ]
-------------
[ 3 ]
-------------
[ 1 ]
-------------

Enter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): 2 1
-------------
[ 1 ]
-------------
[ 3 ]
-------------
[ 1 ]
-------------
===========
IA Movement
(1, 2), value 0.9999999999004827
===========
-------------
[ 1 ]
-------------
[ 1 ]
-------------
[ 1 ]
-------------

Enter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): 2 1
-------------
[ 0 ]
-------------
[ 1 ]
-------------
[ 1 ]
-------------
===========
IA Movement
(0, 1), value 1.0
===========
-------------
[ 0 ]
-------------
[ 1 ]
-------------
[ 0 ]
-------------

 Game Over 

Play again? [Y/n]: n
```
