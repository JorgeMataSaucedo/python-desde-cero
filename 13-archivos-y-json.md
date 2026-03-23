# Capitulo 13 — Archivos y JSON

> Guardar datos que sobrevivan al cerrar el programa.

---

## 13.1 El problema

Todo lo que guardas en variables se pierde cuando el programa termina:

```python
puntos = 100    # Existe mientras el programa corre
# Cierras la terminal... puntos ya no existe
```

Para que los datos persistan, necesitas guardarlos en un archivo.

## 13.2 Abrir archivos — open()

```python
archivo = open("datos.txt", "r")    # Abre para lectura
contenido = archivo.read()          # Lee todo el contenido
archivo.close()                      # SIEMPRE cerrar
```

### Modos de apertura

| Modo | Significado | Si el archivo no existe |
|------|-------------|------------------------|
| `"r"` | Lectura (read) | Error (FileNotFoundError) |
| `"w"` | Escritura (write) | Lo crea. Si existe, lo SOBREESCRIBE |
| `"a"` | Agregar (append) | Lo crea. Si existe, agrega al final |
| `"r+"` | Lectura y escritura | Error |

## 13.3 with — la forma correcta

```python
# SIN with (arriesgado — puedes olvidar cerrar)
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()    # Si hay error antes de esta linea, nunca se cierra

# CON with (seguro — se cierra automaticamente)
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
# Al salir del bloque with, el archivo se cierra SIEMPRE
```

**Siempre usa `with`.** No hay razon para no hacerlo.

## 13.4 Leer archivos de texto

```python
# Leer TODO el contenido como un string
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer linea por linea (lista de strings)
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())    # strip() quita el \n del final

# Leer linea por linea (mas eficiente en archivos grandes)
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

## 13.5 Escribir archivos de texto

```python
# Escribir (sobreescribe si existe)
with open("datos.txt", "w") as archivo:
    archivo.write("Linea 1\n")
    archivo.write("Linea 2\n")

# Agregar al final
with open("datos.txt", "a") as archivo:
    archivo.write("Linea nueva\n")
```

**Cuidado con `"w"`:** sobreescribe TODO el contenido. Si tenias datos, se pierden.

## 13.6 encoding — acentos y ñ

```python
# Sin encoding en Windows, puede fallar con acentos
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

**Siempre agrega `encoding="utf-8"`.** Especialmente en Windows, donde el encoding por defecto no es UTF-8.

## 13.7 JSON — el formato perfecto para datos estructurados

Los archivos de texto sirven para texto plano. Pero si necesitas guardar listas, diccionarios, numeros — necesitas estructura. Para eso existe JSON.

```json
{
    "nombre": "Miguel",
    "edad": 25,
    "hobbies": ["programar", "gaming"]
}
```

JSON es texto, pero con formato. Python lo puede leer y convertir directamente a diccionarios y listas.

## 13.8 El modulo json

```python
import json
```

### json.load — leer JSON desde archivo

```python
import json

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos)           # {'nombre': 'Miguel', 'edad': 25, ...}
print(type(datos))     # <class 'dict'>
print(datos["nombre"]) # "Miguel"
```

El archivo JSON se convierte en un diccionario de Python. Listo para usar.

### json.dump — escribir JSON a archivo

```python
import json

datos = {
    "nombre": "Miguel",
    "edad": 25,
    "hobbies": ["programar", "gaming"]
}

with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=2, ensure_ascii=False)
```

- `indent=2` — formato legible con 2 espacios de indentacion
- `ensure_ascii=False` — respeta acentos y ñ

### json.loads / json.dumps — para strings

```python
# String → Diccionario
texto = '{"nombre": "Miguel", "edad": 25}'
datos = json.loads(texto)

# Diccionario → String
datos = {"nombre": "Miguel", "edad": 25}
texto = json.dumps(datos)
```

La `s` al final significa "string". `load/dump` = archivo. `loads/dumps` = string.

## 13.9 Patron completo: leer → modificar → escribir

```python
import json

def leer_json(ruta):
    """Lee JSON. Si no existe, regresa diccionario vacio."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def escribir_json(ruta, datos):
    """Escribe diccionario a JSON."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

# USO:
datos = leer_json("gastos.json")              # 1. LEER
datos.setdefault("movimientos", [])
datos["movimientos"].append({                   # 2. MODIFICAR
    "concepto": "cafe",
    "monto": 45
})
escribir_json("gastos.json", datos)            # 3. ESCRIBIR
```

Este patron es el corazon de MikaCLI. Todos los modulos lo usan.

## 13.10 Manejo de errores con archivos

```python
import json

try:
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("Archivo no existe, creando uno nuevo")
    datos = {}
except json.JSONDecodeError:
    print("Archivo corrupto, empezando de cero")
    datos = {}
```

**Siempre** maneja estos dos errores cuando lees JSON:
- `FileNotFoundError` — el archivo no existe
- `json.JSONDecodeError` — el archivo existe pero no es JSON valido

## 13.11 pathlib — rutas inteligentes

```python
from pathlib import Path

# Construir rutas de forma portable
ruta = Path("data") / "gastos.json"

# Verificar si existe
if ruta.exists():
    print("El archivo existe")

# Crear directorio si no existe
Path("data").mkdir(exist_ok=True)
```

Ver [[Pathlib y Rutas]] para mas detalle.

---

## Ejercicios

**Ejercicio 13.1:** Crea un programa que escriba tu nombre en un archivo y despues lo lea e imprima.

**Ejercicio 13.2:** Crea un programa que pida nombres al usuario y los guarde en un JSON. Al iniciar, carga los nombres existentes. Al salir, los guarda.

**Ejercicio 13.3:** Crea un mini registro de gastos:
- Guardar gastos en un JSON
- Poder agregar un gasto (monto + concepto)
- Poder ver todos los gastos
- Que los datos persistan entre ejecuciones

**Ejercicio 13.4:** Lee un archivo JSON que no existe y maneja el error correctamente (no debe crashear).

---

> **Checkpoint:** Si puedes leer y escribir JSON, y los datos sobreviven al cerrar el programa, estas listo para el Capitulo 14.

[← Capitulo 12](12-modulos.md) | [Capitulo 14 →](14-errores.md)
