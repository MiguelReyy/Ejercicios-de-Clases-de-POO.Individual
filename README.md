# Ejercicios de Programación Orientada a Objetos en Python

Este repositorio contiene soluciones a varios ejercicios de programación orientada a objetos (POO) en Python. Cada ejercicio aborda un problema específico y proporciona una implementación en Python junto con ejemplos de uso y explicaciones detalladas.

## Contenido

1. [Palíndromo - Método de clase](#palíndromo---método-de-clase)
2. [Palíndromo - Método de instancia](#palíndromo---método-de-instancia)
3. [Puzzle](#puzzle)
4. [Logger](#logger)

## Diseño UML

### Ejercicio 1: Palíndromo - Método de clase

(UML Palíndromo - Método de clase)

### Ejercicio 2: Palíndromo - Método de instancia

(UML Palíndromo - Método de instancia)

### Ejercicio 4: Logger

(UML Logger)

## Palíndromo - Método de clase

### Descripción
Este ejercicio consiste en crear una clase `Palindromo` que contenga un método de clase `esPalindromo()` que determine si una cadena es un palíndromo.

### Comportamiento esperado

```python
print(Palindromo.esPalindromo('radar'))  # Salida: True
print(Palindromo.esPalindromo('sonar'))  # Salida: False
print(Palindromo.esPalindromo('Arde ya la yedra'))  # Salida: False
print(Palindromo.esPalindromo('Ardeyalayedra'))  # Salida: True
print(Palindromo.esPalindromo('!@#$% %$#@!'))  # Salida: True
print(Palindromo.esPalindromo('L O L'))  # Salida: True

```

## Palíndromo - Método de instancia

### Descripción
En este ejercicio, se añade un atributo a la clase Palindromo y se implementa un método test() que comprueba si el atributo es un palíndromo. Además, al destruir la instancia, se muestra el atributo en mayúsculas.

### Comportamiento esperado
```python
p = Palindromo("radar")
print(p.test())  # Salida: True
p = Palindromo("sonar")
print(p.test())  # Salida: False
```
## Puzzle

### Descripción
Este ejercicio presenta un código con un comportamiento poco comprensible y se pide determinar qué mensajes se mostrarán.

### Código

```python
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z')))
```
## Logger Class

### Descripción
La clase `Logger` se utiliza para registrar mensajes en un archivo cada vez que se llama al método `log(mensaje)`. El archivo de registro seguirá un formato específico, comenzando con "--Start log--", seguido de los mensajes recibidos por el método `log`, uno por línea. Al destruir la instancia de `Logger`, se escribirá "--End log: x log(s)--" en la última línea del archivo, donde "x" es el número total de llamadas al método `log`.

### Uso

```python
from logger import Logger

# Crear una instancia de Logger
logger = Logger()

# Registrar mensajes
logger.log("Este es un mensaje de prueba.")
logger.log("Este es otro mensaje de prueba.")

# Al finalizar, el archivo de registro contendrá:
# --Start log--
# Este es un mensaje de prueba.
# Este es otro mensaje de prueba.
# --End log: 2 log(s)--

# La instancia de Logger se destruirá automáticamente al salir




