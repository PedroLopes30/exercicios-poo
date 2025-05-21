class Aluno():
  def __init__(self, nome, nota):
    self.nome = nome
    self.nota = nota

  def foi_aprovado(self):
    if self.nota >= 6:
      return True

class Professor():
  def __init__(self, nome):
    self.nome = nome
    self.alunos = []

  def adicionar_aluno(self, aluno):
    self.alunos.append(aluno)
    

  def media_da_turma(self):
    total_notas = 0
    for aluno in self.alunos:
      total_notas += aluno.nota
    media = total_notas / len(self.alunos)
    return media

  def alunos_aprovados(self):
    aprovados = []
    for aluno in self.alunos:
      if aluno.foi_aprovado():
        aprovados.append(aluno.nome)
    return aprovados

class Escola():
  def __init__(self, nome):
    self.nome = nome
    self.professores = []

  def adcionar_professor(self, professor):
    self.professores.append(professor)

  def relatorio_geral(self):
    print(f"Relatório Geral da Escola {self.nome}:")
    for professor in self.professores:
      print(f"Professor: {professor.nome}")
      print(f"Média da Turma: {professor.media_da_turma():.2f}")
      print(f"Alunos Aprovados: {professor.alunos_aprovados()}")
      print("--------------------------")

# criando alunos
aluno1 = Aluno("João", 7)
aluno2 = Aluno("Maria", 5) 
aluno3 = Aluno("Pedro", 8)
aluno4 = Aluno("Ana", 6)
aluno5 = Aluno("Lucas", 4)
aluno6 = Aluno("Estevão", 3)
aluno7 = Aluno("Rai", 7.5)
aluno8 = Aluno("Tirulipa", 10)
aluno9 = Aluno("Enzo", 2)
aluno10 = Aluno("Fernando", 6)

# testando o método foi_aprovado
print(aluno1.foi_aprovado())
print(aluno5.foi_aprovado())
print("--------------------------")
#criando professores
prof1 = Professor("Adalberto")
prof2 = Professor("Moisés")


#criando escola
escola = Escola("IFRN")
#adcionando alunos na turma do professor 1
prof1.adicionar_aluno(aluno1)
prof1.adicionar_aluno(aluno2)
prof1.adicionar_aluno(aluno3)
prof1.adicionar_aluno(aluno4)
prof1.adicionar_aluno(aluno5)

#adcionando alunos na turma do professor 2
prof2.adicionar_aluno(aluno6)
prof2.adicionar_aluno(aluno7)
prof2.adicionar_aluno(aluno8)
prof2.adicionar_aluno(aluno9)
prof2.adicionar_aluno(aluno10)


#testando o método media_da_turma 
print("Média da turma do Professor:", prof1.nome)
print(prof1.media_da_turma())
print("--------------------------")
print("Média da turma do Professor:", prof2.nome)
print(prof2.media_da_turma())
print("--------------------------")

#testando o método alunos aprovados
print("Alunos aprovados da turma do Professor:", prof1.nome)
print(prof1.alunos_aprovados())
print("--------------------------")
print("Alunos aprovados da turma do Professor:", prof1.nome)
print(prof2.alunos_aprovados())
print("--------------------------")

#criei um método "adcionar_professor" para adcionar um professor a escola
escola.adcionar_professor(prof1)
escola.adcionar_professor(prof2)

#testando método relatorio_geral
escola.relatorio_geral()
