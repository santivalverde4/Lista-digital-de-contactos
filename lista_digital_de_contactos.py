#__________________________________LISTA DIGITAL DE CONTACTOS____________________________________

#___________________________________________MÓDULOS______________________________________________                                                                                          
import os
import re
import webbrowser
#____________________________________FUNCIONES ADICIONALES________________________________________
#Estas están hechas para agilizar y facilitar la funcionalidad del programa

#Función que determina si existe un área o no
#Entradas: la lista áreas y el área de teléfono a consultar
#Salidas: True si está en la lista, de lo contrario retorna False
def obtener_datos_area(areas, area_telefono):
    for elemento in areas:
        if elemento[0] == area_telefono:
            return True, elemento
    return False, None

#Función que da el nombre de cierto área
#Entradas: lista de áreas y el teléfono del área
#Salidas: el nombre del área
def nombre_area(areas, area_telefono):
    for elemento in areas:
        if elemento[0] == area_telefono:
            return elemento[1]

#Función que determina si existe un teléfono o no
#Entradas: la lista contactos y el teléfono a consultar
#Salidas: True si está en la lista, de lo contrario retorna False
def obtener_datos_telefono(contactos, telefono):
    for elemento in contactos:
        if elemento[0] == telefono:
            return True, elemento
    return False, tuple()

#Función que valida si un correo es válido o no
#Entradas: un correo
#Salidas: True si el correo es válido, de lo contrario retorna False
def es_correo_valido(correo):
    partes = correo.split('@')
    if len(partes) == 2 and partes[0] != "" and partes[1] != "":
        return True
    else:
        return False

#Función que crea una fecha de nacimiento
#Entradas: un string 
#Salidas: la fecha, si está incompleta da 0, si solo falta el año retorna la fecha y en el año 0000
def fecha_de_nacimiento(fecha_str):
    if not fecha_str:
        return "0"
    partes_fecha = fecha_str.split("/")
    if len(partes_fecha) != 3:
        return "0"
    dia = partes_fecha[0] if partes_fecha[0] else "00"
    mes = partes_fecha[1] if partes_fecha[1] else "00"
    año = partes_fecha[2] if partes_fecha[2] else "0000"
    return f"{dia}/{mes}/{año}"

#__________________________________________CRUD ÁREAS____________________________________________                       
#En este bloque se encuentran todas posibles acciones con respecto a las áreas

#Función que se encarga de las opciones para las áreas
#Entradas: recibe un numero en el input
#Salidas: redirección del usuario hacia la función a ejercer en el bloque
def registrar_areas(areas):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                            REGISTRAR ÁREAS\n")
        print(" 1. Agregar áreas")
        print(" 2. Consultar áreas")
        print(" 3. Modificar áreas")
        print(" 4. Eliminar áreas")
        print(" 0. Fin")
        opcion = input("    OPCIÓN ")              
        match opcion: 
            case "1":
                agregar_areas(areas)
            case "2":
                consultar_areas(areas)
            case "3":
                modificar_areas(areas)
            case "4":
                eliminar_areas(areas)  
            case "0":
                return
            case _: 
                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#Función que añade un área
#Entradas: un área con su nombre
#Salidas: se añade un área a la lista de áreas
def agregar_areas(areas):
        while True:
            os.system("cls")
            print("\n\n\n-------------------------------------------------------------------------------")
            print("                     LISTA DIGITAL DE CONTACTOS\n")
            print("                     REGISTRAR ÁREAS: AGREGAR ÁREAS\n")
            while True:
                try:
                    area_telefono = input("Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_telefono)
                        if existe_area:
                            input("ESTA ÁREA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR ")
                        else:
                            break
                    else:
                        input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")    
            while True:
                nombre_del_area = input("Nombre del área: ") 
                if len(nombre_del_area) >= 1 and len(nombre_del_area) <= 40:
                    break
                else:
                    input("EL DATO DEBE TENER ENTRE 1 Y 40 CARACTERES ")
            while True:
                try:
                    opcion = input("OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                    if opcion == "A":
                        areas.append((area_telefono, nombre_del_area))
                        break
                    if opcion == "C":
                        print("Operación cancelada")
                        break
                    else:
                        input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                except:
                    input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#Función que consulta si un área existe o no
#Entradas: un área
#Salidas: si el área existe da la opción aceptar, de lo contrario muestra mensaje de que no existe           
def consultar_areas(areas):
    while True:
            os.system("cls")
            print("\n\n\n-------------------------------------------------------------------------------")
            print("                     LISTA DIGITAL DE CONTACTOS\n")
            print("                     REGISTRAR ÁREAS: CONSULTAR ÁREAS\n")
            while True:
                try:
                    area_telefono = input("Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        break
                    else:
                        input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")      
            while True:        
                nombre_del_area = input("Nombre del área: ")
                existe_area, nombre = obtener_datos_area(areas, area_telefono)
                if existe_area == True and nombre_del_area == nombre[1]:
                    opcion = input("OPCIÓN      <A> ACEPTAR ")
                    if opcion == "A":
                        break
                    else:                            
                        input("ESTA OPCIÓN NO ES VÁLIDA")    
                else:
                    input("ESTA AREA NO ESTA REGISTRADA, NO SE PUEDE CONSULTAR")
                    break

#Función que permite modificar el nombre de área
#Entradas: una área
#Salidas: cambia el nombre anterior del área o no
def modificar_areas(areas): #AQUI VER QUE PUEDO PONER DE VDD PARA QUE ESO FUNCIONE
    while True:
            os.system("cls")
            print("\n\n\n-------------------------------------------------------------------------------")
            print("                     LISTA DIGITAL DE CONTACTOS\n")
            print("                     REGISTRAR ÁREAS: MODIFICAR ÁREAS\n")
            # modificar área
            while True:
                try:
                    area_telefono = input("Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, indice_area = obtener_datos_area(areas, area_telefono)
                        if not existe_area:
                            input("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE MODIFICAR")
                        else:
                            print("Nombre actual del área: ", indice_area[1])
                            nuevo_nombre = input("\nNuevo nombre del área: ")
                            opcion = input("OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                            if opcion == "A":
                                eliminar = areas.index(indice_area)
                                del areas[eliminar]
                                areas.append((area_telefono, nuevo_nombre),)
                                break
                            if opcion == "C":
                                break
                            else:
                                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                    else:
                        input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")

#Función que elimina áreas
#Entradas: una área a eliminar
#Salidas: se elimina el área de las áreas registradas o no
def eliminar_areas(areas):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     REGISTRAR ÁREAS: ELIMINAR ÁREAS\n")
        while True:
            try: 
                area_telefono = input("Área: ")
                if area_telefono == "C":
                    return
                area_telefono = int(area_telefono)
                if area_telefono >= 1 and area_telefono <= 999:    
                    break
                else:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
            except:
                input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
        while True:
            os.system("cls")
            print("\n\n\n-------------------------------------------------------------------------------")
            print("                     LISTA DIGITAL DE CONTACTOS\n")
            print("                     REGISTRAR ÁREAS: ELIMINAR ÁREAS\n")
            print(areas)
            area_encontrada = False
            for datos_area in areas:
                if area_telefono == datos_area[0]:
                    area_encontrada = True
                    print("Área: ", datos_area[0])
                    print("Nombre del área: ", datos_area[1])
                    while True:
                        try:
                            opcion = input("OPCIÓN      <A>ACEPTAR  <C>CANCELAR ")
                            if opcion == "A":
                                existen_contactos = False
                                for datos_contacto in contactos:
                                    if area_telefono == datos_contacto[0]:
                                        existen_contactos = True
                                        input("EN ESTA ÁREA HAY CONTACTOS REGISTRADOS, NO SE PUEDE ELIMINAR")
                                        break
                                if existen_contactos == False:
                                    confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO)")
                                    if confirmacion == "SI":
                                        del areas[areas.index(datos_area)]
                                        break
                                    if confirmacion == "NO":
                                        break
                                    else:
                                        input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")
                            if opcion == "C":
                                break
                            else:
                                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")
                        except:
                            input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")
                if not area_encontrada:
                    input("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE ELIMINAR. ")
            break

#_______________________________CONFIGURACIÓN DE LISTA DE CONTACTOS______________________________

#Función que genera un área y tipo de teléfono por omisión (default)
#Entradas: un área y tipo de teléfono
#Salidas: asignación a los valores por omisión
def configuracion_lista_contactos(areas):
    global area_por_omision
    global tipo_telefono_por_omision
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     CONFIGURACIÓN DE LA LISTA DE CONTACTOS\n")
        while True:
            try:
                area_telefono = int(input("Área por omisión: "))
                if area_telefono > 0 and area_telefono < 1000:
                    existe_area, nombre_area_ = obtener_datos_area(areas, area_telefono)
                    if existe_area:
                        print(nombre_area(areas, area_telefono))
                        break
                    else:
                        input("ESTA AREA NO ESTA REGISTRADA, NO SE PUEDE SELECCIONAR")
                else:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
            except:
                input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")

        while True:
            try:
                tipo_telefono = input("Tipo de teléfono por omisión: (M: Móvil, C: Casa, T: Trabajo, O: Otro) ")
                if tipo_telefono in TIPOS_TELEFONO:
                    break
                else:
                    input("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR ")
            except:
                input("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR ")
        while True:
            try: 
                opcion = input("OPCIÓN       <A> ACEPTAR       <C> CANCELAR ")
                if opcion == "A":
                    area_por_omision = area_telefono
                    tipo_telefono_por_omision = nombre_area
                    break
                if opcion == "C":
                    return
                else:
                    input("ESTA OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
            except:
                input("ESTA OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#_________________________________________CRUD CONTACTOS_________________________________________
#En este bloque se encuentran las posibles acciones con respecto a los contactos

#Función que ejecuta el menú de registrar contactos
#Entradas: opción a elegir
#Salidas: redirección del usuario hacia la función a ejercer en el bloque
def registrar_contactos(contactos, areas):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                            REGISTRAR CONTACTOS\n")
        print(" 1. Agregar contactos")
        print(" 2. Consultar contactos")
        print(" 3. Modificar contactos")
        print(" 4. Eliminar contactos")
        print(" 0. Fin")
        opcion = input("    OPCIÓN ")              
        match opcion: 
            case "1":
                agregar_contactos(contactos, areas)
            case "2":
                consultar_contactos(contactos)
            case "3":
                modificar_contactos(contactos)
            case "4":
                eliminar_contactos(contactos)  
            case "0":
                return
            case _: 
                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#Función para agregar contactos
#Entradas: telefono, area, nombre, correo, direccion, nacimiento, pasatiempos, notas del usuario a añadir
#Salidas: adición del contacto o no a la lista

""""""""""""""""""""""""""""""""""""""""""""""""

#esta funcion se encarga de verificar el tamaño de un string
#entrada: un string, dos int
#salida: un booleano
def verificar_string(string, de, hasta):
    if len(string) >= de and len(string) <= hasta:
        return True
    else:
        return False
    
#esta funcion se encarga de verificar si un correo es valido o no. False no es valido, True es valido.
#entrada: un string
#salida: un booleano
def verificar_correo(correo):
    for elemento in correo:
        if elemento == " " or "@" not in correo:
            return False
    if correo.split("@")[0] == "" or correo.split("@")[1] == "":
        return False
    return True

#esta funcion se encarga de verificar si la fecha es valida o no. False no es valida, true si lo es.
#entrada: un string
#salida: un booleano
def fecha_nacimiento(fecha_str):
    #verificamos si el año es 0000 y hacer que funcione cuando lo metamos dentro de datetime
    contador = -1
    año = ""
    while contador > -5:
        año += fecha_str[contador]
        contador -= 1
    if año == "0000":
        fecha_str = fecha_str[:5] + "/2024"
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        return True
    except:
        return False

#--------------------------------------------------------------------

#CASO agregar contactos
#Entradas: contactos y areas
# S: Lista de contactos modificada
def agregar_contactos(contactos, areas): #hacer pruebas
    #revisar telefono
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     REGISTRAR CONTACTOS: AGREGAR\n")
        global area_por_omision
        global tipo_telefono_por_omision
        try: 
            telefono = input("Teléfono: ")
            if telefono == "C":
                return
            if verificar_string(telefono, 5, 12) == False:
                input("TELÉFONO DEBE DE SER UN NÚMERO NATURAL ENTRE 5 Y 12 DÍGITOS ")
                continue
            else:
                telefono = int(telefono)
        except:
            input("TELÉFONO DEBE DE SER UN NÚMERO NATURAL ENTRE 5 Y 12 DÍGITOS ")
            continue

        #revisar area
        while True:
            try:
                area = input("Área: ")
                if area == "":
                    area = area_por_omision
                area = int(area)
                if area >= 1 and area <= 999:
                    validar = 0
                    for elemento in range(len(areas)):
                        if area == areas[elemento][0]:
                            validar = 1
                            break
                    if validar == 0:
                        input("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE SELECCIONAR ")
                        continue
                else:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                    continue
            except:
                input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                continue

            #revisar telefono
            while True:
                registrado = 0
                for elementos in contactos:
                    if [area, telefono] == [elementos[0], elementos[1]]:
                        input("ESTE TELÉFONO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR ")
                        registrado = 1
                        break
                if registrado == 1:
                    break
                else:
                    #revisar demás datos
                    #tipo telefono
                    while True:
                        tipo_telefono = input("Tipo de teléfono (M, C, T, O): ")
                        if tipo_telefono == "":
                            tipo_telefono = tipo_telefono_por_omision
                        if tipo_telefono in TIPOS_TELEFONO:
                            break
                        else:
                            input("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR ")
                    #nombre del contacto
                    while True:
                        nombre = input("Nombre contacto: ")
                        if verificar_string(nombre, 1, 50) == False:
                            input("EL NOMBRE DEL CONTACTO DEBE DE SER ENTRE 1 A 50 CARACTERES ")
                        else:
                            break
                    #correo
                    while True:
                        correo = input("Correo electrónico: ")
                        if verificar_correo(correo) == True:
                            break
                        else:
                            input("EL CORREO ELECTRÓNICO ES INVALIDO ")
                    #direccion
                    while True:
                        direccion = input ("Dirección física: ")
                        if verificar_string(direccion, 0, 80) == False:
                            input("DIRECCIÓN FISICA DEBE DE SER ENTRE 0 A 80 CARACTERES ")
                        else:
                            break
                    #fecha de nacimiento
                    while True:
                        fecha = input ("Fecha de nacimiento: ")
                        no_ocurre = 0
                        if fecha.count("/") == 2: 
                            for elemento in fecha:
                                if elemento != "/" and elemento not in "1234567890":
                                    no_ocurre = 1
                            if no_ocurre != 0:
                                fecha = 0
                            else:
                                if fecha_nacimiento(fecha) == False:
                                    input("LA FECHA DE NACIMIENTO DEBE SER UNA FECHA VÁLIDA ")
                                    continue
                                else:
                                    break
                        else:
                            fecha = 0
                        break
                    #pasatiempos
                    while True:
                        pasatiempos = input ("Pasatiempos: ")
                        if verificar_string(pasatiempos, 0, 60) == False:
                            input("PASATIEMPOS DEBE DE SER ENTRE 0 Y 60 CARACTERES ")
                        else:
                            break
                    #Notas
                    while True:
                        notas = input("Notas: ")
                        if verificar_string(notas, 0, 60) == False:
                            input("NOTAS DEBE DE SER ENTRE 0 Y 60 CARACTERES ")
                        else:
                            break
                    #aceptar o cancelar
                    while True:
                        opcion = input("OPCIÓN      <A>ACEPTAR  <C>CANCELAR ")
                        if opcion == "A":
                            contactos += [[telefono, area, tipo_telefono, nombre, correo, direccion, fecha, pasatiempos, notas]]
                            break
                        if opcion == "C":
                            break
                        if opcion != "A" and opcion != "C":
                            input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")
                    break
            break

""""""""""""""""""""""""""""""""""""""""""""""""

#Función que busca si un contacto ya ha sido registrado
#Entradas: un número de teléfono y un área
#Salidas: Si existe, los datos del contacto, de lo contrario dice que no existe
def consultar_contactos(contactos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     REGISTRAR CONTACTOS: CONSULTAR\n")
        global area_por_omision
        while True:
            try: 
                telefono = input("Teléfono: ")
                if telefono == "C":
                    return
                if len(telefono) >= 5 and len(telefono) <= 12:
                    telefono = int(telefono)
                    break
                else:
                    input("EL TELEFONO DEBE SER ENTRE 5 Y 12 DÍGITOS")
            except:
                input("EL TELEFONO DEBE SER ENTRE 5 Y 12 DÍGITOS")
        while True:
            try:
                area_telefono = input("Área: ")
                if area_telefono == "":
                    area_telefono = area_por_omision
                else:
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, datos_area = obtener_datos_area(areas, area_telefono)
                        if existe_area == False:
                            input("ESTA AREA NO ESTA REGISTRADA, NO SE PUEDE BUSCAR")
                        else:
                            break
                    else:
                        input("ÁREA DEBE SER UN NUMERO ENTRE 1 Y 999")
            except:
                input("ÁREA DEBE SER UN NUMERO ENTRE 1 Y 999")
        
        encontrado = False
        for elementos in contactos:
            if telefono == elementos[0]:
                os.system("cls")
                print("\n\n\n-------------------------------------------------------------------------------")
                print("                     LISTA DIGITÁL DE CONTACTOS\n")
                print("                     REGISTRAR CONTACTOS: CONSULTAR\n")
                print("Teléfono: ", elementos[0])
                print("Área: ", elementos[1])
                print("Tipo de teléfono: ", elementos[2])
                print("Nombre del contacto: ", elementos[3])
                print("Correo electrónico: ", elementos[4])
                print("Dirección física: ", elementos[5])
                print("Fecha de nacimiento: ", elementos[6])
                print("Pasatiempos: ", elementos[7])
                print("Notas: ", elementos[8], "\n")
                encontrado = True
                while True:
                    try:
                        opcion = input("OPCIÓN     <A>ACEPTAR ")
                        if opcion == "A":
                            break
                        else:
                            input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")
                    except:
                        input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")
        if not encontrado:
                input("ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE CONSULTAR")

#Función que modifica a un contacto
#Entradas: nuevos datos
#Salidas: reasignación de datos a un contacto
def modificar_contactos(contactos):
     while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     REGISTRAR CONTACTOS: MODIFICAR\n")
        global area_por_omision
        #ingresa el telefono
        while True:
            try: 
                telefono = input("Teléfono: ")
                if telefono == "C":
                    return
                telefono = int(telefono)
                break
            except:
                input("INGRESE UN NÚMERO DE TELÉFONO VÁLIDO ")
        #ingresa el area
        while True:
            try:
                area = input("Área: ")
                if area == "":
                    area = area_por_omision
                area = int(area)
                break
            except:
                input("INGRESE UNA ÁREA VALIDA ")
        #verifica que exista el telefono
        existe = 0
        for elementos in contactos:
            if area == elementos [1] and telefono == elementos[0]:
                existe = 1
                break
        if existe == 0:
            input("ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR ")
            continue
        else:
            os.system("cls")
            print("\n\n\n-------------------------------------------------------------------------------")
            print("                     REGISTRAR CONTACTOS: MODIFICAR\n")
            print("Teléfono: ", elementos[0])
            print("Área: ", elementos[1])
            #muestra los datos actuales, pide los datos nuevos y los verifica

            while True: #verifica tipo telefono
                print("Tipo de teléfono (M,C,T,O): ", elementos[2], end = "")   
                tipo_telefono = input("        ")
                if tipo_telefono == "":
                    tipo_telefono = elementos[2]
                    break
                else:
                    if tipo_telefono in TIPOS_TELEFONO:
                        break
                    else:
                        input("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR ")
            while True: #verifica el nombre del contacto
                print("Nombre del contacto: ", elementos[3], end = "")
                nombre_contacto = input("        ")
                if nombre_contacto == "":
                    nombre_contacto = elementos[3]
                    break
                else:
                    if verificar_string(nombre_contacto, 1, 50) == False:
                        input("EL NOMBRE DEL CONTACTO DEBE DE SER ENTRE 1 A 50 CARACTERES ")
                    else:
                        break
            while True: # verifica el correo
                print("Correo electrónico: ", elementos[4], end = "")
                correo = input("        ")
                if correo == "":
                    correo = elementos[4]
                    break
                else:
                    if verificar_correo(correo) == False:
                        input("EL CORREO ELECTRÓNICO ES INVALIDO ")
                    else:
                        break
            while True: #verifica la direccion
                print("Dirección física: ", elementos[5], end = "")
                direccion = input("        ")
                if direccion == "":
                    direccion = elementos[5]
                    break
                else:
                    if verificar_string(direccion, 0, 80) == False:
                        input("DIRECCIÓN FISICA DEBE DE SER ENTRE 0 A 80 CARACTERES ")
                    else:
                        break
            while True: #verifica la fecha de nacimiento
                print("Fecha de nacimiento: ", elementos[6], end = "")
                fecha = input("        ")
                if fecha == "":
                    fecha = elementos[6]
                    break
                else:
                    no_ocurre = 0
                    if fecha.count("/") == 2: 
                        for elemento in fecha:
                            if elemento != "/" and elemento not in "1234567890":
                                no_ocurre = 1
                        if no_ocurre != 0:
                            fecha = 0
                        else:
                            if fecha_nacimiento(fecha) == False:
                                input("LA FECHA DE NACIMIENTO DEBE SER UNA FECHA VÁLIDA ")
                                continue
                            else:
                                break
                    else:
                        fecha = 0
                    break
            while True: #verifica los pasatiempos
                print("Pasatiempos: ", elementos[7], end = "")
                pasatiempos = input("        ")
                if pasatiempos == "":
                    pasatiempos = elementos[7]
                    break
                else:
                    if verificar_string(pasatiempos, 0, 60) == False:
                        input("PASATIEMPOS DEBE DE SER ENTRE 0 Y 60 CARACTERES ")
                    else:
                        break
            while True: #verifica las notas
                print("Notas: ", elementos[8], end = "")
                notas = input("        ")
                if notas == "":
                    notas = elementos[8]
                    break
                else:
                    if verificar_string(notas, 0, 60) == False:
                        input("NOTAS DEBE DE SER ENTRE 0 Y 60 CARACTERES ")
                    else:
                        break
            while True: #selecciona alguna opcion
                opcion = input("OPCIÓN      <A>ACEPTAR  <C>CANCELAR ")
                if opcion == "A":
                    contactos += [[telefono, area, tipo_telefono, nombre_contacto, correo, direccion, fecha, pasatiempos, notas]]
                    del contactos [contactos.index(elementos)]
                    break
                if opcion == "C":
                    break
                if opcion != "A" and opcion != "C":
                    input("OPCIÓN NO ES PERMITIDA. DAR <INTRO> ")

#Función que elimina contactos
#Entradas: un teléfono
#Salidas: eliminación de un contacto o no
def eliminar_contactos(contactos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     REGISTRAR CONTACTOS: ELIMINAR\n")
        global area_por_omision
        while True:
            try: 
                telefono = input("Teléfono: ")
                if telefono == "C":
                    return
                if len(telefono) >= 5 and len(telefono) <= 12:
                    telefono = int(telefono)
                    break
                else:
                    input("NÚMERO DE TELÉFONO DEBE SER ENTRE 5 Y 12 NÚMEROS")
            except:
                input("INGRESE UN NÚMERO DE TELÉFONO VÁLIDO ")
            
        for elementos in contactos:
                if telefono == elementos[0]:
                    os.system("cls")
                    print("\n\n\n-------------------------------------------------------------------------------")
                    print("                     LISTA DIGITAL DE CONTACTOS\n")
                    print("                     REGISTRAR CONTACTOS: ELIMINAR\n")
                    print("Teléfono: ", elementos[0])
                    print("Área: ", elementos[1])
                    print("Tipo de teléfono: ", elementos[2])
                    print("Nombre del contacto: ", elementos[3])
                    print("Correo electrónico: ", elementos[4])
                    print("Dirección física: ", elementos[5])
                    print("Fecha de nacimiento: ", elementos[6])
                    print("Pasatiempos: ", elementos[7])
                    print("Notas: ", elementos[8], "\n")
                    while True:
                        try:
                            opcion1 = input("OPCIÓN      <A>ACEPTAR  <C>CANCELAR ")
                            if opcion1 == "A":
                                while True:
                                    try:
                                        confirmacion = input("¿ESTÁ SEGURO DE QUERER ELIMINAR ESTE CONTACTO?   <A>ACEPTAR  <C>CANCELAR ")
                                        if confirmacion == "A":
                                            del contactos[contactos.index(elementos)]
                                            break
                                        if confirmacion == "C":
                                            break
                                        else:
                                            input("INGRESE UNA OPCIÓN VALIDA ")
                                    except:
                                        input("INGRESE UNA OPCIÓN VALIDA ")
                                break
                            if opcion1 == "C":
                                break
                            else:
                                input("INGRESE UNA OPCIÓN VALIDA ")
                        except:
                            input("INGRESE UNA OPCIÓN VALIDA ")
    
#___________________________________CRUD GRUPOS DE CONTACTOS_____________________________________
#En este bloque se encuentran las posibles acciones hacia los grupos de contactos

#Función que ejecuta el menú para administrar las opciones a los grupos
#Entradas: la opción a elegir
#Salidas: redirección del usuario hacia la función a ejercer en el bloque
def administrar_grupos(contactos, areas, grupos, contactos_por_grupos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ADMINISTAR GRUPOS DE CONTACTOS\n")
        print(" 1. Agregar grupos")
        print(" 2. Agregar contactos a los grupos")
        print(" 3. Modificar grupos")
        print(" 4. Eliminar grupos")
        print(" 5. Eliminar contactos de los grupos")
        print(" 0. Fin")
        opcion = input("    OPCIÓN ")              
        match opcion: 
            case "1":
                agregar_grupos(grupos, contactos_por_grupos)
            case "2":
                agregar_contactos_grupos(grupos, contactos_por_grupos, areas, contactos)
            case "3":
                modificar_grupos(grupos)
            case "4":
                eliminar_grupos(grupos, contactos_por_grupos)
            case "5":
                eliminar_contactos_grupos(grupos, contactos_por_grupos, contactos)
            case "0":
                return
            case _:
                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#Función que agrega nuevos grupos
#Entradas: nombre del nuevo grupo
#Salidas: Adición de nuevo grupo a las listas
def agregar_grupos(grupos, contactos_por_grupos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ADMINISTAR GRUPOS DE CONTACTOS: AGREGAR GRUPOS\n")
        while True:
            try:
                nombre_grupo = input("Nombre del grupo:     ")
                if nombre_grupo == "C":
                    return
                if len(nombre_grupo) > 40 or nombre_grupo == "":
                    input("NOMBRE DEL GRUPO DEBE SER ENTRE 1 Y 40 CARÁCTERES")
                else:
                    if nombre_grupo in grupos:
                        input("ESTE GRUPO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
                    else:
                        try:
                            opcion = input("OPCIÓN     <A>ACEPTAR   <C>CANCELAR")
                            if opcion == "A":
                                grupos.append(nombre_grupo)
                                contactos_por_grupos.append([])
                                break
                            if opcion == "C":
                                break
                            else:
                                 input("INGRESE UNA OPCIÓN VALIDA ")
                        except:
                             input("INGRESE UNA OPCIÓN VALIDA ")
            except:
                input("NOMBRE DEL GRUPO DEBE SER ENTRE 1 Y 40 CARÁCTERES")

#Función que agrega contactos a los grupos
#Entradas: un contacto y un grupo
#Salidas: adición del contacto a dicho grupo
def agregar_contactos_grupos(grupos, contactos_por_grupos, areas, contactos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ADMINISTRAR GRUPOS DE CONTACTOS: AGREGAR CONTACTOS A GRUPOS\n")
        while True:
            try:
                nombre_grupo = input("Nombre del grupo:     ")
                if nombre_grupo == "C":
                    return
                if len(nombre_grupo) > 40 or nombre_grupo == "":
                    input("EL NOMBRE DEL GRUPO DEBE TENER ENTRE 1 Y 40 CARACTERES")
                else:
                    if nombre_grupo not in grupos:
                        input("ESTE GRUPO NO EXISTE, NO SE PUEDEN AGREGAR CONTACTOS")
                    else:
                        break
            except:
                input("EL NOMBRE DEL GRUPO DEBE TENER ENTRE 1 Y 40 CARACTERES")

        while True:
            try:
                telefono = input("Teléfono: ")
                if telefono == "C":
                    return
                if len(telefono) >= 5 and len(telefono) <= 12:
                    telefono = int(telefono)
                    existe_telefono, info_telefono = obtener_datos_telefono(contactos, telefono)
                    if not existe_telefono:
                        input("ESTE CONTACTO NO EXISTE, NO SE PUEDE AGREGAR AL GRUPO")
                    else:
                        for elemento in contactos:
                            if elemento[0] == telefono:
                                print("Área: ", elemento[1])
                                for correspondencia in areas:
                                    if correspondencia[0] == elemento[1]:
                                        print("Nombre del área: ", correspondencia[1])
                                        print("Nombre del contacto", elemento[3])
                                        while True:
                                            try:
                                                opcion = input("OPCIÓN  <A> ACEPTAR  <C> CANCELAR ")
                                                if opcion == "A":
                                                    for nombre in grupos:
                                                        if nombre == nombre_grupo:
                                                            indice = grupos.index(nombre)
                                                            contactos_por_grupos[indice].append((telefono, elemento[1]))
                                                            print("Contacto agregado correctamente al grupo", nombre_grupo)
                                                            break
                                                if opcion == "C":
                                                    break
                                                else:
                                                    input("ESTA OPCIÓN NO ES VÁLIDA")
                                            except:
                                                input("ESTA OPCIÓN NO ES VÁLIDA")
                else:
                    input("ESTE NÚMERO DE TELÉFONO NO ES VÁLIDO")
            except:
                input("ESTE NÚMERO DE TELÉFONO NO ES VÁLIDO")

#Función que modifica el nombre de un grupo
#Entradas: el nombre de un grupo
#Salidas: modificación del nombre del grupo
def modificar_grupos(grupos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ADMINISTRAR GRUPOS DE CONTACTOS: MODIFICAR GRUPOS\n")
        while True:
            try:
                nombre_grupo = input("Nombre del grupo: ")
                if nombre_grupo == "C":
                    return
                if nombre_grupo not in grupos:
                    input("EL GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")
                else:
                    os.system("cls")
                    print("\n\n\n-------------------------------------------------------------------------------")
                    print("                     LISTA DIGITAL DE CONTACTOS\n")
                    print("                     ADMINISTRAR GRUPOS DE CONTACTOS: MODIFICAR GRUPOS\n")
                    while True:
                        try:
                            print("Nombre del grupo: ", nombre_grupo, end = "    ")
                            nuevo_nombre_grupo = input("Nuevo nombre del grupo: ")
                            if len(nuevo_nombre_grupo) > 40:
                                input("EL NOMBRE DEL GRUPO DEBE TENER MENOS DE 40 CARACTERES")
                            else:
                                opcion = input("OPCIÓN <A> ACEPTAR  <C> CANCELAR: ").upper()
                                if opcion == "A":
                                    grupos[grupos.index(nombre_grupo)] = nuevo_nombre_grupo  
                                    os.system("cls")  # Limpiar la pantalla
                                    print("\n\n\n-------------------------------------------------------------------------------")
                                    print("                     LISTA DIGITAL DE CONTACTOS\n")
                                    print("                     ADMINISTRAR GRUPOS DE CONTACTOS: MODIFICAR GRUPOS\n")
                                    break
                                if opcion == "C":
                                    break
                                else:
                                    input("OPCIÓN INVÁLIDA, INTENTE DE NUEVO")
                        except:
                            input("ERROR AL MODIFICAR EL NOMBRE DEL GRUPO, INTENTE DE NUEVO")
            except:
                input("INGRESE UN NOMBRE VÁLIDO")
         
#Función que elimina grupos
#Entradas: grupos a eliminar
#Salidas: eliminación de grupos de la lista
def eliminar_grupos(grupos, contactos_por_grupos):        
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ADMINISTRAR GRUPOS DE CONTACTOS: ELIMINAR GRUPOS\n")
        try:
            nombre_grupo = input("Nombre del grupo: ")
            if nombre_grupo == "C":
                return
            if nombre_grupo not in grupos:
                input("EL GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE ELIMINAR")
            else:
                os.system("cls")
                print("\n\n\n-------------------------------------------------------------------------------")
                print("                     LISTA DIGITAL DE CONTACTOS\n")
                print("                     ADMINISTRAR GRUPOS DE CONTACTOS: ELIMINAR GRUPOS\n")
                print("Nombre del grupo: ", nombre_grupo)
                while True:
                    try:
                        opcion = input("OPCIÓN    <A> ACEPTAR   <C> CANCELAR: ").upper()
                        if opcion == "A":
                            confirmacion = input("CONFIRMACIÓN DE ELIMINACIÓN SI - NO  ")
                            if confirmacion == "SI":
                                indice = grupos.index(nombre_grupo)
                                del grupos[indice]
                                del contactos_por_grupos[indice]
                                break
                            if confirmacion == "NN":
                                break
                            else:
                                input("OPCIÓN INVÁLIDA, INTENTE DE NUEVO")
                        elif opcion == "C":
                            break
                        else:
                            input("OPCIÓN INVÁLIDA, INTENTE DE NUEVO")
                    except:
                        input("OPCIÓN INVÁLIDA, INTENTE DE NUEVO")
        except:
            input("ESTE NOMBRE DE GRUPO NO ES VÁLIDO")

#Función que elimina a un contacto de un grupo
#Entradas: un contacto y un grupo
#Salidas: eliminación del contacto del grupo o no
def eliminar_contactos_grupos(grupos, contactos_por_grupos, contactos):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ADMINISTRAR GRUPOS DE CONTACTOS: ELIMINAR CONTACTOS DE GRUPOS\n")
        try:
            nombre_grupo = input("Nombre del grupo: ")
            if nombre_grupo == "C":
                return
            if nombre_grupo not in grupos:
                input("ESTE GRUPO NO EXISTE, NO SE PUEDEN ELIMINAR CONTACTOS")
            else:
                while True:
                    try:
                        telefono = input("Teléfono: ")
                        if telefono == "C":
                            return
                        if len(telefono) >= 5 and len(telefono) <= 12:
                            telefono = int(telefono)
                            area_telefono = None
                            for contacto in contactos:
                                if contacto[0] == telefono:
                                    area_telefono = contacto[1]
                                    print("Área:", area_telefono)
                                    for area in areas:
                                        if contacto[1] == area[0]:
                                            print("Nombre del área:", area[1])
                                    break
                            else:
                                input("ESTE CONTACTO NO EXISTE, NO SE PUEDE ELIMINAR")
                                continue
                            
                            opcion = input("OPCIÓN     <A> ACEPTAR    <C> CANCELAR: ").upper()
                            if opcion == "A":
                                indice_grupo = grupos.index(nombre_grupo)
                                grupo_contactos = contactos_por_grupos[indice_grupo]
                                for indice, (tel, info) in enumerate(grupo_contactos):
                                    if tel == telefono:
                                        del contactos_por_grupos[indice_grupo][indice]
                                        os.system("cls")  # Limpiar la pantalla
                                        print("\n\n\n-------------------------------------------------------------------------------")
                                        print("                     LISTA DIGITAL DE CONTACTOS\n")
                                        print("                     ADMINISTRAR GRUPOS DE CONTACTOS: ELIMINAR CONTACTOS DE GRUPOS\n")
                                        break
                                else:
                                    input("ESTE CONTACTO NO PERTENECE AL GRUPO")
                            elif opcion == "C":
                                break
                            else:
                                input("INGRESE UNA OPCIÓN VÁLIDA")
                        else:
                            input("INGRESE UN NÚMERO DE TELÉFONO VÁLIDO")
                    except:
                        input("ESTE NÚMERO DE TELÉFONO NO ES VÁLIDO")
        except:
            input("ESTE GRUPO NO EXISTE, NO SE PUEDEN ELIMINAR CONTACTOS")

#__________________________________________LISTA DE CONTACTOS______________________________________
#Función que usa comodines para buscar un contacto busqye mucho en internet y también pedí ayuda a mis compañeros pero no entendí muy bien la vdd. 
def lista_de_contactos(grupos, contactos_por_grupos, contactos):
    input("DAR <INTRO>")

def tipo_comodin(patron):
    contador_comodin = patron.count("%")
    
    if contador_comodin == 1:
        if patron.startswith("%"):
            return "inicio_final"
        elif patron.endswith("%"):
            return "final_inicio"
        else:
            return "medio"
    elif contador_comodin == 2:
        return "doble"
    elif contador_comodin == 3:
        return "triple"
    else:
        return "ninguno"

def buscar_info(patron, indice, contactos):
    resultados = []
    
    if not patron:
        return contactos
    
    tipo = tipo_comodin(patron)
    
    if tipo == "inicio_final":
        patron = patron[1:]
        for contacto in contactos:
            if str(contacto[indice]).lower().endswith(patron.lower()):
                resultados.append(contacto)
    
    elif tipo == "final_inicio":
        patron = patron[:-1]
        for contacto in contactos:
            if str(contacto[indice]).lower().startswith(patron.lower()):
                resultados.append(contacto)
    
    elif tipo == "medio":
        inicio, final = patron.split("%")[0], patron.split("%")[1]
        for contacto in contactos:
            if str(contacto[indice]).lower().startswith(inicio.lower()) and \
               str(contacto[indice]).lower().endswith(final.lower()):
                resultados.append(contacto)
    
    elif tipo == "doble":
        patron = patron[1:-1]
        for contacto in contactos:
            if patron.lower() in str(contacto[indice]).lower():
                resultados.append(contacto)
    
    elif tipo == "triple":
        primer_patron, segundo_patron = patron.split("%")[1:]
        primer_patron, segundo_patron = primer_patron.lower(), segundo_patron.lower()
        for contacto in contactos:
            if primer_patron in str(contacto[indice]).lower():
                indices = [match.start() for match in re.finditer(primer_patron, str(contacto[indice]).lower())]
                for idx in indices:
                    if segundo_patron in str(contacto[indice][idx:]).lower():
                        resultados.append(contacto)
    
    else:
        for contacto in contactos:
            if patron.lower() == str(contacto[indice]).lower():
                resultados.append(contacto)
    
    return resultados

#__________________________________________________AYUDA__________________________________________
def abrir_enlace(url):
    webbrowser.open(url)

url = "https://sites.google.com/view/listadigitaldecontactos/home"
abrir_enlace(url)

#________________________________________________ACERCA DE________________________________________
def acerca_de():
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                     ACERCA DEL PROGRAMA\n")
        print("\n\nNombre del programa: Lista digitál de contactos")
        print("\nVersión: 1.0.0")
        print("\nFecha de creación: 14 de abril del 2024")
        print("\nAutór: Santiago Valverde Álvarez\n")
        volver = input("PARA VOLVER DIJITE 0:    ")
        match volver:
            case "0":
                return
            case _:
                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#__________________________________ CONSTANTES / VARIABLES / ESTRUCTURAS___________________________                                              

TIPOS_TELEFONO = ("M", "C", "T", "O")

areas = [] 
contactos = [] 
grupos = [] 
contactos_por_grupos = [] 

area_por_omision = 0
tipo_telefono_por_omision = ""

#__________________________________________MENÚ PRINCIPAL________________________________________ 
while True:
    os.system("cls")
    print("\n\n\n-------------------------------------------------------------------------------")
    print("                     LISTA DIGITAL DE CONTACTOS\n")
    print(" 1. Registrar áreas")
    print(" 2. Configuración de lista de contactos")
    print(" 3. Registrar contactos")
    print(" 4. Administrar grupos de contactos")
    print(" 5. Lista de contactos")
    print(" 6. Ayuda")
    print(" 7. Acerca de")
    print(" 0. Fin")
    opcion = input("    OPCIÓN ")              
    match opcion: 
        case "1":
            registrar_areas(areas)
        case "2":
            configuracion_lista_contactos(areas)
        case "3":
            registrar_contactos(contactos, areas)
        case "4":
            administrar_grupos(contactos, areas, grupos, contactos_por_grupos)
        case "5":
            lista_de_contactos(grupos, contactos_por_grupos, contactos)
        case "6":
            abrir_enlace(url)
        case "7":
            acerca_de()
        case "0":
            break
        case _:
            input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
print("FIN DEL PROGRAMA")