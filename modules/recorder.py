import customtkinter
import threading
from colorama import Fore
from components.centerWindow import centerWindow
from RealtimeSTT import AudioToTextRecorder

customtkinter.set_appearance_mode("dark")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green
running = False

def recorderWindow(root, recorder):
    
    # ---------- Configuração Gravação ---------- #
    def runRecord():
        global running
        running = True
        print(Fore.LIGHTMAGENTA_EX + "Pode falar!")
        
        while running:
            data = recorder.text()
            if data != "" and running != False:
                print(data)
            else: pass
        
    def startRecord(btnStart, btnStop):
        run = threading.Thread(target=runRecord)
        run.daemon= True
        run.start()
        btnStart.configure(state=customtkinter.DISABLED)
        btnStop.configure(state=customtkinter.NORMAL)
        return run

    def stopRecord(recWin, btnStart, btnStop):
        global running
        running = False
        recorder.stop()
        btnStart.configure(state=customtkinter.NORMAL)
        btnStop.configure(state=customtkinter.DISABLED)
        print(Fore.GREEN + 'Gravação finalizada')
    # ---------- Fim - Configuração Gravação ---------- #

    # ---------- Tratamento Fechamento de Janelas ---------- #
    def closeRecordWindow(recWin):
        recWin.grab_release()
        recWin.destroy()
    # ---------- Fim - Tratamento Fechamento de Janelas ---------- #

    # ---------- Janela de Gravação ---------- #
    def Window():
        recWin = customtkinter.CTkToplevel()
        recWin.title("Janela de Gravação")
        recWin.geometry("400x600")
        width = 400
        height = 520
        x, y = centerWindow(recWin, width, height)
        recWin.geometry(f'{width}x{height}+{x}+{y}')
        recWin.resizable(False, False)
        
        # Bloqueia a janela principal de interações
        recWin.transient(root)
        recWin.grab_set()
        
        # Intercepta o fechamento da janela
        recWin.protocol("WM_DELETE_WINDOW", lambda: closeRecordWindow(recWin))
        
        # Layout
        btnStart = customtkinter.CTkButton(recWin, text="Iniciar Gravação",
                                                    command=lambda: startRecord(btnStart, btnStop),
                                                    fg_color='green')
        btnStart.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        
        btnStop = customtkinter.CTkButton(recWin, text="Parar Gravação",
                                                    command=lambda: stopRecord(recWin, btnStart, btnStop),
                                                    fg_color="#950606",
                                                    state=customtkinter.DISABLED)
        btnStop.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    # ---------- Fim - Janela de Gravação ---------- #
    Window()
