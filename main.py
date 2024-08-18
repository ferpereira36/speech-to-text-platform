import customtkinter
from colorama import Fore
from PIL import Image
import os
import sys
from modules.recorder import RecorderWindow
from components.centerWindow import CenterWindow

customtkinter.set_appearance_mode("dark")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green
root = customtkinter.CTkToplevel()

# ---------- Tratamento Fechamento de Janelas ---------- #
def closeMainWindow():
    root.after(500, root.destroy)
    root.after(500, root.quit)
    sys.exit()
    # os._exit(0)
# ---------- Fim - Tratamento Fechamento de Janelas ---------- #

def recorder(btnRecord):
    btnRecord.configure(state=customtkinter.DISABLED)
    RecorderWindow()

def main():
    # ---------- Janela Principal ---------- #
    print(Fore.CYAN + 'Iniciando App...')
    root.title('Aplicação p/ Comp. Móvel e Ubíqua')
    width = 400
    height = 240
    x, y = CenterWindow(root, width, height)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.resizable(False, False)

    # Intercepta o fechamento da janela
    root.protocol("WM_DELETE_WINDOW", lambda: closeMainWindow())

    # Layout  
    my_image = Image.open("./assets/transcricao.png")
    photo = customtkinter.CTkImage(my_image, size=((64, 64)))

    frameRecord = customtkinter.CTkFrame(root)
    frameRecord.pack(padx=20, pady=20, expand=True)

    textRecord = customtkinter.CTkLabel(frameRecord, text="Gravação",
                                                    font=("Helvetica", 16, "bold"))
    textRecord.pack()

    imgRecord = customtkinter.CTkLabel(frameRecord, text="", image=photo)
    imgRecord.pack(pady=10)

    btnRecord = customtkinter.CTkButton(frameRecord, text="Testar",
                                                    font=("Helvetica", 14),
                                                    command=lambda: recorder(btnRecord))
    btnRecord.pack(pady=10)

    # Loop
    root.mainloop()
    # ---------- Fim - Janela Principal ---------- #

if __name__ == "__main__":
    main()