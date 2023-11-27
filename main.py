from data_stark import *
import re

def extraer_iniciales(nombre:str) -> str:
    
    if not nombre:
        retorno = "N/A" #Si no existe el nombre devuelvo N/A.
    else:
        nombre_heroe = re.sub(r"the", "", nombre) #Reemplazo los "the" por un carácter vacío.
        nombre_heroe = re.sub(r"-", " ", nombre_heroe) #Reemplazo los "-" por un espacio.
        iniciales = re.findall(r"[A-Z]", nombre_heroe) #Creo una lista con las letras en mayús que encuentre.
        nombre_iniciales = ".".join(iniciales) #Unifico la lista en un sólo str con "." como unificador.
        retorno = nombre_iniciales  #Devuelvo las iniciales en el formato pedido.

    return retorno

def obtener_dato_formato(dato:str) -> bool or str:
    if type(dato) != str: #Si el tipo de dato es distinto a STR entonces devolverá False.
        retorno = False
    else:
        dato_minusculas = dato.lower() #Pasar a minúsculas el dato.
        dato_minusculas = re.sub(r" ", "_", dato_minusculas) #Reemplazar los espacios vacios con un "_".
        retorno = dato_minusculas #Devuelve el dato en formato de snake_case.
    
    return retorno

def stark_imprimir_nombre_con_iniciales(diccionario:dict) -> bool:
    if type(diccionario) != dict: #Si el tipo de "diccionario" es distinto a dict entonces devuelve False.
        retorno = False
    elif "nombre" in diccionario: #Si "nombre" se encuentra en diccionario entonces...
        nombre_heroe = diccionario["nombre"] #Asigno la clave "nombre" a la variable nombre_heroe.
        nombre_snake = obtener_dato_formato(nombre_heroe) #nombre_snake utiliza la función nombrada para obtener el nombre en snake_case.
        nombre_iniciales = extraer_iniciales(nombre_heroe)  #nombre_iniciales utiliza la función para obtener las inciales del nombre.
        print("* {0} {1}".format(nombre_snake, nombre_iniciales)) #Hace un print con el nombre en snake y las iniciales del nombre.
        retorno = True #Devuelve True en caso de que fuera posible operar el diccionario.
    
    return retorno #Devuelve la variable retorno que tendrá un True o False según fuera posible utilizar la función.

def stark_imprimir_nombres_con_iniciales(lista:list) -> bool:
    if type(lista) == list and lista != []: #Si el tipo de la lista pasada es list y, la lista no está vacía entonces...
        for elemento in lista:
            stark_imprimir_nombre_con_iniciales(elemento) #Utiliza la función mencionada para imprimir cada nombre de la lista.
        retorno = True #Devuelve True en caso de que fuera posible operar con la lista.
    else:
        retorno = False #Devuelve False encaso de que no fuera posible operar con la lista.

    return retorno #Devuelve la variable retorno que será un True o un False según sea posible operar la lista.

def generar_codigo_heroe(diccionario:dict, id:int) -> str:

    for elemento in diccionario: #Recorro el diccionario.
        genero = diccionario["genero"] #Asigno a la variable genero la clave "genero" del diccionario.
        if genero != "F" and genero != "M" and genero != "NB" or diccionario == {}:
            retorno = "N/A" #Si los generos son distintos de "F, M o NB" o el diccionario está vacio, devolverá "N/A".
        else:
            if genero == "F": 
                retorno = "F-2" + str(id).zfill(7) 
            elif genero == "M":
                retorno = "M-1" + str(id).zfill(7)
            elif genero == "NB":
                retorno = "NB-0" + str(id).zfill(6)
        #En los 3 casos, asignara a retorno el codigo según el género, más el ID y rellenara la cadena para que tenga 10 caracteres.
    return retorno #Devolverá retorno, que será un STR que contendrá el código del heroe o N/A en caso de no poder operar con el diccionario.

def stark_generar_codigos_heroes(lista:list) -> bool or str:

    if lista != []: #Si la lista no se encuentra vacía...
        id = 0 #Contador que indicará el ID de cada heroe.
        for elemento in lista:
            if type(elemento) == dict: #Si el tipo de "elemento" es diccionario entonces...
                nombre = elemento["nombre"] #Se asigna a la variable "nombre" el contenido de la clave "nombre" del diccionario.
                id += 1 #Se suma 1 al ID por cada iteración en la lista.
                codigo = generar_codigo_heroe(elemento, id) #Se utiliza la función mencionada para generar el código del heroe según género.
                nombre_snake_case = obtener_dato_formato(nombre) #Se utiliza la función para conseguir el nombre en snake_case.
                iniciales = extraer_iniciales(nombre) #Se utiliza la función para conseguir las iniciales del nombre.
                retorno = "* {0} ({1}) | {2}".format(nombre_snake_case, iniciales, codigo) #Devolvera un STR con el formato requerido.
                print(retorno) #Imprime el retorno.
            else:
                retorno = False #Si "elemento" no es un dict entonces retornará False. 
        print("Se asignaron {0} códigos.".format(id)) #Al terminar la iteración imprimira la cantidad de codigos que se generaron.
    else:
        retorno = False #
    return retorno #Devuelve la variable retorno.

def sanitizar_entero(numero_a_sanitizar:str) -> int:
    dato_a_analizar = numero_a_sanitizar.strip() #Quita los espacios vacíos en la cadena pasada por parametro.
    buscar_numero = re.search(r"[0-9]+", dato_a_analizar) #Utiliza expresiones regulares para buscar uno o más digitos numericos.
    buscar_digitos = re.search(r"[a-zA-Z]+", dato_a_analizar) #Utiliza expresiones regulares para buscar letras mayusculas o minusculas.
    buscar_caracteres = re.search(r"[\W]+", dato_a_analizar) #Utiliza expresiones regulares para encontrar caracteres especiales.

    if buscar_numero: #Si se encontró uno o más dígitos numericos...
        es_negativo = re.search(r"^-", dato_a_analizar) #Busca "-" al principio de la cadena.
        if es_negativo:
            retorno = -2 #Si se encuentra un "-" al principio de la cadena, devolverá -2 indicando que es un número negativo.
        else: #Si no es negativo intentará castear el STR a INT.
            try:
                retorno = int(dato_a_analizar) #Castea a INT el STR pasado por parametro.
            except:
                retorno = -3 #En caso de no ser posible por alguna razón devuelve -3.
    elif buscar_numero == None: #Si no encontró números en la cadena...
        if buscar_caracteres or buscar_digitos:  #Si tiene caracteres especiales o letras minusculas o mayúsculas...
            retorno = -1 #Asigna -1 al retorno, indicando que encontró caracteres/letras en la cadena.
        else:
            retorno = -3 #Asigna -3 al retorno en caso de otros posibles errores.

    return retorno #Devuelve el retorno que podrá ser -1 en caso de caracteres no numericos. -2 en caso de numeros negativos. 
    # -3 En otros casos, en caso de que el STR sea un número positivo, entonces lo casteara a entero y lo asignará a retorno.

def sanitizar_flotante(numero_a_sanitizar:str) -> float or int:
    dato_a_analizar = numero_a_sanitizar.strip() #Quita los espacios vacíos en la cadena pasada por parametro.
    buscar_numero_flotante = re.search(r"[0-9]+\.[0-9]+", dato_a_analizar) #Utiliza expresiones regulares para buscar uno o más digitos numericos.
    buscar_digitos = re.search(r"[a-zA-Z]+", dato_a_analizar) #Utiliza expresiones regulares para buscar letras mayusculas o minusculas.
    buscar_caracteres = re.search(r"[\W]+", dato_a_analizar) #Utiliza expresiones regulares para encontrar caracteres especiales.

    if buscar_numero_flotante: #Si se encontró uno o más números seguido de un "." y otro número o más numeros...
        es_negativo = re.search(r"^-", dato_a_analizar) #Busca "-" al principio de la cadena.
        if es_negativo:
            retorno = -2 #Si se encuentra un "-" al principio de la cadena, devolverá -2 indicando que es un número negativo.
        else: #Si no es negativo intentará castear el STR a INT.
            try:
                retorno = float(dato_a_analizar) #Castea a FLOAT el STR pasado por parametro.
            except:
                retorno = -3 #En caso de no ser posible por alguna razón devuelve -3.
    elif buscar_numero_flotante == None: #Si no encontró flotantes en la cadena...
        if buscar_caracteres or buscar_digitos:  #Si tiene caracteres especiales o letras minusculas o mayúsculas...
            retorno = -1 #Asigna -1 al retorno, indicando que encontró caracteres/letras en la cadena.
        else:
            retorno = -3 #Asigna -3 al retorno en caso de otros posibles errores.

    return retorno #Devuelve el retorno que podrá ser -1 en caso de caracteres no numericos. -2 en caso de numeros negativos. 
    # -3 En otros casos, en caso de que el STR sea un número positivo flotante, entonces lo casteara a float y lo asignará a retorno.

def sanitizar_string(cadena:str) -> str:
    cadena_a_analizar = cadena.strip() #Quita los espacios vacíos en la cadena pasada por parametro.
    buscar_numero = re.search(r"[0-9]+", cadena_a_analizar) #Utiliza expresiones regulares para buscar uno o más digitos numericos.
    if buscar_numero: #Si hay números en la cadena entonces...
        retorno = "N/A" #Se asignará N/A a la variable retorno.
    else: 
        cadena_modificada = re.sub("/", " ", cadena_a_analizar).lower() #En caso de que no haya números en la cadena, se reemplazaran...
        retorno = cadena_modificada #... "/" si se encuentran en la cadena por un espacio vacío, y luego la cadena será pasada a minúsculas...
        # ... finalmente, se asignará la cadena modificada a la variable retorno.
    return retorno # Devolverá retorno que será "N/A" en caso de una cadena con números o la cadena sanitizada.

def sanitizar_dato(diccionario:dict, clave:str, tipo_dato:str) -> bool:
    if tipo_dato in ("entero", "int", "flotante", "float", "cadena", "string"):#Verifico si el dato que pasé coincide con los especificados.
        clave_a_sanitizar = clave.lower()#Paso a minúsculas la clave buscada para evitar posibles errores.
        tipo_dato_sanitizado = tipo_dato.lower()#Paso a minúsculas el tipo de dato buscado para evitar posibles errores.

        if clave_a_sanitizar in diccionario:#Si la clave que estoy buscando se encuentra en el diccionario entonces...
            clave_solicitada = diccionario[clave_a_sanitizar]#Asigno a clave_solicitada el valor que se encuentra dentro de la clave.
            if tipo_dato == "entero" or tipo_dato == "int":#Si el tipo de dato es entero o int...
                diccionario[clave_a_sanitizar] = sanitizar_entero(clave_solicitada)#Sanitizo el dato a int.
                retorno = True#Devuelvo True en caso de que se haya sanitizado algún dato.
            elif tipo_dato == "flotante" or tipo_dato == "float":#Si el tipo de dato es flotante...
                diccionario[clave_a_sanitizar] = sanitizar_flotante(clave_solicitada)#Sanitizo el dato a float.
                retorno = True#Devuelvo True en caso de que se haya sanitizado algún dato.
            elif tipo_dato == "cadena" or tipo_dato == "string":#Si el tipo de dato es un String...
                diccionario[clave_a_sanitizar] = sanitizar_string(clave_solicitada)#Sanitizo el dato a STR.
                retorno = True#Devuelvo True en caso de que se haya sanitizado algún dato.
        elif clave_a_sanitizar not in diccionario:#Si la clave no se encuentra en el diccionario.
            print("La clave especificada no existe en el héroe")#Printeo mensaje de error.
            retorno = False#Devuelvo false en caso de no poder sanitizar datos.
    else:
        print("Tipo de dato no reconocido.")#Si "tipo_dato" no se encuentra entre los especificados, entonces mostrará mensaje de error...
        retorno = False#Y devolverá false.

    return retorno#Devuelve retorno que podrá ser un True o False según se haya sanitizado algún dato.

def stark_normalizar_datos(lista:list):#FALTA COMENTAR
    if lista != [] and type(lista) == list: #Si no está vacía y lo que pasamos por parametro es una lista entonces...
        for elemento in lista: #Recorro la lista.
            sanitizar_altura = sanitizar_dato(elemento, "altura", "float")#Normalizo todos los datos con las funciones anteriores.
            sanitizar_peso = sanitizar_dato(elemento, "peso", "entero")
            sanitizar_color_ojos = sanitizar_dato(elemento, "color_ojos", "string")
            sanitizar_color_pelo = sanitizar_dato(elemento, "color_pelo", "string")
            sanitizar_fuerza = sanitizar_dato(elemento, "fuerza", "entero")
            sanitizar_inteligencia = sanitizar_dato(elemento, "inteligencia", "string")
        print("Datos normalizados")
    else:
        print("Lista se encuentra vacía.")#Si no se cumple la primera condición, imprime un mensaje de error.

def stark_imprimir_indice_nombre(lista:list) -> list:#FALTA COMENTAR.
    lista_palabras = []
    if lista != [] and type(lista) == list:
        for elemento in lista:
            nombre = elemento["nombre"]
            nombre_sin_the = re.sub(r"the", "", nombre)
            nombres_con_guiones = re.sub(r" ", "-", nombre_sin_the)
            nombres_sin_espacios = nombres_con_guiones.strip()
            lista_palabras.append(nombres_sin_espacios)
        lista_palabras_unidas = "-".join(lista_palabras)
        lista_final = lista_palabras_unidas = "-".join(lista_palabras)
        retorno = re.sub(r"--", "-", lista_final)
    else:
        retorno = "Lista vacía o no es una lista."
    
    return retorno

def generar_separador(patron:str, largo:int, imprimir:bool) -> str:#FALTA COMENTAR.
    if len(patron) > 0 and len(patron) <= 2 and largo > 0 and largo <= 235:
        separador = patron * largo
        if imprimir: 
            print(separador)
            retorno = separador
        else:
            retorno = separador
    else:
        separador = "N/A"
    return separador

def generar_encabezado(titulo:str) -> str:#FALTA COMENTAR.
    separador = generar_separador("*", 50, False)
    encabezado = print("{0}\n{1}\n{2}".format(separador, titulo.upper(), separador))

def imprimir_ficha_heroe(diccionario:dict, id:int) -> str:#FALTA COMENTAR.

        nombre = diccionario["nombre"]
        nombre_iniciales = extraer_iniciales(nombre)
        nombre_formato = obtener_dato_formato(nombre)
        nombre_iniciales_formato = nombre_formato + " " + "(" + nombre_iniciales + ")"
        identidad = diccionario["identidad"]
        identidad_formato = obtener_dato_formato(identidad)
        consultora = diccionario["empresa"]
        consultora_formato = obtener_dato_formato(consultora)
        altura = diccionario["altura"]
        peso = diccionario["peso"]
        fuerza = diccionario["fuerza"]
        color_pelo = diccionario["color_pelo"]
        color_ojos = diccionario["color_ojos"]
        codigo = generar_codigo_heroe(diccionario, id)
       
        generar_encabezado("PRINCIPAL")
        nombre_iniciales_formato
        print("NOMBRE DEL HÉROE: {0}".format(nombre_iniciales_formato))
        print("IDENTIDAD SECRETA: {0}".format(identidad_formato))
        print("CONSULTORA: {0}".format(consultora_formato))
        print("CODIGO DE HEROE: {0}".format(codigo))
        generar_encabezado("FISICO")
        print("ALTURA: {0} cm".format(altura))
        print("PESO: {0} kg".format(peso))
        print("FUERZA: {0} N".format(fuerza))
        generar_encabezado("SEÑAS PARTICULARES")
        print("COLOR DE OJOS: {0}".format(color_ojos))
        print("COLOR DE PELO: {0}".format(color_pelo))

def stark_navegar_fichas(lista:list):#FALTA COMENTAR.

    id = 1
    posicion_lista = 0
    while True:
        imprimir_ficha_heroe(lista[posicion_lista], id)
        opcion = input("Ingrese opción: \n1-Ir a la izquierda.\n2-Ir a la derecha.\n3-Volver al menú.")
        if opcion == "1":
            if posicion_lista == 0:
                posicion_lista = 23
                id = 24
            else:
                posicion_lista -= 1
                id -= 1
        elif opcion == "2":
            if posicion_lista == 23:
                posicion_lista = 0
                id = 1
            else:
                posicion_lista += 1
                id += 1
        elif opcion == "3":
            print("Volviendo al menú...")
            break
        else:
            print("Introduzca una opción valida...")
            opcion

def menu_stark(lista:list):#FALTA COMENTAR.
    
    normalizados = False
    while True:
        opcion = \
input('''1 - Imprimir la lista de nombres junto con sus iniciales
2 - Imprimir la lista de nombres y el código del mismo
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
6 - Salir
Ingrese opción:''')
        if opcion == "1":
            stark_imprimir_nombres_con_iniciales(lista)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista)
        elif opcion == "3" and normalizados == False:
            normalizados = True
            for elemento in lista:
                sanitizar_dato(elemento, "nombre", "string")
                sanitizar_dato(elemento, "identidad", "string")
                sanitizar_dato(elemento, "empresa", "string")
                sanitizar_dato(elemento, "altura", "float")
                sanitizar_dato(elemento, "peso", "float")
                sanitizar_dato(elemento, "genero", "string")
                sanitizar_dato(elemento, "color_ojos", "string")
                sanitizar_dato(elemento, "color_pelo", "string")
                sanitizar_dato(elemento, "fuerza", "entero")
                sanitizar_dato(elemento, "inteligencia", "string")
            print("Datos normalizados con éxito.")
        elif opcion == "3" and normalizados == True:
            print("Datos ya normalizados.")
        elif opcion == "4":
            print(stark_imprimir_indice_nombre(lista))
        elif opcion == "5":
            stark_navegar_fichas(lista)
        elif opcion == "6":
            print("Saliendo de S.T.A.R.K.IV")
            break
        else:
            print("Introduzca una opción valida...")
            opcion

menu_stark(lista_personajes)