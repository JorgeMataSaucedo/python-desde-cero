# Capitulo 8 — Tuplas

> Como una lista, pero que no se puede modificar. Para cuando los datos no deben cambiar.

---

## 8.1 Que es una tupla?

Una tupla es como una lista, pero **inmutable**: una vez creada, no se puede modificar. No puedes agregar, eliminar ni cambiar sus elementos.

```python
coordenadas = (19.4326, -99.1332)    # CDMX
colores_rgb = (255, 0, 0)            # Rojo
datos = ("Miguel", 25, "Monterrey")
```

Las tuplas se crean con parentesis `()` en vez de corchetes `[]`.

## 8.2 Para que sirve si no se puede modificar?

Exactamente por eso. Hay datos que NO deben cambiar:
- Coordenadas geograficas
- Colores RGB
- Dias de la semana
- Configuraciones fijas

Si usas una lista, alguien (o tu mismo por accidente) podria modificarla. Con una tupla, Python te protege.

```python
dias = ("lunes", "martes", "miercoles", "jueves", "viernes")
dias[0] = "domingo"    # TypeError: 'tuple' object does not support item assignment
```

## 8.3 Crear tuplas

```python
# Con parentesis
colores = ("rojo", "verde", "azul")

# Sin parentesis (tambien funciona)
colores = "rojo", "verde", "azul"

# Tupla de un solo elemento (necesita la coma)
solo_uno = ("rojo",)       # Esto SI es tupla
no_es_tupla = ("rojo")     # Esto es un string entre parentesis

# Tupla vacia
vacia = ()

# Desde una lista
lista = [1, 2, 3]
tupla = tuple(lista)       # (1, 2, 3)
```

**Ojo con la tupla de un elemento:** la coma al final es lo que la hace tupla, no los parentesis.

## 8.4 Acceder a elementos

Funciona exactamente igual que las listas:

```python
datos = ("Miguel", 25, "Monterrey")

print(datos[0])      # "Miguel"
print(datos[-1])     # "Monterrey"
print(datos[1:])     # (25, "Monterrey")
print(len(datos))    # 3
```

## 8.5 Desempaquetado (unpacking)

Esta es la magia de las tuplas:

```python
coordenadas = (19.4326, -99.1332)

# En vez de:
lat = coordenadas[0]
lon = coordenadas[1]

# Puedes hacer:
lat, lon = coordenadas
print(lat)    # 19.4326
print(lon)    # -99.1332
```

El numero de variables DEBE coincidir con el numero de elementos:
```python
a, b, c = (1, 2, 3)       # Bien
a, b = (1, 2, 3)           # ValueError: too many values to unpack
```

### Desempaquetado con *

```python
primero, *resto = (1, 2, 3, 4, 5)
print(primero)    # 1
print(resto)      # [2, 3, 4, 5]  (nota: es una lista)

primero, *medio, ultimo = (1, 2, 3, 4, 5)
print(primero)    # 1
print(medio)      # [2, 3, 4]
print(ultimo)     # 5
```

## 8.6 Intercambiar variables

Un truco clasico de Python usando tuplas:

```python
a = 10
b = 20

# En otros lenguajes necesitas variable temporal:
# temp = a
# a = b
# b = temp

# En Python:
a, b = b, a
print(a)    # 20
print(b)    # 10
```

Python crea una tupla temporal `(b, a)` = `(20, 10)` y la desempaqueta en `a, b`.

## 8.7 Tuplas en funciones

Las funciones pueden regresar multiples valores usando tuplas:

```python
def dividir(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo    # Regresa una tupla

resultado = dividir(10, 3)
print(resultado)    # (3, 1)

# O desempaquetado directamente:
cociente, residuo = dividir(10, 3)
print(cociente)     # 3
print(residuo)      # 1
```

## 8.8 Metodos de tuplas

Las tuplas solo tienen 2 metodos (porque son inmutables):

```python
datos = (1, 2, 3, 2, 4, 2)

print(datos.count(2))     # 3  (cuantas veces aparece el 2)
print(datos.index(3))     # 2  (en que posicion esta el 3)
```

## 8.9 Tupla vs Lista — cuando usar cual?

| Usa Lista `[]` cuando... | Usa Tupla `()` cuando... |
|--------------------------|--------------------------|
| Los datos van a cambiar | Los datos son fijos |
| Necesitas agregar/eliminar | Solo necesitas leer |
| Es una coleccion que crece | Es un grupo de valores relacionados |
| Ej: lista de compras | Ej: coordenadas (lat, lon) |
| Ej: registros de gastos | Ej: color RGB (255, 0, 0) |
| Ej: tareas pendientes | Ej: configuracion constante |

**Regla simple:** si vas a usar `.append()`, necesitas una lista. Si nunca vas a modificarla, usa tupla.

---

## Ejercicios

**Ejercicio 8.1:** Crea una tupla con los meses del año. Pide al usuario un numero (1-12) y muestra el mes correspondiente.

**Ejercicio 8.2:** Crea una funcion que reciba una lista de numeros y regrese una tupla con (minimo, maximo, promedio).

**Ejercicio 8.3:** Usa desempaquetado para intercambiar los valores de 3 variables:
```python
a, b, c = 1, 2, 3
# Haz que queden: a=3, b=1, c=2
```

**Ejercicio 8.4:** Dada una lista de tuplas con (nombre, calificacion), encuentra al estudiante con la mejor nota:
```python
estudiantes = [
    ("Ana", 95),
    ("Carlos", 87),
    ("Diana", 92),
    ("Miguel", 98)
]
# Imprime: "El mejor estudiante es Miguel con 98"
```

---

> **Checkpoint:** Si entiendes que las tuplas son listas inmutables y sabes usar desempaquetado, estas listo para el Capitulo 9.

[← Capitulo 7](07-listas.md) | [Capitulo 9 →](09-diccionarios.md)
