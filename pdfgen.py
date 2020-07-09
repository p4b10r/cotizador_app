#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas

c=canvas.Canvas("pdfgen.pdf")

c.drawImage("3DLUXimage.png",10,750,100,100, mask="auto")

c.drawString(500,800, "vamolopibe")


c.save()
