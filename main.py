import openpyxl as xl


class Conta:

    def __init__(self, nome, classificacao):
        
        self.nome = nome
        self.classificacao = classificacao
        
        try:
            total_contas = len(base_contas['A'])
            self.cod = base_contas['A'][total_contas - 1].value + 1
        except TypeError:
            self.cod = 1

        classificacao_valida = False
        while not classificacao_valida:
            try:
                self.verifica_classificacao()
                classificacao_valida = True
            except ValueError:
                print('Erro: Classificação já existente.', end='\n\n')
                self.classificacao = int(input('Classificação: '))

    def verifica_classificacao(self):
        
        for cell in base_contas['C']:
            if cell.value == self.classificacao:
                raise ValueError


class Lancamento:

    global base_lancamentos

    def __init__(self, valor, data, debito, credito, descricao, parcelas):
        
        self.valor = valor
        self.data = data
        self.debito = debito
        self.credito = credito
        self.descricao = descricao
        
        if parcelas == '':
            self.parcelas = 1
        else:
            self.parcelas = int(parcelas)
        
        try:
            total_lancamentos = len(base_lancamentos['A'])
            self.cod = base_lancamentos['A'][total_lancamentos - 1].value + 1
        except TypeError:
            self.cod = 1

        debito_valido = False
        while not debito_valido:
            try:
                self.verifica_debito()
                debito_valido = True
            except ValueError:
                print('Erro: Conta não existente.', end='\n\n')
                self.debito = int(input('Débito: '))

        credito_valido = False
        while not credito_valido:
            try:
                self.verifica_credito()
                credito_valido = True
            except ValueError:
                print('Erro: Conta não existente.', end='\n\n')
                self.credito = int(input('Crédito: '))

    def verifica_debito(self):
        
        contas = []
        for cell in base_contas['A']:
            contas.append(cell.value)

        if self.debito in contas:
            pass
        else:
            raise ValueError

    def verifica_credito(self):

        contas = []
        for cell in base_contas['A']:
            contas.append(cell.value)

        if self.credito in contas:
            pass
        else:
            raise ValueError


try:
    df = xl.load_workbook(r'base.xlsx')

    base_contas = df['Contas']
    base_lancamentos = df['Lançamentos']

except FileNotFoundError:
    df = xl.Workbook()
    
    df.create_sheet('Contas', 0)
    df.create_sheet('Lançamentos', 1)
    df.remove(df['Sheet'])

    base_contas = df['Contas']
    base_contas.append(['Código', 'Nome', 'Classificação'])

    base_lancamentos = df['Lançamentos']
    base_lancamentos.append(['Código', 'Data', 'Débito', 'Crédito', 'Valor', 'Descrição'])

    df.save('base.xlsx')

print('\nSistema contabil', end='\n\n')
print('1 - Criar contas\n2 - Lançar\n3 - Sair', end='\n\n')


escolha = int(input('O que você deseja fazer? '))

if escolha == 1:
    print()
    nome_conta = input('Nome da conta: ')
    class_conta = int(input('Classificação: '))
    conta = Conta(nome_conta, class_conta)

    base_contas.append([conta.cod, conta.nome, conta.classificacao])

elif escolha == 2:
    print()
    data_lanc = input('Data: ')
    debito_lanc = int(input('Débito: '))
    credito_lanc = int(input('Crédito: '))
    valor_lanc = float(input('Valor: '))
    descr_lanc = input('Descrição: ')
    parcelas_lanc = input('Parcelas: ')
    lanc = Lancamento(valor_lanc, data_lanc, debito_lanc, credito_lanc, descr_lanc, parcelas_lanc)

    base_lancamentos.append([lanc.cod, lanc.data, lanc.debito, lanc.credito, lanc.valor, lanc.descricao])

elif escolha == 3:
    pass

else:
    print('Opção não disponível')

df.save('base.xlsx')
