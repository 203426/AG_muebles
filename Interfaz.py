import tkinter as tk
from tkinter import messagebox 
class Interfaz:
    def __init__(self, window):
        #TKinter
        self.wind = window
        self.wind.geometry("1000x400")
        # self.wind.eval("tk::PlaceWindow .")
        self.wind.title('Algoritmo genetico')
        self.wind.columnconfigure(0, weight=0)
        #////
        self.label1=tk.Label(self.wind,text="Ingrese la cantidad de generaciones a crear:")
        self.label1.grid(column=0, row=1)
        self.generaciones=tk.IntVar(value=10)

        self.entry1=tk.Entry(self.wind, width=20, textvariable=self.generaciones)
        self.entry1.grid(column=0, row=2)

        self.label2=tk.Label(self.wind,text="Probabilidad de mutación del gen:")
        self.label2.grid(column=0, row=3)
        self.prob_muta_gen=tk.IntVar(value=1.0)

        self.entry2=tk.Entry(self.wind, width=20, textvariable=self.prob_muta_gen)
        self.entry2.grid(column=0, row=4)

        self.label3=tk.Label(self.wind,text="Ingresa el tamaño de la población :")
        self.label3.grid(column=0, row=5)
        self.tamanio_pob=tk.IntVar(value=10)

        self.entry3=tk.Entry(self.wind, width=20, textvariable=self.tamanio_pob)
        self.entry3.grid(column=0, row=6)

        self.label4=tk.Label(self.wind,text="Ingrese la cantidad de veces que se muta el individuo:")
        self.label4.grid(column=2, row=1)
        self.n_mutacion=tk.IntVar(value=3)

        self.entry4=tk.Entry(self.wind, width=20, textvariable=self.n_mutacion)
        self.entry4.grid(column=2, row=2)


        self.label5=tk.Label(self.wind,text="Ingrese la probabilidad de mutacion:")
        self.label5.grid(column=2, row=3)
        self.prob_mutacion=tk.IntVar(value=1.0)

        self.entry5=tk.Entry(self.wind, width=20, textvariable=self.prob_mutacion)
        self.entry5.grid(column=2, row=4)

        self.boton=tk.Button(self.wind, text="Aplicar")
        self.boton.grid(column=1, row=6)
        self.boton.config(command=self.aplicar_datos)

        self.wind.mainloop()
    def get_tamanio_pob(self):
        return int(self.tamanio_pob.get())
    def get_prob_muta_gen(self):
        return float(self.prob_muta_gen.get())
    def get_prob_mutacion(self):
        return float(self.prob_mutacion.get())
    def get_n_mutacion(self):
        return int(self.n_mutacion.get())
    def get_generaciones(self):
        return int(self.generaciones.get())
    def aplicar_datos(self):
        self.wind.destroy()