import tkinter as tk
from tkinter import messagebox 
class Interfaz:
    def __init__(self, window):
        #TKinter
        self.wind = window
        self.wind.geometry("1200x400")
        # self.wind.eval("tk::PlaceWindow .")
        self.wind.title('Algoritmo genetico')
        self.wind.columnconfigure(0, weight=0)
        #////
        self.label1=tk.Label(self.wind,text="Ingrese el numero de muebles:")
        self.label1.grid(column=0, row=0)
        self.n_muebles=tk.IntVar()

        self.entry1=tk.Entry(self.wind, width=20, textvariable=self.n_muebles )
        self.entry1.grid(column=0, row=1)

        self.label7=tk.Label(self.wind,text="Ingrese la media para el precio de los muebles:")
        self.label7.grid(column=0, row=2)
        self.media=tk.IntVar()

        self.entry7=tk.Entry(self.wind, width=20, textvariable=self.media)
        self.entry7.grid(column=0, row=3)

        self.label8=tk.Label(self.wind,text="Ingrese la desviacion estandar para el precio de los muebles:")
        self.label8.grid(column=0, row=4)
        self.desviacion_estandar=tk.IntVar()

        self.entry8=tk.Entry(self.wind, width=20, textvariable=self.desviacion_estandar)
        self.entry8.grid(column=0, row=5)

        self.label2=tk.Label(self.wind,text="Ingrese la cantidad de generaciones a crear:")
        self.label2.grid(column=0, row=6)
        self.generaciones=tk.IntVar()

        self.entry2=tk.Entry(self.wind, width=20, textvariable=self.generaciones)
        self.entry2.grid(column=0, row=7)

        self.label2=tk.Label(self.wind,text="Probabilidad de mutación del gen:")
        self.label2.grid(column=0, row=8)
        self.prob_muta_gen=tk.IntVar()

        self.entry2=tk.Entry(self.wind, width=20, textvariable=self.prob_muta_gen)
        self.entry2.grid(column=0, row=9)

        self.label3=tk.Label(self.wind,text="Ingrese el primer rango para el tiempo:")
        self.label3.grid(column=2, row=0)
        self.rango1=tk.IntVar()

        self.entry3=tk.Entry(self.wind, width=20, textvariable=self.rango1)
        self.entry3.grid(column=2, row=1)


        self.label4=tk.Label(self.wind,text="Ingrese el segundo rango para el tiempo:")
        self.label4.grid(column=2, row=2)
        self.rango2=tk.IntVar()

        self.entry4=tk.Entry(self.wind, width=20, textvariable=self.rango2)
        self.entry4.grid(column=2, row=3)


        self.label5=tk.Label(self.wind,text="Ingrese la cantidad de veces que se muta el individuo:")
        self.label5.grid(column=2, row=4)
        self.n_mutacion=tk.IntVar()

        self.entry5=tk.Entry(self.wind, width=20, textvariable=self.n_mutacion)
        self.entry5.grid(column=2, row=5)


        self.label6=tk.Label(self.wind,text="Ingrese la probabilidad de mutacion:")
        self.label6.grid(column=2, row=6)
        self.prob_mutacion=tk.IntVar()

        self.entry6=tk.Entry(self.wind, width=20, textvariable=self.prob_mutacion)
        self.entry6.grid(column=2, row=7)

        self.label7=tk.Label(self.wind,text="Ingrese el tamaño de la población:")
        self.label7.grid(column=2, row=8)
        self.tamanio_poblacion=tk.IntVar()

        self.entry7=tk.Entry(self.wind, width=20, textvariable=self.tamanio_poblacion)
        self.entry7.grid(column=2, row=9)

        self.label8=tk.Label(self.wind,text="Ingrese las horas de trabajo:")
        self.label8.grid(column=2, row=10)
        self.horas=tk.IntVar()

        self.entry8=tk.Entry(self.wind, width=20, textvariable=self.horas)
        self.entry8.grid(column=2, row=11)

        self.boton=tk.Button(self.wind, text="Aplicar")
        self.boton.grid(column=1, row=12)
        self.boton.config(command=self.aplicar_datos)

        self.wind.mainloop()
    def get_horas(self):
        return int(self.horas.get())
    def get_prob_muta_gen(self):
        return float(self.prob_muta_gen.get())
    def get_tamanio_poblacion(self):
        return int(self.tamanio_poblacion.get())
    def get_desviacion_estandar(self):
        return int(self.desviacion_estandar.get())
    def get_media(self):
        return int(self.media.get())
    def get_prob_mutacion(self):
        return float(self.prob_mutacion.get())
    def get_n_mutacion(self):
        return int(self.n_mutacion.get())
    def get_rango2(self):
        return int(self.rango2.get())
    def get_rango1(self):    
        return int(self.rango1.get())
    def get_generaciones(self):
        return int(self.generaciones.get())
    def get_n_muebles(self):
        return int(self.n_muebles.get())
    def aplicar_datos(self):
        self.wind.destroy()