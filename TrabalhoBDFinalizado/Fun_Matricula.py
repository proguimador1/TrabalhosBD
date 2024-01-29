import sqlite3
class Matricula():

    def __init__(self, cpfAluno, codigoDisciplina):
        self.cpfAluno = cpfAluno
        self.codigoDisciplina = codigoDisciplina

    @staticmethod
    def adicionar(self):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT MAX(idMatriculado) FROM Matriculado").fetchone()[0] + 1

        cursor.execute("INSERT INTO Matriculado (cpfAluno,codigoDisciplina,idMatriculado) VALUES('" +
                       self.cpfAluno + "','" + self.codigoDisciplina + "',%i)" % (count))
        cursor.execute("INSERT INTO Nota (id_matriculado) VALUES(%i)" % (count))
        con.commit()

        cursor.close()
        con.close()


    @staticmethod
    def consultar_cpf(cpfAluno):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT CPF, nome FROM Aluno WHERE CPF like '" + cpfAluno + "'").fetchall()
        if len(informacoes) == 0:
            cursor.close()
            con.close()
            return 'Aluno não cadastrado!'
        else:
            count = cursor.execute("SELECT codigoDisciplina FROM Matriculado WHERE cpfAluno like '" + cpfAluno + "'").fetchall()
            count1 = cursor.execute("SELECT idMatriculado FROM Matriculado WHERE cpfAluno like '" + cpfAluno + "'").fetchall()
            informacoes.append(len(count))
            for i in range(len(count)):
                informacoes.append(cursor.execute("SELECT * FROM Disciplina WHERE codigo like '" + count[i][0] + "'").fetchall())
                count2 = cursor.execute("SELECT cpfProfessor FROM Disciplina WHERE codigo like '" + count[i][0] + "'").fetchone()[0]
                informacoes.append(cursor.execute("SELECT nome FROM Professor WHERE CPF like '" + count2 + "'").fetchall())
                informacoes.append(cursor.execute("SELECT * FROM Nota WHERE id_matriculado like %i"%(count1[i][0])).fetchall())
            cursor.close()
            con.close()
            return informacoes




    @staticmethod
    def consultar_id(id):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()
        id = str(id)
        informacoes = cursor.execute(
                "SELECT * FROM Matriculado WHERE idMatriculado like '" + id + "'").fetchall()


        if len(informacoes) == 0:
            cursor.close()
            con.close()
            return 'Matricula inexistente!'
        else:
            count = informacoes[0][1]
            count1 = informacoes[0][2]


            informacoes.append(
                cursor.execute("SELECT Nome FROM Aluno WHERE CPF like '" + count + "'").fetchall())

            informacoes.append(
                    cursor.execute("SELECT * FROM Disciplina WHERE codigo like " + count1).fetchall())
            count2 = cursor.execute(
                "SELECT cpfProfessor FROM Disciplina WHERE codigo like " + count1).fetchone()[0]
            informacoes.append(
                cursor.execute("SELECT nome FROM Professor WHERE CPF like '" + count2 + "'").fetchall())
            informacoes.append(
                    cursor.execute("SELECT * FROM Nota WHERE id_matriculado like " + id).fetchall())
            cursor.close()
            con.close()
            return informacoes



    @staticmethod
    def consultar_disciplina(codigo):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        informacoes = [cursor.execute("SELECT * FROM Disciplina WHERE codigo like %i"%(int(codigo))).fetchone()]

        con.commit()
        cursor.close()
        con.close()

        if informacoes[0] == None:
           return 'Disciplina não cadastrada!'
        else:
            return informacoes



    @staticmethod
    def remover(ID):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        cursor.execute("DELETE FROM Nota WHERE id_matriculado like '" + ID + "'")
        con.commit()

        cursor.execute("DELETE FROM Matriculado WHERE idMatriculado like '" + ID + "'")
        con.commit()

        cursor.close()
        con.close()


class nota():
    def __init__(self, n1, n2, n3, nef, id):
        self.n1 = str(n1)
        self.n2 = str(n2)
        self.n3 = str(n3)
        self.nef = str(nef)
        self.id = str(id)

    @staticmethod
    def inserir_notas(self):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()

        cursor.execute("UPDATE Nota SET primeiraNota = " + self.n1 + "," +
                        " segundaNota = " + self.n2 + "," +
                       " terceiraNota = " + self.n3 + "," +
                       " NEF = " + self.nef +
                       " WHERE id_matriculado like " + self.id)

        con.commit()

        cursor.close()
        con.close()


    @staticmethod
    def consultar_nota(ID):
        con = sqlite3.connect("SGN.db")
        cursor = con.cursor()
        informacoes = cursor.execute("SELECT * FROM Nota WHERE id_matriculado like %i" % (ID)).fetchall()
        con.commit()

        cursor.close()
        con.close()
        return informacoes



