from tkinter import *
import numpy as np
import Fun_Aluno as FA
import Fun_Professor as FP
import Fun_Endereco as FE
import Fun_Matricula as FM

######### Interface de Consulta ############

def consultar_informacoes():
    interface_inicial = Tk()
    interface_inicial.title("Sistema de gerenciamento de notas")

    botao1 = Button(interface_inicial, text="Consultar Aluno", command=pega_cpf_aluno, font=("Arial", 15))
    botao1.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_inicial, text="Consultar Professor", command=pega_cpf_prof, font=("Arial", 15))
    botao2.grid(column=2, row=0, padx=10, pady=10)

    botao4 = Button(interface_inicial, text="Consultar matrícula", command=pega_cpf_Mat, font=("Arial", 15))
    botao4.grid(column=4, row=0, padx=10, pady=10)


def pega_cpf_aluno():
    def Consultar_aluno():
        cpf_aluno = aux.get()
        m = FA.Aluno.consultar(cpf_aluno)
        m1 = 'teste'
        if type(m) == type(m1):
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=(m))
            texto.grid(column=0, row=0, padx=10, pady=10)

        else:
            a = FE.Endereco.consultar(m[0][2])
            t = FA.Aluno.consultar_tel(cpf_aluno)
            t1 = ""
            for i in range(len(t)):
                t1 = t1 + t[i][0] + " "
            interface_sim = Tk()
            interface_sim.title("...")

            texto = Label(interface_sim, text=("CPF: " + m[0][0] + "\n" +
                                               "Nome: " + m[0][1] + "\n" +
                                               "Telefone: " + t1 + "\n" +
                                               "Endereço: " + a[0][1] + ', ' + a[0][2] + "\n" +
                                               'Complemento: ' + a[0][5] + "\n" +
                                               'CEP: ' + a[0][4] + '\n' +
                                               'Bairro: ' + a[0][3]), font=("Arial", 15)
                          )

            texto.grid(column=0, row=0, padx=10, pady=10)

    interface_cpf = Tk()
    interface_cpf.title("...")

    texto = Label(interface_cpf, text="Digite o CPF do aluno:", font=("Arial", 15))
    texto.grid(column=0, row=0, padx=10, pady=10)

    aux = Entry(interface_cpf, width=20, font=("Arial", 15))
    aux.grid(column=1, row=0, padx=10, pady=10)

    botao = Button(interface_cpf, text="Consultar", command=Consultar_aluno, font=("Arial", 15))
    botao.grid(column=0, row=1, padx=10, pady=10)

def pega_cpf_prof():
    def Consultar_prof():
        cpf_prof = aux.get()
        m = FP.Professor.consultar(cpf_prof)
        m1 = "teste"
        if type(m) == type(m1):
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=(m))
            texto.grid(column=0, row=0, padx=10, pady=10)
        else:
            a = FE.Endereco.consultar(m[0][2])
            t = FP.Professor.consultar_tel(cpf_prof)
            t1 = ""
            for i in range(len(t)):
                t1 = t1 + str(t[i][0]) + " "
            interface_sim = Tk()
            interface_sim.title("...")

            texto = Label(interface_sim, text=("CPF: " + m[0][0] + "\n" +
                                               "Nome: " + m[0][1] + "\n" +
                                               "Telefone: " + t1 + "\n" +
                                               "Endereço: " + a[0][1] + ', ' + a[0][2] + "\n" +
                                               'Complemento: ' + a[0][5] + "\n" +
                                               'CEP: ' + a[0][4] + '\n' +
                                               'Bairro: ' + a[0][3]), font=("Arial", 15)
                          )

            texto.grid(column=0, row=0, padx=10, pady=10)

    interface_cpf = Tk()
    interface_cpf.title("...")

    texto = Label(interface_cpf, text="Digite o CPF do professor:", font=("Arial", 15))
    texto.grid(column=0, row=0, padx=10, pady=10)

    aux = Entry(interface_cpf, width=20, font=("Arial", 15))
    aux.grid(column=1, row=0, padx=10, pady=10)

    botao = Button(interface_cpf, text="Consultar", command=Consultar_prof, font=("Arial", 15))
    botao.grid(column=0, row=1, padx=10, pady=10)


def pega_cpf_Mat():
    def Consultar_cpf():
        cpfAluno = aux.get()
        m = FM.Matricula.consultar_cpf(cpfAluno)
        m1 = "teste"
        if type(m) == type(m1):
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=(m))
            texto.grid(column=0, row=0, padx=10, pady=10)
        else:
            for i in range(m[1]):
                notas = [m[4 + 3*i][0][0],m[4 + 3*i][0][1],m[4 + 3*i][0][2]]
                if type(notas[0]) != type(1.1):
                    media = ""
                    notas[0] = ""
                if type(notas[1]) != type(1.1):
                    media = ""
                    notas[1] = ""
                if type(notas[2]) != type(1.1):
                    media = ""
                    notas[2] = ""
                if type(notas[0]) == type(notas[1]) and type(notas[1]) == type(notas[2]) and type(notas[2]) == type(1.1):
                    media = round(np.mean(notas),1)
                if type(m[4 + 3*i][0][3]) != type(0.0):
                    nef = " "
                elif m[4 + 3*i][0][3] == 0.0:
                    nef = " "
                else:
                    nef = str(m[4 + 3*i][0][3])
                interface_sim = Tk()
                interface_sim.title("Informações de Matrícula")

                texto = Label(interface_sim, text=("Dados sobre a matricula de " + m[0][1] + ": \n" +
                                                   "Código da Matrícula: " + str(m[4 + 3*i][0][4]) + "\n" +
                                                   "Diciplina: " + str(m[2 + 3*i][0][0]) + " - " + m[2 + 3*i][0][1] + "\n" +
                                                   "Horário: " + m[2 + 3*i][0][2] + "\n" +
                                                   "Pofessor: " + m[3 + 3*i][0][0] + "\n" +
                                                   "Notas:  N1 = " + str(notas[0]) + "  N2 = " + str(notas[1]) +
                                                   "  N3 = " + str(notas[2]) + "\n" +
                                                   "Média = " + str(media) + "  NEF = " + nef), font=("Arial", 15)
                              )

                texto.grid(column=0, row=0, padx=10, pady=10)

    interface_cpf = Tk()
    interface_cpf.title("...")

    texto = Label(interface_cpf, text="Digite o CPF do aluno:", font=("Arial", 15))
    texto.grid(column=0, row=0, padx=10, pady=10)

    aux = Entry(interface_cpf, width=20)
    aux.grid(column=1, row=0, padx=10, pady=10)

    botao = Button(interface_cpf, text="Consultar", command=Consultar_cpf, font=("Arial", 15))
    botao.grid(column=0, row=1, padx=10, pady=10)

######### Interface de alteração ############

def alterar_informações():
    interface_alterar = Tk()
    interface_alterar.title("Alteração de dados")

    botao1 = Button(interface_alterar, text="Alterar Aluno", command=alterar_aluno, font=("Arial", 15))
    botao1.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_alterar, text="Alterar Professor", command=alterar_prof, font=("Arial", 15))
    botao2.grid(column=2, row=0, padx=10, pady=10)

    botao3 = Button(interface_alterar, text="Alterar matrícula", command=alterar_matr, font=("Arial", 15))
    botao3.grid(column=3, row=0, padx=10, pady=10)

    texto_resposta = Label(interface_alterar, text="", font=("Arial", 15))
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)


def alterar_aluno():
    interface_alterar = Tk()
    interface_alterar.title("Alteração de dados de aluno")

    botao1 = Button(interface_alterar, text="Editar", command=editar_aluno, font=("Arial", 15))
    botao1.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_alterar, text="Remover", command=excluir_aluno, font=("Arial", 15))
    botao2.grid(column=2, row=0, padx=10, pady=10)

    botao3 = Button(interface_alterar, text="Incluir", command=incluir_aluno, font=("Arial", 15))
    botao3.grid(column=3, row=0, padx=10, pady=10)

    texto_resposta = Label(interface_alterar, text="", font=("Arial", 15))
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)


def alterar_prof():
    interface_alterar = Tk()
    interface_alterar.title("Alteração de dados de Professor")

    botao1 = Button(interface_alterar, text="Editar", command=editar_professor, font=("Arial", 15))
    botao1.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_alterar, text="Remover", command=excluir_professor, font=("Arial", 15))
    botao2.grid(column=2, row=0, padx=10, pady=10)

    botao3 = Button(interface_alterar, text="Incluir", command=incluir_professor, font=("Arial", 15))
    botao3.grid(column=3, row=0, padx=10, pady=10)

    texto_resposta = Label(interface_alterar, text="", font=("Arial", 15))
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)


def alterar_matr():
    interface_alterar = Tk()
    interface_alterar.title("Alteração de dados de matricula")

    botao2 = Button(interface_alterar, text="Incluir Matrícula", command=incluir_matricula, font=("Arial", 15))
    botao2.grid(column=2, row=0, padx=10, pady=10)

    botao3 = Button(interface_alterar, text="Incluir Notas", command=incluir_notas, font=("Arial", 15))
    botao3.grid(column=3, row=0, padx=10, pady=10)

    botao4 = Button(interface_alterar, text="Excluir Matricula", command=excluir_matricula, font=("Arial", 15))
    botao4.grid(column=4, row=0, padx=10, pady=10)

    texto_resposta = Label(interface_alterar, text="", font=("Arial", 15))
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)


######### Interface de alteração para inclusão ############

def incluir_aluno():
    def inc_aluno():
        ENDERECO = FE.Endereco(rua.get(),numero.get(), bairro.get(),cep.get(),comp.get())
        ALUNO = FA.Aluno(nome.get(),cpf.get(),tel)
        a = FA.Aluno.consultar(cpf.get())
        if type(a)== type(" "):
            FE.Endereco.adicionar(ENDERECO)
            FA.Aluno.adicionar(ALUNO)
        else:
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text='Aluno já cadastrado!', font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)

        interface_ialuno.destroy()



    def inc_tel():
        def inserir():
            tel.append(telefone.get())
            interface_telefone.destroy()

        interface_telefone = Tk()
        interface_telefone.title("Insira o número de telefone")

        telefone = Entry(interface_telefone, width=20, font=("Arial", 15))
        telefone.grid(column=0, row=0, padx=10, pady=10)

        botao = Button(interface_telefone, text="Inserir", command=inserir, font=("Arial", 15))
        botao.grid(column=0, row=1, padx=10, pady=10)

    tel = []


    interface_ialuno = Tk()
    interface_ialuno.title("Inclusão de aluno")

    texto1 = Label(interface_ialuno, text="Digite o CPF do aluno:", font=("Arial", 15))
    texto1.grid(column=0, row=0, padx=10, pady=10)

    cpf = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cpf.grid(column=1, row=0, padx=10, pady=10)

    texto2 = Label(interface_ialuno, text="Digite o nome do aluno:", font=("Arial", 15))
    texto2.grid(column=0, row=1, padx=10, pady=10)

    nome = Entry(interface_ialuno, width=20, font=("Arial", 15))
    nome.grid(column=1, row=1, padx=10, pady=10)

    botao2 = Button(interface_ialuno, text="Inserir telefone", command=inc_tel, font=("Arial", 15))
    botao2.grid(column=0, row=2, padx=10, pady=10)

    texto3 = Label(interface_ialuno, text="***** Endereço *****", font=("Arial", 15))
    texto3.grid(column=0, row=3, padx=10, pady=10)

    texto4 = Label(interface_ialuno, text="Digite o logradouro:", font=("Arial", 15))
    texto4.grid(column=0, row=4, padx=10, pady=10)

    rua = Entry(interface_ialuno, width=20, font=("Arial", 15))
    rua.grid(column=1, row=4, padx=10, pady=10)

    texto5= Label(interface_ialuno, text="Digite o número da residência:", font=("Arial", 15))
    texto5.grid(column=0, row=5, padx=10, pady=10)

    numero = Entry(interface_ialuno, width=20, font=("Arial", 15))
    numero.grid(column=1, row=5, padx=10, pady=10)

    texto6 = Label(interface_ialuno, text="Digite o Bairro:", font=("Arial", 15))
    texto6.grid(column=0, row=6, padx=10, pady=10)

    bairro = Entry(interface_ialuno, width=20, font=("Arial", 15))
    bairro.grid(column=1, row=6, padx=10, pady=10)

    texto7 = Label(interface_ialuno, text="Digite o CEP:", font=("Arial", 15))
    texto7.grid(column=0, row=7, padx=10, pady=10)

    cep = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cep.grid(column=1, row=7, padx=10, pady=10)

    texto8 = Label(interface_ialuno, text="Digite o complemento:", font=("Arial", 15))
    texto8.grid(column=0, row=8, padx=10, pady=10)

    comp = Entry(interface_ialuno, width=20, font=("Arial", 15))
    comp.grid(column=1, row=8, padx=10, pady=10)


    botao1 = Button(interface_ialuno, text="Finalizar", command=inc_aluno, font=("Arial", 15))
    botao1.grid(column=0, row=9, padx=10, pady=10)

def incluir_professor():
    def inc_prof():
        ENDERECO = FE.Endereco(rua.get(),numero.get(), bairro.get(),cep.get(),comp.get())
        PROF = FP.Professor(nome.get(),cpf.get(),tel)
        a = FP.Professor.consultar(cpf.get())
        if type(a)== type(" "):
            FE.Endereco.adicionar(ENDERECO)
            FP.Professor.adicionar(PROF)
        else:
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text='Professor já cadastrado!', font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)

        interface_ialuno.destroy()



    def inc_tel():
        def inserir():
            tel.append(telefone.get())
            interface_telefone.destroy()

        interface_telefone = Tk()
        interface_telefone.title("Insira o número de telefone")

        telefone = Entry(interface_telefone, width=20)
        telefone.grid(column=0, row=0, padx=10, pady=10)

        botao = Button(interface_telefone, text="Inserir", command=inserir, font=("Arial", 15))
        botao.grid(column=0, row=1, padx=10, pady=10)

    tel = []


    interface_ialuno = Tk()
    interface_ialuno.title("Inclusão de professor")

    texto1 = Label(interface_ialuno, text="Digite o CPF do professor:", font=("Arial", 15))
    texto1.grid(column=0, row=0, padx=10, pady=10)

    cpf = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cpf.grid(column=1, row=0, padx=10, pady=10)

    texto2 = Label(interface_ialuno, text="Digite o nome do professor:", font=("Arial", 15))
    texto2.grid(column=0, row=1, padx=10, pady=10)

    nome = Entry(interface_ialuno, width=20, font=("Arial", 15))
    nome.grid(column=1, row=1, padx=10, pady=10)

    botao2 = Button(interface_ialuno, text="Inserir telefone", command=inc_tel, font=("Arial", 15))
    botao2.grid(column=0, row=2, padx=10, pady=10)

    texto3 = Label(interface_ialuno, text="***** Endereço *****", font=("Arial", 15))
    texto3.grid(column=0, row=3, padx=10, pady=10)

    texto4 = Label(interface_ialuno, text="Digite o logradouro:", font=("Arial", 15))
    texto4.grid(column=0, row=4, padx=10, pady=10)

    rua = Entry(interface_ialuno, width=20, font=("Arial", 15))
    rua.grid(column=1, row=4, padx=10, pady=10)

    texto5= Label(interface_ialuno, text="Digite o número da residência:", font=("Arial", 15))
    texto5.grid(column=0, row=5, padx=10, pady=10)

    numero = Entry(interface_ialuno, width=20, font=("Arial", 15))
    numero.grid(column=1, row=5, padx=10, pady=10)

    texto6 = Label(interface_ialuno, text="Digite o Bairro:", font=("Arial", 15))
    texto6.grid(column=0, row=6, padx=10, pady=10)

    bairro = Entry(interface_ialuno, width=20, font=("Arial", 15))
    bairro.grid(column=1, row=6, padx=10, pady=10)

    texto7 = Label(interface_ialuno, text="Digite o CEP:", font=("Arial", 15))
    texto7.grid(column=0, row=7, padx=10, pady=10)

    cep = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cep.grid(column=1, row=7, padx=10, pady=10)

    texto8 = Label(interface_ialuno, text="Digite o complemento:", font=("Arial", 15))
    texto8.grid(column=0, row=8, padx=10, pady=10)

    comp = Entry(interface_ialuno, width=20, font=("Arial", 15))
    comp.grid(column=1, row=8, padx=10, pady=10)


    botao1 = Button(interface_ialuno, text="Finalizar", command=inc_prof, font=("Arial", 15))
    botao1.grid(column=0, row=9, padx=10, pady=10)

def incluir_matricula():
    def inc_matricula():
        MATRICULA = FM.Matricula(cpf.get(), disciplina.get())

        a = FA.Aluno.consultar(cpf.get())
        b = FM.Matricula.consultar_disciplina(disciplina.get())
        if type(a) != type(" "):
            if type(b) != type(" "):
                FM.Matricula.adicionar(MATRICULA)
            else:
                interface_a = Tk()
                interface_a.title("...")
                texto = Label(interface_a, text=b, font=("Arial", 15))
                texto.grid(column=0, row=0, padx=10, pady=10)
        else:
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=a, font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)

        interface_ialuno.destroy()

    interface_ialuno = Tk()
    interface_ialuno.title("Inclusão de matrícula")

    texto1 = Label(interface_ialuno, text="Digite o CPF do aluno:", font=("Arial", 15))
    texto1.grid(column=0, row=0, padx=10, pady=10)

    cpf = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cpf.grid(column=1, row=0, padx=10, pady=10)

    texto2 = Label(interface_ialuno, text="Digite o código da disciplina:", font=("Arial", 15))
    texto2.grid(column=0, row=1, padx=10, pady=10)

    disciplina = Entry(interface_ialuno, width=20, font=("Arial", 15))
    disciplina.grid(column=1, row=1, padx=10, pady=10)

    botao2 = Button(interface_ialuno, text="Inserir", command=inc_matricula, font=("Arial", 15))
    botao2.grid(column=0, row=2, padx=10, pady=10)

def incluir_notas():
    def pega_notas():
        def inc_notas():
            if n1.get() == '': N1 = 'NULL'
            else: N1 = n1.get()
            if n2.get() == '': N2 = 'NULL'
            else: N2 = n2.get()
            if n3.get() == '': N3 = 'NULL'
            else: N3 = n3.get()
            if nef.get() == '': NEF = 'NULL'
            else: NEF = nef.get()
            Y = FM.Matricula.consultar_id(id.get())
            if type(Y) == type(""):
                interface_a = Tk()
                interface_a.title("...")
                texto = Label(interface_a, text='Matrícula inexistente.\n Notas descartadas.', font=("Arial", 15))
                texto.grid(column=0, row=0, padx=10, pady=10)
            else:
                NOTA = FM.nota(N1, N2, N3, NEF, id.get())
                FM.nota.inserir_notas(NOTA)
        interface_b = Tk()
        interface_b.title("Inclusão de matrícula")

        texto2 = Label(interface_b, text="Digite a nota N1:", font=("Arial", 15))
        texto2.grid(column=0, row=1, padx=10, pady=10)

        n1 = Entry(interface_b, width=20, font=("Arial", 15))
        n1.grid(column=1, row=1, padx=10, pady=10)

        texto3 = Label(interface_b, text="Digite a nota N2:", font=("Arial", 15))
        texto3.grid(column=0, row=2, padx=10, pady=10)

        n2 = Entry(interface_b, width=20, font=("Arial", 15))
        n2.grid(column=1, row=2, padx=10, pady=10)

        texto4 = Label(interface_b, text="Digite a nota N3:", font=("Arial", 15))
        texto4.grid(column=0, row=3, padx=10, pady=10)

        n3 = Entry(interface_b, width=20, font=("Arial", 15))
        n3.grid(column=1, row=3, padx=10, pady=10)

        texto5 = Label(interface_b, text="Digite a nota NEF:", font=("Arial", 15))
        texto5.grid(column=0, row=4, padx=10, pady=10)

        nef = Entry(interface_b, width=20, font=("Arial", 15))
        nef.grid(column=1, row=4, padx=10, pady=10)

        botao2 = Button(interface_b, text="Inserir", command=inc_notas, font=("Arial", 15))
        botao2.grid(column=0, row=5, padx=10, pady=10)

    interface_ialuno = Tk()
    interface_ialuno.title("Inclusão de matrícula")

    texto1 = Label(interface_ialuno, text="Digite o código da matricula:", font=("Arial", 15))
    texto1.grid(column=0, row=1, padx=10, pady=10)

    id = Entry(interface_ialuno, width=20, font=("Arial", 15))
    id.grid(column=1, row=1, padx=10, pady=10)

    botao1 = Button(interface_ialuno, text="Inserir", command=pega_notas, font=("Arial", 15))
    botao1.grid(column=0, row=2, padx=10, pady=10)


######### Interface de alteração para exclusão ############

def excluir_aluno():
    def exc_aluno():
        cpf_aluno = aux.get()
        x = FA.Aluno.consultar(cpf_aluno)
        FA.Aluno.remover(cpf_aluno)
        FE.Endereco.remover(str(x[0][2]))

    def Consultar_aluno():
        cpf_aluno = aux.get()
        m = FA.Aluno.consultar(cpf_aluno)
        m1 = 'teste'
        if type(m) == type(m1):
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=(m), font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)

        else:
            a = FE.Endereco.consultar(m[0][2])
            t = FA.Aluno.consultar_tel(cpf_aluno)
            t1 = ""
            for i in range(len(t)):
                t1 = t1 + t[i][0] + " "
            interface_sim = Tk()
            interface_sim.title("Excluir Aluno")

            texto = Label(interface_sim, text=("Confirme os dados do aluno antes de clicar em excluir!\n\n" +
                                                "CPF: " + m[0][0] + "\n" +
                                               "Nome: " + m[0][1] + "\n" +
                                               "Telefone: " + t1 + "\n" +
                                               "Endereço: " + a[0][1] + ', ' + a[0][2] + "\n" +
                                               'Complemento: ' + a[0][5] + "\n" +
                                               'CEP: ' + a[0][4] + '\n' +
                                               'Bairro: ' + a[0][3]), font=("Arial", 15)
                          )

            texto.grid(column=0, row=0, padx=10, pady=10)
            botao1 = Button(interface_sim, text="Excluir", command=exc_aluno, font=("Arial", 15))
            botao1.grid(column=0, row=1, padx=10, pady=10)

    interface_cpf = Tk()
    interface_cpf.title("...")

    texto = Label(interface_cpf, text="Digite o CPF do aluno que deseja excluir:", font=("Arial", 15))
    texto.grid(column=0, row=0, padx=10, pady=10)

    aux = Entry(interface_cpf, width=20, font=("Arial", 15))
    aux.grid(column=1, row=0, padx=10, pady=10)

    botao = Button(interface_cpf, text="Consultar", command=Consultar_aluno, font=("Arial", 15))
    botao.grid(column=0, row=1, padx=10, pady=10)

def excluir_professor():
    def exc_professor():
        cpf_prof = aux.get()
        x = FP.Professor.consultar(cpf_prof)
        FP.Professor.remover(cpf_prof)
        FE.Endereco.remover(str(x[0][2]))

    def Consultar_prof():
        cpf_prof = aux.get()
        m = FP.Professor.consultar(cpf_prof)
        m1 = "teste"
        if type(m) == type(m1):
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=(m), font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)
        else:
            a = FE.Endereco.consultar(m[0][2])
            t = FP.Professor.consultar_tel(cpf_prof)
            t1 = ""
            for i in range(len(t)):
                t1 = t1 + str(t[i][0]) + " "
            interface_sim = Tk()
            interface_sim.title("...")

            texto = Label(interface_sim, text=("Confirme os dados do professor antes de clicar em excluir!\n\n" +
                                                "CPF: " + m[0][0] + "\n" +
                                               "Nome: " + m[0][1] + "\n" +
                                               "Telefone: " + t1 + "\n" +
                                               "Endereço: " + a[0][1] + ', ' + a[0][2] + "\n" +
                                               'Complemento: ' + a[0][5] + "\n" +
                                               'CEP: ' + a[0][4] + '\n' +
                                               'Bairro: ' + a[0][3]), font=("Arial", 15)
                          )

            texto.grid(column=0, row=0, padx=10, pady=10)
            botao1 = Button(interface_sim, text="Consultar", command=exc_professor, font=("Arial", 15))
            botao1.grid(column=0, row=1, padx=10, pady=10)

    interface_cpf = Tk()
    interface_cpf.title("...")

    texto = Label(interface_cpf, text="Digite o CPF do professor:", font=("Arial", 15))
    texto.grid(column=0, row=0, padx=10, pady=10)

    aux = Entry(interface_cpf, width=20, font=("Arial", 15))
    aux.grid(column=1, row=0, padx=10, pady=10)

    botao = Button(interface_cpf, text="Consultar", command=Consultar_prof, font=("Arial", 15))
    botao.grid(column=0, row=1, padx=10, pady=10)

def excluir_matricula():
    def confirmar_exc_matricula():
        ID = codigo.get()
        FM.Matricula.remover(ID)


    def exc_matricula():
        id = codigo.get()
        m = FM.Matricula.consultar_id(id)
        m1 = "teste"
        if type(m) == type(m1):
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=(m), font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)
        else:
            notas = [m[4][0][0], m[4][0][1], m[4][0][2]]
            if type(notas[0]) != type(1.1):
                media = ""
                notas[0] = ""
            if type(notas[1]) != type(1.1):
                media = ""
                notas[1] = ""
            if type(notas[2]) != type(1.1):
                media = ""
                notas[2] = ""
            if type(notas[0]) == type(notas[1]) and type(notas[1]) == type(notas[2]) and type(notas[2]) == type(
                    1.1):
                media = round(np.mean(notas), 1)
            if type(m[4][0][3]) != type(0.0):
                nef = " "
            elif m[4][0][3] == 0.0:
                nef = " "
            else:
                nef = str(m[4][0][3])

            interface_b = Tk()
            interface_b.title("Informações de Matrícula")

            texto = Label(interface_b, text=("Confira os dados antes de clicar em excluir" + "\n\n\n" +
                                                "Dados sobre a matricula de " + m[1][0][0] + ". \n" +
                                               "Código da Matrícula: " + str(m[0][0]) + "\n" +
                                               "Diciplina: " + str(m[2][0][0]) + " - " + m[2][0][1] + "\n" +
                                               "Horário: " + m[2][0][2] + "\n" +
                                               "Pofessor: " + m[3][0][0] + "\n" +
                                               "Notas:  N1 = " + str(notas[0]) + "  N2 = " + str(notas[1]) +
                                               "  N3 = " + str(notas[2]) + "\n" +
                                               "Média = " + str(media) + "  NEF = " + nef), font=("Arial", 15)
                          )

            texto.grid(column=0, row=0, padx=10, pady=10)
            botao = Button(interface_b, text="Excluir", command=confirmar_exc_matricula, font=("Arial", 15))
            botao.grid(column=0, row=1, padx=10, pady=10)


    interface_ialuno = Tk()
    interface_ialuno.title("Excluir matrícula")

    texto1 = Label(interface_ialuno, text="Digite o código da matricula que será excluída:", font=("Arial", 15))
    texto1.grid(column=0, row=0, padx=10, pady=10)

    codigo = Entry(interface_ialuno, width=20, font=("Arial", 15))
    codigo.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_ialuno, text="Excluir", command=exc_matricula, font=("Arial", 15))
    botao2.grid(column=0, row=2, padx=10, pady=10)


######### Interface de alteração para edição ############

def editar_aluno():
    def edi_aluno():

        ID = FA.Aluno.consultar(cpf.get())
        if type(ID) != type(" "):
            FE.Endereco.alterar(ID[0][2],rua.get(),numero.get(), bairro.get(), cep.get(), comp.get())
            FA.Aluno.incluirTelefone(cpf.get(),tel)
        else:
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text= ID, font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)

        interface_ialuno.destroy()

    def inc_tel():
        def inserir():
            tel.append(telefone.get())
            interface_telefone.destroy()

        interface_telefone = Tk()
        interface_telefone.title("Insira o número de telefone")

        telefone = Entry(interface_telefone, width=20, font=("Arial", 15))
        telefone.grid(column=0, row=0, padx=10, pady=10)

        botao = Button(interface_telefone, text="Inserir", command=inserir, font=("Arial", 15))
        botao.grid(column=0, row=1, padx=10, pady=10)

    tel = []

    interface_ialuno = Tk()
    interface_ialuno.title("Editar dados do aluno")

    texto1 = Label(interface_ialuno, text="Digite o CPF do aluno:", font=("Arial", 15))
    texto1.grid(column=0, row=0, padx=10, pady=10)

    cpf = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cpf.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_ialuno, text="Inserir telefone", command=inc_tel, font=("Arial", 15))
    botao2.grid(column=0, row=2, padx=10, pady=10)

    texto3 = Label(interface_ialuno, text="***** Endereço *****", font=("Arial", 15))
    texto3.grid(column=0, row=3, padx=10, pady=10)

    texto4 = Label(interface_ialuno, text="Digite o logradouro:", font=("Arial", 15))
    texto4.grid(column=0, row=4, padx=10, pady=10)

    rua = Entry(interface_ialuno, width=20, font=("Arial", 15))
    rua.grid(column=1, row=4, padx=10, pady=10)

    texto5 = Label(interface_ialuno, text="Digite o número da residência:", font=("Arial", 15))
    texto5.grid(column=0, row=5, padx=10, pady=10)

    numero = Entry(interface_ialuno, width=20, font=("Arial", 15))
    numero.grid(column=1, row=5, padx=10, pady=10)

    texto6 = Label(interface_ialuno, text="Digite o Bairro:", font=("Arial", 15))
    texto6.grid(column=0, row=6, padx=10, pady=10)

    bairro = Entry(interface_ialuno, width=20, font=("Arial", 15))
    bairro.grid(column=1, row=6, padx=10, pady=10)

    texto7 = Label(interface_ialuno, text="Digite o CEP:", font=("Arial", 15))
    texto7.grid(column=0, row=7, padx=10, pady=10)

    cep = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cep.grid(column=1, row=7, padx=10, pady=10)

    texto8 = Label(interface_ialuno, text="Digite o complemento:", font=("Arial", 15))
    texto8.grid(column=0, row=8, padx=10, pady=10)

    comp = Entry(interface_ialuno, width=20, font=("Arial", 15))
    comp.grid(column=1, row=8, padx=10, pady=10)

    botao1 = Button(interface_ialuno, text="Finalizar", command=edi_aluno, font=("Arial", 15))
    botao1.grid(column=0, row=9, padx=10, pady=10)


def editar_professor():
    def edi_prof():

        ID = FP.Professor.consultar(cpf.get())
        if type(ID) != type(" "):
            FE.Endereco.alterar(ID[0][2], rua.get(), numero.get(), bairro.get(), cep.get(), comp.get())
            FP.Professor.incluirTelefone(cpf.get(), tel)
        else:
            interface_a = Tk()
            interface_a.title("...")
            texto = Label(interface_a, text=ID, font=("Arial", 15))
            texto.grid(column=0, row=0, padx=10, pady=10)

        interface_ialuno.destroy()

    def inc_tel():
        def inserir():
            tel.append(telefone.get())
            interface_telefone.destroy()

        interface_telefone = Tk()
        interface_telefone.title("Insira o número de telefone")

        telefone = Entry(interface_telefone, width=20, font=("Arial", 15))
        telefone.grid(column=0, row=0, padx=10, pady=10)

        botao = Button(interface_telefone, text="Inserir", command=inserir, font=("Arial", 15))
        botao.grid(column=0, row=1, padx=10, pady=10)

    tel = []

    interface_ialuno = Tk()
    interface_ialuno.title("Editar dados do professor")

    texto1 = Label(interface_ialuno, text="Digite o CPF do professor:", font=("Arial", 15))
    texto1.grid(column=0, row=0, padx=10, pady=10)

    cpf = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cpf.grid(column=1, row=0, padx=10, pady=10)

    botao2 = Button(interface_ialuno, text="Inserir telefone", command=inc_tel, font=("Arial", 15))
    botao2.grid(column=0, row=2, padx=10, pady=10)

    texto3 = Label(interface_ialuno, text="***** Endereço *****", font=("Arial", 15))
    texto3.grid(column=0, row=3, padx=10, pady=10)

    texto4 = Label(interface_ialuno, text="Digite o logradouro:", font=("Arial", 15))
    texto4.grid(column=0, row=4, padx=10, pady=10)

    rua = Entry(interface_ialuno, width=20, font=("Arial", 15))
    rua.grid(column=1, row=4, padx=10, pady=10)

    texto5 = Label(interface_ialuno, text="Digite o número da residência:", font=("Arial", 15))
    texto5.grid(column=0, row=5, padx=10, pady=10)

    numero = Entry(interface_ialuno, width=20, font=("Arial", 15))
    numero.grid(column=1, row=5, padx=10, pady=10)

    texto6 = Label(interface_ialuno, text="Digite o Bairro:", font=("Arial", 15))
    texto6.grid(column=0, row=6, padx=10, pady=10)

    bairro = Entry(interface_ialuno, width=20, font=("Arial", 15))
    bairro.grid(column=1, row=6, padx=10, pady=10)

    texto7 = Label(interface_ialuno, text="Digite o CEP:", font=("Arial", 15))
    texto7.grid(column=0, row=7, padx=10, pady=10)

    cep = Entry(interface_ialuno, width=20, font=("Arial", 15))
    cep.grid(column=1, row=7, padx=10, pady=10)

    texto8 = Label(interface_ialuno, text="Digite o complemento:", font=("Arial", 15))
    texto8.grid(column=0, row=8, padx=10, pady=10)

    comp = Entry(interface_ialuno, width=20, font=("Arial", 15))
    comp.grid(column=1, row=8, padx=10, pady=10)

    botao1 = Button(interface_ialuno, text="Finalizar", command=edi_prof, font=("Arial", 15))
    botao1.grid(column=0, row=9, padx=10, pady=10)

