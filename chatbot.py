import os
import streamlit as st
from pathlib import Path
from anthropic import Anthropic

# --- GET API KEY (Streamlit Cloud secrets > .env > manual input) ---
def get_api_key():
    """Busca la API key en orden: st.secrets, env var, input manual."""
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        pass
    env_key = os.getenv("ANTHROPIC_API_KEY", "")
    if env_key:
        return env_key
    return ""

# --- CONFIG ---
BOOK_DIR = Path(__file__).parent / "docs"
CHAPTERS = sorted(BOOK_DIR.glob("[0-9]*.md"))

# --- LOAD BOOK CONTENT ---
@st.cache_data
def load_book():
    """Carga todo el contenido del libro como contexto."""
    content = []
    for chapter in CHAPTERS:
        text = chapter.read_text(encoding="utf-8")
        content.append(text)
    return "\n\n---\n\n".join(content)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="MikaTutor — Python Desde Cero",
    page_icon="🐍",
    layout="centered"
)

# --- SIDEBAR ---
api_key = get_api_key()

with st.sidebar:
    st.title("MikaTutor 🐍")
    st.markdown("Tu tutor personal de Python")
    st.divider()

    if api_key:
        st.success("Conectado")
    else:
        api_key = st.text_input("API Key de Anthropic", type="password")

    st.divider()
    st.markdown(f"**Capitulos cargados:** {len(CHAPTERS)}")
    st.markdown("[Volver al libro](https://jorgematasaucedo.github.io/python-desde-cero/)")
    st.divider()
    st.markdown("*Hecho por Miguel Mata (Mikata)*")

    if st.button("Limpiar chat"):
        st.session_state.messages = []
        st.rerun()

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = f"""Eres MikaTutor, un tutor de Python para principiantes absolutos. Hablas en español de Mexico, casual pero preciso.

Reglas:
1. Explica como si le hablaras a alguien de 15 años que nunca ha programado
2. Siempre da ejemplos de codigo con explicacion linea por linea
3. Usa analogias de la vida real (cocina, legos, cajas, etc.)
4. Si el concepto es complejo, usa diagramas ASCII
5. Nunca des la respuesta directa a un ejercicio del libro. Da pistas y guia
6. Si preguntan algo avanzado, di "eso lo vemos mas adelante" y redirige a lo basico
7. Si no entienden, explica de otra forma, no repitas lo mismo
8. Motiva al estudiante, reconoce su esfuerzo
9. Si el estudiante pide codigo completo de un ejercicio, dale pistas primero

Tienes acceso al contenido completo del libro "Python Desde Cero". Usa este contenido como referencia para tus explicaciones:

{load_book()}

Cuando el estudiante pregunte algo, basa tu respuesta en el contenido del libro. Si preguntan algo que no esta en el libro, puedes explicarlo pero aclara que es contenido extra.

Empieza presentandote brevemente y preguntando en que tema necesitan ayuda."""

# --- CHAT ---
st.title("MikaTutor 🐍")
st.caption("Preguntame lo que sea sobre Python. Estoy aqui para ayudarte a aprender.")

# Init messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Escribe tu pregunta de Python aqui..."):

    if not api_key:
        st.error("Necesitas poner tu API Key de Anthropic en la barra lateral.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                client = Anthropic(api_key=api_key)

                api_messages = []
                for msg in st.session_state.messages:
                    api_messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })

                response = client.messages.create(
                    model="claude-sonnet-4-5-20250929",
                    max_tokens=2048,
                    system=SYSTEM_PROMPT,
                    messages=api_messages
                )

                assistant_msg = response.content[0].text
                st.markdown(assistant_msg)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_msg
                })

            except Exception as e:
                st.error(f"Error: {e}")
