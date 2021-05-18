# Practica 3 - Ricardo Gottheil

## Punto 3

Para este punto usé la librería **memory_profiler** para medir el uso de la memoria de un script en python. En este caso, también usé **numpy** para hacer el **arreglo bidimensional (1000x1000)**, y así medir cuál es el manejo de la memoria.

```bash
Done!
Filename: punto3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4     32.7 MiB     32.7 MiB           1   @profile
     5                                         def main():
     6     40.3 MiB      7.6 MiB           1       m = np.random.uniform(1, 100, size=(1000, 1000))
     7
     8     32.9 MiB     -7.4 MiB           1       del m
     9
    10     32.9 MiB      0.0 MiB           1       print('Done!')
```

En esta tabla se puede ver cuál es la memoria que usa, y como esta incrementa y disminuye a medida que el script se ejecuta.

## Punto 4

Al igual que el punto anterior, usé la librería **memory_profiler** para medir el uso de la memoria de un script en python. En este caso no usé la librería de _numpy_, pero si usé la librería interna de python llamada **random** para generar los números aleatorios, y así posteriormente agregarlos a un arreglo.

```bash
Done!
Filename: punto4.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     6     17.2 MiB     17.2 MiB           1   @profile
     7                                         def main():
     8     17.2 MiB      0.0 MiB           1       arrayNumbers = []
     9
    10     17.2 MiB      0.0 MiB        1001       for i in range(1000):
    11     17.2 MiB      0.0 MiB        1000           n = random.randint(0,100)
    12     17.2 MiB      0.0 MiB        1000           arrayNumbers.append(n)
    13
    14     17.2 MiB      0.0 MiB           1       del arrayNumbers
    15
    16     17.2 MiB      0.0 MiB           1       print('Done!')
```
