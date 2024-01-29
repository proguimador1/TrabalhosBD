from tkinter import *
import Fun_Interface as FI


interface_inicial = Tk()
interface_inicial.title("Sistema de gerenciamento de notas")


botao1 = Button(interface_inicial, text="Consultar", command=FI.consultar_informacoes)
botao1.grid(column=1, row=0, padx=10, pady=10)


botao5 = Button(interface_inicial, text="Alterar informações", command=FI.alterar_informações)
botao5.grid(column=5, row=0, padx=10, pady=10)


texto_resposta = Label(interface_inicial, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


interface_inicial.mainloop()


