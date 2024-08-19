import customtkinter
from customtkinter import filedialog
import speech_recognition as sr
from colorama import Fore

def archive_to_text():
    window_recog = customtkinter.CTkToplevel()
    window_recog.withdraw()  # Esconde a janela

    # Abre o explorador de arquivos
    file_path = filedialog.askopenfilename(
        filetypes=[("Arquivos de Áudio .wav", "*.wav")]
    )

    if not file_path:
        print(Fore.BLUE + "Nenhum arquivo selecionado.")
        return

    # Inicializa o Recognizer
    recognizer = sr.Recognizer()

    # Usa o Recognizer para transcrever o áudio
    with sr.AudioFile(file_path) as source:
        
        # Lê todo o áudio do arquivo
        audio_data = recognizer.record(source)
        
        try:
            # Especifica a transcrição em português
            text = recognizer.recognize_google(audio_data, language='pt-BR')
            print(Fore.WHITE + "Transcrição: ", text)
        
        # Trata problemas com o áudio
        except sr.UnknownValueError:
            print(Fore.YELLOW + "Não foi possível entender o áudio")
            
        # Trata problemas com a API da Google
        except sr.RequestError as e:
            print(Fore.RED + f"Erro ao solicitar resultados da API de reconhecimento de fala; {e}")
