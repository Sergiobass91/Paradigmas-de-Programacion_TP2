from tkinter import Tk, Frame, Label, Radiobutton, Button, Entry, StringVar
from openpyxl import Workbook

def clearData():
    entryNombre.delete(0, 'END')
    entryApellido.delete(0, 'END')
    entryEdad.delete(0, 'END')
    entryDisparo1.delete(0, 'END')
    entryDisparo2.delete(0, 'END')
    entryDisparo3.delete(0, 'END')

def guardaDatos():
    print(entryNombre.get())
    print(entryApellido.get())
    print(entryEdad.get())
    print(sexo)
    print(entryDisparo1.get())
    print(entryDisparo2.get())
    print(entryDisparo3.get())



def main():
    pass


if __name__ == "__main__":

    sexo = ''
    root = Tk()
    root.title('2do TP Entregable')
    root.resizable(0,0)

    #Setea  y configura Frame 
    frame = Frame()
    frame.pack()
    frame.config(bg='#147E99', width='340', height='430', bd=6, relief='groove')
    
    #Setea Textos y entradas
    labelNombre = Label(frame, text='Nombre', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    labelNombre.grid(row='0',column='0', sticky='w', padx='10', pady='10')
    entryNombre = Entry(frame)
    entryNombre.grid(row='0',column='1')

    labelApellido = Label(frame, text='Apellido', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    labelApellido.grid(row='1',column='0', sticky='w', padx='10', pady='10')
    entryApellido = Entry(frame)
    entryApellido.grid(row='1',column='1', padx='10')

    labelEdad = Label(frame, text='Edad', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    labelEdad.grid(row='2',column='0', sticky='w', padx='10', pady='10')
    entryEdad = Entry(frame)
    entryEdad.grid(row='2',column='1', padx='10')

    checkMasculino = Radiobutton(frame, text='Masculino', variable=sexo, value= 'M', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    checkMasculino.grid(row='3',column='0', columnspan=2)
    checkFemenino = Radiobutton(frame, text='Femenino', variable=sexo, value= 'F', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    checkFemenino.grid(row='3',column='2', padx='10')

    labeDisparo1 = Label(frame, text='Disparo 1', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    labeDisparo1.grid(row='4',column='0', sticky='w', padx='10', pady='10')
    entryDisparo1 = Entry(frame)
    entryDisparo1.grid(row='4',column='1', padx='10')

    labeDisparo2 = Label(frame, text='Disparo 2', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    labeDisparo2.grid(row='5',column='0', sticky='w', padx='10', pady='10')
    entryDisparo2 = Entry(frame)
    entryDisparo2.grid(row='5',column='1', padx='10')

    labeDisparo3 = Label(frame, text='Disparo 3', bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    labeDisparo3.grid(row='6',column='0', sticky='w', padx='10', pady='10')
    entryDisparo3 = Entry(frame)
    entryDisparo3.grid(row='6',column='1', padx='10')

    #Agrega botones de opciones
    botonSave = Button(frame, text='Guardar', bg='#147E99', fg='#FFFFFF', font=('Calibri',12), command=guardaDatos)
    botonSave.grid(row='7',column='0', sticky='w', padx='10', pady='15')

    botonWinner = Button(frame, text='Ganador', bg='#147E99', fg='#FFFFFF', font=('Calibri',12))
    botonWinner.grid(row='7',column='1', sticky='w', padx='10', pady='15')

    botonExport = Button(frame, text='Exportar xls', bg='#147E99', fg='#FFFFFF', font=('Calibri',12))
    botonExport.grid(row='7',column='2', sticky='w', padx='10', pady='15')

root.mainloop()