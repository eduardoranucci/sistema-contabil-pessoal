from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
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

# print('\nSistema contábil', end='\n\n')
# print('1 - Criar contas\n2 - Lançar\n3 - Consultar plano de contas')
# print('4 - Consultar lançamentos\n5 - Editar conta\n6 - Editar lançamento')
# print('7 - Deletar conta\n8 - Deletar lançamento\n')

# escolha = int(input('O que você deseja fazer? '))

# match escolha:

#     case 1:
#         print()
#         nome_conta = input('Nome da conta: ')
#         class_conta = int(input('Classificação: '))
#         conta = Conta(nome_conta, class_conta, True)

#     case 2:
#         print()
#         data_lanc = input('Data: ')
#         debito_lanc = int(input('Débito: '))
#         credito_lanc = int(input('Crédito: '))
#         valor_lanc = float(input('Valor: '))
#         descr_lanc = input('Descrição: ')
#         parcelas = input('Parcelas: ')
#         lanc = Lancamento(valor_lanc, data_lanc, debito_lanc, credito_lanc, descr_lanc, True)

#     case 3:
#         Conta.consulta_plano_de_contas()

#     case 4:
#         Lancamento.consulta_lancamentos()

#     case 5:
#         print()
#         Conta.edita_conta(int(input('Código da conta: ')))

#     case 6:
#         print()
#         Lancamento.edita_lancamento(int(input('Código do lançamento: ')))

#     case 7:
#         print()
#         Conta.deleta_conta(int(input('Código da conta: ')))

#     case 8:
#         print()
#         Lancamento.deleta_lancamento(int(input('Código do lançamento: ')))

#     case opcao_invalida:
#         print(f'{opcao_invalida} não é uma opção valida.')

df.save('base.xlsx')


########################################################################################################################################################################################


main = Tk()
main.title('Contabilidade')
main.geometry('1000x625')
main.resizable(False, False)

# barra_menus = Menu(main)
# menu_opcoes = Menu(barra_menus, tearoff=0)
# menu_opcoes.add_command(label='Teste', command=main.quit)
# menu_opcoes.add_separator()
# menu_opcoes.add_command(label='Fechar', command=main.quit)
# barra_menus.add_cascade(label='Opções', menu=menu_opcoes)

# main.config(menu=barra_menus)

notebook = ttk.Notebook(main)
notebook.place(x=1, y=0, width=1000, height=625)

# criacao das abas
aba_contas = Frame(notebook)
aba_lacamentos = Frame(notebook)
aba_relatorios = Frame(notebook)

# posicionando as abas
notebook.add(aba_contas, text='Contas')
notebook.add(aba_lacamentos, text='Lançamentos')
notebook.add(aba_relatorios, text='Relatorios')

# cor das abas
cor_padrao = '#DFDFDF'
Frame(aba_contas, bg=cor_padrao).place(height=624, width=999)
Frame(aba_lacamentos, bg=cor_padrao).place(height=624, width=999)
Frame(aba_relatorios, bg=cor_padrao).place(height=624, width=999)

# ABA CONTAS #

Frame(aba_contas, bg='#000000').place(x=5, y=5, width=350, height=590)
Frame(aba_contas, bg='#D4D4D4').place(x=6, y=6, width=348, height=588)

Label(aba_contas, text='Criar contas', bg='#C0C0C0', font=('Arial', 14, 'bold')).place(x=6, y=10, width=348, height=25)

Label(aba_contas, text='Classificação:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=50, height=25)
valor_classificacao = Entry(aba_contas)
valor_classificacao.place(x=130, y=50, width=100, height=25)

Label(aba_contas, text='Descrição:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=85, height=25)
valor_descricao = Entry(aba_contas)
valor_descricao.place(x=130, y=85, width=100, height=25)

Label(aba_contas, text='Código:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=120, height=25)
valor_codigo = Entry(aba_contas)
valor_codigo.place(x=130, y=120, width=100, height=25)

tree = ttk.Treeview(aba_contas, columns=('Classificação', 'Descrição', 'Código'), show='headings')
tree.column('Classificação', minwidth=25, width=100)
tree.column('Descrição', minwidth=50, width=250)
tree.column('Código', minwidth=50, width=25)
tree.heading('Classificação', text='Classificação')
tree.heading('Descrição', text='Descrição')
tree.heading('Código', text='Código')

tree.place(x=365, y=5, width=625, height=590)

Button(aba_contas, text='Gravar').place(x=19, y=200, width=75, height=25)

Button(aba_contas, text='Alterar').place(x=143, y=200, width=75, height=25)

Button(aba_contas, text='Excluir').place(x=264, y=200, width=75, height=25)

# ABA LANCAMENTOS #

Frame(aba_lacamentos, bg='#000000').place(x=5, y=5, width=350, height=590)
Frame(aba_lacamentos, bg='#D4D4D4').place(x=6, y=6, width=348, height=588)

tree = ttk.Treeview(aba_lacamentos, columns=('Id', 'Data', 'Débito', 'Crédito', 'Valor', 'Descrição'), show='headings')
tree.column('Id', minwidth=10, width=10)
tree.column('Data', minwidth=10, width=40)
tree.column('Débito', minwidth=10, width=20)
tree.column('Crédito', minwidth=10, width=20)
tree.column('Valor', minwidth=10, width=35)
tree.column('Descrição', minwidth=10, width=330)
tree.heading('Id', text='Id')
tree.heading('Data', text='Data')
tree.heading('Débito', text='Débito')
tree.heading('Crédito', text='Crédito')
tree.heading('Valor', text='Valor')
tree.heading('Descrição', text='Descrição')

tree.place(x=365, y=5, width=625, height=590)

Label(aba_lacamentos, text='Lançar', bg='#C0C0C0', font=('Arial', 14, 'bold')).place(x=6, y=10, width=348, height=25)

Label(aba_lacamentos, text='Data:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=50, height=25)
valor_data = DateEntry(aba_lacamentos)
valor_data.place(x=100, y=50, width=100, height=25)

Label(aba_lacamentos, text='Débito:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=85, height=25)
valor_debito = Entry(aba_lacamentos)
valor_debito.place(x=100, y=85, width=100, height=25)

Label(aba_lacamentos, text='Crédito:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=120, height=25)
valor_credito = Entry(aba_lacamentos)
valor_credito.place(x=100, y=120, width=100, height=25)

Label(aba_lacamentos, text='Valor:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=155, height=25)
valor_valor = Entry(aba_lacamentos)
valor_valor.place(x=100, y=155, width=100, height=25)

Label(aba_lacamentos, text='Descrição:', font=('Arial', 12), bg='#D4D4D4').place(x=16, y=190, height=25)
valor_descrisao = Text(aba_lacamentos)
valor_descrisao.place(x=19, y=215, width=320, height=100)

Button(aba_lacamentos, text='Gravar').place(x=19, y=350, width=75, height=25)

Button(aba_lacamentos, text='Alterar').place(x=143, y=350, width=75, height=25)

Button(aba_lacamentos, text='Excluir').place(x=264, y=350, width=75, height=25)

# def valor():
#     print(valor_descrisao.get('1.0', 'end-1c'))

tree.insert('', END, values=('1', '14/09/2022', '1125', '1975', '10000,00', 'Saldo anterior - 31/12/2021'))

# ABA RELATORIOS #

Frame(aba_relatorios, bg='#000000').place(x=5, y=5, width=325, height=590)
Frame(aba_relatorios, bg='#D4D4D4').place(x=6, y=6, width=323, height=588)

Frame(aba_relatorios, bg='#000000').place(x=335.5, y=5, width=325, height=590)
Frame(aba_relatorios, bg='#D4D4D4').place(x=336.5, y=6, width=323, height=588)

Frame(aba_relatorios, bg='#000000').place(x=667, y=5, width=325, height=590)
Frame(aba_relatorios, bg='#D4D4D4').place(x=668, y=6, width=323, height=588)

# razão
Label(aba_relatorios, text='Razão', bg='#C0C0C0', font=('Arial', 14, 'bold')).place(x=6, y=10, width=323, height=25)
Label(aba_relatorios, text='Conta:', font=('Arial', 12), bg='#D4D4D4').place(x=26, y=80, height=25)
valor_conta_razao = Entry(aba_relatorios)
valor_conta_razao.place(x=124, y=80, height=25, width=75)

Label(aba_relatorios, text='Período:', font=('Arial', 12), bg='#D4D4D4').place(x=26, y=125, height=25)
Label(aba_relatorios, text='a', font=('Arial', 12), bg='#D4D4D4').place(x=156.5, y=160, height=25, width=10)
valor_data_inicial_razao = DateEntry(aba_relatorios)
valor_data_inicial_razao.place(x=26, y=160, width=98, height=25)

valor_data_final_razao = DateEntry(aba_relatorios)
valor_data_final_razao.place(x=199, y=160, width=98, height=25)

Button(aba_relatorios, text='Gerar').place(x=124, y=235, width=75, height=25)

# resumo
Label(aba_relatorios, text='Resumo', bg='#C0C0C0', font=('Arial', 14, 'bold')).place(x=336.5, y=10, width=323, height=25)

tree = ttk.Treeview(aba_relatorios, columns=('Mês', 'Débito', 'Crédito', 'Saldo'), show='headings')
tree.column('Mês', minwidth=10, width=10)
tree.column('Débito', minwidth=10, width=10)
tree.column('Crédito', minwidth=10, width=10)
tree.column('Saldo', minwidth=10, width=10)
tree.heading('Mês', text='Mês')
tree.heading('Débito', text='Débito')
tree.heading('Crédito', text='Crédito')
tree.heading('Saldo', text='Saldo')

tree.place(x=346, y=275, width=305, height=268)

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in meses:
    tree.insert('', END, values=(i, '0,00', '0,00', '0,00'))

Label(aba_relatorios, text='Conta:', font=('Arial', 12), bg='#D4D4D4').place(x=348, y=80, height=25, width=75)
Label(aba_relatorios, text='Ano:', font=('Arial', 12), bg='#D4D4D4').place(x=343, y=125, height=25, width=75)

valor_conta_resumo = Entry(aba_relatorios)
valor_conta_resumo.place(x=460.5, y=80, height=25, width=75)

valor_ano_resumo = Entry(aba_relatorios)
valor_ano_resumo.place(x=460.5, y=125, height=25, width=75)

Button(aba_relatorios, text='Gerar').place(x=460.5, y=200, width=75, height=25)

# balancete
Label(aba_relatorios, text='Balancete', bg='#C0C0C0', font=('Arial', 14, 'bold')).place(x=668, y=10, width=323, height=25)
Label(aba_relatorios, text='Conta:', font=('Arial', 12), bg='#D4D4D4').place(x=699, y=80, height=25)
valor_conta_balancete = Entry(aba_relatorios)
valor_conta_balancete.place(x=797, y=80, height=25, width=75)

Label(aba_relatorios, text='Período:', font=('Arial', 12), bg='#D4D4D4').place(x=699, y=125, height=25)
Label(aba_relatorios, text='a', font=('Arial', 12), bg='#D4D4D4').place(x=829.5, y=160, height=25, width=10)
valor_data_inicial_balancete = DateEntry(aba_relatorios)
valor_data_inicial_balancete.place(x=699, y=160, width=98, height=25)

valor_data_final_balancete = DateEntry(aba_relatorios)
valor_data_final_balancete.place(x=872, y=160, width=98, height=25)

Button(aba_relatorios, text='Gerar').place(x=797, y=235, width=75, height=25)

main.mainloop()
