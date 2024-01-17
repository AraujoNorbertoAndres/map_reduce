import funciones as f

texto = input('ingrese su texto texto que desea mapear: ')

diccionario = f.mapeo_reducido(texto)

f.crear_archivos(diccionario)

f.graficos(diccionario)

print('     -------------------------------')
print('     - archivos generado con exito -')
print('     -------------------------------')