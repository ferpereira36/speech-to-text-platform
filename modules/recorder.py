import customtkinter
import threading
from colorama import Fore
from RealtimeSTT import AudioToTextRecorder
import time
import threading
from components.centralizer import window_centralizer
from googletrans import Translator


customtkinter.set_appearance_mode("dark")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green
translator = Translator()
running = False
recorder = None

def speech_to_text(root, btn_recorder_main, btn_transcription_main):
    
    # ---------- Configuração Gravação ---------- #
    def write_text(data, input_text, check_var):
        if (check_var.get() == 'on'):
            # print('\n COM TRADUÇÃO \n')
            eng = translator.translate(data, src="pt", dest='en')
            # print(eng.text)
            input_text.configure(text=eng.text)
            input_text.update()
            
        if (check_var.get() == 'off'):
            # print('\n SEM TRADUÇÃO \n')
            # print(data)
            input_text.configure(text=data)
            input_text.update()
        
    
    def run_recorder(input_text, check_var):
        global running
        running = True
        global recorder
        print(Fore.LIGHTMAGENTA_EX + "Pode falar!")
        
        while running:
            data = recorder.text()
            if data != "" and running != False:
                write_text(data, input_text, check_var)
            else: pass
        
    def start_recorder(btn_start, btn_stop, input_text, check_translator, check_var):
        run = threading.Thread(target=run_recorder, args=(input_text, check_var,))
        run.daemon= True
        run.start()
        btn_start.configure(state=customtkinter.DISABLED)
        check_translator.configure(state=customtkinter.DISABLED)
        btn_stop.configure(state=customtkinter.NORMAL)
        return run

    def stop_recorder(btn_start, btn_stop, check_translator):
        global running
        running = False
        global recorder
        recorder.stop()
        btn_start.configure(state=customtkinter.NORMAL)
        check_translator.configure(state=customtkinter.NORMAL)
        btn_stop.configure(state=customtkinter.DISABLED)
        print(Fore.GREEN + 'Gravação finalizada')
    # ---------- Fim - Configuração Gravação ---------- #

    # ---------- Tratamento Fechamento de Janelas ---------- #
    def close_window(window_recorder):
        recorder.shutdown()
        window_recorder.grab_release()
        btn_recorder_main.configure(state = customtkinter.NORMAL)
        btn_transcription_main.configure(state = customtkinter.NORMAL)
        window_recorder.destroy()
        
    def disable_event():
        pass
    # ---------- Fim - Tratamento Fechamento de Janelas ---------- #

    # ---------- Janela de Configuração ---------- #
    def configuracao(text_config, window_config, btn_start):
        global recorder
        try:
            text_config.configure(text="Iniciando configurações...")
            text_config.update()
            print(Fore.GREEN + 'Iniciando configurações...')
            
            # Configura a biblioteca RealtimeSTT
            recorder = AudioToTextRecorder(language='pt',
                                            device='cuda',
                                            model='tiny',
                                            spinner=True,
                                            enable_realtime_transcription=True)
            
            text_config.configure(text="Configurado!")
            text_config.update()
            print(Fore.GREEN + 'Configurado!')
            time.sleep(1)
            btn_start.configure(state=customtkinter.NORMAL)

            # Inicia a aplicação tkinter
            window_config.grab_release()
            window_config.destroy()
        
        except Exception as e:
            text_config.configure(text="Tentando configurar...")
            text_config.update()
            print(Fore.YELLOW + 'Tentando configurar... ', {e})
    # ---------- Fim - Janela de Configuração ---------- #
    
    def checkbox_event(check_var):
        print("Valor alterado para: ", check_var.get())

    # ---------- Janela de Gravação ---------- #
    def main(root):
        window_recorder = customtkinter.CTkToplevel(root)
        window_recorder.title("Janela de Gravação")
        width = 400
        height = 520
        x, y = window_centralizer(window_recorder, width, height)
        window_recorder.geometry(f'{width}x{height}+{x}+{y}')
        window_recorder.resizable(False, False)
        window_recorder.iconbitmap("./assets/iconBook.ico")
        
        window_recorder.transient(root)
        window_recorder.grab_set()
        
        # Intercepta o fechamento da janela
        window_recorder.protocol("WM_DELETE_WINDOW", lambda: close_window(window_recorder))
        
        # Layout
        btn_start = customtkinter.CTkButton(window_recorder,
                                            text="Iniciar Gravação",
                                            command=lambda: start_recorder(btn_start, btn_stop, input_text, check_translator, check_var),
                                            fg_color='green',
                                            state=customtkinter.DISABLED)
        btn_start.grid(row=0, column=0, padx=10, pady=10)
        
        btn_stop = customtkinter.CTkButton(window_recorder,
                                            text="Parar Gravação",
                                            command=lambda: stop_recorder(btn_start, btn_stop, check_translator),
                                            fg_color="#950606",
                                            state=customtkinter.DISABLED)
        btn_stop.grid(row=0, column=1, padx=10, pady=10)
        
        check_var = customtkinter.StringVar(window_recorder, value="off")
        
        check_translator = customtkinter.CTkCheckBox(window_recorder,
                                                     text="Traduzir para inglês automaticamente",
                                                     checkbox_width=16,
                                                     checkbox_height=16,
                                                     variable=check_var,
                                                     onvalue="on",
                                                     offvalue="off",
                                                     command=lambda: checkbox_event(check_var))
        check_translator.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        input_text = customtkinter.CTkLabel(window_recorder,
                                            width=360,
                                            height=400,
                                            text="",
                                            fg_color='#2e2e2e',
                                            bg_color='white',
                                            wraplength=360,
                                            padx=10,
                                            pady=10,
                                            anchor='nw',
                                            justify='left',
                                            font=("Helvetica", 12),
                                            state=customtkinter.DISABLED)
        input_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        window_recorder.grid_columnconfigure(0, weight=1)
        window_recorder.grid_columnconfigure(1, weight=1)
        
        # ---------- Janela de Configuração Inicial ---------- #
        window_config = customtkinter.CTkToplevel(window_recorder)
        window_config.title('Config. Microfone')
        w = 240
        h = 96
        xx, yy = window_centralizer(window_config, width, height)
        window_config.geometry(f'{w}x{h}+{xx}+{yy}')
        window_config.resizable(False, False)
        window_config.iconbitmap("./assets/iconBook.ico")
        
        window_config.transient(window_recorder)
        window_config.grab_set()
        
        # Desabilitando o evento de fechamento da janela de configurações
        window_config.protocol("WM_DELETE_WINDOW", disable_event)

        # Layout
        text_config = customtkinter.CTkLabel(window_config,
                                             text="",
                                             font=("Helvetica", 14, "bold"))
        text_config.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        
        threading.Thread(target=configuracao, args=(text_config, window_config, btn_start)).start()
        # ---------- Fim - Janela de Configuração Inicial ---------- #
        
        window_recorder.mainloop()
    # ---------- Fim - Janela de Gravação ---------- #
    main(root)
