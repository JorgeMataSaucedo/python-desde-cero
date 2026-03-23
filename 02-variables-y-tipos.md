# Capitulo 2 — Variables y Tipos de Datos

> Una variable es una caja con etiqueta. Le pones nombre, le metes algo adentro, y despues lo usas.

---

## 2.1 Que es una variable?

Una variable es un espacio en la memoria de tu computadora donde guardas un dato. Le pones un nombre para poder referirte a ese dato despues.

```python
nombre = "Miguel"
edad = 25
esta_activo = True
```

**Lo que pasa aqui:**
- Python crea un espacio en memoria
- Guarda el valor ("Miguel", 25, True)
- Le pone la etiqueta (nombre, edad, esta_activo)
- Cuando escribes `nombre` despues, Python sabe que te refieres a "Miguel"

```
  Memoria de Python:

  nombre ─────────→ ┌───────────┐
                     │ "Miguel"  │  (str)
                     └───────────┘

  edad ───────────→ ┌───────────┐
                     │    25     │  (int)
                     └───────────┘

  esta_activo ────→ ┌───────────┐
                     │   True    │  (bool)
                     └───────────┘

  La variable es la flecha (etiqueta).
  El valor es lo que esta en la caja.
```

## 2.2 Reglas para nombrar variables

```python
# BIEN — snake_case (palabras separadas por guion bajo)
nombre_completo = "Miguel Mata"
edad_actual = 25
es_estudiante = True

# MAL — Python no acepta esto
mi nombre = "Miguel"     # Espacios no se permiten
2edad = 25               # No puede empezar con numero
class = "A"              # 'class' es palabra reservada de Python
```

**Convencion en Python:** todo en minusculas, palabras separadas por `_` (snake_case). No es obligatorio pero es lo que hace todo el mundo. Si escribes `miNombre` (camelCase) funciona, pero gritara "este viene de JavaScript".

## 2.3 Tipos de datos

Python tiene varios tipos de datos. Los basicos son:

### int — numeros enteros
```python
edad = 25
temperatura = -5
poblacion = 1000000
```

No llevan punto decimal. Pueden ser positivos o negativos. No tienen limite de tamaño (Python maneja numeros gigantes sin problema).

### float — numeros decimales
```python
estatura = 1.75
precio = 99.99
pi = 3.14159
```

Llevan punto decimal. Se llaman "float" por "floating point" (punto flotante).

**Cuidado con los floats:**
```python
print(0.1 + 0.2)   # 0.30000000000000004 (no es 0.3!)
```
Esto pasa en TODOS los lenguajes. Las computadoras no representan decimales perfectamente. Para dinero, usa enteros (centavos) o la libreria `decimal`.

### str — texto (strings)
```python
nombre = "Miguel"
apellido = 'Mata'          # Comillas simples o dobles, ambas funcionan
mensaje = "Hola, mundo!"
vacio = ""                  # String vacio (existe pero no tiene nada)
```

Un string es una secuencia de caracteres. Siempre va entre comillas.

### bool — verdadero o falso
```python
es_mayor = True
tiene_cuenta = False
```

Solo dos valores posibles: `True` o `False` (con mayuscula inicial). Se usa para condiciones y logica.

### NoneType — la nada
```python
resultado = None
```

`None` significa "no hay valor". No es 0, no es "", no es False. Es la ausencia de valor. Es como `null` en JavaScript o SQL.

## 2.4 Saber el tipo de un dato

```python
print(type(25))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("Hola"))     # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
```

`type()` te dice que tipo de dato es. Util para debuggear cuando algo no funciona.

## 2.5 Conversion de tipos (casting)

A veces necesitas convertir un tipo a otro:

```python
# String a entero
edad_texto = "25"
edad_numero = int(edad_texto)     # 25 (ahora es int)

# Entero a string
edad = 25
edad_texto = str(edad)            # "25" (ahora es str)

# String a float
precio_texto = "99.99"
precio = float(precio_texto)      # 99.99 (ahora es float)

# Float a entero (TRUNCA, no redondea)
precio = 99.99
entero = int(precio)              # 99 (se pierde el .99)
```

**Cuando lo necesitas:**
```python
# Esto NO funciona:
edad = 25
print("Tengo " + edad + " años")    # TypeError!

# Opcion 1: convertir a string
print("Tengo " + str(edad) + " años")

# Opcion 2: usar f-string (MEJOR)
print(f"Tengo {edad} años")
```

El f-string convierte automaticamente. Por eso es la forma preferida.

## 2.6 Reasignar variables

Las variables pueden cambiar de valor:

```python
puntos = 0
print(puntos)    # 0

puntos = 10
print(puntos)    # 10

puntos = puntos + 5
print(puntos)    # 15
```

Y Python es **dinamicamente tipado**, lo que significa que una variable puede cambiar de tipo:

```python
dato = 42          # Es int
dato = "cuarenta"  # Ahora es str
dato = True        # Ahora es bool
```

Esto es posible pero NO recomendable. Que una variable cambie de tipo es confuso y fuente de bugs.

## 2.7 Constantes

Python no tiene constantes reales (como `const` en JavaScript). La convencion es usar MAYUSCULAS:

```python
PI = 3.14159
MAX_INTENTOS = 3
NOMBRE_APP = "MikaCLI"
```

Nada te impide cambiarlas, pero el nombre en mayusculas le dice a todo dev: "esto no se toca".

## 2.8 Multiples asignaciones

```python
# Asignar varias variables en una linea
x, y, z = 1, 2, 3
print(x)    # 1
print(y)    # 2
print(z)    # 3

# Mismo valor a varias variables
a = b = c = 0
```

Es un atajo. Usalo con moderacion — si pones 5 variables en una linea se vuelve dificil de leer.

---

## Ejercicios

**Ejercicio 2.1:** Crea variables para tu informacion personal y muestralas:
```python
nombre = "tu nombre"
edad = tu_edad
ciudad = "tu ciudad"
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")
```

**Ejercicio 2.2:** Que tipo de dato es cada uno? Usa `type()` para verificar:
```python
a = 42
b = "42"
c = 42.0
d = True
e = None
```

**Ejercicio 2.3:** Intenta esto y explica por que falla:
```python
resultado = "10" + 5
```

**Ejercicio 2.4:** Convierte y suma:
```python
texto1 = "100"
texto2 = "50"
# Haz que esto imprima 150 (no "10050")
```

**Ejercicio 2.5:** Crea un programa que calcule tu edad en dias (aproximado):
```python
edad_anios = tu_edad
edad_dias = edad_anios * 365
print(f"He vivido aproximadamente {edad_dias} dias")
```

---

> **Checkpoint:** Si entiendes que `"25"` y `25` son cosas diferentes (uno es texto, otro es numero), estas listo para el Capitulo 3.

[← Capitulo 1](01-instalacion.md) | [Capitulo 3 →](03-operadores.md)
