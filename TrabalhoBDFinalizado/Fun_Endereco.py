import sqlite3


class Endereco():
    def __init__(self,rua,numero,bairro,CEP,complemento):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.CEP = CEP
        self.complemento = complemento

    def adicionar(self):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT MAX(idEndereco) FROM Endereco").fetchone()[0]+1

        cursor.execute("INSERT INTO Endereco(idEndereco,rua,numero,bairro,CEP,complemento) VALUES(%i,'" % (count) +
                       self.rua + "','" + self.numero + "','" + self.bairro + "','" +
                       self.CEP + "','" + self.complemento + "')")
        con.commit()

        return count

        cursor.close()
        con.close()

    @staticmethod
    def alterar(id,NovaRua,NovoNumero,NovoBairro,NovoCEP,NovoComplemento):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        cursor.execute("UPDATE Endereco SET rua = '"+NovaRua+"',"+
        "numero = '"+NovoNumero+"', bairro = '"+NovoBairro+"',"+
        "CEP = '"+NovoCEP+"', complemento = '"+NovoComplemento+
        "' WHERE idEndereco = %i"%(id))
        con.commit()

        cursor.close()
        con.close()

    @staticmethod
    def remover(id):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        cursor.execute("DELETE FROM Endereco WHERE idEndereco like '" + id + "'")
        con.commit()

        cursor.close()
        con.close()



    @staticmethod
    def consultar(id):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Endereco WHERE idEndereco = %i"%(id)).fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Endereço inexistente!'