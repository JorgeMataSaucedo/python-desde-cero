# Capitulo 15 — Clases

> Programacion orientada a objetos. Crear tus propios tipos de datos.

---

## 15.1 El problema que resuelven las clases

Imagina que manejas datos de personas con diccionarios:

```python
persona1 = {"nombre": "Miguel", "edad": 25}
persona2 = {"nombre": "Diego", "edad": 24}
persona3 = {"nomber": "Ilse", "edad": 23}    # Typo en "nomber"!
```

Con diccionarios no hay proteccion. Puedes escribir mal una llave y Python no te dice nada. Las clases te dan estructura.

## 15.2 Que es una clase?

Una clase es un **plano** para crear objetos. Define que datos tiene (atributos) y que puede hacer (metodos).

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear objetos (instancias)
miguel = Persona("Miguel", 25)
diego = Persona("Diego", 24)

print(miguel.nombre)    # "Miguel"
print(diego.edad)       # 24
```

**Analogia:** la clase es el molde de galletas. Los objetos son las galletas. Todas tienen la misma forma (nombre, edad) pero diferente contenido.

## 15.3 __init__ — el constructor

`__init__` es un metodo especial que se ejecuta automaticamente cuando creas un objeto:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Guarda nombre en el objeto
        self.edad = edad        # Guarda edad en el objeto
```

- `self` — se refiere al objeto que se esta creando. Es como decir "yo mismo"
- `self.nombre = nombre` — "mi nombre es el nombre que me pasaron"
- Se ejecuta automaticamente al hacer `Persona("Miguel", 25)`

## 15.4 self — la referencia al objeto

`self` es el primer parametro de TODOS los metodos de una clase. Representa al objeto actual.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Ahora tengo {self.edad} años!")

miguel = Persona("Miguel", 25)
miguel.presentarse()       # Soy Miguel y tengo 25 años
miguel.cumplir_anios()     # Ahora tengo 26 años!
```

Cuando llamas `miguel.presentarse()`, Python automaticamente pasa `miguel` como `self`. No lo escribes tu al llamar, pero SI al definir.

## 15.5 Atributos vs Metodos

```python
class Carro:
    def __init__(self, marca, modelo, km):
        # ATRIBUTOS — datos que tiene (sustantivos)
        self.marca = marca
        self.modelo = modelo
        self.km = km

    # METODOS — cosas que hace (verbos)
    def conducir(self, distancia):
        self.km += distancia
        print(f"Recorriste {distancia} km. Total: {self.km} km")

    def info(self):
        print(f"{self.marca} {self.modelo} — {self.km:,} km")
```

- **Atributos** = variables del objeto (marca, modelo, km)
- **Metodos** = funciones del objeto (conducir, info)

## 15.6 Ejemplo real: Medicamento

```python
class Medicamento:
    def __init__(self, nombre, hora_programada, frecuencia="diario"):
        self.nombre = nombre
        self.hora_programada = hora_programada
        self.frecuencia = frecuencia
        self.tomado_hoy = False

    def tomar(self):
        if self.tomado_hoy:
            print(f"{self.nombre} ya fue tomado hoy.")
            return
        self.tomado_hoy = True
        print(f"{self.nombre} registrado como tomado.")

    def estado(self):
        status = "TOMADO" if self.tomado_hoy else "PENDIENTE"
        print(f"{self.nombre:<15} {status:<10} ({self.hora_programada})")

# Uso
norapred = Medicamento("Norapred", "16:30")
norapred.estado()     # Norapred        PENDIENTE  (16:30)
norapred.tomar()      # Norapred registrado como tomado.
norapred.estado()     # Norapred        TOMADO     (16:30)
norapred.tomar()      # Norapred ya fue tomado hoy.
```

## 15.7 __str__ — representacion como texto

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

miguel = Persona("Miguel", 25)
print(miguel)    # Miguel (25 años)
```

Sin `__str__`, `print(miguel)` muestra algo como `<__main__.Persona object at 0x...>`. Con `__str__`, muestra lo que tu definas.

## 15.8 Metodos que regresan datos

```python
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
            return False
        self.saldo -= monto
        return True

    def obtener_saldo(self):
        return self.saldo

cuenta = CuentaBancaria("Miguel", 1000)
cuenta.depositar(500)
exito = cuenta.retirar(200)
print(f"Saldo: ${cuenta.obtener_saldo():,}")    # Saldo: $1,300
```

## 15.9 Encapsulamiento — proteger datos

En Python no hay atributos "privados" reales, pero la convencion es usar `_` al inicio:

```python
class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self._password = password    # "privado" por convencion

    def verificar_password(self, intento):
        return intento == self._password
```

`_password` le dice a otros devs: "no accedas a esto directamente, usa el metodo `verificar_password`". Python no te obliga, pero es la convencion.

## 15.10 Herencia — reutilizar clases

Una clase puede heredar de otra:

```python
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hablar(self):
        print(f"{self.nombre} dice {self.sonido}!")

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Guau")

    def traer(self):
        print(f"{self.nombre} trajo la pelota!")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Miau")

firulais = Perro("Firulais")
firulais.hablar()     # Firulais dice Guau!
firulais.traer()      # Firulais trajo la pelota!

mishi = Gato("Mishi")
mishi.hablar()        # Mishi dice Miau!
```

- `class Perro(Animal)` — Perro hereda de Animal
- `super().__init__(...)` — llama al constructor del padre
- Perro tiene todo lo de Animal MAS lo propio (`traer`)

## 15.11 Cuando usar clases vs diccionarios

| Usa Diccionarios cuando... | Usa Clases cuando... |
|---------------------------|---------------------|
| Solo almacenas datos | Datos + comportamiento |
| Estructura simple | Logica compleja |
| Datos de API o JSON | Modelos de negocio |
| Scripts rapidos | Proyectos grandes |

**Para MikaCLI v1.0** usamos diccionarios (es mas simple). **Para MikaRH** usaremos clases (Pydantic models con FastAPI).

---

## Ejercicios

**Ejercicio 15.1:** Crea una clase `Producto` con nombre, precio y cantidad. Metodos: `total()` que regrese precio * cantidad, y `__str__`.

**Ejercicio 15.2:** Crea una clase `ListaCompras` que internamente use una lista de `Producto`. Metodos: `agregar(producto)`, `eliminar(nombre)`, `total()`, `mostrar()`.

**Ejercicio 15.3:** Crea una clase `CuentaBancaria` con depositar, retirar (con validacion), y transferir a otra cuenta.

**Ejercicio 15.4:** Crea una jerarquia de clases:
- `Vehiculo` (base) — marca, modelo, velocidad
- `Carro(Vehiculo)` — puertas
- `Moto(Vehiculo)` — tipo (deportiva, urbana)
- Cada uno con un metodo `info()` que muestre sus datos

**Ejercicio 15.5:** Crea una clase `Contacto` y una clase `Directorio`:
- `Contacto` — nombre, telefono, email
- `Directorio` — lista de contactos, agregar, buscar, eliminar, mostrar todos

---

> **Checkpoint:** Si puedes crear una clase con `__init__`, atributos, metodos y `__str__`, ya tienes las bases de POO. Felicidades, terminaste la teoria fundamental de Python.

[← Capitulo 14](14-errores.md) | [Capitulo 16 →](16-proyecto-final.md)
