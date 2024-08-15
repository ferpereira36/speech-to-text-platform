from RealtimeSTT import AudioToTextRecorder
import customtkinter
from colorama import Fore
from PIL import Image
import os
from modules.recorder import recorderWindow
from components.centerWindow import centerWindow

customtkinter.set_appearance_mode("dark")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green
root = customtkinter.CTk()

# ---------- Tratamento Fechamento de Janelas ---------- #
def closeMainWindow():
    recorder.shutdown()
    root.after(500, root.destroy)
    root.after(500, root.quit)
    os._exit(0)
# ---------- Fim - Tratamento Fechamento de Janelas ---------- #

# ---------- Janela Principal ---------- #
def mainWindow():
    print(Fore.CYAN + 'Iniciando App...')
    root.title('Aplicação p/ Comp. Móvel e Ubíqua')
    width = 400
    height = 240
    x, y = centerWindow(root, width, height)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.resizable(False, False)
    
    # Intercepta o fechamento da janela
    root.protocol("WM_DELETE_WINDOW", lambda: closeMainWindow())
    
    # Layout  
    my_image = customtkinter.CTkImage(Image.open('./assets/transcricao.png'),
                                      size=(64, 64))
    
    frameRecord = customtkinter.CTkFrame(root)
    frameRecord.pack(padx=20, pady=20, expand=True)
    
    textRecord = customtkinter.CTkLabel(frameRecord, text="Gravação",
                                                    font=("Helvetica", 16, "bold"))
    textRecord.pack()
    
    imgRecord = customtkinter.CTkLabel(frameRecord, text="", image=my_image)
    imgRecord.pack(pady=10)
    
    btnRecord = customtkinter.CTkButton(frameRecord, text="Testar",
                                                    font=("Helvetica", 14),
                                                    command=lambda: recorderWindow(root, recorder))
    btnRecord.pack(pady=10)
    
    # Loop
    root.mainloop()
# ---------- Fim - Janela Principal ---------- #

# ---------- Inicializa Aplicação ---------- #
try:
    # Configura a biblioteca RealtimeSTT
    recorder = AudioToTextRecorder(language='pt',
                                    device='cuda',
                                    model='tiny',
                                    spinner=True,
                                    enable_realtime_transcription=True)
    
    print(Fore.GREEN + 'Configurado!')

    # Inicia a aplicação tkinter
    mainWindow()
    
except:
    # Trata para retornar à configuração
    print(Fore.YELLOW + 'Tentando configurar...')
# ---------- Fim - Inicializa Aplicação ---------- #