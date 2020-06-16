# Gian Lucas Quinhones Alves

menu = ['1- Cadastrar Sala', '2- Relatório de Salas', '3- Cadastrar Disciplina',
    '4- Relatório Disciplinas', '5- Relatório de disciplinas por semestre', '6- Relacionar Salas as disciplinas']

lst_salas = []

lst_disciplina = []

class Sala:
    def __init__(self, numero):

        self.numero = numero
        self.andar = self.setAndar()
        self.capacidade = None

    def mostraDadosSalas(self):
        print('Sala - Andar - Capacidade')
        print(f'{self.numero} ---- {self.andar} ---- {self.capacidade}')

    def setAndar(self):
        return self.numero[0]

    def setCapacidade(self, capc):
        self.capacidade = int(capc)

class Disciplina:
    def __init__(self, nome, semestre):

        self.nome = nome.upper()
        self.semestre = semestre
        self.sala = None

    def mostraDadosDisciplinas(self):
        if (self.sala == None):
            print(f'Disciplina: {self.nome} ... Semestre: {self.semestre}... Sala: Não definida!')    
        else:
            print(f'Disciplina: {self.nome} ... Semestre: {self.semestre}... Sala: {self.sala}')    

    def mostraDadosDisciplinasPorSemestre(self):
        print(f'{self.nome}')    

    def configSala(self, x):
        self.sala = x

def chamaMenu():
    print('-'*10)
    print('   Menu  ')
    print('-'*10)
    for x in menu:
        print(f'{x}')

def printErro(valor, texto):
    print()
    print(f'Valor {valor} incorreto{texto}.')
    print()

def cadastraSala():
    while True:
        numeroSala = str(input('Digite o numero da sala: '))
        if len(numeroSala) == 3:
            validaSala = int(numeroSala[0])
            if (validaSala > 0):
                salaX = Sala(numeroSala)
                break
            else:
                printErro(numeroSala, ', o numero da sala não pode começar em zero')
        else:
            printErro(numeroSala, ', o numero da sala deve conter 3 numeros')

    while True:
        capSala = int(input('Digite a capaciade da sala: '))
        if(capSala > 0 and capSala < 41):
            salaX.setCapacidade(capSala)
            lst_salas.append(salaX)
            break
        else:
            printErro(capSala, ', digite valores de 1 a 40')
def relatorioSala():
    for x in lst_salas:
        x.mostraDadosSalas()
def cadastrarDisciplina():
    nome = input('Digite o nome da disciplina: ')
    while True:
        semestre = int(input('Digite o semestre: '))
        if(semestre > 0 and semestre < 11):
            disciplicaX = Disciplina(nome, semestre)
            lst_disciplina.append(disciplicaX)
            break
        else:
            printErro(semestre, ', digite valores de 1 a 10')
def relatorioDisciplina():
    for x in lst_disciplina:
        x.mostraDadosDisciplinas() 
def relatorioPorSemestre():
    semestre = int(input('Digite o semestre: '))
    print(f'Disciplinas do {semestre} semestre:')
    for x in lst_disciplina:
        if (x.semestre == semestre):
            x.mostraDadosDisciplinasPorSemestre()
def relacionarSalaDisciplina():
    cont = 0
    while True:
        validaDisciplina = True
        validaSala = True
        while validaDisciplina:
            for x in lst_disciplina:
                x.mostraDadosDisciplinas()
            print()
            disciplina = input('Digite a disciplina: ')
            for x in lst_disciplina:
                if x.nome == disciplina.upper():
                    validaDisciplina = False
                    break
                else:
                    pass
                cont += 1
        print()
        while validaSala:
            for x in lst_salas:
                x.mostraDadosSalas()
            print()
            sala = input('Digite a sala: ')
            print()
            for x in lst_salas:
                if x.numero == sala:
                    lst_disciplina[cont].configSala(sala)
                    print(x.numero)
                    validaSala = False
                else:
                    pass
        break
    

while True:
    chamaMenu()
    print()
    escolha = int(input())
    if escolha == 1:
        cadastraSala()
    elif escolha == 2:
        relatorioSala()
    elif escolha == 3:
        cadastrarDisciplina()
    elif escolha == 4:
        relatorioDisciplina()
    elif escolha == 5:
        relatorioPorSemestre()
    elif escolha == 6:
        relacionarSalaDisciplina()
    else:
        print()
        printErro(escolha, '')   
    
