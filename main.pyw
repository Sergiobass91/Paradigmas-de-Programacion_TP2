from tkinter import *
from cargaParticipantes import cargaParticipantes

def main():
    pass



# def clearData():
#     entryNombre.delete(0, END)
#     entryApellido.delete(0, END)
#     entryEdad.delete(0, END)
#     entryDisparo1.delete(0, END)
#     entryDisparo2.delete(0, END)
#     entryDisparo3.delete(0, END)

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
    labelNombre = Label(frame, text='Nombre', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='0',column='0', sticky='w', padx='10', pady='10')
    entryNombre = Entry(frame).grid(row='0',column='1')

    labelApellido = Label(frame, text='Apellido', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='1',column='0', sticky='w', padx='10', pady='10')
    entryApellido = Entry(frame).grid(row='1',column='1', padx='10')

    labelEdad = Label(frame, text='Edad', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='2',column='0', sticky='w', padx='10', pady='10')
    entryEdad = Entry(frame).grid(row='2',column='1', padx='10')

    checkMasculino = Radiobutton(frame, text='Masculino', variable=sexo, value= 'M', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='3',column='0', columnspan=2)
    checkMasculino = Radiobutton(frame, text='Femenino', variable=sexo, value= 'F', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='3',column='2', padx='10')

    labeDisparo1 = Label(frame, text='Disparo 1', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='4',column='0', sticky='w', padx='10', pady='10')
    entryDisparo1 = Entry(frame).grid(row='4',column='1', padx='10')

    labeDisparo2 = Label(frame, text='Disparo 2', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='5',column='0', sticky='w', padx='10', pady='10')
    entryDisparo2 = Entry(frame).grid(row='5',column='1', padx='10')

    labeDisparo3 = Label(frame, text='Disparo 3', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='6',column='0', sticky='w', padx='10', pady='10')
    entryDisparo3 = Entry(frame).grid(row='6',column='1', padx='10')

    #Agrega botones de opciones
    botonSave = Button(frame, text='Guardar', bg='#147E99', fg='#FFFFFF', font=('Calibri',12)).grid(row='7',column='0', sticky='w', padx='10', pady='15')
    botonWinner = Button(frame, text='Ganador', bg='#147E99', fg='#FFFFFF', font=('Calibri',12)).grid(row='7',column='1', sticky='w', padx='10', pady='15')
    botonExport = Button(frame, text='Exportar xls', bg='#147E99', fg='#FFFFFF', font=('Calibri',12)).grid(row='7',column='2', sticky='w', padx='10', pady='15')

root.mainloop()