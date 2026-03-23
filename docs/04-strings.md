# Capitulo 4 — Strings

> Todo lo que es texto en Python. Manipularlo, formatearlo, y hacerlo bonito.

---

## 4.1 Que es un string?

Un string es una secuencia de caracteres (letras, numeros, simbolos) encerrada entre comillas:

```python
nombre = "Miguel"
saludo = 'Hola mundo'
vacio = ""
```

Comillas dobles o simples, da igual. Pero se consistente: si empezaste con dobles, usa dobles en todo el proyecto.

## 4.2 Strings multilinea

Para texto que ocupa varias lineas, usa triple comillas:

```python
mensaje = """
Este es un texto
que ocupa varias
lineas.
"""
print(mensaje)
```

Util para mensajes largos, docstrings, y texto formateado.

## 4.3 Acceder a caracteres

Un string es como una lista de caracteres. Puedes acceder por indice:

```python
nombre = "Miguel"

print(nombre[0])     # M   (primer caracter, indice 0)
print(nombre[1])     # i
print(nombre[-1])    # l   (ultimo caracter)
print(nombre[-2])    # e   (penultimo)
```

**Los indices empiezan en 0, no en 1.** Esto es universal en programacion.

```
M  i  g  u  e  l
0  1  2  3  4  5    ← indices positivos
-6 -5 -4 -3 -2 -1   ← indices negativos
```

## 4.4 Slicing (rebanar)

Puedes extraer pedazos de un string:

```python
texto = "Python Desde Cero"

print(texto[0:6])     # "Python"   (del indice 0 al 5)
print(texto[7:12])    # "Desde"    (del indice 7 al 11)
print(texto[:6])      # "Python"   (desde el inicio hasta 5)
print(texto[7:])      # "Desde Cero" (desde 7 hasta el final)
print(texto[-4:])     # "Cero"     (ultimos 4 caracteres)
```

La sintaxis es `[inicio:fin]`. El inicio se incluye, el fin NO.

## 4.5 Metodos de strings

Los strings tienen funciones incorporadas (metodos) que puedes usar:

### Cambiar mayusculas/minusculas
```python
texto = "Hola Mundo"

print(texto.upper())      # "HOLA MUNDO"
print(texto.lower())      # "hola mundo"
print(texto.title())      # "Hola Mundo"
print(texto.capitalize()) # "Hola mundo" (solo primera letra)
```

### Buscar y reemplazar
```python
texto = "Hola mundo, hola Python"

print(texto.find("mundo"))        # 5 (indice donde empieza)
print(texto.find("Java"))         # -1 (no lo encontro)
print(texto.count("hola"))        # 1 (cuenta ocurrencias, case sensitive)
print(texto.replace("Hola", "Hey"))  # "Hey mundo, hola Python"
```

### Verificar contenido
```python
print("123".isdigit())     # True (solo numeros)
print("abc".isalpha())     # True (solo letras)
print("abc123".isalnum())  # True (letras y numeros)
print("   ".isspace())     # True (solo espacios)
print("hola".startswith("ho"))  # True
print("hola".endswith("la"))    # True
```

### Limpiar espacios
```python
texto = "   Hola mundo   "

print(texto.strip())       # "Hola mundo" (quita espacios de ambos lados)
print(texto.lstrip())      # "Hola mundo   " (solo izquierda)
print(texto.rstrip())      # "   Hola mundo" (solo derecha)
```

`strip()` es muy util cuando recibes datos del usuario. Siempre escribe espacios de mas.

### Separar y unir
```python
# split — separar un string en lista
texto = "manzana,naranja,uva"
frutas = texto.split(",")
print(frutas)    # ["manzana", "naranja", "uva"]

# join — unir una lista en string
frutas = ["manzana", "naranja", "uva"]
texto = ", ".join(frutas)
print(texto)     # "manzana, naranja, uva"
```

## 4.6 Concatenacion

Unir strings:

```python
# Con +
nombre = "Miguel"
saludo = "Hola " + nombre + "!"
print(saludo)    # "Hola Miguel!"

# Con f-string (MEJOR)
saludo = f"Hola {nombre}!"
print(saludo)    # "Hola Miguel!"
```

El `+` funciona pero se vuelve un desastre con muchas variables. Usa f-strings siempre.

## 4.7 F-Strings — la forma moderna

F-strings (formatted string literals) son la forma preferida de formatear texto en Python:

```python
nombre = "Miguel"
edad = 25

# Basico — interpolar variables
print(f"Me llamo {nombre} y tengo {edad} años")

# Expresiones dentro de {}
print(f"En 5 años tendre {edad + 5}")
print(f"Nombre en mayusculas: {nombre.upper()}")

# Formateo de numeros
precio = 1500.5
print(f"Total: ${precio:,.2f}")    # Total: $1,500.50

# Alineacion
print(f"|{'Izquierda':<20}|")      # |Izquierda           |
print(f"|{'Derecha':>20}|")        # |            Derecha|
print(f"|{'Centro':^20}|")         # |       Centro       |
```

**Recuerda:** la `f` antes de las comillas activa la magia. Sin ella, los `{}` son texto normal.

## 4.8 Caracteres especiales (escape)

```python
# Salto de linea
print("Linea 1\nLinea 2")
# Linea 1
# Linea 2

# Tabulacion
print("Col1\tCol2\tCol3")
# Col1    Col2    Col3

# Comilla dentro de string
print("El dijo \"hola\"")      # El dijo "hola"
print('El dijo "hola"')        # El dijo "hola" (mejor)

# Backslash literal
print("Ruta: C:\\Users\\Miguel")
```

## 4.9 Los strings son inmutables

No puedes cambiar un caracter individual:

```python
nombre = "Miguel"
nombre[0] = "m"    # TypeError! Los strings no se modifican
```

Para "cambiar" un string, creas uno nuevo:
```python
nombre = "Miguel"
nombre = "m" + nombre[1:]    # "miguel"
# O mejor:
nombre = nombre.lower()      # "miguel"
```

## 4.10 Longitud de un string

```python
nombre = "Miguel"
print(len(nombre))    # 6
```

`len()` funciona con strings, listas, diccionarios, y cualquier coleccion.

---

## Ejercicios

**Ejercicio 4.1:** Crea un programa que reciba un nombre y lo imprima en mayusculas, minusculas y titulo:
```python
nombre = "miGUeL mAtA"
# Imprime las 3 versiones
```

**Ejercicio 4.2:** Extrae las iniciales de un nombre completo:
```python
nombre = "Miguel Angel Mata Saucedo"
# Resultado esperado: "M.A.M.S."
# Pista: usa .split() para separar por espacios
```

**Ejercicio 4.3:** Cuenta cuantas veces aparece la letra "a" en una frase:
```python
frase = "La manzana roja estaba en la canasta"
# Usa .count() o un for loop
```

**Ejercicio 4.4:** Crea una tabla formateada con f-strings:
```python
# Imprime algo como:
# Producto        Precio     Cantidad
# ----------------------------------------
# Cafe            $45.00            3
# Pan             $28.50            2
# Leche           $32.00            1
```

**Ejercicio 4.5:** Limpia y valida una entrada de usuario:
```python
entrada = "   mIgUeL   "
# Limpia espacios, convierte a titulo
# Resultado: "Miguel"
```

---

> **Checkpoint:** Si puedes usar f-strings con formateo y conoces `strip()`, `split()`, `lower()`, estas listo para el Capitulo 5.

[← Capitulo 3](03-operadores.md) | [Capitulo 5 →](05-input.md)
