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

        self.pestanas=ttk.Notebook(window)
        self.pestanas.pack()
        self.p1=ttk.Frame(window)
        self.p2=ttk.Frame(window)

        self.pestanas.add(self.p1, text="Cotización")
        self.pestanas.add(self.p2, text="Variables")




        cliente=StringVar()
        empresa=StringVar()
        email=StringVar()
        comentarios=StringVar()

        descripcion=StringVar()
        pesolote=StringVar()
        tiempolote=StringVar()
        qpiezas=StringVar()
        qlotes=StringVar()

        costofijo=DoubleVar()
        maquinas=StringVar()
        horascubiertas=DoubleVar()
        factormtto=DoubleVar()
        factorerror=DoubleVar()
        depreciacion=DoubleVar()
        costohorareal=DoubleVar()
        costomaterialpeso=DoubleVar()

        pla=DoubleVar()
        abs=DoubleVar()
        petg=DoubleVar()
        tecnico=DoubleVar()

        #========================FUNCIONES===============================

        #::::::::::::::::::::::::DATACLIENTE::::::::::::::::::::::::::::
        def insDataCliente():
            if(len(cliente.get())!=0):
                backend.insertDataCliente(cliente.get(), empresa.get(), email.get(), comentarios.get())
                backend.getClientes(self.treecliente)

        def cleDataCliente():

            if(len(cliente.get())!=0):
                backend.clearDataCliente()
                backend.getClientes(self.treecliente.delete(*self.treecliente.get_children()))

        #::::::::::::::::::::::::DATALOTE::::::::::::::::::::::::::::
        def insDataLote():
            if(len(descripcion.get())!=0):
                backend.insertDataLote(descripcion.get(), float(pesolote.get()), float(tiempolote.get()), int(qpiezas.get()), int(qlotes.get()))
                backend.getLote(self.treelote)
        def cleDataLote():

            if(len(descripcion.get())!=0):
                backend.clearDataLote()
                backend.getLote(self.treelote.delete(self.treelote.get_children()))

        def delDataLote():
            self.treelote.item(self.treelote.selection())["text"][0]
            backend.deleteDataLote(self.treelote.item(self.treelote.selection())["text"])
            backend.getLote(self.treelote)

        #::::::::::::::::::::::::DATACOSTOS::::::::::::::::::::::::::::

        def insDataCostos():

            backend.insDataCostos(float(costofijo.get()), int(maquinas.get()), float(factormtto.get()), float(horascubiertas.get()),float(factorerror.get()),float(depreciacion.get()), float(costohorareal.get()),float(costomaterialpeso.get()))
            backend.getDataCostos(self.treevariable)


        def delDataCostos():

            backend.deleteDataCostos(self.treevariable)
            backend.getDataCostos(self.treevariable.delete(*self.treevariable.get_children()))


        #::::::::::::::::::::::::DATAMATERIAL:::::::::::::::::::::::::::::::

        def insDataMaterial():
            backend.insertDataMaterial(float(pla.get()),float(abs.get()),float(petg.get()),float(tecnico.get()))
            backend.getDataMaterial(self.treematerial)

        def delDataMaterial():
            backend.deleteDataMaterial(self.treematerial)
            backend.getDataMaterial(self.treematerial.delete(*self.treematerial.get_children()))




    #========================PESTAÑA1==================================
        dataframe=LabelFrame(self.p1, text='Datos de cotización')
        dataframe.grid(row=0, column=0, sticky=W)

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
        varframe=LabelFrame(self.p1, text='Variables de lote')
        varframe.grid(row=1, column=0, sticky=W)
        #input peso
        Label(varframe, text='Descripción: ').grid(row=0, column=0)
        self.txtdescripcion=Entry(varframe, textvariable=descripcion)
        self.txtdescripcion.grid(row=0, column=1)
        Label(varframe, text='Peso de lote [g]: ').grid(row=1, column=0)
        self.txtpeso=Entry(varframe, textvariable=pesolote)
        self.txtpeso.focus()
        self.txtpeso.grid(row=1, column=1)
        #input tiempo
        Label(varframe, text='Tiempo lote [hrs]: ').grid(row=2, column=0)
        self.txttiempo=Entry(varframe, textvariable=tiempolote)
        self.txttiempo.grid(row=2, column=1)
        #Cantidad de piezas
        Label(varframe, text="Cantidad de piezas: ").grid(row=3, column=0)
        self.txtpiezas=Entry(varframe, textvariable=qpiezas)
        self.txtpiezas.grid(row=3, column=1)
        #cantidad de pasadas
        Label(varframe, text='Cantidad lotes: ').grid(row=4, column=0)
        self.txtcantidad=Entry(varframe, textvariable=qlotes)
        self.txtcantidad.grid(row=4, column=1)
        Label(varframe, text="Seleccione Material: ").grid(row=5, column=0, columnspan=2)
        self.txtmaterial=LabelFrame(varframe, text="Selección de Material")
        self.txtmaterial.grid(row=5, column=0, columnspan=2)
        opciones=['PLA+', 'ABS', 'PETG', 'TECNICO']
        tkarg=StringVar(self.txtmaterial)
        tkarg.set(opciones[0])
        menu=OptionMenu(self.txtmaterial, tkarg, *opciones)
        menu.pack()
        self.anadirlote=ttk.Button(varframe,text="Añadir Lote", command=insDataLote).grid(row=6,column=0, columnspan=2,sticky=W+E)

        #self.buttonframe=LabelFrame(self.wind)
        #self.buttonframe.grid(row=4, column=0, columnspan=3)
        #sticky=W+E ocupa todo el ancho disponible, west + east
        #ttk.Button(self.buttonframe, text='Cotizar',).grid(row=0, sticky=W+E)

        clienteframe=LabelFrame(self.p1, text="Cliente")
        clienteframe.grid(row=0, column=1,sticky=W+E+N)
        self.treecliente=ttk.Treeview(clienteframe, height=1, column=('#1','#2','#3'))
        self.treecliente.grid(row=1, column=0)
        self.treecliente.heading('#0', text="Cliente", anchor=CENTER)
        self.treecliente.heading('#1', text="Empresa", anchor=CENTER)
        self.treecliente.heading('#2', text="Email", anchor=CENTER)
        self.treecliente.heading('#3', text="Comentarios", anchor=CENTER)


        ttk.Button(clienteframe, text="Limpiar Cliente", command=cleDataCliente).grid(row=2, columnspan=2, sticky=W+E)

        #Tabla
        loteframe=LabelFrame(self.p1, text='Lotes')
        loteframe.grid(row=1, column=1, sticky=E+N)
        self.treelote=ttk.Treeview(loteframe, height=6, column=('#1','#2','#3','#4',"#5"))
        self.treelote.grid(row=1, column=0)
        self.treelote.heading('#0', text='Descripción', anchor=CENTER)
        self.treelote.column("#0", width=340)
        self.treelote.heading('#1', text='Peso [g]', anchor=CENTER)
        self.treelote.column("#1", width=80)
        self.treelote.heading('#2', text='Tiempo [hrs]',anchor=CENTER)
        self.treelote.column("#2", width=90)
        self.treelote.heading('#3', text='Cant. piezas [un]',anchor=CENTER)
        self.treelote.column("#3", width=100)
        self.treelote.heading('#4', text='Cant. lotes [un]',anchor=CENTER)
        self.treelote.column("#4", width=100)
        self.treelote.heading('#5', text='Costo [$]',anchor=CENTER)
        self.treelote.column("#5", width=80)
        backend.getLote(self.treelote)

        ttk.Button(loteframe, text="Limpiar Lotes", command=delDataLote).grid(row=2, columnspan=1, sticky=W+E)
        ttk.Button(loteframe, text="Cotizar").grid(row=3, columnspan=1, sticky=W+E)


        cotizframe=LabelFrame(self.p1, text="Cotización")
        cotizframe.grid(row=2, column=1, sticky=E+W, columnspan=1)
        self.treecotiz=ttk.Treeview(cotizframe, height=1, column=("#1","#2"))
        self.treecotiz.heading("#0", text="Cliente", anchor=CENTER)
        self.treecotiz.heading("#1", text="Cantidad", anchor=CENTER)
        self.treecotiz.heading("#2", text="Total", anchor=CENTER)
        ttk.Button(cotizframe, text="Exportar pdf").grid(row=0, column=3, sticky=W+E)

        self.treecotiz.grid(row=0, column=0)

    #========================PESTAÑA2==================================

        fijosframe=LabelFrame(self.p2, text="Cálculo de costos")
        fijosframe.grid(row=0, column=0)
        Label(fijosframe, text="Costos Fijos [$/mes]: ").grid(row=0, column=0)
        self.txtcostofijo=Entry(fijosframe,textvariable=costofijo)
        self.txtcostofijo.grid(row=0,column=1)
        Label(fijosframe, text="Número de Máquinas: ").grid(row=1, column=0)
        self.txtmaquinas=Entry(fijosframe,textvariable=maquinas)
        self.txtmaquinas.grid(row=1,column=1)
        Label(fijosframe, text="Horas a cubrir: ").grid(row=2, column=0)
        self.txthorascubiertas=Entry(fijosframe,textvariable=horascubiertas)
        self.txthorascubiertas.grid(row=2,column=1)
        Label(fijosframe, text="Factor de Mantenimiento: ").grid(row=3, column=0)
        self.txtfactormtto=Entry(fijosframe,textvariable=factormtto)
        self.txtfactormtto.grid(row=3,column=1)
        Label(fijosframe, text="Factor de error: ").grid(row=4, column=0)
        self.txtfactorerror=Entry(fijosframe,textvariable=factorerror)
        self.txtfactorerror.grid(row=4,column=1)
        Label(fijosframe, text="Depreciación: ").grid(row=5, column=0)
        self.txtdepreciacion=Entry(fijosframe,textvariable=depreciacion)
        self.txtdepreciacion.grid(row=5,column=1)
        ttk.Button(fijosframe, text="Eliminar", command=delDataCostos).grid(row=6, column=0,columnspan=2,sticky=W+E)
        ttk.Button(fijosframe, text="Actualizar", command=insDataCostos).grid(row=7, column=0,columnspan=2,sticky=W+E)



        materialframe=LabelFrame(self.p2, text="Costo de material")
        materialframe.grid(row=1, column=0,sticky=W+E+N+S)
        Label(materialframe, text="PLA+ [$/kg]:                   ").grid(row=0, column=0, sticky=W+E)
        self.txtpla=Entry(materialframe,textvariable=pla)
        self.txtpla.grid(row=0, column=1, sticky=W+E, columnspan=2)
        Label(materialframe, text="ABS [$/kg]:                    ").grid(row=1, column=0)
        self.txtabs=Entry(materialframe,textvariable=abs)
        self.txtabs.grid(row=1, column=1)
        Label(materialframe, text="PETG [$/kg]:                    ").grid(row=2, column=0)
        self.txtpetg=Entry(materialframe,textvariable=petg)
        self.txtpetg.grid(row=2, column=1)
        Label(materialframe, text="Técnico [$/kg]:                   ").grid(row=3, column=0)
        self.txttecnico=Entry(materialframe,textvariable=tecnico)
        self.txttecnico.grid(row=3, column=1)
        ttk.Button(materialframe, text="Eliminar",command=delDataMaterial).grid(row=4, column=0, columnspan=2, sticky=W+E)
        ttk.Button(materialframe, text="Actualizar",command=insDataMaterial).grid(row=5, column=0, columnspan=2, sticky=W+E)

        variableframe=LabelFrame(self.p2, text="Variables")
        variableframe.grid(row=0, column=1, sticky=W+E+N+S)
        self.treevariable=ttk.Treeview(variableframe, height=3, column=("#1","#2","#3","#4","#5","#6"))
        self.treevariable.heading("#0", text="Costo Fijo [mens]", anchor=CENTER)
        self.treevariable.column("#0",width=100)
        self.treevariable.heading("#1", text="N° Máquinas", anchor=CENTER)
        self.treevariable.column("#1",width=80)
        self.treevariable.heading("#2", text="F. Mtto", anchor=CENTER)
        self.treevariable.column("#2",width=50)
        self.treevariable.heading("#3", text="F. Error", anchor=CENTER)
        self.treevariable.column("#3",width=50)
        self.treevariable.heading("#4", text="Hrs. Cubiertas", anchor=CENTER)
        self.treevariable.column("#4",width=100)
        self.treevariable.heading("#5", text="Depreciación", anchor=CENTER)
        self.treevariable.column("#5",width=100)
        self.treevariable.heading("#6", text="Costo Hora Real", anchor=CENTER)
        self.treevariable.column("#6",width=130)
        self.treevariable.grid(row=0,column=0)
        backend.getDataCostos(self.treevariable)

        treematerialframe=LabelFrame(self.p2, text="Costo de material")
        treematerialframe.grid(row=1, column=1, sticky=N+S+E+W)
        self.treematerial=ttk.Treeview(treematerialframe, height=1, column=("#1","#2","#3"))
        self.treematerial.heading("#0", text="PLA+ [$/g]", anchor=CENTER)
        self.treematerial.heading("#1",text="ABS [$/g]", anchor=CENTER)
        self.treematerial.heading("#2", text="PETG [$/g]", anchor=CENTER)
        self.treematerial.heading("#3",text="Técnico [$/g]",anchor=CENTER)
        self.treematerial.grid(row=1,column=1)
        backend.getDataMaterial(self.treematerial)
if __name__=="__main__":
    window=Tk()
    app=Cotizador(window)
    window.mainloop()
