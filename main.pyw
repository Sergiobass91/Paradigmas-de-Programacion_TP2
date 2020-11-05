from tkinter import Tk, Frame, Label, Radiobutton, Button, Entry, StringVar, IntVar, messagebox
import openpyxl

def clearData():
    entryNombre.delete(0, 'end')
    entryApellido.delete(0, 'end')
    entryEdad.delete(0, 'end')
    entryDisparo1.delete(0, 'end')
    entryDisparo2.delete(0, 'end')
    entryDisparo3.delete(0, 'end')

def guardaDatos():
    listaCarga = [entryNombre.get(),entryApellido.get(),entryEdad.get(),sexo,entryDisparo1.get(),entryDisparo2.get(),entryDisparo3.get()]
    with open ('participantes.txt', 'a', encoding='UTF-8', newline='\n') as file:
        file.writelines(listaCarga)
        file.write("\n")

    clearData()


def defineSexo():
    define = 'M' if sexo.get() == 1 else 'F'
    messagebox.showinfo(message=define)
    return define



def cargaXls():

    listFieldNames = ['Nombre','Apellido','Edad','Disparo 1','Disparo 2','Disparo 3']
    book = openpyxl.Workbook()
    sheet= book.active
    # sheet['A1'] = 'Nombre'
    # sheet['B1'] = 'Apellido'
    # sheet['C1'] = 'Edad'
    # sheet['D1'] = 'Sexo'
    # sheet['E1'] = 'Disparo 1'
    # sheet['F1'] = 'Disparo 2'
    # sheet['G1'] = 'Disparo 3'
    sheet.cell(row=3, column=2, value='PRUEBA')
    for i in range(len(listFieldNames)):
        for name in listFieldNames:
            print(name) #DEBUG
            sheet.cell(row=1, column=i+1, value=name)
        

    book.save(filename='cargaParticipantesExcel.xlsx')






if __name__ == "__main__":

    root = Tk()
    root.title('2do TP Entregable')
    root.resizable(0,0)

    #Setea  y configura Frame 
    frame = Frame()
    frame.pack()
    frame.config(bg='#147E99', width='340', height='430', bd=6, relief='groove')
    
    
    #Setea Textos y entradas
    Label(frame, text='Nombre', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='0',column='0', sticky='w', padx='10', pady='10')
    entryNombre = Entry(frame)
    entryNombre.grid(row='0',column='1')
    Label(frame, text='Apellido', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='1',column='0', sticky='w', padx='10', pady='10')
    entryApellido = Entry(frame)
    entryApellido.grid(row='1',column='1', padx='10')

    Label(frame, text='Edad', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='2',column='0', sticky='w', padx='10', pady='10')
    entryEdad = Entry(frame)
    entryEdad.grid(row='2',column='1', padx='10')
    sexo = IntVar()
    checkMasculino = Radiobutton(frame, text='Masculino',variable=sexo, value= 1, command=defineSexo, bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    checkMasculino.grid(row='3',column='0') #, columnspan=2
    checkFemenino = Radiobutton(frame, text='Femenino',variable=sexo, value= 2, command=defineSexo, bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    checkFemenino.grid(row='3',column='1', padx='10')

    Label(frame, text='Disparo 1', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='4',column='0', sticky='w', padx='10', pady='10')
    entryDisparo1 = Entry(frame)
    entryDisparo1.grid(row='4',column='1', padx='10')

    Label(frame, text='Disparo 2', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='5',column='0', sticky='w', padx='10', pady='10')
    entryDisparo2 = Entry(frame)
    entryDisparo2.grid(row='5',column='1', padx='10')

    Label(frame, text='Disparo 3', bg='#147E99', fg='#FFFFFF', font=('Calibri',14)).grid(row='6',column='0', sticky='w', padx='10', pady='10')
    entryDisparo3 = Entry(frame)
    entryDisparo3.grid(row='6',column='1', padx='10')

    #Agrega botones de opciones
    botonSave = Button(frame, text='Guardar', bg='#147E99', fg='#FFFFFF', font=('Calibri',12), command= guardaDatos)
    botonSave.grid(row='7',column='0', sticky='w', padx='10', pady='15')

    botonWinner = Button(frame, text='Ganador', bg='#147E99', fg='#FFFFFF', font=('Calibri',12))
    botonWinner.grid(row='7',column='1', sticky='w', padx='10', pady='15')

    botonExport = Button(frame, text='Exportar xls', bg='#147E99', fg='#FFFFFF', font=('Calibri',12), command=cargaXls)
    botonExport.grid(row='7',column='2', sticky='w', padx='10', pady='15')



root.mainloop()