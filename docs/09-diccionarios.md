# Capitulo 9 — Diccionarios

> Tu estructura de datos mas poderosa. Datos con nombre: llave y valor.

---

## 9.1 Que es un diccionario?

Un diccionario es una coleccion de pares **llave:valor**. En vez de acceder por posicion (como listas), accedes por nombre.

Piensa en un diccionario real: buscas la palabra (llave) y encuentras su definicion (valor).

```python
persona = {
    "nombre": "Miguel",
    "edad": 25,
    "ciudad": "Monterrey"
}
```

Se crea con llaves `{}` y cada par se separa por comas. La llave y el valor se separan por `:`.

```
  Un diccionario en memoria:

  persona ──→ ┌──────────────────────────────┐
              │  "nombre" ──→ "Miguel"        │
              │  "edad"   ──→  25             │
              │  "ciudad" ──→ "Monterrey"     │
              └──────────────────────────────┘

  Lista: buscas por POSICION  →  frutas[0]
  Diccionario: buscas por NOMBRE  →  persona["nombre"]
```

## 9.2 Acceder a valores

```python
persona = {"nombre": "Miguel", "edad": 25, "ciudad": "Monterrey"}

# Con corchetes
print(persona["nombre"])     # "Miguel"
print(persona["edad"])       # 25

# Si la llave no existe:
print(persona["telefono"])   # KeyError!

# Con .get() — forma segura
print(persona.get("nombre"))           # "Miguel"
print(persona.get("telefono"))         # None (no crashea)
print(persona.get("telefono", "N/A"))  # "N/A" (valor por defecto)
```

**Regla:** usa `.get()` cuando no estas seguro si la llave existe. Usa `[]` cuando SABES que existe.

## 9.3 Agregar y modificar

```python
persona = {"nombre": "Miguel", "edad": 25}

# Agregar nuevo par
persona["ciudad"] = "Monterrey"
print(persona)    # {"nombre": "Miguel", "edad": 25, "ciudad": "Monterrey"}

# Modificar existente
persona["edad"] = 26
print(persona)    # {"nombre": "Miguel", "edad": 26, "ciudad": "Monterrey"}
```

Es la misma sintaxis para agregar y modificar. Si la llave existe, la sobreescribe. Si no existe, la crea.

## 9.4 Eliminar

```python
persona = {"nombre": "Miguel", "edad": 25, "ciudad": "Monterrey"}

# del — elimina por llave
del persona["ciudad"]
print(persona)    # {"nombre": "Miguel", "edad": 25}

# pop — elimina y regresa el valor
edad = persona.pop("edad")
print(edad)       # 25
print(persona)    # {"nombre": "Miguel"}

# pop con valor por defecto (no crashea si no existe)
valor = persona.pop("telefono", "No existe")
print(valor)      # "No existe"
```

## 9.5 Verificar si una llave existe

```python
persona = {"nombre": "Miguel", "edad": 25}

print("nombre" in persona)      # True
print("telefono" in persona)    # False
print("telefono" not in persona)  # True
```

`in` verifica LLAVES, no valores:
```python
print("Miguel" in persona)    # False (busca en llaves, no en valores)
```

## 9.6 Recorrer un diccionario

```python
persona = {"nombre": "Miguel", "edad": 25, "ciudad": "Monterrey"}

# Solo llaves
for llave in persona:
    print(llave)
# nombre, edad, ciudad

# Solo valores
for valor in persona.values():
    print(valor)
# Miguel, 25, Monterrey

# Llaves Y valores
for llave, valor in persona.items():
    print(f"{llave}: {valor}")
# nombre: Miguel
# edad: 25
# ciudad: Monterrey
```

`.items()` es el mas util. Te da ambas cosas al mismo tiempo.

## 9.7 Metodos utiles

```python
persona = {"nombre": "Miguel", "edad": 25}

# keys — todas las llaves
print(persona.keys())      # dict_keys(['nombre', 'edad'])

# values — todos los valores
print(persona.values())    # dict_values(['Miguel', 25])

# items — todos los pares
print(persona.items())     # dict_items([('nombre', 'Miguel'), ('edad', 25)])

# update — fusionar dos diccionarios
extra = {"ciudad": "Monterrey", "pais": "Mexico"}
persona.update(extra)
print(persona)
# {"nombre": "Miguel", "edad": 25, "ciudad": "Monterrey", "pais": "Mexico"}

# setdefault — agregar solo si NO existe
persona.setdefault("nombre", "Otro")    # No hace nada (ya existe)
persona.setdefault("telefono", "N/A")   # Agrega telefono: "N/A"
```

## 9.8 Diccionarios anidados

Un diccionario puede contener otros diccionarios o listas:

```python
usuario = {
    "nombre": "Miguel",
    "edad": 25,
    "direccion": {
        "calle": "Av. Universidad 123",
        "ciudad": "Monterrey",
        "estado": "Nuevo Leon"
    },
    "hobbies": ["programar", "gaming", "musica"]
}

# Acceder a datos anidados
print(usuario["direccion"]["ciudad"])    # "Monterrey"
print(usuario["hobbies"][0])             # "programar"
```

Esto es EXACTAMENTE la estructura de un archivo JSON. Cuando lees un JSON en Python, obtienes diccionarios anidados.

## 9.9 Lista de diccionarios

La estructura mas comun en programacion real:

```python
empleados = [
    {"nombre": "Ana", "puesto": "Dev", "salario": 35000},
    {"nombre": "Carlos", "puesto": "QA", "salario": 28000},
    {"nombre": "Diana", "puesto": "PM", "salario": 40000},
]

# Acceder al segundo empleado
print(empleados[1]["nombre"])    # "Carlos"

# Recorrer todos
for emp in empleados:
    print(f"{emp['nombre']} - {emp['puesto']} - ${emp['salario']:,}")

# Buscar uno especifico
for emp in empleados:
    if emp["nombre"] == "Ana":
        print(f"Ana gana ${emp['salario']:,}")
        break
```

Esta estructura es tu pan de cada dia. Los archivos JSON de MikaCLI son exactamente esto.

## 9.10 Diccionario vs Lista — cuando usar cual?

| Usa Lista `[]` cuando... | Usa Diccionario `{}` cuando... |
|--------------------------|-------------------------------|
| Importa el orden | Importa el nombre de cada dato |
| Accedes por posicion | Accedes por llave |
| Son elementos similares | Son atributos de una cosa |
| Ej: lista de nombres | Ej: datos de UNA persona |
| Ej: numeros para sumar | Ej: configuracion de la app |

**Combinados:** lista de diccionarios = tabla de base de datos.

---

## Ejercicios

**Ejercicio 9.1:** Crea un diccionario con tus datos personales (nombre, edad, ciudad, hobby favorito). Imprimelo formateado.

**Ejercicio 9.2:** Crea un mini directorio telefonico:
```
1. Agregar contacto (nombre + telefono)
2. Buscar contacto por nombre
3. Mostrar todos los contactos
4. Salir
```

**Ejercicio 9.3:** Dado un texto, cuenta cuantas veces aparece cada palabra:
```python
texto = "el gato y el perro y el pajaro"
# Resultado: {"el": 3, "gato": 1, "y": 2, "perro": 1, "pajaro": 1}
```

**Ejercicio 9.4:** Crea una lista de 3 productos con nombre, precio y cantidad. Calcula el total de la compra.
```python
productos = [
    {"nombre": "Cafe", "precio": 45, "cantidad": 2},
    ...
]
```

**Ejercicio 9.5:** Dado un diccionario anidado de un estudiante con materias y calificaciones, calcula el promedio general:
```python
estudiante = {
    "nombre": "Miguel",
    "materias": {
        "python": [90, 85, 95],
        "bases_datos": [88, 92, 78],
        "ingles": [70, 75, 80]
    }
}
```

---

> **Checkpoint:** Si puedes crear, acceder, modificar y recorrer diccionarios, felicidades. Ya tienes el 80% de lo que necesitas para construir MikaCLI.

[← Capitulo 8](08-tuplas.md) | [Capitulo 10 →](10-ciclos.md)
