Nesse projeto, com o objetivo de aprofundar meus conhecimentos em algumas bibliotecas da linguagem Python, desenvolvi um programa que utiliza imagens contendo texto e aplica técnicas de Reconhecimento Óptico de Caracteres (OCR) para filtrar e extrair o texto presente. Para implementar essa funcionalidade central, optei por integrar as bibliotecas OpenCV para a leitura da imagem e Pytesseract para a transformação da imagem em texto.
Além disso, para proporcionar uma experiência mais amigável ao usuário, incorporei a biblioteca Tkinter, que é responsável por criar interfaces gráficas. Essa adição não apenas torna o programa mais acessível, mas também oferece uma plataforma visual para interação.

É valido ressaltar, também, que o código está em uma versão inicial, ou seja, a precisão do processamento ainda pode conter algumas falhas.

OBSERVAÇÃO IMPORTANTE: No sistema operacional Windows, para o funcionamento correto do programa, a blioteca do Pytesseract precisa de algumas configurações necessárias.

1. No terminal, instalar a biblioteca: pip install pytesseract
2. Instalar o pytesseract na máquina 

![config](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/ff0edcc8-45ff-4036-8505-b355d1f3dbf1)

OBS: Nessa etapa, você deve salvar esse caminho.

3. Após essa etapa, vá até o arquivo ocr_process_all.py, na função 'segunda_janela(self)', na variável caminho, e coloque o caminho que você salvou. Além disso deve-se colocar essa parte ao final do caminho -> \tesseract.exe

![config2](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/fb838f16-0e0a-4bc4-817e-5aabdb482c36)

Pronto! O código irá funcionar.


![1](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/7e152739-972b-4de5-b691-50d3903b59c9)

![image_1](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/9603e474-bf4f-482f-a531-975f4bc9ea90)

![2](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/6ecc9827-9767-46c6-9158-68971bb1e661)

![3](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/e5091216-6a8a-445e-bfd7-8a90795fddb4)

![image_2](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/b00ef491-3cf5-43a0-ae15-04ec96826c67)

![4](https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/7cc47101-33f0-485d-8c12-50f568ae9dd5)

Vídeo para demonstração: https://github.com/PauloTelless/OCR-Python-Fullstack/assets/126625776/06dea0a6-c6fc-4ce1-8f58-f7b08ad6839f
