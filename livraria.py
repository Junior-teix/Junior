import tkinter as tk
from tkinter import messagebox

valorPadx = 5
valorPady = 5
fonte = ['calibri',12]
largura = 40

livraria = []

def limparTela():
        entryIsbn.delete(0,tk.END)
        entryTitulo.delete(0,tk.END)
        entryAutor.delete(0,tk.END)
        entryEditora.delete(0,tk.END)
        entryPaginas.delete(0,tk.END)
        entryAno.delete(0,tk.END)
        entryGenero.delete(0,tk.END)
        
def gravar():
    livro ={'ISBN' : entryIsbn.get(),
         'Titulo'  : entryTitulo.get(),
         'Autor'   : entryAutor.get(),
         'Editora' : entryEditora.get(),
         'Paginas' : entryPaginas.get(),
         'Ano'     : entryAno.get(),
         'Genero'  : entryGenero.get(),
        }
    
    livraria.append(livro)
    messagebox.showinfo('Sucesso','livro cadastrado')
    limparTela()

janela= tk.Tk()
janela.title('CADASTRO DE LIVROS')
janela.geometry('1000x600')


labeIsbn = tk.Label(janela,text='CODIGO ISBN',bg='blue',fg='white', font=fonte,width=largura,)
labeIsbn.grid(row=0,column=0,padx=valorPadx,pady=valorPady)
entryIsbn = tk.Entry(janela,font=fonte,width=largura,)
entryIsbn.grid(row=0,column=1,padx=valorPadx,pady=valorPady)

labelTitulo = tk.Label(janela,text='TITULO',bg='blue',fg='white', font=fonte,width=largura,)
labelTitulo.grid(row=1,column=0,padx=valorPadx,pady=valorPady)
entryTitulo= tk.Entry(janela,font=fonte,width=largura,)
entryTitulo.grid(row=1,column=1,padx=valorPadx,pady=valorPady)

labelAutor = tk.Label(janela,text='AUTOR',bg='blue',fg='white', font=fonte,width=largura,)
labelAutor.grid(row=2,column=0,padx=valorPadx,pady=valorPady)
entryAutor= tk.Entry(janela,font=fonte,width=largura,)
entryAutor.grid(row=2,column=1,padx=valorPadx,pady=valorPady)

labelEditora = tk.Label(janela,text='EDITORA',bg='blue',fg='white', font=fonte,width=largura,)
labelEditora.grid(row=3,column=0,padx=valorPadx,pady=valorPady)
entryEditora = tk.Entry(janela,font=fonte,width=largura,)
entryEditora.grid(row=3,column=1,padx=valorPadx,pady=valorPady)

labelPaginas = tk.Label(janela,text='PAGINA',bg='blue',fg='white', font=fonte,width=largura,)
labelPaginas.grid(row=4,column=0,padx=valorPadx,pady=valorPady)
entryPaginas = tk.Entry(janela,font=fonte,width=largura,)
entryPaginas.grid(row=4,column=1,padx=valorPadx,pady=valorPady)

labelAno = tk.Label(janela,text='ANO',bg='blue',fg='white', font=fonte,width=largura,)
labelAno.grid(row=5,column=0,padx=valorPadx,pady=valorPady)
entryAno = tk.Entry(janela,font=fonte,width=largura,)
entryAno.grid(row=5,column=1,padx=valorPadx,pady=valorPady)

labelGenero = tk.Label(janela,text='GENERO',bg='blue',fg='white', font=fonte,width=largura,)
labelGenero.grid(row=6,column=0,padx=valorPadx,pady=valorPady)
entryGenero = tk.Entry(janela,font=fonte,width=largura,)
entryGenero.grid(row=6,column=1,padx=valorPadx,pady=valorPady)

buttonGravar = tk.Button(janela,text='GRAVAR',bg='#76d161',width= 20,font=['Arial',12],command=gravar)
buttonGravar.grid(row=7,column=0,padx=valorPadx,pady=valorPady)

buttonExcluir = tk.Button(janela,text='ESCLUIR',bg='#76d161',width= 20,font=['Arial',12])
buttonExcluir.grid(row=8,column=0,padx=valorPadx,pady=valorPady)

buttonLocalizar = tk.Button(janela,text='LOCALIZAR',bg='#76d161',width= 20,font=['Arial',12])
buttonLocalizar.grid(row=9,column=0,padx=valorPadx,pady=valorPady)

listagem = tk.Text(janela)
listagem.grid(row=10,column=0,columnspan=2,padx=5,pady=5)

janela.mainloop()
