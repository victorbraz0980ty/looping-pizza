import customtkinter

# Aparência
customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("dark-blue")

# Janela principal (Tela inicial)
root = customtkinter.CTk()
root.title("Pizza Loop")
root.geometry("700x500")

# =========================
# FUNÇÃO ABRIR TELA APÓS LOGIN
# =========================
def abrir_tela_inicial():
    janela_sistema = customtkinter.CTkToplevel(root)
    
    # Pega a largura e altura do monitor do usuário
    largura_monitor = janela_sistema.winfo_screenwidth()
    altura_monitor = janela_sistema.winfo_screenheight()
    
    # Define o tamanho da janela para o tamanho total do monitor
    janela_sistema.geometry(f"{largura_monitor}x{altura_monitor}+0+0")
    
    # Opcional: Maximiza a janela (Funciona melhor no Windows)
    janela_sistema.state("zoomed")
    
    janela_sistema.title("Pizza Loop - Sistema")
    janela_sistema.attributes("-topmost", True)

    titulo = customtkinter.CTkLabel(janela_sistema, text="Bem-vindo ao Sistema! 🍕", font=("Arial", 40, "bold"))
    titulo.pack(expand=True) # expand=True centraliza no meio da tela cheia

# =========================
# FUNÇÃO ABRIR LOGIN
# =========================
def abrir_login():
    root.withdraw() # Esconde a tela inicial

    janela_login = customtkinter.CTkToplevel(root)
    janela_login.geometry("700x500")    
    
    janela_login.title("Login")
    janela_login.attributes("-topmost", True)
    
    # Garante que se fechar no X, o programa encerra
    janela_login.protocol("WM_DELETE_WINDOW", root.destroy)

    # Título
    titulo = customtkinter.CTkLabel(janela_login, text="Tela de Login", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # Entrada nome
    entrada_nome = customtkinter.CTkEntry(janela_login, placeholder_text="Digite seu nome")
    entrada_nome.pack(pady=10)

    # Entrada senha
    entrada_senha = customtkinter.CTkEntry(janela_login, placeholder_text="Digite sua senha", show="*")
    entrada_senha.pack(pady=10)

    # Checkbox
    checkbox = customtkinter.CTkCheckBox(janela_login, text="Lembrar login")
    checkbox.pack(pady=10)

    # Botão login - AGORA CHAMA A FUNÇÃO DEFINIDA NO TOPO
    def acao_login():
        janela_login.withdraw() # Esconde o login ao entrar
        abrir_tela_inicial()

    botao_login = customtkinter.CTkButton(janela_login, text="Entrar", command=acao_login)
    botao_login.pack(pady=10)

    # Botão cadastro
    def ir_para_cadastro():
        janela_login.destroy() # Fecha o login antes de abrir cadastro
        abrir_cadastro()

    botao_cadastro = customtkinter.CTkButton(
        janela_login, text="Criar conta", command=ir_para_cadastro
    )
    botao_cadastro.pack(pady=10)

    # Botão voltar
    def voltar_inicio():
        janela_login.destroy()
        root.deiconify() # Mostra a tela inicial de volta

    botao_voltar = customtkinter.CTkButton(janela_login, text="Voltar", command=voltar_inicio)
    botao_voltar.pack(pady=10)  

# =========================
# FUNÇÃO ABRIR CADASTRO
# =========================
def abrir_cadastro():   
    root.withdraw()
    janela_cadastro = customtkinter.CTkToplevel(root)
    janela_cadastro.geometry("500x400")
    janela_cadastro.title("Cadastro")
    janela_cadastro.attributes("-topmost", True)
    
    janela_cadastro.protocol("WM_DELETE_WINDOW", root.destroy)

    titulo = customtkinter.CTkLabel(janela_cadastro, text="Página de Cadastro", font=("Arial", 18, "bold"))
    titulo.pack(pady=20)

    entrada_nome = customtkinter.CTkEntry(janela_cadastro, placeholder_text="Digite seu nome")
    entrada_nome.pack(pady=10)

    entrada_email = customtkinter.CTkEntry(janela_cadastro, placeholder_text="Digite seu email")
    entrada_email.pack(pady=10)

    entrada_senha = customtkinter.CTkEntry(janela_cadastro, placeholder_text="Digite sua senha", show="*")
    entrada_senha.pack(pady=10)

    botao_cadastrar = customtkinter.CTkButton(janela_cadastro, text="Cadastrar")
    botao_cadastrar.pack(pady=10)

    # Botão fechar (que agora volta para o Login)
    def voltar_login():
        janela_cadastro.destroy()
        abrir_login()

    botao_fechar = customtkinter.CTkButton(
        janela_cadastro, text="Voltar para Login", command=voltar_login
    )
    botao_fechar.pack(pady=10)


# =========================
# TELA INICIAL
# =========================

titulo = customtkinter.CTkLabel(root, text="Pizza Loop 🍕", font=("Arial", 30, "bold"))
titulo.pack(pady=60)

subtitulo = customtkinter.CTkLabel(root, text="Bem-vindo ao sistema da pizzaria")
subtitulo.pack(pady=10)

botao_entrar = customtkinter.CTkButton(root, text="Entrar", command=abrir_login)
botao_entrar.pack(pady=30)  
root.mainloop()
