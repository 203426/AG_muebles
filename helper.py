from Mueble import Mueble
import random

def crear_muebles():
    muebles=[]
    data=[  {'nombre':'silla','precio':300,'pata_silla_delantera':2,'pata_silla_trasera':2,'pata_mesa':0,'refuerzos':4,'tornillos':8,'respaldos':1,'asientos':1,'tablas':0,'tuercas':4},
            {'nombre':'mesa','precio':900,'pata_silla_delantera':0,'pata_silla_trasera':0,'pata_mesa':4,'refuerzos':4,'tornillos':10,'respaldos':0,'asientos':0,'tablas':1,'tuercas':6},
            {'nombre':'banco','precio':150,'pata_silla_delantera':0,'pata_silla_trasera':0,'pata_mesa':4,'refuerzos':4,'tornillos':4,'respaldos':0,'asientos':0,'tablas':0,'tuercas':4},
            {'nombre':'silla2','precio':250,'pata_silla_delantera':2,'pata_silla_trasera':2,'pata_mesa':0,'refuerzos':2,'tornillos':6,'respaldos':1,'asientos':1,'tablas':0,'tuercas':0},
            {'nombre':'mesa3','precio':1200,'pata_silla_delantera':0,'pata_silla_trasera':0,'pata_mesa':6,'refuerzos':10,'tornillos':14,'respaldos':0,'asientos':0,'tablas':2,'tuercas':10},
            {'nombre':'silla3','precio':1200,'pata_silla_delantera':3,'pata_silla_trasera':3,'pata_mesa':0,'refuerzos':2,'tornillos':10,'respaldos':1,'asientos':1,'tablas':0,'tuercas':0}

        ]
    for x,gen in enumerate(data):
        aux=[x+1]
        for _,y in gen.items():
            aux.append(y)
        mueble=Mueble(aux)
        muebles.append(mueble)
    return muebles
def crear_pedidos(n_pedidos,muebles ,rango1,rango2):
    pedidos=[]
    for x in range(n_pedidos):
        cantidad=round(random.uniform(rango1,rango2))
        mueble=random.choice(muebles).nombre
        pedidos.append({'id':x+1,'cantidad':cantidad,'mueble':mueble})
    return pedidos
def generar_rango_cruza(cant_genes):
    # se crea el rango a evaluar en individuo1 y While para que a y b no sean iguales
    a, b = 0, 0
    while a == b:
        a, b = random.choices(cant_genes, k=2)
    # condicion para que "a" siempre sea menor que "b"
    if a > b:
        a, b = b, a
    return a, b

# crea un arreglo temporal con -1 el cual será el arreglo que se retorna como resultado de la cruza
def llenar_resultado(n):
    resultado = []
    for _ in range(n):
        resultado.append(-1)
    return resultado
def arr_numeros(numero):
    arr = []
    for num in range(numero):
        arr.append(num)
    return arr