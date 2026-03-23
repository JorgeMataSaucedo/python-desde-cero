# Capitulo 10 — Ciclos

> Repetir cosas sin escribir el mismo codigo 100 veces.

---

## 10.1 Para que sirven los ciclos?

Imagina que quieres imprimir los numeros del 1 al 100. Sin ciclos:

```python
print(1)
print(2)
print(3)
# ... 97 lineas mas ...
print(100)
```

Con un ciclo:
```python
for i in range(1, 101):
    print(i)
```

Dos lineas. Eso es el poder de los ciclos.

```
  Como funciona un ciclo for:

  nombres = ["Diego", "Ilse", "Miguel"]

  Vuelta 1:  nombre = "Diego"  → print("Hola Diego!")
       │
  Vuelta 2:  nombre = "Ilse"   → print("Hola Ilse!")
       │
  Vuelta 3:  nombre = "Miguel" → print("Hola Miguel!")
       │
  Se acabaron los elementos → SALE del ciclo


  Como funciona un ciclo while:

  ┌──→ condicion es True? ──NO──→ SALE del ciclo
  │          │
  │         SI
  │          │
  │          ▼
  │    ejecuta el bloque
  │          │
  └──────────┘  (vuelve a preguntar)
```

## 10.2 for — repetir un numero conocido de veces

### Recorrer una lista

```python
nombres = ["Diego", "Ilse", "Miguel"]

for nombre in nombres:
    print(f"Hola {nombre}!")

# Hola Diego!
# Hola Ilse!
# Hola Miguel!
```

**Como funciona:**
1. Python toma el primer elemento de la lista ("Diego") y lo guarda en `nombre`
2. Ejecuta el bloque indentado
3. Toma el siguiente elemento ("Ilse") y repite
4. Cuando se acaban los elementos, sale del ciclo

### Recorrer un range

`range()` genera una secuencia de numeros:

```python
# range(fin) — de 0 a fin-1
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# range(inicio, fin) — de inicio a fin-1
for i in range(1, 6):
    print(i)
# 1, 2, 3, 4, 5

# range(inicio, fin, paso) — con incremento
for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8

# Contar hacia atras
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Recorrer un string

```python
for letra in "Python":
    print(letra)
# P, y, t, h, o, n
```

### Recorrer un diccionario

```python
persona = {"nombre": "Miguel", "edad": 25}

# Solo llaves (por defecto)
for llave in persona:
    print(llave)

# Llaves y valores
for llave, valor in persona.items():
    print(f"{llave}: {valor}")
```

### enumerate — indice + elemento

```python
frutas = ["manzana", "naranja", "uva"]

for i, fruta in enumerate(frutas):
    print(f"{i + 1}. {fruta}")

# 1. manzana
# 2. naranja
# 3. uva
```

## 10.3 while — repetir mientras una condicion sea True

```python
contador = 0

while contador < 5:
    print(f"Vuelta {contador}")
    contador += 1

# Vuelta 0
# Vuelta 1
# Vuelta 2
# Vuelta 3
# Vuelta 4
```

**Como funciona:**
1. Evalua la condicion (`contador < 5`)
2. Si es True, ejecuta el bloque
3. Vuelve al paso 1
4. Si es False, sale del ciclo

**Cuidado con ciclos infinitos:**
```python
# ESTO NUNCA TERMINA (no incrementa el contador)
contador = 0
while contador < 5:
    print(contador)
    # Falta: contador += 1
```

Si te pasa, presiona `Ctrl+C` en la terminal para detenerlo.

### while True — ciclo infinito controlado

```python
while True:
    opcion = input("Escribe 'salir' para terminar: ")
    if opcion == "salir":
        break
    print(f"Escribiste: {opcion}")

print("Fin del programa")
```

`while True` se repite para siempre. La unica forma de salir es con `break`. Es util para menus y programas interactivos.

## 10.4 break — salir del ciclo

`break` termina el ciclo inmediatamente:

```python
for i in range(100):
    if i == 5:
        break
    print(i)

# 0, 1, 2, 3, 4 (se detuvo en 5)
```

Util para buscar algo y detenerse cuando lo encuentras:
```python
nombres = ["Ana", "Carlos", "Diana", "Miguel"]

for nombre in nombres:
    if nombre == "Diana":
        print("Encontrada!")
        break
```

## 10.5 continue — saltar a la siguiente vuelta

`continue` salta el resto del bloque y pasa a la siguiente iteracion:

```python
for i in range(10):
    if i % 2 == 0:
        continue    # Salta los pares
    print(i)

# 1, 3, 5, 7, 9
```

Es como decir "este no me interesa, siguiente".

## 10.6 for vs while — cuando usar cual?

| Usa `for` cuando... | Usa `while` cuando... |
|---------------------|----------------------|
| Sabes cuantas veces repetir | No sabes cuantas veces |
| Recorres una coleccion | Esperas una condicion |
| Cuentas de X a Y | El usuario decide cuando parar |
| Ej: recorrer lista | Ej: menu interactivo |
| Ej: procesar registros | Ej: pedir datos hasta que sean validos |

**Regla simple:** si tienes una coleccion o un rango, usa `for`. Si dependes de una condicion externa, usa `while`.

## 10.7 Ciclos anidados

Un ciclo dentro de otro:

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()    # Salto de linea

# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

Por cada vuelta del ciclo externo, el ciclo interno ejecuta TODAS sus vueltas. 3 x 3 = 9 impresiones.

## 10.8 Patron comun: acumulador

```python
# Sumar todos los numeros de una lista
numeros = [10, 20, 30, 40]
total = 0    # Variable acumuladora

for num in numeros:
    total += num

print(total)    # 100
```

El acumulador empieza en 0 (o [] si es lista) y se va llenando en cada vuelta.

## 10.9 Patron comun: filtrar

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(pares)    # [2, 4, 6, 8, 10]
```

Recorres una lista y agregas a otra solo los que cumplen una condicion.

## 10.10 Patron comun: buscar

```python
productos = [
    {"nombre": "Cafe", "precio": 45},
    {"nombre": "Pan", "precio": 28},
    {"nombre": "Leche", "precio": 32},
]

buscar = "Pan"
encontrado = None

for prod in productos:
    if prod["nombre"] == buscar:
        encontrado = prod
        break

if encontrado:
    print(f"Encontrado: {encontrado['nombre']} - ${encontrado['precio']}")
else:
    print(f"{buscar} no existe")
```

Estos tres patrones (acumular, filtrar, buscar) los vas a usar constantemente en MikaCLI.

---

## Ejercicios

**Ejercicio 10.1:** Imprime la tabla de multiplicar de un numero dado por el usuario.

**Ejercicio 10.2:** Cuenta cuantos numeros positivos, negativos y ceros hay en una lista:
```python
numeros = [5, -3, 0, 8, -1, 0, 4, -7, 0, 2]
```

**Ejercicio 10.3:** Crea un juego de adivinar el numero:
```python
# Python elige un numero random entre 1 y 100
# El usuario tiene que adivinarlo
# Pistas: "Muy alto" o "Muy bajo"
# Cuenta los intentos
# import random; numero = random.randint(1, 100)
```

**Ejercicio 10.4:** Dada una lista de diccionarios (productos con precio), encuentra el mas caro y el mas barato.

**Ejercicio 10.5:** Crea un programa que pida calificaciones hasta que el usuario escriba -1. Muestra: promedio, mayor, menor, y cuantas son aprobatorias (>= 70).

---

> **Checkpoint:** Si dominas for, while, break y los patrones acumular/filtrar/buscar, estas listo para el Capitulo 11.

[← Capitulo 9](09-diccionarios.md) | [Capitulo 11 →](11-funciones.md)
