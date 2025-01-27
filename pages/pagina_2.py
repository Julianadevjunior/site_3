import streamlit as st
import pandas as pd
import main
from pathlib import Path
import shutil
from PIL import Image, ImageOps
import os

cod = 2

# Função para corrigir a orientação da imagem
def correct_image_orientation(image):
    return ImageOps.exif_transpose(image)

def resize_image(image, size=(500, 500)):  # Ajuste o tamanho conforme necessário
    return image.resize(size, Image.Resampling.LANCZOS)

def format_valor(valor):
    valor = str(valor)
    if ',' in valor:
        valor = valor.replace(',', '-')
    if '.' in valor:
        valor = valor.replace('.', ',')
    if '-' in valor:
        valor = valor.replace('-', '.')
    return valor

# Inicializar o estado das rotações
if "rotations" not in st.session_state:
    st.session_state["rotations"] = [0] * len(os.listdir(f'images/imovel_{cod}'))

# Função para carregar e rotacionar imagens, com cache
@st.cache_data(show_spinner=False)
def load_and_rotate_image(filepath, rotation_angle):
    img = Image.open(filepath).rotate(rotation_angle)
    return img

bd = pd.read_excel('bd_imoveis.xlsx')

st.page_link(label='🏡Voltar', page=main.pagina_inicio)

cont = st.container(border=True, key=f'container {cod}')
with cont:
    st.text('Descrição:')
    st.text(bd['descricao'].loc[cod])

# Criar colunas para exibir imagens
num_colunas = 2
colunas = st.columns(num_colunas)

for i, img in enumerate(os.listdir(f'images/imovel_{cod}')):
    with colunas[i % num_colunas]:
        if i != 0:
                # Carregar e rotacionar imagem com cache
                imagem = f'images/imovel_{cod}/{img}'
                img = load_and_rotate_image(imagem, st.session_state["rotations"][0])
                corrected_image = correct_image_orientation(img)
                dimencionado = resize_image(corrected_image, size=(300, 300))
                # Exibir imagem
                st.image(dimencionado, use_container_width=True)