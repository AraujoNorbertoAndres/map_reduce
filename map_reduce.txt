import re
import pandas as pd
import matplotlib.pyplot as plt

# esta funcion toma una cadena de caracteres
# saca carecteres especiales y los numeros, luego los adiciona a una lista vacia
# a continuacion recorre nuevamente esta lista con las palabras que se le adiciono sacando aquellas palabras que tiene una longitud menor a 3 caracteres
# esta funcion no es necesario llamarla a menos que quieras una lista de palabras a secas

def mapeo(texto):
    palabras = []
    palabra = ''
    for i in texto:
        palabra += i
        if i == ' ':
            i.strip()
            palabra = re.sub(r'\W','',palabra)
            palabra = re.sub(r'\d','',palabra)
            palabras.append(palabra)
            palabra = ''
    for j in palabras:
        if len(j) <= 3:
            palabras.remove(j)
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
    plt.savefig("barras.jpg", bbox_inches='tight')
    plt.close('all')
    
    # 4: genera el grafico de torta
    valores = df['cantidad']
    etiquetas = df['palabras']
    fig, ax = plt.subplots()
    plt.pie(valores, labels=etiquetas ,labeldistance=1.1, autopct='%.0f%%')
    #plt.pie(valores, labels=etiquetas, autopct='%.2f%%')
    plt.savefig("torta.jpg", bbox_inches='tight')
    plt.close('all')

texto = input('ingrese su texto texto que desea mapear: ')

diccionario = mapeo_reducido(texto)


with open("diccionario_de_palabras.txt", "w") as file:
    for clave, valor  in diccionario.items():
        file.write("%s : %s\n" %(clave, valor))

graficos(diccionario)

print('-------------------------------')
print('- archivos generado con exito -')
print('-------------------------------')