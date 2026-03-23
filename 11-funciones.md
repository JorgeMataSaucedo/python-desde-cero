# Capitulo 11 — Funciones

> Reutilizar codigo, organizar logica, dejar de repetirse.

---

## 11.1 Que es una funcion?

Una funcion es un bloque de codigo con nombre que puedes llamar cuando quieras. Es como guardar una receta: la escribes una vez y la usas cuantas veces necesites.

```python
# DEFINIR la funcion
def saludar(nombre):
    print(f"Hola {nombre}!")

# LLAMAR la funcion
saludar("Diego")     # Hola Diego!
saludar("Ilse")      # Hola Ilse!
saludar("Miguel")    # Hola Miguel!
```

Sin funciones, tendrias que repetir el mismo codigo cada vez.

```
  Como funciona una funcion:

  ┌─────────────────────────────────────┐
  │  saludar("Diego")                   │  ← LLAMADA
  └──────────────┬──────────────────────┘
                 │
                 ▼
  ┌─────────────────────────────────────┐
  │  def saludar(nombre):               │  ← DEFINICION
  │      nombre = "Diego"  (se asigna)  │
  │      print(f"Hola {nombre}!")       │
  │                                     │
  │      Salida: "Hola Diego!"          │
  └─────────────────────────────────────┘

  Dato entra (argumento) → se procesa → resultado sale (return o print)
```

## 11.2 Anatomia de una funcion

```python
def calcular_area(base, altura):
    """Calcula el area de un rectangulo."""
    area = base * altura
    return area
```

- `def` — palabra clave que define una funcion
- `calcular_area` — nombre de la funcion (snake_case)
- `(base, altura)` — parametros (datos que recibe)
- `"""..."""` — docstring (documentacion, opcional pero recomendado)
- Cuerpo — el codigo indentado que ejecuta
- `return` — lo que regresa la funcion

## 11.3 Parametros y argumentos

```python
# 'nombre' y 'edad' son PARAMETROS (en la definicion)
def presentarse(nombre, edad):
    print(f"Soy {nombre} y tengo {edad} años")

# "Miguel" y 25 son ARGUMENTOS (en la llamada)
presentarse("Miguel", 25)
```

### Parametros con valor por defecto

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo} {nombre}!")

saludar("Miguel")               # Hola Miguel! (usa el default)
saludar("Miguel", "Buenos dias") # Buenos dias Miguel!
```

Los parametros con default van AL FINAL:
```python
# BIEN
def funcion(obligatorio, opcional=10):

# MAL
def funcion(opcional=10, obligatorio):  # SyntaxError
```

### Argumentos por nombre (keyword arguments)

```python
def crear_usuario(nombre, edad, ciudad):
    print(f"{nombre}, {edad}, {ciudad}")

# Por posicion (el orden importa)
crear_usuario("Miguel", 25, "Monterrey")

# Por nombre (el orden NO importa)
crear_usuario(ciudad="Monterrey", nombre="Miguel", edad=25)
```

## 11.4 return — regresar valores

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)    # 8
```

### Funcion sin return

```python
def saludar(nombre):
    print(f"Hola {nombre}")

resultado = saludar("Miguel")
print(resultado)    # None
```

Si no hay `return`, la funcion regresa `None`. No es un error, pero significa que la funcion "hace algo" en vez de "calcular algo".

### Return multiples valores

```python
def estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    return minimo, maximo, promedio    # Regresa tupla

menor, mayor, prom = estadisticas([10, 20, 30, 40])
print(f"Min: {menor}, Max: {mayor}, Promedio: {prom}")
```

### Return como salida anticipada

```python
def dividir(a, b):
    if b == 0:
        print("No se puede dividir entre cero")
        return    # Sale de la funcion sin regresar valor
    return a / b
```

`return` sin valor termina la funcion inmediatamente. Util para validaciones.

## 11.5 Alcance de variables (scope)

Las variables creadas DENTRO de una funcion solo existen dentro de ella:

```python
def mi_funcion():
    mensaje = "Hola"    # Variable LOCAL
    print(mensaje)

mi_funcion()
print(mensaje)    # NameError: 'mensaje' is not defined
```

Las variables creadas FUERA de funciones son globales:

```python
nombre = "Miguel"    # Variable GLOBAL

def saludar():
    print(f"Hola {nombre}")    # Puede LEER la variable global

saludar()    # Hola Miguel
```

**Regla:** las funciones pueden LEER variables globales, pero no deben MODIFICARLAS. Si necesitas un dato, pasalo como parametro.

```python
# MAL — modifica variable global
contador = 0
def incrementar():
    global contador    # Esto funciona pero es mala practica
    contador += 1

# BIEN — recibe y regresa
def incrementar(contador):
    return contador + 1

contador = 0
contador = incrementar(contador)
```

## 11.6 Funciones como bloques de LEGO

Las funciones se pueden llamar entre si:

```python
def limpiar_nombre(nombre):
    return nombre.strip().title()

def validar_edad(edad_texto):
    if not edad_texto.isdigit():
        return None
    edad = int(edad_texto)
    if edad < 0 or edad > 150:
        return None
    return edad

def registrar_persona():
    nombre = limpiar_nombre(input("Nombre: "))
    edad = validar_edad(input("Edad: "))

    if edad is None:
        print("Edad invalida")
        return

    print(f"Registrado: {nombre}, {edad} años")
```

Cada funcion hace UNA cosa. `registrar_persona` las orquesta. Si mañana cambias como se valida la edad, solo tocas `validar_edad`.

## 11.7 Patron leer-modificar-escribir

El patron mas comun en MikaCLI:

```python
def agregar_gasto(monto, concepto):
    # 1. LEER
    datos = leer_json(GASTOS_FILE)

    # 2. MODIFICAR
    nuevo = {"monto": monto, "concepto": concepto, "fecha": "2026-03-21"}
    datos.setdefault("movimientos", [])
    datos["movimientos"].append(nuevo)

    # 3. ESCRIBIR
    escribir_json(GASTOS_FILE, datos)

    print(f"Gasto registrado: ${monto} — {concepto}")
```

## 11.8 Docstrings

```python
def calcular_balance(movimientos):
    """Calcula el balance total (ingresos - gastos).

    Args:
        movimientos: Lista de diccionarios con 'tipo' y 'monto'.

    Returns:
        float: El balance calculado.
    """
    ingresos = sum(m["monto"] for m in movimientos if m["tipo"] == "ingreso")
    gastos = sum(m["monto"] for m in movimientos if m["tipo"] == "gasto")
    return ingresos - gastos
```

El docstring documenta: que hace, que recibe, que regresa. No es obligatorio en funciones simples, pero en funciones importantes marca la diferencia.

## 11.9 Cuantas funciones necesito?

**Regla de oro:** si necesitas usar "y" para describir lo que hace una funcion, son varias funciones:

```python
# MAL — "lee el archivo Y calcula el balance Y lo imprime"
def procesar_gastos():
    # 50 lineas haciendo de todo

# BIEN — cada una hace UNA cosa
def leer_gastos():
    ...
def calcular_balance(gastos):
    ...
def mostrar_balance(balance):
    ...
```

**Otra regla:** si una funcion pasa de 50 lineas, probablemente esta haciendo demasiado. Dividela.

---

## Ejercicios

**Ejercicio 11.1:** Crea una funcion que reciba una lista de numeros y regrese solo los pares:
```python
def filtrar_pares(numeros):
    # Tu codigo
    pass

print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
```

**Ejercicio 11.2:** Crea una funcion que reciba un precio y un porcentaje de descuento, y regrese el precio final:
```python
def aplicar_descuento(precio, descuento=10):
    pass

print(aplicar_descuento(100))       # 90.0
print(aplicar_descuento(100, 25))   # 75.0
```

**Ejercicio 11.3:** Crea un mini sistema de calificaciones con estas funciones:
- `agregar_calificacion(lista, nombre, nota)` — agrega a la lista
- `obtener_promedio(lista)` — calcula promedio
- `obtener_mejor(lista)` — regresa el de mejor nota
- `mostrar_reporte(lista)` — imprime todo formateado

**Ejercicio 11.4:** Crea una funcion `es_palindromo(texto)` que regrese True si el texto se lee igual al derecho y al reves. Ejemplo: "anita lava la tina" → True.

**Ejercicio 11.5:** Crea un conversor de unidades con funciones:
- `km_a_millas(km)`
- `celsius_a_fahrenheit(c)`
- `kg_a_libras(kg)`
Haz un menu que permita elegir que conversion hacer.

---

> **Checkpoint:** Si puedes crear funciones que reciben datos, los procesan y regresan resultados, estas listo para el Capitulo 12.

[← Capitulo 10](10-ciclos.md) | [Capitulo 12 →](12-modulos.md)
