import random
ids = []
palabras = []
significados = []
categorias = []
idiomas = []
fechas = []
observaciones = []
#------------------------------------------------#
#--|menu_principal_alimentador_de_diccionarios|--#
#------------------------------------------------#
while True:
    print("menu principal alimentador de diccionarios")
    print("1) crear palabra")
    print("2) editar palabra")
    print("3) eliminar palabra")
    print("4) buscar palabra")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-------------------#
    #--|crear_palabra|--#
    #-------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_palabra = 1
        else:
            id_palabra = ids[-1] + 1
        palabra = input("palabra: ")
        significado = input("significado: ")
        categoria = input("categoría: ")
        idioma = input("idioma: ")
        fecha = input("fecha: ")
        observacion = input("observación: ")
        ids.append(id_palabra)
        palabras.append(palabra)
        significados.append(significado)
        categorias.append(categoria)
        idiomas.append(idioma)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("palabra registrada correctamente.")
        print("id:", id_palabra)
    #--------------------#
    #--|editar_palabra|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar palabra")
            for i in range(len(ids)):
                print(f"{ids[i]} | {palabras[i]} | {significados[i]} | {categorias[i]} | {idiomas[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {palabras[posicion]} | {significados[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                palabras[posicion] = input("nueva palabra: ")
                significados[posicion] = input("nuevo significado: ")
                categorias[posicion] = input("nueva categoría: ")
                idiomas[posicion] = input("nuevo idioma: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_palabra|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar palabra")
            for i in range(len(ids)):
                print(f"{ids[i]} | {palabras[i]} | {significados[i]} | {categorias[i]} | {idiomas[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {palabras[posicion]} | {significados[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    palabras.pop(posicion)
                    significados.pop(posicion)
                    categorias.pop(posicion)
                    idiomas.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_palabra|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar palabra")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {palabras[posicion]} | {significados[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            español = 0
            ingles = 0
            otros = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {palabras[i]} | {significados[i]} | {categorias[i]} | {idiomas[i]} | {fechas[i]} | {observaciones[i]}")
                if idiomas[i].lower() == "español" or idiomas[i].lower() == "espanol":
                    español += 1
                elif idiomas[i].lower() == "inglés" or idiomas[i].lower() == "ingles":
                    ingles += 1
                else:
                    otros += 1
            print("estadísticas alimentador de diccionarios")
            print("cantidad de palabras:", len(ids))
            print("palabras en español:", español)
            print("palabras en inglés:", ingles)
            print("palabras en otros idiomas:", otros)
            print("primera palabra:", palabras[0])
            print("última palabra:", palabras[-1])
            posicion = random.randint(0, len(ids) - 1)
            print("simulación de alimentación del diccionario")
            print("palabra agregada al diccionario:")
            print(f"{ids[posicion]} | {palabras[posicion]} | {significados[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el alimentador de diccionarios.")
        break
    else:
        print("opción no válida.")