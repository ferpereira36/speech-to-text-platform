import customtkinter
from customtkinter import filedialog
import speech_recognition as sr
from colorama import Fore
import threading
from components.centralizer import window_centralizer
import time
from PIL import Image

def transcribe_audio(recognizer, audio_data, progress_bar, progress_label, window_recog, start_button):
    try:
        # Atualiza a barra de progresso enquanto a transcrição está em andamento
        progress_bar.set(0.5)
        progress_label.configure(text="Transcrevendo...")

        # Realiza a transcrição do áudio
        text = recognizer.recognize_google(audio_data, language='pt-BR')
        # Cria um arquivo txt
        with open("transcrição.txt", "w") as archive:
            # Escreve no arquivo
            archive.write("Áudio extraído e transcrito:\n\n")
            archive.write(text)
        print(Fore.WHITE + "Transcrição: ", text)
        progress_label.configure(text="Transcrição completa!")

        # Define a barra como completa
        progress_bar.set(1)

    except sr.UnknownValueError:
        print(Fore.YELLOW + "Não foi possível entender o áudio")
        progress_label.configure(text="Erro: Áudio não compreendido")

    except sr.RequestError as e:
        print(Fore.RED + f"Erro ao solicitar resultados da API de reconhecimento de fala; {e}")
        progress_label.configure(text="Erro na API de transcrição")

    finally:
        # Oculta a barra de progresso após a finalização
        progress_bar.grid_remove()
        # Aguarda 1 seg para fechar a janela
        time.sleep(1)
        start_button.configure(state=customtkinter.NORMAL)
        window_recog.destroy()
        
        

def select_archive(window_recog, start_button):
    # Abre o explorador de arquivos
    file_path = filedialog.askopenfilename(
        filetypes=[("Arquivos de Áudio .wav", "*.wav")]
    )

    if not file_path:
        print(Fore.BLUE + "Nenhum arquivo selecionado.")
        return

    # Inicializa o Recognizer
    recognizer = sr.Recognizer()
    
    start_button.configure(state=customtkinter.DISABLED)
    
    # Adiciona uma barra de progresso e um rótulo
    progress_label = customtkinter.CTkLabel(window_recog, text="Carregando...")
    progress_label.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

    progress_bar = customtkinter.CTkProgressBar(window_recog, width=300)
    progress_bar.grid(row=2, column=0, padx=20, pady=10, columnspan=2)
    progress_bar.set(0)  # Define o progresso inicial como 0
    
    def recognize_and_transcribe(window_recog, start_button):
        
        # Usa o Recognizer para transcrever o áudio
        with sr.AudioFile(file_path) as source:
            
            # Lê todo o áudio do arquivo
            audio_data = recognizer.record(source)
            
            transcribe_audio(recognizer, audio_data, progress_bar, progress_label, window_recog, start_button)
    
    # Inicia a transcrição em uma thread para não travar a interface
    threading.Thread(target=recognize_and_transcribe, args=(window_recog, start_button,)).start()

def close_recog_window(window_recog):
    window_recog.grab_release()
    window_recog.destroy()

def archive_to_text(root):
    window_recog = customtkinter.CTkToplevel(root)
    window_recog.title("Transcrição por arquivo")
    
    width = 400
    height = 192
    x, y = window_centralizer(window_recog, width, height)
    window_recog.geometry(f'{width}x{height}+{x}+{y}')
    window_recog.resizable(False, False)
    window_recog.iconbitmap("./assets/iconBook.ico")
    
    window_recog.transient(root)
    window_recog.grab_set()
    
    # Intercepta o fechamento da janela
    window_recog.protocol("WM_DELETE_WINDOW", lambda: close_recog_window(window_recog))
    
    # Layout
    start_button = customtkinter.CTkButton(window_recog,
                                           text="Selecionar Arquivo",
                                           command=lambda: select_archive(window_recog, start_button))
    start_button.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
    
    window_recog.grid_columnconfigure(0, weight=1)
    window_recog.grid_columnconfigure(1, weight=1)
