#!/usr/bin/env python
# -*- coding: utf-8 -*-

from backend import *
from index import *
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Image
from reportlab.lib.pagesizes import letter



class GeneradorCotizacion:
    def __init__(self,titulo,data,nombrePdf):
        self.titulo=titulo
        self.data=data
        self.nombrePdf=nombrePdf
        self.estilo=getSampleStyleSheet()


    def datosCliente(self,nombre,empresa,email):
        self.nombre=nombre
        self.empresa=empresa
        self.email=email
