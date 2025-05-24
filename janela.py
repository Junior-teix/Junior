import tkinter as tk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo('ATENÇÃO',f'Olá {entryNome.get()}')

valorPadX= 10
valorPadY= 10

janelaPrincipal = tk.Tk()
janelaPrincipal.title('minha primeira janela')
janelaPrincipal.geometry('800x600') # define o tamanho da janela
janelaPrincipal.configure(bg='gray') # muda a cor da janela
labelFrase = tk.Label(janelaPrincipal,text='Seja bem vindo!',bg='blue',fg='white',font=['Arial',15])

labelFrase.pack(padx=valorPadX,pady=valorPadY) # gerenciador de posição(posiciona o objeto na tela)

labelNome= tk.Label(janelaPrincipal,text='Digite seu nome',bg= 'gray')
labelNome.pack(padx=valorPadX,pady=valorPadY)

entryNome= tk.Entry(janelaPrincipal,width=60,font=['calibri',12],bg= 'light gray',fg='black')
entryNome.pack(padx=valorPadX,pady=valorPadY)

buttonEnviar= tk.Button(janelaPrincipal,text='Enviar',width=20,font=['calibri',10],bg='gray',fg='black',command=lambda: messagebox.showinfo('ATENÇÃO',f'Olá {entryNome.get()}'))
buttonEnviar.pack(padx=valorPadX,pady=valorPadY) 

janelaPrincipal.mainloop()