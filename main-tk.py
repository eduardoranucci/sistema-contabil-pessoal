from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry









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