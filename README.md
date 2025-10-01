import tkinter as tk
import time

def atualizar_hora():
    hora_atual = time.strftime('%H:%M:%S')
    texto.config(text=hora_atual)
    janela.after( 1000, atualizar_hora)

janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("250x100")
janela.configure(bg='black')

texto = tk.Label(janela, font=('Courier', 40), bg='black', fg='red')
texto.pack(anchor='center')

atualizar_hora()
janela.mainloop()
