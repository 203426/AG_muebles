class Mueble:
    def __init__(self,data):

        self.id = data[0]
        self.nombre= data[1]
        self.precio = data[2]
        self.pata_silla_delantera = data[3]
        self.pata_silla_trasera = data[4]
        self.refuerzos = data[5]
        self.pata_mesa = data[6]
        self.tornillos = data[7]
        self.respaldos = data[8]
        self.asientos = data[9]
        self.tablas = data[10]
        self.tuercas = data[11]

    def __repr__(self):
        return str(self.__dict__)
    def get_material(self):
        return ([self.pata_silla_delantera, self.pata_silla_trasera,self.pata_mesa,self.refuerzos,self.tornillos,self.respaldos,self.asientos,self.tablas,self.tuercas])