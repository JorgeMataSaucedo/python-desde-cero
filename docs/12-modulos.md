# Capitulo 12 — Modulos

> Organizar tu codigo en multiples archivos. Dejar de tener todo en un solo .py gigante.

---

## 12.1 Por que modulos?

Imagina un archivo `main.py` con 2000 lineas. Donde esta la funcion de gastos? Quien sabe, busca entre las 2000 lineas. Eso es un infierno.

Los modulos te permiten separar tu codigo por responsabilidad:

```
mi_proyecto/
├── main.py          ← Solo rutea comandos
├── gastos.py        ← Todo lo de gastos
├── salud.py         ← Todo lo de salud
└── utils.py         ← Funciones compartidas
```

Cada archivo es un modulo. Cada modulo se enfoca en UNA cosa.

```
  Sin modulos:                   Con modulos:

  ┌──────────────┐               ┌──────────┐
  │   main.py    │               │ main.py  │ ← solo rutea
  │              │               └────┬─────┘
  │  2000 lineas │                    │
  │  de todo     │          ┌─────────┼──────────┐
  │  mezclado    │          ▼         ▼          ▼
  │              │     ┌─────────┐ ┌────────┐ ┌───────┐
  │  CAOS        │     │salud.py │ │gastos.py│ │utils.py│
  └──────────────┘     │ 80 lin  │ │ 100 lin│ │ 30 lin│
                       └─────────┘ └────────┘ └───────┘

  Cada archivo sabe lo suyo. Facil de encontrar, facil de arreglar.
```

## 12.2 Que es un modulo?

Un modulo es simplemente un archivo `.py`. Cuando tienes `salud.py`, Python lo trata como un modulo llamado `salud`.

```python
# salud.py
def mostrar_estado():
    print("Todo bien")

def registrar_toma(med):
    print(f"Tomaste {med}")
```

## 12.3 import — usar codigo de otro archivo

### import completo

```python
# main.py
import salud

salud.mostrar_estado()
salud.registrar_toma("Norapred")
```

Importas el modulo completo. Para usar algo, escribes `modulo.funcion()`.

### from ... import (selectivo)

```python
# main.py
from salud import mostrar_estado, registrar_toma

mostrar_estado()              # Sin prefijo
registrar_toma("Norapred")    # Sin prefijo
```

Solo traes lo que necesitas. No necesitas el prefijo `salud.`

### from ... import * (todo)

```python
from salud import *    # Importa TODO
```

Funciona pero es mala practica. No sabes que estas importando y puede haber conflictos de nombres.

## 12.4 Paquetes — carpetas con modulos

Un paquete es una carpeta que contiene modulos y un archivo `__init__.py`:

```
modules/
├── __init__.py      ← Le dice a Python: "esto es un paquete"
├── salud.py
├── gastos.py
└── utils.py
```

```python
# Importar desde un paquete
from modules.salud import mostrar_estado
from modules.utils import leer_json
```

La notacion de punto (`.`) representa carpetas:
- `modules.salud` = `modules/salud.py`
- `modules.utils` = `modules/utils.py`

### __init__.py

Puede estar vacio. Solo su presencia le dice a Python que la carpeta es un paquete. Sin el:

```python
from modules.salud import algo
# ModuleNotFoundError: No module named 'modules'
```

## 12.5 Modulos de la libreria estandar

Python viene con modulos incluidos que no necesitas instalar:

```python
import json          # Leer/escribir JSON
import os            # Interactuar con el sistema operativo
import sys           # Argumentos de terminal, salir del programa
import datetime      # Fechas y horas
import random        # Numeros aleatorios
import math          # Funciones matematicas
from pathlib import Path  # Rutas de archivos
```

Estos ya estan en Python. Solo haces `import` y listo.

## 12.6 if __name__ == "__main__"

Esta linea aparece en muchos archivos Python:

```python
# calculadora.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == "__main__":
    # Esto SOLO se ejecuta si corres: python calculadora.py
    print(sumar(2, 3))
    print(restar(5, 2))
```

**Como funciona:**
- Cuando ejecutas `python calculadora.py`, Python asigna `__name__ = "__main__"`
- Cuando alguien hace `import calculadora`, Python asigna `__name__ = "calculadora"`

Entonces:
- `python calculadora.py` → ejecuta el bloque if → imprime resultados
- `from calculadora import sumar` → NO ejecuta el bloque if → solo importa las funciones

Es util para tener codigo de prueba que no se ejecuta cuando alguien importa tu modulo.

## 12.7 Estructura de un proyecto real

```
MikaCLI/
├── main.py              ← Entry point (rutea comandos)
├── config.py            ← Constantes y configuracion
├── modules/
│   ├── __init__.py      ← Paquete
│   ├── salud.py         ← Modulo de salud
│   ├── gastos.py        ← Modulo de gastos
│   ├── tareas.py        ← Modulo de tareas
│   └── utils.py         ← Funciones compartidas
├── data/
│   ├── salud.json       ← Datos de salud
│   └── gastos.json      ← Datos de gastos
└── tests/
    ├── test_salud.py    ← Tests de salud
    └── test_gastos.py   ← Tests de gastos
```

**Flujo de imports:**
```
main.py
  ├── from modules.salud import manejar_salud
  └── from modules.gastos import manejar_gastos

modules/salud.py
  ├── from config import SALUD_FILE
  └── from modules.utils import leer_json, escribir_json

modules/utils.py
  └── import json

config.py
  └── from pathlib import Path
```

## 12.8 Errores comunes

### ModuleNotFoundError
```
ModuleNotFoundError: No module named 'modules'
```
- Falta `__init__.py` en la carpeta
- Estas ejecutando desde el directorio equivocado (debes estar en la raiz del proyecto)

### ImportError
```
ImportError: cannot import name 'funcion' from 'modulo'
```
- La funcion no existe en ese modulo (revisa el nombre)
- Typo en el nombre de la funcion

### Circular import
```python
# salud.py importa algo de gastos.py
# gastos.py importa algo de salud.py
# BOOM — ImportError
```
Solucion: saca lo compartido a `utils.py`. Los modulos nunca deben importarse entre si en circulo.

---

## Ejercicios

**Ejercicio 12.1:** Crea dos archivos:
- `operaciones.py` con funciones: sumar, restar, multiplicar, dividir
- `main.py` que importe y use esas funciones

**Ejercicio 12.2:** Reorganiza el ejercicio del directorio telefonico (cap 9) en:
- `contactos.py` — funciones de agregar, buscar, mostrar
- `main.py` — menu y logica principal

**Ejercicio 12.3:** Crea un paquete `utils/` con:
- `utils/__init__.py`
- `utils/texto.py` — funciones de limpiar, validar texto
- `utils/numeros.py` — funciones de validar numeros, calcular
- `main.py` — usa ambos modulos

---

> **Checkpoint:** Si puedes crear archivos separados y conectarlos con import, estas listo para el Capitulo 13.

[← Capitulo 11](11-funciones.md) | [Capitulo 13 →](13-archivos-y-json.md)
