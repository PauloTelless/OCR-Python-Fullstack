from tkinter import *
from tkinter import filedialog
import cv2
import pytesseract

class AplicativoOCR:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("OCR PROCESS")

        # Definir o tamanho inicial da janela principal
        self.largura_janela = 600
        self.altura_janela = 400

        # Configurar a geometria da janela principal para centralizar na tela e definir a cor de fundo
        self.janela.geometry(f"{self.largura_janela}x{self.altura_janela}+{self.janela.winfo_screenwidth()//2 - self.largura_janela//2}+{self.janela.winfo_screenheight()//2 - self.altura_janela//2}")
        self.janela.configure(bg='lightgray')  # Definir a cor de fundo

        # Criar o widget Label
        self.texto_titulo = Label(self.janela, text='OCR PROCESS', font=('Arial', 24, 'bold'), fg='white', bg='lightgray')
        self.texto_titulo.pack(side='top', pady=20)  # Centralizar o rótulo na parte superior

        # Criar o widget Button
        self.botao = Button(self.janela, text='Escolher imagem', command=self.abrir_explorador, font=('Arial', 14, 'bold'), border='3px' , bg='gray', fg='white')
        self.botao.pack(side='top', pady=20)  # Centralizar o botão na parte superior
        self.botao.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centralizar vertical e horizontalmente

        # Criar o widget Label para mostrar o diretório selecionado
        self.texto_diretorio = Label(self.janela, text="", font=('Arial', 12, 'bold'), fg='black', bg='lightgray')
        self.texto_diretorio.pack(side='top', pady=20)  # Centralizar o texto_diretorio na parte superior

        # Criar o segundo botão (inicialmente desativado)
        self.botao_segunda_janela = Button(self.janela, text='Processar', font=('Arial', 16, 'bold') ,command=self.segunda_janela, state=DISABLED, border='2px' ,bg='gray', fg='white')
        self.botao_segunda_janela.pack(side='top', pady=20)  # Centralizar o botão na parte superior
        self.botao_segunda_janela.place(relx=0.5, rely=0.7, anchor=CENTER)  # Centralizar vertical e horizontalmente

    def abrir_explorador(self):
        global diretorio
        diretorio = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;")])

        self.texto_diretorio["text"] = f"Imagem escolhida: {diretorio}"
        # Ativar o segundo botão após escolher a imagem
        self.botao_segunda_janela["state"] = NORMAL

    def segunda_janela(self):
        # Criação da segunda janela com o mesmo tamanho da janela principal
        segunda_janela = Toplevel(self.janela)
        segunda_janela.title("Texto Extraído")

        # Configuração do caminho do Tesseract
        caminho = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = caminho

        # Leitura da imagem e extração de texto
        imagem = cv2.imread(diretorio)
        texto_extraido = pytesseract.image_to_string(imagem)

        # Criar o widget Label para mostrar o texto extraído
        texto_imagem = Label(segunda_janela, text=texto_extraido, font=('Arial', 12, 'bold'), fg='black', bg='white')
        texto_imagem.pack(side='top', pady=20)  # Centralizar o texto_imagem na parte superior

        # Configurar o tamanho da segunda janela igual à janela principal
        largura_segunda_janela = 600
        altura_segunda_janela = 400

        # Configurar a geometria da segunda janela para centralizar na tela e definir a cor de fundo
        segunda_janela.geometry(f"{largura_segunda_janela}x{altura_segunda_janela}+{segunda_janela.winfo_screenwidth()//2 - largura_segunda_janela//2}+{segunda_janela.winfo_screenheight()//2 - altura_segunda_janela//2}")
