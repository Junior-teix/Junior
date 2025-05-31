import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

itens = []

def Adicionar():
    item = entryItem.get()
    if item.strip() !='':
        itens.append(item)

        comboItens = ttk.Combobox(janela,values=itens)
        comboItens.set('Conteudo de itens')
        comboItens.grid(row=1,column=0,padx=5,pady=5)
        entryItem.delete(0,tk.END)

janela = tk.Tk()
janela.title('testando listas')
janela.geometry('800x600')

labelItem = tk.Label(janela,text='digite um item')
labelItem.grid(row=0,column=0,padx=5,pady=5)
entryItem = tk.Entry(janela)
entryItem.grid(row=0,column=1,padx=5,pady=5)

buttonItem = tk.Button(janela,text='Adicionar',command=Adicionar)
buttonItem.grid(row=0,column=2,padx=5,pady=5)



janela.mainloop()