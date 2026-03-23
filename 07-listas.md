# Capitulo 7 — Listas

> Tu primera estructura de datos. Una coleccion ordenada de cosas.

---

## 7.1 Que es una lista?

Una lista es una coleccion ordenada de elementos. Piensa en ella como una fila de cajones numerados donde cada cajon puede guardar lo que sea.

```python
frutas = ["manzana", "naranja", "uva"]
numeros = [1, 2, 3, 4, 5]
mezcla = ["Miguel", 25, True, 3.14]    # Puede mezclar tipos
vacia = []                               # Lista vacia
```

Las listas se crean con corchetes `[]` y los elementos se separan por comas.

```
  Una lista en memoria:

  frutas ──→ ┌─────────┬─────────┬───────┐
             │"manzana"│"naranja"│ "uva" │
             └─────────┴─────────┴───────┘
               [0]        [1]      [2]

  Es como una fila de casilleros numerados.
  El primero SIEMPRE es [0], no [1].
```

## 7.2 Acceder a elementos

Cada elemento tiene un indice (posicion), empezando desde 0:

```python
frutas = ["manzana", "naranja", "uva", "kiwi"]

print(frutas[0])     # "manzana"  (primero)
print(frutas[1])     # "naranja"  (segundo)
print(frutas[-1])    # "kiwi"     (ultimo)
print(frutas[-2])    # "uva"      (penultimo)
```

```
 manzana   naranja   uva     kiwi
   [0]       [1]     [2]     [3]
  [-4]      [-3]    [-2]    [-1]
```

Si intentas acceder a un indice que no existe:
```python
print(frutas[10])    # IndexError: list index out of range
```

## 7.3 Modificar elementos

A diferencia de los strings, las listas SI se pueden modificar:

```python
frutas = ["manzana", "naranja", "uva"]
frutas[1] = "platano"
print(frutas)    # ["manzana", "platano", "uva"]
```

## 7.4 Slicing (rebanar)

Funciona igual que con strings:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[1:3])    # [20, 30]    (del indice 1 al 2)
print(numeros[:3])     # [10, 20, 30] (desde inicio hasta 2)
print(numeros[2:])     # [30, 40, 50] (desde 2 hasta el final)
print(numeros[-2:])    # [40, 50]     (ultimos 2)
```

## 7.5 Metodos de listas

### Agregar elementos

```python
frutas = ["manzana", "naranja"]

# append — agrega al FINAL
frutas.append("uva")
print(frutas)    # ["manzana", "naranja", "uva"]

# insert — agrega en una posicion especifica
frutas.insert(1, "kiwi")
print(frutas)    # ["manzana", "kiwi", "naranja", "uva"]
```

`append()` es el que mas vas a usar. Es el equivalente a `push()` de JavaScript.

### Eliminar elementos

```python
frutas = ["manzana", "naranja", "uva", "kiwi"]

# remove — elimina por VALOR (el primero que encuentre)
frutas.remove("naranja")
print(frutas)    # ["manzana", "uva", "kiwi"]

# pop — elimina por INDICE y regresa el elemento
eliminado = frutas.pop(1)
print(eliminado)  # "uva"
print(frutas)     # ["manzana", "kiwi"]

# pop sin indice — elimina el ultimo
ultimo = frutas.pop()
print(ultimo)     # "kiwi"
print(frutas)     # ["manzana"]

# del — elimina por indice (no regresa nada)
del frutas[0]
print(frutas)     # []

# clear — vacia la lista completa
frutas = [1, 2, 3]
frutas.clear()
print(frutas)     # []
```

### Buscar

```python
frutas = ["manzana", "naranja", "uva", "naranja"]

# index — posicion de un elemento
print(frutas.index("uva"))     # 2
# Si no existe: ValueError

# count — cuantas veces aparece
print(frutas.count("naranja"))  # 2

# in — existe en la lista?
print("uva" in frutas)          # True
print("kiwi" in frutas)         # False
```

### Ordenar

```python
numeros = [3, 1, 4, 1, 5, 9, 2]

# sort — ordena la lista original (la modifica)
numeros.sort()
print(numeros)    # [1, 1, 2, 3, 4, 5, 9]

# sort descendente
numeros.sort(reverse=True)
print(numeros)    # [9, 5, 4, 3, 2, 1, 1]

# sorted — regresa una lista NUEVA, no modifica la original
original = [3, 1, 2]
ordenada = sorted(original)
print(original)   # [3, 1, 2] (no cambio)
print(ordenada)   # [1, 2, 3] (nueva lista)

# reverse — invierte el orden (no ordena, solo invierte)
letras = ["a", "b", "c"]
letras.reverse()
print(letras)     # ["c", "b", "a"]
```

## 7.6 Longitud de una lista

```python
frutas = ["manzana", "naranja", "uva"]
print(len(frutas))    # 3
```

`len()` funciona con listas, strings, diccionarios — cualquier coleccion.

## 7.7 Recorrer una lista

### Con for

```python
frutas = ["manzana", "naranja", "uva"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Me gusta la manzana
# Me gusta la naranja
# Me gusta la uva
```

`fruta` es una variable temporal que toma el valor de cada elemento en cada vuelta del ciclo. Puedes nombrarla como quieras, pero por convencion usa el singular del nombre de la lista.

### Con indice (enumerate)

```python
frutas = ["manzana", "naranja", "uva"]

for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# 0: manzana
# 1: naranja
# 2: uva
```

`enumerate()` te da el indice Y el elemento al mismo tiempo. Muy util cuando necesitas saber la posicion.

## 7.8 Listas anidadas (lista de listas)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0])       # [1, 2, 3]    (primera fila)
print(matriz[0][1])    # 2            (fila 0, columna 1)
print(matriz[2][2])    # 9            (fila 2, columna 2)
```

## 7.9 Copiar listas

Cuidado con esto:

```python
# Esto NO copia, crea una referencia
original = [1, 2, 3]
copia = original          # "copia" apunta al MISMO objeto
copia.append(4)
print(original)           # [1, 2, 3, 4]  SORPRESA! Se modifico la original

# Para copiar de verdad:
original = [1, 2, 3]
copia = original.copy()   # Crea una lista NUEVA
copia.append(4)
print(original)           # [1, 2, 3]  (no cambio)
print(copia)              # [1, 2, 3, 4]
```

Esto pasa porque las listas son objetos. Cuando dices `copia = original`, ambas variables apuntan al mismo lugar en memoria. `.copy()` crea un objeto nuevo.

## 7.10 Funciones utiles con listas

```python
numeros = [10, 5, 8, 3, 15]

print(len(numeros))    # 5      (cantidad de elementos)
print(min(numeros))    # 3      (menor)
print(max(numeros))    # 15     (mayor)
print(sum(numeros))    # 41     (suma total)
```

---

## Ejercicios

**Ejercicio 7.1:** Crea una lista de 5 nombres. Imprimelos numerados:
```
1. Ana
2. Carlos
3. Diego
...
```

**Ejercicio 7.2:** Crea un programa que pida numeros al usuario hasta que escriba 0. Despues muestra: el mayor, el menor, la suma y el promedio.

**Ejercicio 7.3:** Dada una lista de numeros, crea dos listas nuevas: una con los pares y otra con los impares.
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [2, 4, 6, 8, 10]
# impares = [1, 3, 5, 7, 9]
```

**Ejercicio 7.4:** Simula una lista de compras:
```
1. Agregar producto
2. Eliminar producto
3. Ver lista
4. Salir
```

**Ejercicio 7.5:** Invierte una lista SIN usar `.reverse()` ni slicing. Usa un for loop.

---

> **Checkpoint:** Si puedes agregar, eliminar, buscar y recorrer elementos de una lista, estas listo para el Capitulo 8.

[← Capitulo 6](06-condicionales.md) | [Capitulo 8 →](08-tuplas.md)
