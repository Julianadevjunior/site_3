import os
import streamlit as st
import pandas as pd
import main
from pathlib import Path
import shutil
from PIL import Image, ImageOps

bd = pd.read_excel('bd_imoveis.xlsx')

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
    st.session_state["rotations"] = [0] * len(os.listdir('images'))

# Função para carregar e rotacionar imagens, com cache
@st.cache_data(show_spinner=False)
def load_and_rotate_image(filepath, rotation_angle):
    img = Image.open(filepath).rotate(rotation_angle)
    return img

cod = 0

st.page_link(label='🏡Voltar', page=main.pagina_inicio)

st.markdown(f'Página {cod}')

# Criar colunas para exibir imagens
num_colunas = 2
colunas = st.columns(num_colunas)

for num_page in range(0, len(os.listdir('pages'))):
    font_1 = 18
    font_2 = 15
    tipo = bd['pronto'].loc[num_page]
    with colunas[num_page % num_colunas]:
        if num_page != 0:
            cont = st.container(border=True, height=620)
            with cont:
                pasta_images = [os.listdir(f'images/imovel_{num_page}')]
                imagem = f'images/imovel_{num_page}/{pasta_images[0][0]}'
                st.write({pasta_images[0][0]})
                # Carregar e rotacionar imagem com cache
                st.write(imagem, num_page)
                img = load_and_rotate_image(imagem, st.session_state["rotations"][0])
                corrected_image = correct_image_orientation(img)
                dimencionado = resize_image(corrected_image, size=(300, 300))
                # Exibir imagem
                st.image(dimencionado, use_container_width=True)

                valor = f"{float(bd['valor'].loc[num_page]):,.0f}"
                iptu = bd['iptu'].loc[num_page]
                cond = bd['condominio'].loc[num_page]
                entrada = f"{float(bd['entrada'].loc[num_page]):,.0f}"
                area = bd['area'].loc[num_page]
                quarto = bd['quartos'].loc[num_page]
                banheiro = bd['banheiro'].loc[num_page]
                vaga = bd['vaga'].loc[num_page]
                entrega = bd['entrega'].loc[num_page]
                bairro = bd['bairro'].loc[num_page]

                if tipo == 'sim':
                    col1, col2, col3 = st.columns([1, 4, 1])
                    with col2:
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_1}px">Total R${format_valor(valor)}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">{bairro}</div>',
                            unsafe_allow_html=True)

                    col4, col5, col6 = st.columns([2, 1, 2])
                    with col4:
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">IPTU: R${format_valor(iptu)}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">Cond: R${format_valor(cond)}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">📐: {area}m²</div>',
                            unsafe_allow_html=True)

                    with col6:
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">🛏️: {quarto}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">🚽: {banheiro}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">🚘: {vaga}</div>',
                            unsafe_allow_html=True)

                if tipo == 'não':
                    col1, col2, col3 = st.columns([1, 4, 1])
                    with col2:
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_1}px">Total R${format_valor(valor)}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">Entrada: R${format_valor(entrada)}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">{bairro}</div>',
                            unsafe_allow_html=True)

                    col4, col5, col6 = st.columns([2, 1, 2])
                    with col4:
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">entrega: R${entrega}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">Àrea: {area}m²</div>',
                            unsafe_allow_html=True)

                    with col6:
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">🛏️ -> {quarto}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">🚽 -> {banheiro}</div>',
                            unsafe_allow_html=True)
                        st.markdown(
                            f'<div style="text-align:center; font-size:{font_2}px">🚘 -> {vaga}</div>',
                            unsafe_allow_html=True)

                st.page_link(f'pages/pagina_{num_page}.py')


