# Capitulo 1 — Instalacion

> Antes de cocinar, necesitas una cocina. Aqui la armamos.

---

## 1.1 Que es Python?

Python es un lenguaje de programacion. Un lenguaje de programacion es simplemente una forma de darle instrucciones a tu computadora. Asi como el español tiene reglas (sujeto, verbo, predicado), Python tiene las suyas.

Por que Python?
- Es el lenguaje mas popular del mundo (2026)
- Se usa en inteligencia artificial, web, automatizacion, ciencia de datos
- Su sintaxis parece ingles. Es facil de leer
- Tiene trabajo. Mucho. Y bien pagado

## 1.2 Instalar Python

### Windows

1. Ve a [python.org/downloads](https://python.org/downloads)
2. Descarga la version mas reciente (3.12 o superior)
3. **IMPORTANTE:** En el instalador, marca la casilla que dice **"Add Python to PATH"**. Si no la marcas, nada funciona despues
4. Click en "Install Now"
5. Espera a que termine

### Verificar que se instalo

Abre una terminal (busca "cmd" o "PowerShell" en el menu de Windows) y escribe:

```
python --version
```

Deberias ver algo como:
```
Python 3.12.x
```

Si ves eso, ya estas. Si dice "no se reconoce el comando", reinstala y asegurate de marcar "Add to PATH".

### Mac

1. Abre Terminal
2. Escribe: `brew install python` (si tienes Homebrew)
3. O descarga desde [python.org/downloads](https://python.org/downloads)
4. Verifica con `python3 --version`

### Linux

Python ya viene instalado en la mayoria de distros. Verifica con:
```
python3 --version
```

## 1.3 Instalar VS Code (tu editor de codigo)

VS Code es donde vas a escribir tu codigo. Es gratis, rapido, y lo usa medio mundo.

1. Ve a [code.visualstudio.com](https://code.visualstudio.com)
2. Descarga e instala
3. Abre VS Code
4. Ve a Extensions (icono de cuadros en la barra lateral izquierda)
5. Busca "Python" e instala la extension oficial de Microsoft

Eso es todo. No necesitas mas extensiones por ahora.

## 1.4 Tu primer programa

Vamos a verificar que todo funciona:

1. Abre VS Code
2. Crea una carpeta nueva donde quieras (ejemplo: `Documentos/python-practica`)
3. Abre esa carpeta en VS Code (File → Open Folder)
4. Crea un archivo nuevo: `hola.py`
5. Escribe esto:

```python
print("Hola mundo, aqui empieza todo.")
```

6. Guardalo (Ctrl+S)
7. Abre la terminal dentro de VS Code (Terminal → New Terminal, o Ctrl+`)
8. Escribe:

```
python hola.py
```

Deberias ver:
```
Hola mundo, aqui empieza todo.
```

Si lo ves, felicidades. Ya eres programador. Bueno, todavia no. Pero ya ejecutaste codigo. Eso es mas de lo que hace el 99% de la gente que "quiere aprender a programar".

## 1.5 La terminal — tu nueva amiga

La terminal (cmd, PowerShell, o Terminal en Mac/Linux) es donde ejecutas programas. No le tengas miedo. Solo son comandos de texto.

Comandos basicos que necesitas:

| Comando | Que hace | Ejemplo |
|---------|----------|---------|
| `cd carpeta` | Entrar a una carpeta | `cd Documentos` |
| `cd ..` | Subir un nivel | `cd ..` |
| `dir` (Windows) / `ls` (Mac/Linux) | Ver archivos en la carpeta | `dir` |
| `python archivo.py` | Ejecutar un programa | `python hola.py` |
| `cls` (Windows) / `clear` (Mac/Linux) | Limpiar la pantalla | `cls` |

No necesitas mas por ahora. Con el tiempo le agarras confianza.

## 1.6 Como funciona Python (simplificado)

Cuando escribes `python hola.py`, esto es lo que pasa:

1. Python abre el archivo `hola.py`
2. Lee el codigo de arriba hacia abajo, linea por linea
3. Ejecuta cada instruccion en orden
4. Cuando llega al final, termina

No hay compilacion, no hay build. Escribes, ejecutas, ves resultado. Eso hace a Python rapido para aprender.

---

## Ejercicios

**Ejercicio 1.1:** Crea un archivo llamado `mi_nombre.py` que imprima tu nombre completo.

**Ejercicio 1.2:** Crea un archivo que imprima 3 lineas diferentes:
```
Mi nombre es [tu nombre]
Tengo [tu edad] años
Estoy aprendiendo Python
```

**Ejercicio 1.3:** Intenta ejecutar un archivo que no existe: `python no_existe.py`. Lee el mensaje de error. No le tengas miedo a los errores — son Python diciendote que paso.

---

> **Checkpoint:** Si llegaste aqui y tu `hola.py` funciono, estas listo para el Capitulo 2.

[← Indice](00-indice.md) | [Capitulo 2 →](02-variables-y-tipos.md)
