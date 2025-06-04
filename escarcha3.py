import streamlit as st
from streamlit_image_select import image_select
import os
import time

# ---------------------------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------------------------
st.set_page_config(page_title="DETECCIÓN DE ESCARCHA", layout="wide")
st.title("DETECCIÓN DE ESCARCHA")
st.write("")
st.write("")
st.write("")

# ---------------------------------------------------------------------------
# Función utilitaria: nivel de escarcha según el número de imagen
# ---------------------------------------------------------------------------

def frost_level(img_number: int) -> int | str:
    if img_number == 1:
        return 1
    elif img_number in (2, 3, 4):
        return 2
    elif img_number in (5, 6, 7):
        return 3
    elif img_number in (8, 9, 10):
        return 4
    elif img_number == 11:
        return 5
    return "-"

# ---------------------------------------------------------------------------
# Carga de imágenes (1.png … 11.png en la misma carpeta)
# ---------------------------------------------------------------------------
image_files = [f"{i}.png" for i in range(1, 12) if os.path.isfile(f"{i}.png")]

# ---------------------------------------------------------------------------
# Diseño: dos columnas (izquierda miniaturas; derecha imagen grande + nivel)
# ---------------------------------------------------------------------------
left_col, right_col = st.columns([1, 2], gap="large")  # izquierda más estrecha

# -------------------- Miniaturas (columna izquierda) -----------------------
with left_col:
    selected_idx = image_select(
        label="",                  # sin texto adicional
        images=image_files,
        return_value="index",      # índice del elemento seleccionado
        key="thumbnails",          # mantiene el estado entre recargas
    )

# -------------------- Imagen grande + Nivel (columna derecha) --------------
with right_col:
    big_img_placeholder = st.empty()
    level_placeholder = st.empty()

# ---------------------------------------------------------------------------
# Lógica al seleccionar una miniatura
# ---------------------------------------------------------------------------
if selected_idx is not None:
    selected_file = image_files[selected_idx]
    img_number = int(os.path.splitext(os.path.basename(selected_file))[0])

    # Imagen grande (ocupa todo el ancho de la columna derecha)
    big_img_placeholder.image(selected_file, use_container_width=True)

    # Mensaje provisional mientras "calcula" el nivel
    level_placeholder.markdown("### Nivel de Escarcha: Determinando…")

    time.sleep(4)  # pausa intencionada ~4 s

    # Nivel final
    level_placeholder.markdown(f"### Nivel de Escarcha: {frost_level(img_number)}")
