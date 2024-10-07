import fitz  # Importa a biblioteca fitz (PyMuPDF) para manipulação de PDFs
import tkinter as tk
from tkinter import filedialog

caminho = filedialog.askopenfilename()
if caminho:
    print("Arquivo selecionado:", caminho)
# Solicita ao usuário o caminho do arquivo PDF
pdf = caminho



diretorio = filedialog.askdirectory()
if diretorio:
        # Abre o documento PDF
        PDF_DOCUMENT = fitz.open(caminho)

        # Loop para percorrer todas as páginas do PDF
        for page in range(len(PDF_DOCUMENT)):
            # Carrega a página atual
            pagina = PDF_DOCUMENT.load_page(page)
            
            # Renderiza a página como uma imagem (pixmap)
            pix = pagina.get_pixmap()
            
            # Define o caminho completo da imagem a ser salva
            nome_pdf = f'{diretorio}/pag{page + 1}.jpeg'  # Caminho completo para salvar a imagem
            
            # Salva a imagem no disco
            pix.save(nome_pdf)
# Fecha o documento PDF após a conversão
PDF_DOCUMENT.close()
