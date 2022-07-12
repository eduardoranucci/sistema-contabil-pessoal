# from tkinter import *
# from tkinter import font

# root = Tk()
# root.title('Font Families')
# fonts=list(font.families())
# fonts.sort()

# def populate(frame):
#     '''Put in the fonts'''
#     listnumber = 1
#     for item in fonts:
#         label = "listlabel" + str(listnumber)
#         label = Label(frame,text=item,font=(item, 16)).pack()
#         listnumber += 1

# def onFrameConfigure(canvas):
#     '''Reset the scroll region to encompass the inner frame'''
#     canvas.configure(scrollregion=canvas.bbox("all"))

# canvas = Canvas(root, borderwidth=0, background="#ffffff")
# frame = Frame(canvas, background="#ffffff")
# vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)

# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")

# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame)

# # root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# class App:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.tree = ttk.Treeview()
#         self.tree.pack()
#         for i in range(10):
#             self.tree.insert("", "end", text="Item %s" % i)
#         self.tree.bind("<Double-1>", self.OnDoubleClick)
#         self.root.mainloop()

#     def OnDoubleClick(self, event):
#         item = self.tree.selection()[0]
#         print("you clicked on", self.tree.item(item,"text"))

# if __name__ == "__main__":
#     app = App()
    
    
# # Import Required Library
# from tkinter import *
# #import win32api
# from tkinter import filedialog
  
# # Create Tkinter Object
# root = Tk()
  
# # Set Title and geometry
# root.title('Print Hard Copies')
# root.geometry("200x200")
 
# def file_save():
#     f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
#     if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
#         return
#     text2save = str('Teste') # starts from `1.0`, not `0.0`
#     f.write(text2save)
#     f.close() # `()` was missing. 
  
# # Make Button
# Button(root, text="Print File", command=file_save).pack(pady=75)
  
# # Execute Tkinter
# root.mainloop()

clas = '1234567890'
meta = '1.2.34.56.7890'
print(len(clas))

clas_p = f'{clas[0]}.{clas[1]}.{clas[2:4]}.{clas[4:6]}.{clas[6:]}'
print(meta)
print(clas_p)