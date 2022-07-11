from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def inserir():
    if v_id.get()=='' or v_nome.get()=='' or v_num.get()=='':
        messagebox.showinfo(title='Erro', message='Digite todos os dados.')
        return

    tree.insert('', 'end', values=(v_id.get(), v_nome.get(), v_num.get()))

    v_id.delete(0, END)
    v_nome.delete(0, END)
    v_num.delete(0, END)
    v_id.focus()

def deletar():
    try:
        selecao = tree.selection()[0]
        tree.delete(selecao)
    except IndexError:
        messagebox.showinfo(title='Erro', message='Selecione uma linha.')

def obter():
    try:
        selecao = tree.selection()[0]
        valores = tree.item(selecao, 'values')
        print(valores)
    except IndexError:
        messagebox.showinfo(title='Erro', message='Selecione uma linha.')

app = Tk()
app.title('Contabilidade')
app.geometry('1000x625')

lb_id = Label(app, text='Id')
v_id = Entry(app)

lb_nome = Label(app, text='Nome')
v_nome = Entry(app)

lb_num = Label(app, text='Número')
v_num = Entry(app)

tree = ttk.Treeview(app, columns=('Id', 'Nome', 'Número'), show='headings')
tree.column('Id', minwidth=10, width=50)
tree.column('Nome', minwidth=10, width=250)
tree.column('Número', minwidth=10, width=150)
tree.heading('Id', text='Id')
tree.heading('Nome', text='Nome')
tree.heading('Número', text='Número')

btn_inserir = Button(app, text='Inserir', command=inserir)
btn_deletar = Button(app, text='Deletar', command=deletar)
btn_obter = Button(app, text='Obter', command=obter)

lb_id.grid(column=0, row=0, sticky='w', padx=13)
v_id.grid(column=0, row=1)

lb_nome.grid(column=1, row=0, sticky='w', padx=13)
v_nome.grid(column=1, row=1)

lb_num.grid(column=2, row=0, sticky='w', padx=13)
v_num.grid(column=2, row=1)

tree.grid(column=0, row=3, columnspan=3, pady=5, padx=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)

#tree.pack()

#for id, nome, num in lista:
#    tree.insert("", "end", values=(id, nome, num))

app.mainloop()