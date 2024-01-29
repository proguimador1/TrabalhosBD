CREATE TABLE Aluno(
  nome TEXT NOT NULL,
  CPF TEXT PRIMARY KEY,
  id_Endereco INTEGER UNIQUE,
  FOREIGN KEY(id_Endereco) REFERENCES Endereco(idEndereco)
);
CREATE TABLE Endereco(
  idEndereco INTEGER primary key,
  rua TEXT,
  numero TEXT,
  bairro TEXT,
  CEP TEXT,
  complemento TEXT
);
CREATE TABLE Telefone(
  idTelefone INTEGER PRIMARY KEY,
  numero TEXT,
  cpfAluno TEXT,
  cpfProfessor TEXT,
  FOREIGN KEY(cpfAluno) REFERENCES Aluno(CPF),
  FOREIGN KEY(cpfProfessor) REFERENCES Professor(cpf)
);
CREATE TABLE Disciplina(
  codigo INTEGER PRIMARY KEY,
  nome TEXT,
  horario TEXT,
  cpfProfessor TEXT,
  FOREIGN KEY(cpfProfessor) REFERENCES Professor(cpf)
);
CREATE TABLE Nota(
  primeiraNota REAL,
  segundaNota REAL,
  terceiraNota REAL,
  NEF REAL,
  id_matriculado INTEGER PRIMARY KEY,
  FOREIGN KEY(id_matriculado) REFERENCES Matriculado(idMatriculado)
);
CREATE TABLE Matriculado(
  idMatriculado INTEGER PRIMARY KEY,
  cpf_aluno TEXT,
  cod_disciplina INTEGER,
  FOREIGN KEY(cpf_aluno) REFERENCES Aluno(CPF),
  FOREIGN KEY(cod_disciplina) REFERENCES Disciplina(codigo)
);
CREATE TABLE Professor(
  nome TEXT NOT NULL,
  cpf TEXT PRIMARY KEY,
  id_Endereco INTEGER,
  FOREIGN KEY(id_Endereco) REFERENCES Endereco(idEndereco)
);

INSERT INTO Endereco(idEndereco,numero,rua,bairro,CEP,complemento)
VALUES (1,'605','Joaquim Lino','Jacarecanga','321',NULL),
(2,'2355','Betel','Raquel de Queiroz','607','B102'),
(3,'122','13 de Maio','Benfica','608','A');

INSERT INTO Endereco(idEndereco,numero,rua,bairro,CEP,complemento)
VALUES (4,'17','Carlos Braga','Dende','012',NULL),
(5,'103','12 de Maio','Joao 23','108','C'),
(6,'27','Granada','Benfica','610',NULL);

INSERT INTO Aluno(CPF,nome,id_Endereco)
VALUES ('052','Guilherme',1),('012','Bruno',2),('000','Siclano',3);

INSERT INTO Professor(cpf,nome,id_Endereco)
VALUES ('999','Ismayle',5),
('444','Bonfim',6),
('222','Julio Cezar',4);

INSERT INTO Telefone(idTelefone,numero,cpfAluno,cpfProfessor)
VALUES (1,'984','052',NULL),
(2,'852','012',NULL),
(3,'972','012',NULL),
(4,'965', NULL,'999'),
(5,'944', NULL,'444');

INSERT INTO Disciplina(codigo,nome,horario,cpfProfessor)
VALUES (1,'Banco de Dados','24CD-Manha','999'),
(2,'Teoria da Computacao','35CD-Manha','444'),
(3,'Calculo Diferencial e Integral','35CD-Tarde',222);

INSERT INTO Matriculado(idMatriculado,cpf_aluno,cod_disciplina)
VALUES (1,'052',1),
(2,'052',3),
(3,'012',1),
(4,'012',2),
(5,'000',1);

INSERT INTO Nota(primeiraNota,segundaNota,terceiraNota,NEF,id_matriculado)
VALUES (8.5,7.8,10,NULL,1),
(7,9,NULL,NULL,2),
(6,8,8,NULL,3),
(6,7,9,NULL,4),
(5,6.5,3,5.5,5);

UPDATE Nota
set primeiranota = 8.5
WHERE id_matriculado = 3;

DELETE FROM Telefone
WHERE idTelefone = 3;

SELECT *
FROM Aluno;

SELECT *
FROM Telefone
where idTelefone < 5;

select nome
FROM Disciplina;
