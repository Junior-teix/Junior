# janela principal
import tkinter as tk
from tkinter import messagebox

def somar():
    num1 = float(entryNum1.get())
    num2 = float(entryNum2.get())
    resultado = num1 + num2
    messagebox.showinfo('Resultado', f'A soma é {resultado:.2f}')

def subtraçao():
    num1 = float(entryNum1.get())
    num2 = float(entryNum2.get())
    resultado = num1 - num2
    messagebox.showinfo('Resultado', f'A subtraçao é {resultado:.2f}')
 
def multiplicaçao():
    num1 = float(entryNum1.get())
    num2 = float(entryNum2.get())
    resultado = num1 * num2
    messagebox.showinfo('Resultado', f'A multiplicaçao é {resultado:.2f}')

def divisao():
    num1 = float(entryNum1.get())
    num2 = float(entryNum2.get())
    resultado = num1 / num2
    messagebox.showinfo('Resultado', f'A divisao é {resultado:.2f}')
    


valorPadx = 5
valorPady = 5
fonte = ['Arial',12]
largura = 40

janela= tk.Tk()
janela.title('Calculadora v1.0')
janela.geometry('800x250')

labelNum1 = tk.Label(janela,text='Digite um numero', font=fonte,width=largura,)
labelNum1.grid(row=0,column=0,padx=valorPadx,pady=valorPady)

entryNum1 = tk.Entry(janela,font=fonte,width=largura,justify='right')
entryNum1.grid(row=0,column=1,padx=valorPadx,pady=valorPady)

labelNum2 = tk.Label(janela,text='Digite outro numero', font=fonte,width=largura,)
labelNum2.grid(row=1,column=0,padx=valorPadx,pady=valorPady)

entryNum2 = tk.Entry(janela,font=fonte,width=largura,justify='right')
entryNum2.grid(row=1,column=1,padx=valorPadx,pady=valorPady)

#botoes
buttonCalcular = tk.Button(janela,text='Somar',bg='gray',width= 30,command=somar)
buttonCalcular.grid(row=2,column=0,padx=valorPadx,pady=valorPady)

buttonCalcular = tk.Button(janela,text='Subtrair',bg='gray',width= 30,command=subtraçao)
buttonCalcular.grid(row=2,column=1,padx=valorPadx,pady=valorPady)

buttonCalcular = tk.Button(janela,text='Multiplicar',bg='gray',width= 30,command=multiplicaçao)
buttonCalcular.grid(row=3,column=0,padx=valorPadx,pady=valorPady)

buttonCalcular = tk.Button(janela,text='Dividir',bg='gray',width= 30,command=divisao)
buttonCalcular.grid(row=3,column=1,padx=valorPadx,pady=valorPady)

janela.mainloop()
