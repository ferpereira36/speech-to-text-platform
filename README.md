<p align="center">
  <h2 align="center">Plataforma de Transcrição de Audio em Texto</h2>
</p>

### 📌 Sobre

Esta aplicação é um projeto que está sendo desenvolvido durante a graduação em Eng. da Computação. Tem como objetivo a transcrição de audio em texto para auxiliar PCD, mas também pode ser usada para outros fins.

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)

### 💻 Rodando o projeto

Esta aplicação depende do pacote Microsoft C++ Build Tools. É possível obtê-lo através do site da [Microsoft](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/). Durante a instalação, selecione a opção "Desenvolvimento para desktop com C++".

Caso você possua placa de vídeo compativel com CUDA é possível acelerar o processamento da aplicação. Para isso é necessário seguir as seguintes etapas:

> **Nota**: *Veja se sua placa de vídeo NVIDIA tem suporte para CUDA, visite o site oficial [CUDA GPUs](https://developer.nvidia.com/cuda-gpus).*

##### Para CUDA 11.8:
```bash
pip install torch==2.3.1+cu118 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
```

##### Para CUDA 12.X:
```bash
pip install torch==2.3.1+cu121 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121
```
Realize a troca ```2.3.1``` para a versão compatível com PyTorch do seu sistema.

1. **Instale o NVIDIA CUDA Toolkit**:
    - Selecione entre CUDA 11.8 ou CUDA 12.X Toolkit
      - Para 12.X visite [NVIDIA CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) e selecione a versão mais recente.
      - Para 11.8 visite [NVIDIA CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive).
    - Selecione seu sistema operacional e versão.
    - Baixe e instale o software.

2. **Instale o NVIDIA cuDNN**:
    - Selecione entre CUDA 11.8 ou CUDA 12.X Toolkit
      - Para 12.X visite [cuDNN Downloads](https://developer.nvidia.com/cudnn-downloads).
        - Selecione seu sistema operacional e versão.
        - Baixe e instale o software.
      - Para 11.8, visite [NVIDIA cuDNN Archive](https://developer.nvidia.com/rdp/cudnn-archive).
        - Clique em "Download cuDNN v8.7.0 (November 28, 2022), for CUDA 11.x".
        - Baixe e instale o software.

##### Alternando entre CPU e GPU:

A partir da biblioteca [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) é possível escolher se você deseja utilizar CUDA ou somente a CPU (caso não tenha placa de vídeo compatível com CUDA). Para isso altere o valor de **device** para "cpu" ou "cuda"

##### Como iniciar o projeto:

> **Nota**: *É recomendado a criação de um **ambiente virtual**, devido a possíveis conflitos entre bibliotecas.*

```bash
# Clone este repositório
$ git clone

# Acesse a pasta do projeto no terminal/cmd
$ cd speech-to-text-platform

# Instale as dependências
$ pip install RealtimeSTT customtkinter colorama Pillow

# Execute a aplicação
$ python main.py
```

### 🔗 Autor

Feito com ❤️ por **Fernando Pereira** 👋🏽 [Entre em contato!](https://www.linkedin.com/in/ferpereira36/) 
