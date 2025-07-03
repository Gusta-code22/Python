import customtkinter as ct
from time import sleep

ct.set_appearance_mode("Dark")
janela = ct.CTk()
janela.title('Login')
janela.geometry("800x600")


def abrirnova():
    janela.destroy()
    janela2 = ct.CTk()
    janela2.title('dados')
    janela2.geometry("800x600")
    mensagem = ct.CTkLabel(janela2, text="Login efetuado com sucesso!", font=("Arial", 16))
    mensagem.pack(pady=50)
    janela2.mainloop()


titulo = ct.CTkLabel(janela, text='Login', font=('Arial', 25, 'bold'))
titulo.pack(pady=30)


def dados():
    if Email.get() and senha.get():
        texto_auxiliar.configure(text='Login efetuado')
        texto_auxiliar.after(2000, lambda: texto_auxiliar.configure(text=''))  # 2 segundos
        texto.configure(text=f'Email: {Email.get()}\nSenha: {senha.get()}')
        texto.after(3000, lambda: texto.configure(text=''))  # 3 segundos
        texto.after(3000, abrirnova)
    elif Email.get():
        texto_auxiliar.configure(text='Digite a senha')
    elif senha.get():
        texto_auxiliar.configure(text='Digite o email')
    else:
        texto_auxiliar.configure(text='Digite o email e a senha')


Email = ct.CTkEntry(janela, placeholder_text='Digite seu email', font=('Arial', 16))
Email.place(x=200, y=100)

texto = ct.CTkLabel(janela, text='', font=('Arial', 16))
texto.place(x=200, y=350)

texto_auxiliar = ct.CTkLabel(janela, text='', font=('Arial', 16, 'bold'))
texto_auxiliar.place(x=200, y=300)  # 200 pixels para a direita e 400 para baixo

senha = ct.CTkEntry(janela, placeholder_text='Senha', show='*', font=('Arial', 16))
senha.place(x=500, y=100)

botao = ct.CTkButton(janela, text='Fazer login', command=dados)
botao.place(x=200, y=200)

checkbox_valor = ct.BooleanVar()


def mostrar_senha():
    if checkbox_valor.get():
        senha.configure(show='')
    else:
        senha.configure(show='*')


checkbox = ct.CTkCheckBox(janela,
                          variable=checkbox_valor,
                          text='Mostrar senha',
                          command=mostrar_senha)
checkbox.place(x=500, y=200)

janela.mainloop()
