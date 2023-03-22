from helper import crear_muebles,generar_rango_cruza,llenar_resultado,arr_numeros
import random
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from Interfaz import Interfaz
class AlgoritmoGenetico:
    def __init__(self, muebles,n_individuos, tamanio_poblacion,horas_trabajo,n_generaciones,prob_mutacion,n_mutaciones,prob_mutacion_gen):
        self.tamanio_poblacion = tamanio_poblacion
        self.n_individuos = n_individuos
        self.horas_trabajo = horas_trabajo
        self.muebles = muebles
        self.n_generaciones = n_generaciones
        self.poblacion=[]
        self.mejor_individuo=[]
        self.media_individuo=[]
        self.peor_individuo=[]
        self.prob_mutacion=prob_mutacion
        self.n_mutaciones=n_mutaciones
        self.prob_mutacion_gen=prob_mutacion_gen
        self.cant_genes=arr_numeros(self.n_individuos)
        self.penalizacion=100
        self.primera_genetica()
        self.bucle_algoritmo()
    def primera_genetica(self):
        individuo_aux=[]
        for mueble in self.muebles:
            individuo_aux.append(mueble.id)
        for _ in range(self.tamanio_poblacion):
            random.shuffle(individuo_aux)
            individuo = individuo_aux.copy()
            self.poblacion.append(self.crear_individuo(individuo))

    def bucle_algoritmo(self):
        aux = 0
        while (aux < self.n_generaciones):
            self.generacion=aux+1
            poblacion_nueva = []
            # Hacer todo el bucle del algoritmo
            for i in range(len(self.poblacion)):
                if i == (len(self.poblacion)-1):
                    individuo = self.cruza(self.poblacion[i].get(
                        'data'), self.poblacion[0].get('data'))
                    poblacion_nueva.append(individuo)
                else:
                    individuo = self.cruza(self.poblacion[i].get(
                        'data'), self.poblacion[i+1].get('data'))
                    poblacion_nueva.append(individuo)
            # Se hace la mutación
            self.mutacion(poblacion_nueva)

            # Se calcula la aptitud para cada individuo y se agrega id
            poblacion_aptitud=[]
            for indiv in poblacion_nueva:
                poblacion_aptitud.append(self.agregar_aptitud(indiv))
            # Se insertan los nuevos en la población general
            for indiv in poblacion_aptitud:
                self.poblacion.append(indiv)
            self.ordenar_poblacion_por_aptitud()
            # Poda hasta tener el numero de individuos iniciales
            self.graficar_individuos(aux+1)
            self.poda()
            self.mejor_individuo.append(self.poblacion[0])
            self.media_individuo.append(self.poblacion[round(self.tamanio_poblacion/2)])
            self.peor_individuo.append(self.poblacion[self.tamanio_poblacion-1])
            print(f'Mejor individuo: {self.poblacion[0]}')
            print(f'Peor individuo: {self.poblacion[self.tamanio_poblacion-1]}')
            print(f'Generación {aux+1}')
            for indiv in self.poblacion:
                print(indiv)
            aux += 1
    def mutacion(self, nueva_poblacion):
        for individuo in nueva_poblacion:
            if random.uniform(0,1) <= self.prob_mutacion:
                for _ in range(self.n_mutaciones):
                    if random.uniform(0,1) <= self.prob_mutacion_gen:
                        a, b = random.choices(self.cant_genes, k=2)
                        individuo.get('data')[a], individuo.get('data')[
                            b] = individuo.get('data')[b], individuo.get('data')[a]
    def poda(self):
        while len(self.poblacion) != self.tamanio_poblacion:
            self.poblacion.pop()
    def cruza(self, indiv1, indiv2):
        # llenado parametros iniciales
        resultado = []
        indiv1_copy = indiv1.copy()
        index_aux = 0
        # Se crea un arreglo temporal con -1 el cual será el arreglo que se retorna como resultado de la cruza
        resultado = llenar_resultado(self.n_individuos)
        a, b = generar_rango_cruza(self.cant_genes)

        # se introduce a resultado los valores seleccionados del primer individuo
        for i in range(a, b+1):
            resultado[i] = indiv1[i]
            index_aux = i

        # for para eliminar los datos que ya se usaron del individuo1 (se creó un arreglo auxiliar)
        for i in range(a, b+1):
            indiv1_copy.remove(indiv1[i])

        datos_restantes = len(indiv1)-len(indiv1[a:b+1])
        index_aux += 1
        aux_result = index_aux
        aux_indv2 = index_aux
        for _ in range(datos_restantes):

            band = False
            while band == False:
                if aux_indv2 >= len(indiv2):
                    aux_indv2 = 0
                if aux_result >= len(resultado):
                    aux_result = 0
                if indiv2[aux_indv2] in indiv1_copy:
                    resultado[aux_result] = indiv2[aux_indv2]
                    indiv1_copy.remove(indiv2[aux_indv2])
                    aux_result += 1
                    aux_indv2 += 1
                    band = True
                else:
                    aux_indv2 += 1
        individuo = self.crear_data(resultado)
        return individuo
    def agregar_aptitud(self, individuo):
        return self.calcular_data(individuo.get('data'))
    def ordenar_poblacion_por_aptitud(self):
        self.poblacion.sort(key=lambda aptitud: aptitud['aptitud'], reverse=True)
    def crear_data(self, data):
        return {'data':data}
    def calcular_data(self, data):
        horas=0
        aux=0
        ganancia=0
        muebles=0
        for gen in data:
            if aux <= self.horas_trabajo:
                muebles +=1
                aux += self.muebles[gen-1].tiempo
        for x in range(muebles-1):
            ganancia += self.muebles[data[x]-1].precio
            horas += self.muebles[data[x]-1].tiempo
            
        aptitud= self.calcular_aptitud(ganancia, horas)
        return {'data':data, 'aptitud':aptitud,'ganancia':round(ganancia,2),'horas':horas, 'muebles':muebles-1}
        # return {'data':data, 'aptitud':aptitud,'ganancia':round(ganancia,2),'horas':horas}
    def calcular_aptitud(self, ganancia, horas):
        return round( ganancia - (self.penalizacion*(self.horas_trabajo-horas)),2)
    def crear_individuo(self,individuo_data):
        data= self.calcular_data(individuo_data)
        individuo = data
        return individuo
    def graficar_individuos(self,n_generacion):
        fig,aux=plt.subplots()
        arr_x=[]
        arr_y=[]
        for index,individuo in enumerate(self.poblacion):
            arr_x.append(index+1)
            arr_y.append(individuo['aptitud'])
        plt.stem(arr_x,arr_y,label='Aptitud')
        aux.set_title(f'Individuos en generacion: {n_generacion}',fontdict={'fontsize':20,'fontweight':'bold'})
        aux.set_xlabel('Individuo',fontdict={'fontsize':15,'fontweight':'bold', 'color':'tab:red'})
        aux.set_ylabel('Aptitud',fontdict={'fontsize':15,'fontweight':'bold', 'color':'tab:blue'})
        aux.legend(loc='upper right',prop={'size':10})
        # plt.grid()
        plt.savefig(f'./images/generacion_{self.generacion}')
        plt.close()
def generar_grafica(algoritmo):
    list_epocas = []
    list_mejores_aptitud = []
    list_peores_aptitud = []
    list_media_aptitud=[]
    for x in algoritmo.media_individuo:
        list_media_aptitud.append(x.get('aptitud'))
    for k in algoritmo.mejor_individuo:
        list_mejores_aptitud.append(k.get('aptitud'))
    for j in algoritmo.peor_individuo:
        list_peores_aptitud.append(j.get('aptitud'))
    for i in range(algoritmo.n_generaciones):
        list_epocas.append(i+1)  
    fig, ax = plt.subplots()
    ax.plot(list_epocas, list_mejores_aptitud,label='Mejores Aptitud')
    ax.plot(list_epocas, list_media_aptitud,label='Aptitud Media')
    ax.plot(list_epocas, list_peores_aptitud, color='red',label='Peores Aptitud')
    index=algoritmo.n_generaciones -1
    ax.text(0.5,5050,f'Mejor individuo {algoritmo.mejor_individuo[index]}')
    ax.legend(loc='lower right')
    plt.savefig('images/evolucion_aptitud')
    plt.show()  



if __name__ == "__main__":
    window = tk.Tk()
    entrada= Interfaz(window)
    n_muebles=entrada.get_n_muebles()
#                          15            1                                  6                        1000                      300                          
    muebles=crear_muebles(n_muebles,
                          rango1=entrada.get_rango1(),
                          rango2=entrada.get_rango2(), 
                          media=entrada.get_media(), 
                          desviacion_estandar=entrada.get_desviacion_estandar()
                          )
    AG=AlgoritmoGenetico(muebles,
                        n_individuos=n_muebles, #15
                        tamanio_poblacion= entrada.get_tamanio_poblacion(), #20 
                        horas_trabajo=entrada.get_horas(), #20
                        n_generaciones=entrada.get_generaciones(), #10
                        prob_mutacion=entrada.get_prob_mutacion(), #0.7
                        n_mutaciones=entrada.get_n_mutacion(), #2
                        prob_mutacion_gen=entrada.get_prob_muta_gen() #0.7
                        )
    generar_grafica(AG)