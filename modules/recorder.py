import customtkinter
import threading
from colorama import Fore
from RealtimeSTT import AudioToTextRecorder
import time
import sys
import os
import threading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.centerWindow import CenterWindow


customtkinter.set_appearance_mode("dark")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green
recWin = customtkinter.CTk()
running = False
recorder = None

def RecorderWindow():
    # ---------- Configuração Gravação ---------- #
    def RunRecord():
        global running
        running = True
        global recorder
        print(Fore.LIGHTMAGENTA_EX + "Pode falar!")
        
        while running:
            data = recorder.text()
            if data != "" and running != False:
                print(data)
            else: pass
        
    def StartRecord(btnStart, btnStop):
        run = threading.Thread(target=RunRecord)
        run.daemon= True
        run.start()
        btnStart.configure(state=customtkinter.DISABLED)
        btnStop.configure(state=customtkinter.NORMAL)
        return run

    def StopRecord(btnStart, btnStop):
        global running
        running = False
        global recorder
        recorder.stop()
        btnStart.configure(state=customtkinter.NORMAL)
        btnStop.configure(state=customtkinter.DISABLED)
        print(Fore.GREEN + 'Gravação finalizada')
    # ---------- Fim - Configuração Gravação ---------- #

    # ---------- Tratamento Fechamento de Janelas ---------- #
    def CloseRecordWindow(recWin):
        recorder.shutdown()
        recWin.destroy()
        # sys.exit()
    # ---------- Fim - Tratamento Fechamento de Janelas ---------- #

    def configuracao(textConfig, configWin, btnStart):
        global recorder
        try:
            textConfig.configure(text="Iniciando configurações...")
            textConfig.update()
            print(Fore.GREEN + 'Iniciando configurações...')
            
            # Configura a biblioteca RealtimeSTT
            recorder = AudioToTextRecorder(language='pt',
                                            device='cuda',
                                            model='tiny',
                                            spinner=True,
                                            enable_realtime_transcription=True)
            
            textConfig.configure(text="Configurado!")
            textConfig.update()
            print(Fore.GREEN + 'Configurado!')
            time.sleep(1)
            btnStart.configure(state=customtkinter.NORMAL)

            # Inicia a aplicação tkinter
            configWin.grab_release()
            configWin.destroy()
        
        except Exception as e:
            textConfig.configure(text="Tentando configurar...")
            textConfig.update()
            print(Fore.YELLOW + 'Tentando configurar... ', {e})

    # ---------- Janela de Gravação ---------- #
    def main():
        recWin.title("Janela de Gravação")
        width = 400
        height = 520
        x, y = CenterWindow(recWin, width, height)
        recWin.geometry(f'{width}x{height}+{x}+{y}')
        recWin.resizable(False, False)
        
        # Intercepta o fechamento da janela
        recWin.protocol("WM_DELETE_WINDOW", lambda: CloseRecordWindow(recWin))
        
        # Layout
        btnStart = customtkinter.CTkButton(recWin, text="Iniciar Gravação",
                                                    command=lambda: StartRecord(btnStart, btnStop),
                                                    fg_color='green',
                                                    state=customtkinter.DISABLED)
        btnStart.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        
        btnStop = customtkinter.CTkButton(recWin, text="Parar Gravação",
                                                    command=lambda: StopRecord(btnStart, btnStop),
                                                    fg_color="#950606",
                                                    state=customtkinter.DISABLED)
        btnStop.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        
        
        configWin = customtkinter.CTkToplevel(recWin)
        w = 200
        h = 96
        xx, yy = CenterWindow(configWin, width, height)
        configWin.geometry(f'{w}x{h}+{xx}+{yy}')
        configWin.resizable(False, False)
        
        configWin.transient(recWin)
        configWin.grab_set()

        textConfig = customtkinter.CTkLabel(configWin, text="", font=("Helvetica", 14, "bold"))
        textConfig.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        
        threading.Thread(target=configuracao, args=(textConfig, configWin, btnStart)).start()
        
        recWin.mainloop()
    
    if __name__ == "__main__":
        main()
    else:
        main()
    # ---------- Fim - Janela de Gravação ---------- #