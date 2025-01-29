import streamlit as st
import pandas as pd
from pathlib import Path
import shutil
from PIL import Image, ImageOps

# Função para corrigir a orientação da imagem
def correct_image_orientation(image):
    return ImageOps.exif_transpose(image)

def resize_image(image, size=(500, 500)):  # Ajuste o tamanho conforme necessário
    return image.resize(size, Image.Resampling.LANCZOS)

corretor = 'Felipe Carlos'
creci = 'CRECI 194707-F'
st.markdown(f"""<p style="font-size:25px; text-align: center"><b>{corretor}</b></p>""", unsafe_allow_html=True)
st.markdown(f"""<p style="font-size:15px; text-align: center"><b>{creci}</b></p>""", unsafe_allow_html=True)

st.divider()

pagina_inicio = st.Page(title='Inicio', page='pages/pagina_inicio.py')
pagina_1 = st.Page(title='👉🏾Saiba mais cod-1', page='pages/pagina_1.py')
pagina_2 = st.Page(title='👉🏾Saiba mais cod-2', page='pages/pagina_2.py')
pagina_3 = st.Page(title='👉🏾Saiba mais cod-3', page='pages/pagina_3.py')
pagina_4 = st.Page(title='👉🏾Saiba mais cod-4', page='pages/pagina_4.py')
pagina_5 = st.Page(title='👉🏾Saiba mais cod-5', page='pages/pagina_5.py')
pagina_6 = st.Page(title='👉🏾Saiba mais cod-6', page='pages/pagina_6.py')
pagina_7 = st.Page(title='👉🏾Saiba mais cod-7', page='pages/pagina_7.py')
pagina_8 = st.Page(title='👉🏾Saiba mais cod-8', page='pages/pagina_8.py')
pagina_9 = st.Page(title='👉🏾Saiba mais cod-9', page='pages/pagina_9.py')
pagina_10 = st.Page(title='👉🏾Saiba mais cod-10', page='pages/pagina_10.py')
pagina_11 = st.Page(title='👉🏾Saiba mais cod-11', page='pages/pagina_11.py')
pagina_12 = st.Page(title='👉🏾Saiba mais cod-12', page='pages/pagina_12.py')
pagina_13 = st.Page(title='👉🏾Saiba mais cod-13', page='pages/pagina_13.py')
pagina_14 = st.Page(title='👉🏾Saiba mais cod-14', page='pages/pagina_14.py')
pagina_15 = st.Page(title='👉🏾Saiba mais cod-15', page='pages/pagina_15.py')

pg = st.navigation(pages=[pagina_inicio, pagina_1, pagina_2, pagina_3, pagina_4, pagina_5, pagina_6, pagina_7, pagina_8, pagina_9, pagina_10, pagina_11, pagina_12, pagina_13, pagina_14, pagina_15], position='hidden')
pg.run()