import sqlite3
import Fun_Endereco as FE


class Aluno():

    def __init__(self, nome, CPF, telefones):
        self.nome = nome
        self.CPF = CPF
        self.telefones = telefones

    def adicionar(self):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT MAX(idEndereco) FROM Endereco").fetchone()[0]

        cursor.execute("INSERT INTO Aluno (nome,CPF,id_Endereco) VALUES('" +
                       self.nome + "','" + self.CPF + "',%i)" % (count))
        con.commit()



        count = cursor.execute("SELECT MAX(idTelefone) FROM Telefone").fetchone()[0] + 1

        for i in range(0, len(self.telefones)):
            cursor.execute(
                "INSERT INTO Telefone(idTelefone,numero,cpfAluno) VALUES(%i,'" % (count + i) + self.telefones[
                    i] + "','" + self.CPF + "')")
            con.commit()

        cursor.close()
        con.close()

    @staticmethod
    def incluirTelefone(CPF, tel):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()
        for i in range(len(tel)):
            count = cursor.execute("SELECT MAX(idTelefone) FROM Telefone").fetchone()[0]+1
            cursor.execute("INSERT INTO Telefone(idTelefone, numero, cpfAluno) VALUES(%i, '" %(count) +
                           tel[i] + "', '" + CPF + "')")
            con.commit()
        cursor.close()
        con.close()

    @staticmethod
    def consultar(CPF):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Aluno WHERE CPF like '" + CPF + "'").fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Aluno não cadastrado!'

    @staticmethod
    def consultar_tel(CPF):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT numero FROM Telefone WHERE cpfAluno like '" + CPF + "'").fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return ' '

    @staticmethod
    def remover(CPF):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT idMatriculado FROM Matriculado WHERE cpfAluno like '" + CPF + "'").fetchall()
        for i in range(len(count)):
            cursor.execute("DELETE FROM Nota WHERE id_matriculado like %i" %(count[i][0]))
            con.commit()
            cursor.execute("DELETE FROM Matriculado WHERE idMatriculado like %i"%(count[i][0]))
            con.commit()


        cursor.execute("DELETE FROM Telefone WHERE cpfAluno like '" + CPF + "'")
        con.commit()

        cursor.execute("DELETE FROM Aluno WHERE CPF like '" + CPF + "'")
        con.commit()

        cursor.close()
        con.close()

