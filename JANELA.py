from tkinter import *

# Função que realiza a soma
def soma():
    try:
        n = int(campo_num1.get())  # Obtém o valor do primeiro campo
        n2 = int(campo_num2.get())  # Obtém o valor do segundo campo
        resultado_soma = n + n2
        texto_soma['text'] = f"Resultado: {resultado_soma}"  # Atualiza o texto do resultado
    except ValueError:
        texto_soma['text'] = "Insira números válidos!"  # Tratar erro se não for um número
def sub():
    try:
        n = int(campo_num1.get())
        n2 = int(campo_num2.get())
        resultado_sub = n - n2
        textosub['text'] = f'Resultado: {resultado_sub}'
    except ValueError:
        textosub['text'] = f'Insira algo válido.'
# Criação da janela principal
janela = Tk()
janela.geometry('400x300')
janela.title('Gustavo - Soma')

# Título
texto_teste = Label(janela, text='Olá, Mundo!')
texto_teste.grid(column=0, row=0, padx=10, pady=10)

# Campo de entrada 1
Label(janela, text="Digite o 1º número:").grid(column=0, row=1, padx=10, pady=5)
campo_num1 = Entry(janela)
campo_num1.grid(column=1, row=1, padx=10, pady=5)

# Campo de entrada 2
Label(janela, text="Digite o 2º número:").grid(column=0, row=2, padx=10, pady=5)
campo_num2 = Entry(janela)
campo_num2.grid(column=1, row=2, padx=10, pady=5)

# Botão para realizar a soma
botaosoma = Button(janela, text='Soma', command=soma)
botaosoma.grid(column=1, row=3, padx=10, pady=10)

botaosub = Button(janela, text='Subtrair',command=sub)
botaosub.grid(column=2,row=4,padx=10,pady=10)

textosub = Label(janela,text='')
textosub.grid(column=1,row=4,padx=10,pady=10)

# Rótulo para mostrar o resultado
texto_soma = Label(janela, text="")
texto_soma.grid(column=1, row=4, padx=10, pady=10)

# Loop principal da janela
janela.mainloop()
