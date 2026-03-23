# Capitulo 14 — Manejo de Errores

> Que tu programa nunca le muestre un traceback al usuario. Nunca.

---

## 14.1 Que es un error?

Cuando Python no puede ejecutar algo, lanza una excepcion (error). Si no la manejas, el programa muere mostrando un monton de texto rojo:

```
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    resultado = 10 / 0
ZeroDivisionError: division by zero
```

Para el usuario esto es incomprensible. Para ti como dev, es informacion: te dice que paso, donde, y por que.

## 14.2 Tipos de errores comunes

| Error | Cuando pasa | Ejemplo |
|-------|-------------|---------|
| `SyntaxError` | Codigo mal escrito | `if True print("hola")` (falta `:`) |
| `NameError` | Variable no existe | `print(nombre)` sin definir `nombre` |
| `TypeError` | Tipo incorrecto | `"texto" + 5` |
| `ValueError` | Valor incorrecto | `int("abc")` |
| `KeyError` | Llave no existe en dict | `datos["inexistente"]` |
| `IndexError` | Indice fuera de rango | `lista[99]` en lista de 3 |
| `FileNotFoundError` | Archivo no existe | `open("no_existe.txt")` |
| `ZeroDivisionError` | Division entre cero | `10 / 0` |
| `AttributeError` | Metodo no existe | `5.upper()` (int no tiene upper) |
| `ImportError` | No se puede importar | `from modulo import inexistente` |

`SyntaxError` es el unico que no puedes manejar con try/except — significa que tu codigo esta mal escrito.

## 14.3 try/except — atrapar errores

```python
try:
    numero = int(input("Dame un numero: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Eso no es un numero.")
except ZeroDivisionError:
    print("No puedo dividir entre cero.")
```

**Flujo:**
1. Python ejecuta el bloque `try`
2. Si todo sale bien, salta los `except` y sigue
3. Si hay error, busca el `except` que coincida con el tipo de error
4. Si encuentra uno, ejecuta ese bloque
5. El programa NO muere

## 14.4 Atrapar el mensaje del error

```python
try:
    resultado = int("abc")
except ValueError as e:
    print(f"Error: {e}")
    # Error: invalid literal for int() with base 10: 'abc'
```

`as e` guarda la informacion del error en la variable `e`. Util para mostrar mensajes informativos.

## 14.5 except generico

```python
try:
    algo_riesgoso()
except Exception as e:
    print(f"Algo salio mal: {e}")
```

`Exception` atrapa CUALQUIER error. Usalo como ultimo recurso, no como primera opcion:

```python
# BIEN — especifico
try:
    datos = json.load(archivo)
except FileNotFoundError:
    datos = {}
except json.JSONDecodeError:
    datos = {}

# MAL — generico (no sabes que fallo)
try:
    datos = json.load(archivo)
except Exception:
    datos = {}
```

## 14.6 else — cuando no hubo error

```python
try:
    numero = int(input("Numero: "))
except ValueError:
    print("No es un numero valido")
else:
    # Solo se ejecuta si NO hubo error
    print(f"Tu numero es {numero}")
```

## 14.7 finally — siempre se ejecuta

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    # Se ejecuta SIEMPRE, haya error o no
    print("Proceso terminado")
```

Util para limpiar recursos (cerrar archivos, conexiones). Aunque con `with` no necesitas `finally` para archivos.

## 14.8 Anti-patrones (lo que NO debes hacer)

### Atrapar y callar

```python
# TERRIBLE — el error desaparece y nunca sabes que fallo
try:
    datos = json.load(archivo)
except:
    pass
```

### except desnudo

```python
# MAL — atrapa TODO, incluso Ctrl+C del usuario
try:
    algo()
except:    # Sin tipo de error
    pass
```

Siempre especifica el tipo de error, o al minimo usa `except Exception`.

### try gigante

```python
# MAL — demasiado codigo en el try, no sabes que linea fallo
try:
    datos = leer_json(ruta)
    datos["movimientos"].append(nuevo)
    escribir_json(ruta, datos)
    print("Listo")
    enviar_notificacion()
except Exception:
    print("Error")
```

Mejor: pon solo lo riesgoso en el try.

## 14.9 .get() — alternativa a try/except para diccionarios

```python
datos = {"nombre": "Miguel"}

# Con try/except
try:
    valor = datos["edad"]
except KeyError:
    valor = 0

# Con .get() — mas limpio
valor = datos.get("edad", 0)
```

Para diccionarios, `.get()` es casi siempre mejor que try/except.

## 14.10 Validar ANTES vs atrapar DESPUES

Dos filosofias:

```python
# LBYL — Look Before You Leap (validar antes)
if archivo.exists():
    datos = json.load(open(archivo))
else:
    datos = {}

# EAFP — Easier to Ask Forgiveness than Permission (atrapar despues)
try:
    datos = json.load(open(archivo))
except FileNotFoundError:
    datos = {}
```

Python prefiere EAFP (try/except). Es mas "Pythonico" y maneja mas casos edge.

---

## Ejercicios

**Ejercicio 14.1:** Crea una funcion que divida dos numeros. Maneja division entre cero y tipos invalidos.

**Ejercicio 14.2:** Crea una funcion que lea un archivo JSON de forma segura (maneja archivo inexistente y JSON corrupto).

**Ejercicio 14.3:** Crea un programa que pida la edad al usuario. Sigue pidiendo hasta que de un numero valido entre 1 y 150.

**Ejercicio 14.4:** Dada una lista de diccionarios, accede a una llave que puede no existir en todos los diccionarios. No debe crashear.
```python
personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Carlos"},             # No tiene edad
    {"nombre": "Diana", "edad": 25},
]
# Imprime la edad de cada uno, o "No especificada" si falta
```

---

> **Checkpoint:** Si sabes cuando usar try/except vs .get(), y tu programa nunca muestra un traceback, estas listo para el Capitulo 15.

[← Capitulo 13](13-archivos-y-json.md) | [Capitulo 15 →](15-clases.md)
