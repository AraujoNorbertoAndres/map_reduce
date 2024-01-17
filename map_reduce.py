import funciones as f


texto = input('ingrese su texto texto que desea mapear: ')

diccionario = f.mapeo_reducido(texto)


f.archivos(diccionario)

#with open("diccionario_de_palabras.txt", "w") as file:
#    for clave, valor  in diccionario.items():
#        file.write("%s : %s\n" %(clave, valor))


f.graficos(diccionario)

print('     -------------------------------')
print('     - archivos generado con exito -')
print('     -------------------------------')