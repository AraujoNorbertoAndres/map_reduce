import re
import pandas as pd
import matplotlib.pyplot as plt
import os

# esta funcion toma una cadena de caracteres
# saca carecteres especiales y los numeros, luego los adiciona a una lista vacia
# a continuacion recorre nuevamente esta lista con las palabras que se le adiciono sacando aquellas palabras que tiene una longitud menor a 3 caracteres
# esta funcion no es necesario llamarla a menos que quieras una lista de palabras a secas

def mapeo(texto):
    palabras = []
    palabra = ''
    for i in texto:
        palabra += i
        if i == ' ' or i == '\n':
            palabra = re.sub(r'\W','',palabra)
            palabra = re.sub(r'\d','',palabra)
            palabras.append(palabra)
            palabra = ''

    lista_auxiliar = []
    for l in palabras:
        if len(l) > 3:
            lista_auxiliar.append(l)

    palabras = lista_auxiliar

    return palabras

# esta funcion contabiliza las palabras repetidas y las agrega a un diccionario para su posterior analisis
# se llama a la funcion mapeo()x

def mapeo_reducido(texto):
    contador = 1
    diccionario = {}
    lista = mapeo(texto)
    for k in lista:
        for l in lista:
            if k == l:
                contador += 1
        diccionario.update({k: contador})
        contador = 0
    return diccionario

def graficos(diccionario):
    # 1: genera el dataFrame para pdoer trabajar 
    df = pd.DataFrame(list(diccionario.items()), columns=["palabras", "cantidad"])
    
    # 2: en esta seccion se va generar el df para el grafico de barras 
    # se ordenara de mayor a menor
    # luego seleccionara las primeras filas
    df1 = df.sort_values(by=['cantidad'],ascending=False)
    df2 = df1.head(6)
    
    # 3:genera el grafico de barras 
    x = df2['palabras']
    y = df2['cantidad']
    fig, ax = plt.subplots()
    plt.bar(x, y)
    ax.tick_params(axis='x', rotation=90)
    #plt.figure(figsize=(10,6))
    plt.savefig("barras.jpg", bbox_inches='tight')
    plt.close('all')
    
    # 4: genera el grafico de torta
    valores = df['cantidad']
    etiquetas = df['palabras']
    fig, ax = plt.subplots()
    plt.pie(valores, labels=etiquetas ,labeldistance=1.1, autopct='%.0f%%')
    #plt.figure(figsize=(10,6))
    #plt.pie(valores, labels=etiquetas, autopct='%.2f%%')
    plt.savefig("torta.jpg", bbox_inches='tight')
    plt.close('all')

def crear_archivos(diccionario):
    with open("diccionario_de_palabras.txt", "w") as file:
        for clave, valor  in diccionario.items():
            file.write("%s : %s\n" %(clave, valor))
    
# esta funcion lee un archivo para luego devolverlo como texto
def mapeo_de_archivo(nombre):
    texto = ''

    with open(nombre,'r') as file:
        texto = file.readlines()

    palabra = ''
    palabras = []

    for i in texto:
        for j in i:
            palabra += j
            if j == ' ' or j == '\n':
                palabra = re.sub(r'\W','',palabra)
                palabra = re.sub(r'\d','',palabra)
                palabras.append(palabra)
                palabra = ''

    texto = []
    for l in palabras:
        if len(l) > 3:
            texto.append(l)


    return texto




# desde aca se maneja la funcion lectura_archivo()
# no es necesario llamar a dicha
def ingreso():
    nombre = input('ingrese el nombre del archivo que desea analizar: ')
    texto = mapeo_de_archivo(nombre)
    return texto

