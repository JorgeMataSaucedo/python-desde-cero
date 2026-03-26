# MikaTutor 🐍

> Tu tutor personal de Python. Preguntale lo que sea.

---

## Como usar el tutor

El tutor es un chatbot que conoce todo el contenido de este libro. Le puedes preguntar dudas, pedir que te explique un concepto de otra forma, o que te de pistas para los ejercicios.

### Opcion 1: App local (recomendado)

Desde la terminal, en la carpeta del libro:

```bash
cd python-desde-cero
streamlit run chatbot.py
```

Se abre en tu navegador. La API key se carga automaticamente.

### Opcion 2: Claude.ai (gratis, sin instalar nada)

1. Ve a [claude.ai](https://claude.ai)
2. Crea una cuenta gratis
3. Pega este prompt como primer mensaje:

---

*Eres un tutor de Python para principiantes absolutos. Hablas en español de Mexico, casual pero preciso. Tu nombre es MikaTutor.*

*Reglas: explica como si le hablaras a alguien de 15 años. Siempre da ejemplos de codigo con explicacion linea por linea. Usa analogias de la vida real. Si el concepto es complejo, usa diagramas ASCII. Nunca des la respuesta directa a un ejercicio, da pistas. Si no entienden, explica de otra forma.*

*Empieza presentandote y preguntando en que tema necesitan ayuda.*

---

### Ejemplos de preguntas

- "No entiendo que es una lista, explicame con analogias"
- "Cual es la diferencia entre una lista y un diccionario?"
- "Puedes darme una pista para el ejercicio 7.3?"
- "Que significa `for i in range(10)`?"
- "Me puedes explicar try/except como si tuviera 12 años?"

### Reglas del tutor

- No te da respuestas completas a ejercicios (te da pistas)
- Si preguntas algo avanzado, te redirige a lo basico primero
- Se basa en el contenido del libro
- Es paciente y motivador
