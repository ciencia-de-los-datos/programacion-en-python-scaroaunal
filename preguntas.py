"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from csv import reader
from operator import itemgetter  
import itertools
file = open("data.csv","r")
lines =reader(file, delimiter= "\t")
lines = list(lines)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    x= 0
    for i in range(0,len(lines)):
        x += int(lines[i][1])
    return x


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    primcoluma= [i[0] for i in lines]     # list comphrension que guarda priemra columna
    Noduplicadas = sorted(set(primcoluma)) # ordena los valores sin duplicados de la primera columna
    listadetuplas = [(j,primcoluma.count(j)) for j in Noduplicadas]       
    return listadetuplas   


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    primeracolumaletas = [i[0] for i in lines]
    primerosnumeros= [i[1] for i in lines]
    zipped = list(zip(primeracolumaletas,primerosnumeros))
    zipped.sort(key=itemgetter(0))
    lista =[]
    for key, group in itertools.groupby(zipped,lambda x:x[0]):
        acum = 0 
        for i in list(group):
            acum+=int(i[1])            
        lista.append((key,acum))

    return lista


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    listameses= [x[2][5:7] for x in lines]
    conjuntomeses = sorted(set(listameses))
    salida = [(x,listameses.count(x)) for x in conjuntomeses]    
    return salida


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    listaletras= [x[0] for x in  lines]
    listanumeros = [x[1]for x in lines]    
    zipped = list(zip(listaletras,listanumeros)) 
    zipped.sort(key=itemgetter(0))
    lista=[]

    for key, group in itertools.groupby(zipped,lambda x:x[0]):
        max = 0
        min = 10*100
        for i in group:
            if int(i[1])< int(min):
                min=int(i[1])
            if int(i[1])> max:
                max = int(i[1])  
        lista.append((key,max,min))
    return lista


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    columna4 = [i[4] for i in lines] # se toma la columna 4 del csv
    listadiccionario =[] # se inicializa lista para convertir string en diccionarios
    for elemento in columna4: #permite convertir el formato string original a variable tipo diccionario
        listadalista = [i.split(":") for i in elemento.split(",")] # se parte por : y por ,
        listadiccionario.append(dict(listadalista))
    
    listaclavevalor = [] # a partir del diccionario se desea una lista de tupas con el clave y el valor del dict
    for i in listadiccionario: #permite crear la tupla de clave valor diccionario
        for k,v in i.items():
            listaclavevalor.append((k,v))
    listaclavevalor.sort(key=itemgetter(0))# permite ordenar la lista para realizar el groupby

    lista= []
    for key, group in itertools.groupby(listaclavevalor,lambda x:x[0]): # funcion para agurpar mismas clavs
        max = 0 # se inicializa el max
        min = 10*100 # se inicializa el min
        for i in group: # se itera la variable group
            if int(i[1])< int(min): # se recorre uno por uno preguntando si es el min
                min=int(i[1])
            if int(i[1])> max: # se recorre uno por uno preguntando si es el maximo.
                max = int(i[1])  
        lista.append((key,min,max))
    return lista



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    listanumeros = [i[1] for i in lines]
    listalletras = [i[0] for i in lines]
    zipped = list(zip(listanumeros,listalletras))
    zipped.sort(key = itemgetter(0))
    lista = []
    for key, group in itertools.groupby(zipped, lambda x:x[0]):
        lista1 = [i[1] for i in group]
        lista.append((int(key),lista1))
    return lista


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    listanumeros = [i[1] for i in lines]
    listalletras = [i[0] for i in lines]
    zipped = list(zip(listanumeros,listalletras))
    zipped.sort(key = itemgetter(0))
    lista = []
    for key, group in itertools.groupby(zipped, lambda x:x[0]):
        lista1 = [i[1] for i in group]
        lista1 = set(lista1)
        lista.append((int(key),sorted(list(lista1))))

    return lista


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccionario = [i[4] for i in lines]
    listadiccionario = []
    for elemento in diccionario:
        listadelista = [i.split(":") for i in elemento.split(",")]
        listadiccionario.append(dict(listadelista))

    llaves= []
    for i in listadiccionario:
        for key in i.keys():
            llaves.append(key)

    agrupaciondiccion = sorted(set(llaves))
    agrupaciones = [[j,llaves.count(j)] for j in agrupaciondiccion]
        
    return dict(agrupaciones)



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    listeltras = [i[0] for i in lines]
    Nelementotcol5 = [len(i[3].split(",")) for i in lines] # # elementos columna 5
    columna6 = [i[4] for i in lines]
    listadicionario = []
    for elemento in columna6:
        diccion = [i.split(":") for i in elemento.split(",")]
        listadicionario.append(diccion)
        Nelementotcol6=[len(dic) for dic in listadicionario]   
    lista = []
    for n in range(0,len(listeltras)):
        lista.append((listeltras[n],Nelementotcol5[n],Nelementotcol6[n]))
    
    return lista



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    columna4 = [i[3] for i  in lines] # intenté con un split, pero para realizar el zip queda de otra forma
    columna2 = [i[1] for i in lines]
    serievalores = [j for i in columna4 for j in i]
    letras = sorted(list(set(serievalores)))
    letras.pop(0) # elimina la coma
    zipped= list(zip(columna4,columna2))
    lista = []
    for i in letras:
        acum=0
        for j in zipped:
            if i in j[0]:
                acum+=int(j[1])
        lista.append([i,acum])   

    return dict(lista)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letras = [i[0] for i in lines] #lista de de las primeras letras
    diccionario = [i[4] for i in lines] # lista del diccionario columna 4
    listaDiccionrio = [] 
    for elemento in diccionario: #crenado los diccionarios dentro de la lista
        dic = [j.split(":") for j in elemento.split(",")]
        listaDiccionrio.append(dict(dic))
    listavaores= []    
    for dictelement in listaDiccionrio: #recorre solo los valores del diccionario para almacenaros
        listavalues  = [int(k) for k in dictelement.values()] # toma los values del diccionarios y los convierte en tipo entero
        listavaores.append(sum(listavalues)) # suma cada uno de los elementos de cada lista
 
    zipped = sorted(list(zip(letras,listavaores)))
    lista = []
    for key, group in itertools.groupby(zipped, lambda x:x[0]):
        acum = 0
        for i in list(group):
            acum += i[1]
        lista.append([key,acum])
    return dict(lista)
