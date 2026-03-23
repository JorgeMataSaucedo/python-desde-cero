# Capitulo 5 — Input

> Hacer que tu programa hable con el usuario. Recibir datos, no solo mostrarlos.

---

## 5.1 La funcion input()

`input()` pausa el programa y espera a que el usuario escriba algo:

```python
nombre = input("Como te llamas? ")
print(f"Hola {nombre}!")
```

Cuando ejecutas esto:
```
Como te llamas? Miguel
Hola Miguel!
```

El programa se detiene en `input()`, espera a que escribas y presiones Enter, y guarda lo que escribiste en la variable `nombre`.

## 5.2 input() SIEMPRE regresa string

Esto es lo mas importante de este capitulo:

```python
edad = input("Cuantos años tienes? ")
print(type(edad))    # <class 'str'>
```

Aunque el usuario escriba `25`, Python lo guarda como `"25"` (string, no int). Si intentas hacer matematicas:

```python
edad = input("Tu edad: ")      # Usuario escribe: 25
nueva = edad + 5                # TypeError! No puedes sumar str + int
```

**Solucion: convertir el tipo**
```python
edad = int(input("Tu edad: "))       # Convierte a entero
precio = float(input("Precio: "))    # Convierte a decimal
```

El `int()` o `float()` envuelve al `input()`. Primero se ejecuta `input()` (recibe el string), despues `int()` lo convierte.

## 5.3 Validar entrada del usuario

El usuario puede escribir cualquier cosa. Si esperas un numero y escribe "abc":

```python
edad = int(input("Tu edad: "))
# Usuario escribe: abc
# ValueError: invalid literal for int() with base 10: 'abc'
```

**Solucion: try/except**
```python
try:
    edad = int(input("Tu edad: "))
    print(f"Tienes {edad} años")
except ValueError:
    print("Error: escribe un numero valido")
```

## 5.4 Patron: pedir hasta que sea valido

A veces quieres seguir pidiendo hasta que el usuario de un dato correcto:

```python
while True:
    entrada = input("Tu edad (numero): ")
    if entrada.isdigit():
        edad = int(entrada)
        break
    print("Error: escribe solo numeros")

print(f"Tu edad es {edad}")
```

- `while True` — ciclo infinito (se repite para siempre)
- `.isdigit()` — verifica si el string son puros numeros
- `break` — rompe el ciclo, sale del while
- Si el dato es valido, convierte y sale. Si no, pide de nuevo

## 5.5 Limpiar entrada

Los usuarios escriben con espacios de mas, mayusculas random, de todo:

```python
nombre = input("Tu nombre: ")
nombre = nombre.strip().title()    # Limpia espacios y pone en titulo

# Usuario escribe: "   miGUeL   "
# Resultado: "Miguel"
```

**Buena practica:** siempre limpia la entrada del usuario antes de usarla.

## 5.6 Menus interactivos

Con input puedes hacer menus:

```python
print("=== MENU ===")
print("1. Ver estado")
print("2. Registrar")
print("3. Salir")

opcion = input("Elige una opcion: ")

if opcion == "1":
    print("Mostrando estado...")
elif opcion == "2":
    print("Registrando...")
elif opcion == "3":
    print("Adios!")
else:
    print("Opcion no valida")
```

Nota que comparamos como string (`"1"`, no `1`) porque input siempre regresa string.

## 5.7 Multiples datos en una linea

Puedes pedir varios datos separados por algun caracter:

```python
entrada = input("Nombre y edad (separados por coma): ")
# Usuario escribe: Miguel, 25

partes = entrada.split(",")
nombre = partes[0].strip()
edad = int(partes[1].strip())

print(f"{nombre} tiene {edad} años")
```

`.split(",")` separa el string por comas y regresa una lista. `.strip()` limpia espacios.

---

## Ejercicios

**Ejercicio 5.1:** Crea una calculadora basica:
```python
# Pide dos numeros y una operacion (+, -, *, /)
# Muestra el resultado
# Maneja el caso de division entre cero
```

**Ejercicio 5.2:** Pide el nombre y la edad, calcula el año de nacimiento:
```python
# Si tiene 25 años en 2026, nacio en 2001
# Maneja que la edad sea un numero valido
```

**Ejercicio 5.3:** Crea un programa que pida numeros hasta que el usuario escriba "salir":
```python
# Muestra la suma de todos los numeros ingresados
# Pista: usa while True y break
```

**Ejercicio 5.4:** Crea un mini-registro:
```python
# Pide: nombre, edad, ciudad
# Limpia cada entrada (strip, title)
# Muestra un resumen formateado al final
```

---

> **Checkpoint:** Si sabes que `input()` siempre regresa string y sabes como convertirlo con `int()`, estas listo para el Capitulo 6.

[← Capitulo 4](04-strings.md) | [Capitulo 6 →](06-condicionales.md)
