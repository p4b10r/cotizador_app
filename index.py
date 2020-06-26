#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
import ttk
from Tkinter import *
import sqlite3

import backend


#columnspan indica columnas vacías
#pady indica un espaciado interno en y




class Cotizador:

    def __init__(self,window):


        #ventana
        self.wind=window
        self.wind.title("Cotizador")

        cliente=StringVar()
        empresa=StringVar()
        email=StringVar()
        comentarios=StringVar()

        descripcion=StringVar()
        pesolote=float()
        tiempolote=float()
        qpiezas=int()
        qlotes=int()
        #========================FUNCIONES===============================
        def insDataCliente():
            if(len(cliente.get())!=0):
                backend.insertDataCliente(cliente.get(), empresa.get(), email.get(), comentarios.get())
                backend.getClientes(self.treecliente)

        def cleDataCliente():

            if(len(cliente.get())!=0):
                backend.clearDataCliente()
                backend.getClientes(self.treecliente)





    #========================FRAMES==================================
        dataframe=LabelFrame(self.wind, text='Datos de cotización')
        dataframe.grid(row=1, column=0)

        Label(dataframe, text='Cliente: ').grid(row=1, column=0)
        self.txtcliente=Entry(dataframe, textvariable=cliente)

        self.txtcliente.grid(row=1, column=1)
        Label(dataframe, text='Empresa/Particular: ').grid(row=2, column=0)
        self.txtempresa=Entry(dataframe, textvariable=empresa)
        self.txtempresa.grid(row=2, column=1)

        Label(dataframe, text='Email: ').grid(row=3, column=0)
        self.txtemail=Entry(dataframe, textvariable=email)

        self.txtemail.grid(row=3, column=1)
        Label(dataframe, text='Comentarios: ').grid(row=4, column=0)
        self.txtcomentarios=Entry(dataframe, textvariable=comentarios)

        self.txtcomentarios.grid(row=4, column=1)

        self.anadircliente=ttk.Button(dataframe,text="Añadir Cliente", command=insDataCliente).grid(row=5,column=0, columnspan=2,sticky=W+E)


        #contenedor frame
        varframe=LabelFrame(self.wind, text='Variables de lote')
        varframe.grid(row=1, column=1, pady=10)
        #input peso
        Label(varframe, text='Descripción: ').grid(row=0, column=0)
        self.txtdescripcion=Entry(varframe)
        self.txtdescripcion.grid(row=0, column=1)
        Label(varframe, text='Peso de lote [g]: ').grid(row=1, column=0)
        self.txtpeso=Entry(varframe)
        self.txtpeso.focus()
        self.txtpeso.grid(row=1, column=1)
        #input tiempo
        Label(varframe, text='Tiempo lote [hrs]: ').grid(row=2, column=0)
        self.txttiempo=Entry(varframe)
        self.txttiempo.grid(row=2, column=1)
        #Cantidad de piezas
        Label(varframe, text="Cantidad de piezas: ").grid(row=3, column=0)
        self.txtpiezas=Entry(varframe)
        self.txtpiezas.grid(row=3, column=1)
        #cantidad de pasadas
        Label(varframe, text='Cantidad lotes: ').grid(row=4, column=0)
        self.txtcantidad=Entry(varframe)
        self.txtcantidad.grid(row=4, column=1)
        Label(varframe, text="Seleccione Material: ").grid(row=5, column=0, columnspan=2)
        self.txtmaterial=LabelFrame(varframe, text="Selección de Material")
        self.txtmaterial.grid(row=5, column=0, columnspan=2)
        opciones=['PLA+', 'ABS', 'PETG', 'TECNICO']
        tkarg=StringVar(self.txtmaterial)
        tkarg.set(opciones[0])
        menu=OptionMenu(self.txtmaterial, tkarg, *opciones)
        menu.pack()
        self.anadirlote=ttk.Button(varframe,text="Añadir Lote").grid(row=6,column=0, columnspan=2,sticky=W+E)

        #self.buttonframe=LabelFrame(self.wind)
        #self.buttonframe.grid(row=4, column=0, columnspan=3)
        #sticky=W+E ocupa todo el ancho disponible, west + east
        #ttk.Button(self.buttonframe, text='Cotizar',).grid(row=0, sticky=W+E)

        clienteframe=LabelFrame(self.wind, text="Cliente")
        clienteframe.grid(row=5, column=0, columnspan=2)
        self.treecliente=ttk.Treeview(clienteframe, height=3, column=('#1','#2','#3'))
        self.treecliente.grid(row=1, column=0)
        self.treecliente.heading('#0', text="Cliente", anchor=CENTER)
        self.treecliente.heading('#1', text="Empresa", anchor=CENTER)
        self.treecliente.heading('#2', text="Email", anchor=CENTER)
        self.treecliente.heading('#3', text="Comentarios", anchor=CENTER)


        ttk.Button(self.wind, text="Limpiar Cliente", command=cleDataCliente).grid(row=6, columnspan=2, sticky=W+E)

        #Tabla
        loteframe=LabelFrame(self.wind, text='Lotes')
        loteframe.grid(row=7, column=0, columnspan=2)
        self.treelote=ttk.Treeview(loteframe, height=10, column=('#1','#2','#3'))
        self.treelote.grid(row=1, column=0)
        self.treelote.heading('#0', text='Descripción', anchor=CENTER)
        self.treelote.heading('#1', text='Peso [g]', anchor=CENTER)
        self.treelote.heading('#2', text='Tiempo [hrs]',anchor=CENTER)
        self.treelote.heading('#3', text='Cantidad [un]',anchor=CENTER)
        backend.getLote(self.treelote)



        ttk.Button(self.wind, text="Limpiar Lotes").grid(row=8, columnspan=2, sticky=W+E)
        ttk.Button(self.wind, text="Cotizar").grid(row=9, columnspan=2, sticky=W+E)
        ttk.Button(self.wind, text="Exportar pdf").grid(row=10, columnspan=2, sticky=W+E)



if __name__=="__main__":
    window=Tk()
    app=Cotizador(window)
    window.mainloop()
