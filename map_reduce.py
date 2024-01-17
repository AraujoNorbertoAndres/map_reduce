import funciones as f
import os
import time
#texto = ingreso()



estado = True
opcion = 0
inicio = 0
fin = 0
nombre_archivo = ''

while estado:

    try:
        print('     -------------------------------------   ')
        print('         1)ingreso de texto manual           ')
        print('         2)ingresar archivo                  ')
        print('     -------------------------------------   ')

        opcion = int(input('ingrese una opcion: '))
        if opcion == 1:
            texto = input('ingrese el texto que desea reducir: ')

            inicio = time.time()
            diccionario = f.mapeo_reducido(texto)

            f.crear_archivos(diccionario)

            f.graficos(diccionario)
            fin = time.time()

            print( '     -------------------------------    ' )
            print( '       archivos generado con exito      ' )
            print('        tiempo total: ',round(fin-inicio, 2))
            print( '     -------------------------------    ' )
            estado = False
            
        elif opcion == 2:
            archivo = str(f.ingreso())

            inicio = time.time()
            diccionario = f.mapeo_reducido(archivo)

            f.crear_archivos(diccionario)

            f.graficos(diccionario)
            fin = time.time()

            print( '     -------------------------------    ' )
            print( '       archivos generado con exito      ' )
            print('        tiempo total: ',round(fin-inicio, 2))
            print( '     -------------------------------    ' )
            estado = False

    except TypeError:
        print('     -------------------------------------   ')
        print('             opcion incorrecta')
        print('             intente nuevamente')
        print('     -------------------------------------   ')