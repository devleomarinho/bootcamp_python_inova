import tkinter as tk
from tkinter import ttk

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def cadastrar_pessoa():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())

    imc = calcular_imc(peso,altura)
    resultado_label.config(text=f' Nome: {nome}\n Idade: {idade}anos \n Peso: {peso}kg \n Altura: {altura}m\n IMC: {imc:.2f}')


root = tk.Tk()
root.title('Calculadora de IMC')
fonte_big = ('Arial', 13, "bold")
fonte_small = ('Arial', 12)

botao = ttk.Button(root, text='Calcular IMC', command=cadastrar_pessoa)
botao.grid(row=4, column=0, columnspan=2, padx=5,pady=10)

mensagem_label = ttk.Label(root, text='', font=fonte_small, background='#CCC')
mensagem_label.grid(row=5,column=0,columnspan=2,pady=5)

nome_label = ttk.Label(root, text='Nome:', font=fonte_big, background='#CCC')
nome_label.grid(row=0, column=0, padx=5, pady=10)
nome_entry = ttk.Entry(root, font=fonte_small, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=10)

idade_label = ttk.Label(root, text='Idade:', font=fonte_big, background='#CCC')
idade_label.grid(row=1,column=0,padx=10,pady=5)
idade_entry = ttk.Entry(root, font=fonte_small, width=30)
idade_entry.grid(row=1,column=1,padx=10,pady=5)

peso_label = ttk.Label(root, text='Peso(kg):', font=fonte_big, background='#CCC')
peso_label.grid(row=2,column=0,padx=10,pady=5)
peso_entry = ttk.Entry(root, font=fonte_small, width=30)
peso_entry.grid(row=2,column=1,padx=10,pady=5)

altura_label = ttk.Label(root, text='Altura(m):', font=fonte_big, background='#CCC')
altura_label.grid(row=3,column=0,padx=10,pady=5)
altura_entry = ttk.Entry(root, font=fonte_small, width=30)
altura_entry.grid(row=3,column=1,padx=10,pady=5)

resultado_label = ttk.Label(root, text='', font=fonte_small)
resultado_label.grid(row=5, column=0, columnspan=2, pady=5)

root.geometry('450x400')
root.configure(bg='#CCC')
root.mainloop()

