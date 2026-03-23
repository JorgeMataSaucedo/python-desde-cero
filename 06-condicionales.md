# Capitulo 6 — Condicionales

> Enseñarle a tu programa a tomar decisiones. Si pasa esto, haz aquello.

---

## 6.1 Que es un condicional?

Un condicional es una pregunta que tu programa se hace. Dependiendo de la respuesta (True o False), ejecuta un bloque de codigo u otro.

Es como la vida real:
- **Si** llueve → lleva paraguas
- **Si no** llueve → sal normal

En Python:
```python
llueve = True

if llueve:
    print("Lleva paraguas")
else:
    print("Sal normal")
```

```
  Como piensa un condicional:

                ┌─────────────┐
                │ llueve?     │
                └──────┬──────┘
                       │
                ┌──────┴──────┐
                │             │
               SI            NO
                │             │
                ▼             ▼
          ┌───────────┐ ┌──────────┐
          │  Paraguas  │ │ Sal normal│
          └───────────┘ └──────────┘

  Python evalua la condicion → True o False → ejecuta un camino.
```

## 6.2 if — la pregunta basica

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

**Como funciona:**
1. Python evalua `edad >= 18` → es `True` o `False`?
2. Si es `True`, ejecuta el bloque indentado (lo que esta despues de los `:` con 4 espacios)
3. Si es `False`, se lo salta

**La indentacion es OBLIGATORIA.** Python usa espacios (4 por convencion) para saber que codigo pertenece al if. Si no indentas, te da error. Si indentas mal, se ejecuta codigo que no deberia.

```python
# BIEN
if edad >= 18:
    print("Mayor de edad")     # 4 espacios = pertenece al if

# MAL
if edad >= 18:
print("Mayor de edad")         # Sin indentacion = IndentationError
```

## 6.3 if-else — dos caminos

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

`else` se ejecuta cuando la condicion del `if` es `False`. Es el "plan B".

## 6.4 if-elif-else — multiples caminos

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Bueno")
elif nota >= 70:
    print("Regular")
elif nota >= 60:
    print("Suficiente")
else:
    print("Reprobado")
```

`elif` es la contraccion de "else if". Python evalua de arriba hacia abajo:
1. nota >= 90? No (85 no es >= 90)
2. nota >= 80? **Si** → ejecuta "Bueno" y SE DETIENE
3. No evalua los demas elif ni el else

**Importante:** solo se ejecuta UN bloque. El primero que sea True. Los demas se ignoran.

## 6.5 Condiciones compuestas

Puedes combinar condiciones con `and`, `or`, `not`:

```python
edad = 25
tiene_licencia = True

# AND — ambas deben ser True
if edad >= 18 and tiene_licencia:
    print("Puede manejar")

# OR — al menos una debe ser True
if edad < 18 or not tiene_licencia:
    print("No puede manejar")

# NOT — invierte la condicion
if not tiene_licencia:
    print("Necesita tramitar licencia")
```

## 6.6 Condiciones anidadas

Un if dentro de otro if:

```python
tiene_cuenta = True
saldo = 500

if tiene_cuenta:
    if saldo > 0:
        print("Puede hacer transferencia")
    else:
        print("Saldo insuficiente")
else:
    print("Necesita crear cuenta")
```

Funciona pero se vuelve dificil de leer con muchos niveles. Generalmente es mejor usar `and`:

```python
# Equivalente y mas limpio:
if tiene_cuenta and saldo > 0:
    print("Puede hacer transferencia")
elif tiene_cuenta:
    print("Saldo insuficiente")
else:
    print("Necesita crear cuenta")
```

## 6.7 Ternario — if en una linea

Para casos simples donde solo necesitas asignar un valor:

```python
edad = 25
status = "mayor" if edad >= 18 else "menor"
print(status)    # "mayor"
```

Es equivalente a:
```python
if edad >= 18:
    status = "mayor"
else:
    status = "menor"
```

Usalo solo cuando sea simple y claro. Si la condicion es compleja, usa el if normal.

## 6.8 Valores "truthy" y "falsy"

En Python, muchas cosas se evaluan como True o False en un if:

```python
# Estos son FALSY (se evaluan como False):
if 0:           # False — cero
if "":          # False — string vacio
if []:          # False — lista vacia
if {}:          # False — diccionario vacio
if None:        # False — None
if False:       # False — obviamente

# Todo lo demas es TRUTHY (se evalua como True):
if 1:           # True — cualquier numero distinto de 0
if "hola":      # True — string con contenido
if [1, 2]:      # True — lista con elementos
if {"a": 1}:    # True — diccionario con contenido
```

Esto es muy util para validar datos:
```python
nombre = ""
if nombre:
    print(f"Hola {nombre}")
else:
    print("No escribiste tu nombre")

# Es mas limpio que:
if nombre != "":
    ...
```

## 6.9 Ejemplo real: validar entrada

```python
entrada = input("Tu edad: ")

if not entrada:
    print("No escribiste nada")
elif not entrada.isdigit():
    print("Eso no es un numero")
else:
    edad = int(entrada)
    if edad < 0:
        print("La edad no puede ser negativa")
    elif edad > 150:
        print("No creo que tengas mas de 150 años")
    else:
        print(f"Tienes {edad} años")
```

Este es el tipo de validacion que haces en programas reales. Cubres todos los casos.

---

## Ejercicios

**Ejercicio 6.1:** Clasifica una temperatura:
```python
# Menor a 0: "Congelante"
# 0-15: "Frio"
# 16-25: "Agradable"
# 26-35: "Caliente"
# Mayor a 35: "Insoportable"
```

**Ejercicio 6.2:** Calcula el precio con descuento:
```python
# Si compra mas de 10 unidades: 20% descuento
# Si compra 5-10 unidades: 10% descuento
# Menos de 5: sin descuento
# Pide cantidad y precio unitario, muestra total
```

**Ejercicio 6.3:** Determina si un año es bisiesto:
```python
# Un año es bisiesto si:
# - Es divisible entre 4
# - EXCEPTO si es divisible entre 100
# - EXCEPTO si es divisible entre 400 (entonces SI es bisiesto)
# Ejemplo: 2000 si, 1900 no, 2024 si, 2023 no
```

**Ejercicio 6.4:** Crea un mini cajero:
```python
# Saldo inicial: 1000
# Menu: 1.Consultar, 2.Depositar, 3.Retirar
# Validar que no retire mas de lo que tiene
# Validar que deposite cantidad positiva
```

**Ejercicio 6.5:** Evalua una contraseña:
```python
# Pide una contraseña y evalua:
# - Menos de 6 caracteres: "Muy debil"
# - 6-8 caracteres: "Debil"
# - 9-12 caracteres: "Buena"
# - Mas de 12: "Fuerte"
# Bonus: si tiene numeros Y letras, sube un nivel
```

---

> **Checkpoint:** Si entiendes que `if` evalua True/False y que la indentacion define que codigo pertenece a cada bloque, estas listo para el Capitulo 7.

[← Capitulo 5](05-input.md) | [Capitulo 7 →](07-listas.md)
