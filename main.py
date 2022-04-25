import openpyxl as xl
from prettytable import PrettyTable


class Conta:

    def __init__(self, nome, classificacao, adicionar_na_base=False):
        
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

        if adicionar_na_base:
            base_contas.append([self.cod, self.nome, self.classificacao])

    def verifica_classificacao(self):
        
        for cell in base_contas['C']:
            if cell.value == self.classificacao:
                raise ValueError

    def consulta_plano_de_contas():
        
        tabela = PrettyTable()

        coluna_a, coluna_b, coluna_c = [], [], []
            
        for column in base_contas['A:C']:
            
            for cell in column:
                if cell.row == 1:
                    continue

                match cell.column:

                    case 1:
                        coluna_a.append(cell.value)

                    case 2:
                        coluna_b.append(cell.value)

                    case 3:
                        coluna_c.append(cell.value)
            

        tabela.add_column('Código', coluna_a)
        tabela.add_column('Nome', coluna_b)
        tabela.add_column('Classificação', coluna_c)

        print(f'\n{tabela}')

    def edita_conta(cod):
        
        for cell in base_contas['A']:
            if cell.value == cod:
                linha = cell.row
                print()
                nome = input('Nome: ')
                classificacao = int(input('Classificação: '))
                Conta(nome, classificacao)

                base_contas[f'B{linha}'] = nome
                base_contas[f'C{linha}'] = classificacao

    def deleta_conta(cod):

        for cell in base_contas['A']:
            if cell.value == cod:
                base_contas.delete_rows(cell.row)


class Lancamento:

    global base_lancamentos

    def __init__(self, valor, data, debito, credito, descricao, adicionar_na_base=False):
        
        self.valor = valor
        self.data = data
        self.debito = debito
        self.credito = credito
        self.descricao = descricao
        
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
                print('Erro: Conta débito não existente.', end='\n\n')
                self.debito = int(input('Débito: '))

        credito_valido = False
        while not credito_valido:
            try:
                self.verifica_credito()
                credito_valido = True
            except ValueError:
                print('Erro: Conta crédito não existente.', end='\n\n')
                self.credito = int(input('Crédito: '))

        if adicionar_na_base:
            base_lancamentos.append([self.cod, self.data, self.debito, self.credito, self.valor, self.descricao])

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

    def consulta_lancamentos():
        
        tabela = PrettyTable()

        coluna_a, coluna_b, coluna_c = [], [], []
        coluna_d, coluna_e, coluna_f = [], [] ,[]
            
        for column in base_lancamentos['A:F']:
            
            for cell in column:
                if cell.row == 1:
                    continue

                match cell.column:

                    case 1:
                        coluna_a.append(cell.value)

                    case 2:
                        coluna_b.append(str(cell.value))

                    case 3:
                        coluna_c.append(cell.value)

                    case 4:
                        coluna_d.append(cell.value)

                    case 5:
                        coluna_e.append(cell.value)

                    case 6:
                        coluna_f.append(cell.value)
            
        tabela.add_column('Código', coluna_a)
        tabela.add_column('Data', coluna_b)
        tabela.add_column('Débito', coluna_c)
        tabela.add_column('Crédito', coluna_d)
        tabela.add_column('Valor', coluna_e)
        tabela.add_column('Descrição', coluna_f)

        print(f'\n{tabela}')

    def edita_lancamento(cod):
        
        for cell in base_contas['A']:
            if cell.value == cod:
                linha = cell.row
                print()
                data = input('Data: ')
                debito = int(input('Débito: '))
                credito = int(input('Crédito: '))
                valor = float(input('Valor: '))
                descricao = input('Descrição: ')
                Lancamento(valor, data, debito, credito, descricao)

                base_lancamentos[f'B{linha}'] = data
                base_lancamentos[f'C{linha}'] = debito
                base_lancamentos[f'D{linha}'] = credito
                base_lancamentos[f'E{linha}'] = valor
                base_lancamentos[f'F{linha}'] = descricao

    def deleta_lancamento(cod):

        for cell in base_lancamentos['A']:
            if cell.value == cod:
                base_lancamentos.delete_rows(cell.row)

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

print('\nSistema contábil', end='\n\n')
print('1 - Criar contas\n2 - Lançar\n3 - Consultar plano de contas')
print('4 - Consultar lançamentos\n5 - Editar conta\n6 - Editar lançamento')
print('7 - Deletar conta\n8 - Deletar lançamento\n')

escolha = int(input('O que você deseja fazer? '))

match escolha:

    case 1:
        print()
        nome_conta = input('Nome da conta: ')
        class_conta = int(input('Classificação: '))
        conta = Conta(nome_conta, class_conta, True)

    case 2:
        print()
        data_lanc = input('Data: ')
        debito_lanc = int(input('Débito: '))
        credito_lanc = int(input('Crédito: '))
        valor_lanc = float(input('Valor: '))
        descr_lanc = input('Descrição: ')
        parcelas = input('Parcelas: ')
        lanc = Lancamento(valor_lanc, data_lanc, debito_lanc, credito_lanc, descr_lanc, True)

    case 3:
        Conta.consulta_plano_de_contas()

    case 4:
        Lancamento.consulta_lancamentos()

    case 5:
        print()
        Conta.edita_conta(int(input('Código da conta: ')))

    case 6:
        print()
        Lancamento.edita_lancamento(int(input('Código do lançamento: ')))

    case 7:
        print()
        Conta.deleta_conta(int(input('Código da conta: ')))

    case 8:
        print()
        Lancamento.deleta_lancamento(int(input('Código do lançamento: ')))

    case opcao_invalida:
        print(f'{opcao_invalida} não é uma opção valida.')

df.save('base.xlsx')
