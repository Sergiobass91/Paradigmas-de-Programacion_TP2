#TP2 Paradigmas de Progamación
#Sergio Beltrán Galvis

from mejorDisparo import mejorDisparo
from promedio import promedioDisparos
from tkinter import Tk, Frame, Label, Radiobutton, Button, Entry, StringVar, IntVar, messagebox
import random
import openpyxl
import csv

def borraDatos():
    entryNombre.delete(0, 'end')
    entryApellido.delete(0, 'end')
    entryEdad.delete(0, 'end')
    entryDisparo1.delete(0, 'end')
    entryDisparo2.delete(0, 'end')
    entryDisparo3.delete(0, 'end')

def defineSexo():
    define = 'M' if sexo.get() == 1 else 'F'
    return define


def guardaDatos():
    try:
        tuplaDisparos = (float(entryDisparo1.get()), float(entryDisparo2.get()), float(entryDisparo3.get()))
        mejorDisp = mejorDisparo(tuplaDisparos)
        promedioDisp = promedioDisparos(tuplaDisparos)
        listaParticipantes = []
        datosParticipante = dict()

        datosParticipante['numeroId'] = random.randrange(0,1000)
        datosParticipante['Nombre'] = entryNombre.get()
        datosParticipante['Apellido'] = entryApellido.get()
        datosParticipante['edad'] = entryEdad.get()
        datosParticipante['sexo'] = defineSexo()
        datosParticipante['Disparo1'] = entryDisparo1.get()
        datosParticipante['Disparo2'] = entryDisparo2.get()
        datosParticipante['Disparo3'] = entryDisparo3.get()
        datosParticipante['MejorDisparo'] = mejorDisp
        datosParticipante['promedioDisparo'] = promedioDisp

        listaParticipantes.append(datosParticipante)
        
        with open('tablaParticipantes.csv', 'r', newline='') as csvfile:

            #Verifica si el archivo posee filas con datos
            reader = [row for row in csv.DictReader(csvfile)]
            if len(reader) == 0:
                csvfile.close()
                #Seteea los Headers en la primera iteración
                with open('tablaParticipantes.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=listaParticipantes[0].keys())
                    writer.writeheader()
                    writer.writerows(listaParticipantes)
            else:
                csvfile.close()
                #pasa la primera escritura, omite setear el header.
                with open('tablaParticipantes.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=listaParticipantes[0].keys())
                    writer.writerows(listaParticipantes)

        messagebox.showinfo(title="DBA Message", message="Participante guardado en tabla de datos.")
        borraDatos()
    except:
        messagebox.showwarning(title="Error en Datos", message="Debes completar todos los campos")
    return listaParticipantes


def cargaXls():
    book = openpyxl.Workbook()
    ws = book.active

    f = open('tablaParticipantes.csv')
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)
    f.close()
       
    book.save(filename='cargaParticipantesExcel.xlsx')
    messagebox.showinfo(title="EXCEL", message="Archivo generado con exito!")
    
def ganador():

    with open('tablaParticipantes.csv', 'r', newline='') as csvfile:
        reader = [row for row in csv.DictReader(csvfile)]
        ordenPromedio = sorted(reader, key= lambda k:k['promedioDisparo'])

    messagebox.showinfo(title="GANADOR!", message=f"El ganador es: {ordenPromedio[0]['Nombre']} {ordenPromedio[0]['Apellido']}\nCon un promedio de {ordenPromedio[0]['promedioDisparo']}")


if __name__ == "__main__":

    root = Tk()
    root.title('2do TP Entregable')
    root.resizable(0,0)

    #Setea  y configura Frame 
    frame = Frame()
    frame.pack()
    frame.config(bg='#147E99', width='340', height='430', bd=6, relief='groove')
    sexo = IntVar()
    
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

    
    checkMasculino = Radiobutton(frame, text='Masculino',variable=sexo, value=1, command=defineSexo, bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
    checkMasculino.grid(row='3',column='0') #columnspan=2
    checkFemenino = Radiobutton(frame, text='Femenino',variable=sexo, value=2, command=defineSexo, bg='#147E99', fg='#FFFFFF', font=('Calibri',14))
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

    botonWinner = Button(frame, text='Ganador', bg='#147E99', fg='#FFFFFF', font=('Calibri',12), command=ganador)
    botonWinner.grid(row='7',column='1', sticky='w', padx='10', pady='15')

    botonExport = Button(frame, text='Exportar xls', bg='#147E99', fg='#FFFFFF', font=('Calibri',12), command=cargaXls)
    botonExport.grid(row='7',column='2', sticky='w', padx='10', pady='15')

root.mainloop()