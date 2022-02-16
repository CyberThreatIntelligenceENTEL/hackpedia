#!/usr/bin/python
#Creado y probado por Patricio Perez Carcamo--!
#Version 1, 15 feb 2022--!

import pandas as pd 
import sys
import os
import warnings



def checker():
	data = pd.ExcelFile(file)
	print("Hojas disponibles en el libro: ", data.sheet_names)
	hoja = input("\nDebe escoger una hoja para extraer sus datos: ")
	df = pd.read_excel(file, sheet_name=hoja)
	datos = df.loc[:,"URL"]
	for i in datos:
		r = os.system("""curl --keepalive-time 1 -s -o /dev/null -w '\n|> Code Status:%%{http_code} --> For Site %s' %s""" % (i, i))


file = sys.argv[1]
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
checker()
