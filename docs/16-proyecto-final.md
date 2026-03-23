# Capitulo 16 — Proyecto Final

> Todo lo aprendido en un solo proyecto. Tu primera herramienta real.

---

## 16.1 El proyecto: Gestor de Contactos CLI

Vas a construir un programa de terminal que gestiona una lista de contactos. Usa TODO lo que aprendiste en los 15 capitulos anteriores.

### Que debe hacer:

```
python contactos.py agregar "Miguel Mata" 8112345678 miguel@email.com
python contactos.py buscar "Miguel"
python contactos.py listar
python contactos.py eliminar 1
python contactos.py editar 1 telefono 8198765432
python contactos.py exportar
```

### Funcionalidades:
1. **Agregar** contacto (nombre, telefono, email)
2. **Buscar** por nombre (busqueda parcial)
3. **Listar** todos los contactos formateados
4. **Eliminar** por ID
5. **Editar** un campo de un contacto
6. **Exportar** a archivo CSV

### Estructura del proyecto:

```
gestor-contactos/
├── main.py              ← Entry point, parseo de comandos
├── config.py            ← Constantes y rutas
├── modules/
│   ├── __init__.py
│   ├── contactos.py     ← Logica de contactos (CRUD)
│   └── utils.py         ← Leer/escribir JSON, formateo
├── data/
│   └── (contactos.json se crea automaticamente)
├── tests/
│   └── test_contactos.py
└── .gitignore
```

## 16.2 Conceptos que aplicas

| Capitulo | Concepto | Donde se usa |
|----------|----------|-------------|
| 2 | Variables y tipos | En todas partes |
| 3 | Operadores | IDs autoincrementales |
| 4 | Strings | Formateo, busqueda, limpieza |
| 5 | Input | (Opcional) modo interactivo |
| 6 | Condicionales | Validaciones, ruteo de comandos |
| 7 | Listas | Lista de contactos |
| 9 | Diccionarios | Cada contacto es un diccionario |
| 10 | Ciclos | Recorrer contactos, buscar, filtrar |
| 11 | Funciones | Todo el codigo esta en funciones |
| 12 | Modulos | Separado en archivos |
| 13 | JSON | Persistencia de datos |
| 14 | Errores | Try/except en todo |

## 16.3 Instrucciones

**No hay codigo de ejemplo aqui.** Este es TU proyecto.

1. Lee los requerimientos arriba
2. Planea la estructura (que funciones necesitas?)
3. Empieza por `config.py` y `utils.py` (lo mas simple)
4. Construye `contactos.py` funcion por funcion
5. Conecta todo en `main.py`
6. Agrega tests
7. Maneja todos los errores

**Reglas:**
- Cada linea la escribes tu
- Si no entiendes algo, regresa al capitulo correspondiente
- No copies de internet. Si buscas, entiende y reescribe
- Pide ayuda si te trabas, pero intenta primero

## 16.4 Criterios de evaluacion

Tu proyecto esta completo cuando:

- [ ] Los 6 comandos funcionan correctamente
- [ ] Los datos persisten entre ejecuciones
- [ ] Ningun comando produce un traceback
- [ ] El codigo esta organizado en modulos
- [ ] Tiene al menos 3 tests por modulo
- [ ] El codigo tiene docstrings en funciones importantes
- [ ] Puedes explicar CADA linea que escribiste

**El ultimo punto es el mas importante.**

## 16.5 Y despues?

Si completaste este proyecto, ya estas listo para:

- **MikaCLI** — la version mas ambiciosa con 4 modulos (salud, gastos, roadmap, tareas)
- **FastAPI** — convertir tus funciones en una API web
- **MikaRH** — un SaaS real con base de datos

Los mismos patrones, mayor escala. Los cimientos estan puestos.

---

> **No hay atajos. Solo lineas de codigo y la decision de seguir.**

[← Capitulo 15](15-clases.md) | [Indice →](00-indice.md)
