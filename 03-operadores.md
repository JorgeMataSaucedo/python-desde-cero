# Capitulo 3 — Operadores

> Las matematicas de Python. Sumar, comparar, y decidir.

---

## 3.1 Operadores aritmeticos

Los basicos que ya conoces, mas algunos extras:

```python
a = 10
b = 3

print(a + b)    # 13    Suma
print(a - b)    # 7     Resta
print(a * b)    # 30    Multiplicacion
print(a / b)    # 3.333 Division (SIEMPRE regresa float)
print(a // b)   # 3     Division entera (sin decimales)
print(a % b)    # 1     Modulo (residuo de la division)
print(a ** b)   # 1000  Potencia (10 elevado a la 3)
```

### Division vs Division entera

```python
print(7 / 2)    # 3.5   (division normal, resultado float)
print(7 // 2)   # 3     (division entera, trunca el decimal)
```

`/` siempre regresa float, incluso si el resultado es exacto: `4 / 2` da `2.0`, no `2`.

### Modulo — el operador que nadie entiende al principio

`%` regresa el RESIDUO de una division:

```python
print(10 % 3)   # 1   (10 / 3 = 3 con residuo 1)
print(10 % 2)   # 0   (10 / 2 = 5 con residuo 0)
print(7 % 4)    # 3   (7 / 4 = 1 con residuo 3)
```

Para que sirve? Para saber si un numero es par o impar:
```python
numero = 8
if numero % 2 == 0:
    print("Es par")     # Si el residuo entre 2 es 0, es par
else:
    print("Es impar")
```

## 3.2 Operadores de asignacion

Atajos para modificar una variable:

```python
puntos = 100

puntos += 10    # puntos = puntos + 10  → 110
puntos -= 20    # puntos = puntos - 20  → 90
puntos *= 2     # puntos = puntos * 2   → 180
puntos /= 3     # puntos = puntos / 3   → 60.0
```

`+=` es el mas comun. Lo vas a usar todo el tiempo.

## 3.3 Operadores de comparacion

Comparan dos valores y regresan `True` o `False`:

```python
a = 10
b = 5

print(a == b)    # False   Igual a
print(a != b)    # True    Diferente de
print(a > b)     # True    Mayor que
print(a < b)     # False   Menor que
print(a >= b)    # True    Mayor o igual que
print(a <= b)    # False   Menor o igual que
```

**Cuidado:** `=` es asignacion (guardar valor). `==` es comparacion (preguntar si son iguales).

```python
x = 5      # Asigna 5 a x
x == 5     # Pregunta: x es igual a 5? (True)
```

Este es uno de los errores mas comunes de principiante.

## 3.4 Operadores logicos

Combinan condiciones:

```python
edad = 25
tiene_id = True

# and — AMBAS deben ser True
print(edad >= 18 and tiene_id)     # True (ambas son True)

# or — AL MENOS UNA debe ser True
print(edad >= 18 or tiene_id)      # True (la primera ya es True)

# not — invierte el valor
print(not tiene_id)                 # False (invierte True a False)
```

### Tabla de verdad (memoriza esto)

**and:**
| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

**or:**
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

Truco: `and` es exigente (necesita ambas). `or` es flexible (con una basta).

## 3.5 Operador de identidad

```python
a = None

print(a is None)       # True
print(a is not None)   # False
```

`is` compara identidad (es el MISMO objeto), `==` compara valor (tienen el MISMO contenido). Para `None`, siempre usa `is`:

```python
# BIEN
if resultado is None:
    print("No hay resultado")

# MAL (funciona pero no es la forma correcta)
if resultado == None:
    print("No hay resultado")
```

## 3.6 Operador de pertenencia

```python
frutas = ["manzana", "naranja", "uva"]

print("manzana" in frutas)      # True
print("platano" in frutas)      # False
print("platano" not in frutas)  # True
```

`in` verifica si un elemento esta dentro de una coleccion. Funciona con listas, strings, diccionarios, etc.

```python
# Tambien funciona con strings
mensaje = "Hola mundo"
print("mundo" in mensaje)    # True
print("adios" in mensaje)    # False
```

## 3.7 Precedencia de operadores

Python ejecuta operaciones en este orden (de mayor a menor prioridad):

1. `**` — Potencia
2. `*`, `/`, `//`, `%` — Multiplicacion, division, modulo
3. `+`, `-` — Suma, resta
4. `==`, `!=`, `>`, `<`, `>=`, `<=` — Comparacion
5. `not` — Negacion
6. `and` — Y logico
7. `or` — O logico

```python
resultado = 2 + 3 * 4      # 14 (no 20, porque * va primero)
resultado = (2 + 3) * 4    # 20 (parentesis fuerzan el orden)
```

**Regla simple:** si no estas seguro del orden, usa parentesis. Es mas claro y no hay ambiguedad.

---

## Ejercicios

**Ejercicio 3.1:** Calcula el area de un rectangulo:
```python
base = 15
altura = 8
# Imprime: "El area es: 120"
```

**Ejercicio 3.2:** Convierte temperatura de Celsius a Fahrenheit:
```python
celsius = 30
# Formula: fahrenheit = (celsius * 9/5) + 32
# Imprime el resultado
```

**Ejercicio 3.3:** Determina si un numero es par o impar usando `%`:
```python
numero = 17
# Imprime "par" o "impar"
```

**Ejercicio 3.4:** Que imprime cada linea? Piensalo ANTES de ejecutar:
```python
print(10 > 5 and 3 < 1)
print(10 > 5 or 3 < 1)
print(not True)
print(not (10 > 5))
```

**Ejercicio 3.5:** Calcula cuantos billetes de $200 y cuanto sobra:
```python
total = 1750
billete = 200
# Cuantos billetes? (division entera)
# Cuanto sobra? (modulo)
```

---

> **Checkpoint:** Si entiendes la diferencia entre `=` y `==`, y sabes para que sirve `%`, estas listo para el Capitulo 4.

[← Capitulo 2](02-variables-y-tipos.md) | [Capitulo 4 →](04-strings.md)
