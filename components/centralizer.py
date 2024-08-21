# Função responsável por centralizar as janelas

# app = recebe a janela de referencia
# width = recebe a largura
# height = recebe a height

def window_centralizer(app, width, height):
    # Obtém a largura e altura da tela
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    
    # Calcula a posição x e y para centralizar a janela
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    return x, y