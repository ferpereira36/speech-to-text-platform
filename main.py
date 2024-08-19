import customtkinter
from colorama import Fore
from PIL import Image
import sys
from modules.recorder import speech_to_text
from modules.transcription import archive_to_text
from components.centralizer import window_centralizer

customtkinter.set_appearance_mode("dark")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green
root = customtkinter.CTk()

# ---------- Tratamento Fechamento de Janelas ---------- #
def close_main_window():
    root.after(500, root.destroy)
    root.after(500, root.quit)
    sys.exit()
    # os._exit(0)
# ---------- Fim - Tratamento Fechamento de Janelas ---------- #

def module_speech_to_text(btn_recorder_main, btn_transcription_main):
    btn_recorder_main.configure(state = customtkinter.DISABLED)
    btn_transcription_main.configure(state = customtkinter.DISABLED)
    speech_to_text(root, btn_recorder_main, btn_transcription_main)
    
def module_archive_to_text(btn_recorder_main, btn_transcription_main):
    btn_recorder_main.configure(state = customtkinter.DISABLED)
    btn_transcription_main.configure(state = customtkinter.DISABLED)
    archive_to_text()
    btn_recorder_main.configure(state = customtkinter.NORMAL)
    btn_transcription_main.configure(state = customtkinter.NORMAL)

def main():
    # ---------- Janela Principal ---------- #
    print(Fore.CYAN + 'Iniciando App...')
    root.title('Aplicação p/ Comp. Móvel e Ubíqua')
    width = 400
    height = 184
    x, y = window_centralizer(root, width, height)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.resizable(False, False)

    # Intercepta o fechamento da janela
    root.protocol("WM_DELETE_WINDOW", lambda: close_main_window())

    # Layout  
    image_recorder = Image.open("./assets/recorder.png")
    photo_recorder = customtkinter.CTkImage(image_recorder, size=((64, 64)))

    frame_recorder = customtkinter.CTkFrame(root)
    frame_recorder.grid(row=0, column=0, padx=10, pady=10)

    text_recorder = customtkinter.CTkLabel(frame_recorder, text="Gravação",
                                                    font=("Helvetica", 16, "bold"))
    text_recorder.pack()

    img_recorder = customtkinter.CTkLabel(frame_recorder, text="", image=photo_recorder)
    img_recorder.pack(pady=10)

    btn_recorder_main = customtkinter.CTkButton(frame_recorder, text="Testar",
                                                    font=("Helvetica", 14),
                                                    command=lambda: module_speech_to_text(btn_recorder_main, btn_transcription_main))
    btn_recorder_main.pack(pady=10)
    
    
    image_transcription = Image.open("./assets/transcription.png")
    photo_transcription = customtkinter.CTkImage(image_transcription, size=((64, 64)))
    
    frame_transcription = customtkinter.CTkFrame(root)
    frame_transcription.grid(row=0, column=1, padx=10, pady=10)
    
    text_transcription = customtkinter.CTkLabel(frame_transcription, text="Arquivo",
                                                    font=("Helvetica", 16, "bold"))
    text_transcription.pack()
    
    img_transcription = customtkinter.CTkLabel(frame_transcription, text="", image=photo_transcription)
    img_transcription.pack(pady=10)
    
    btn_transcription_main = customtkinter.CTkButton(frame_transcription, text="Testar",
                                                    font=("Helvetica", 14),
                                                    command=lambda: module_archive_to_text(btn_recorder_main, btn_transcription_main))
    btn_transcription_main.pack(pady=10)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Loop
    root.mainloop()
    # ---------- Fim - Janela Principal ---------- #

if __name__ == "__main__":
    main()