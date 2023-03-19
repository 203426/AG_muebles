class Mueble:
    def __init__(self,id,tiempo,precio):
        self.id=id
        self.tiempo=tiempo
        self.precio=precio

    def __repr__(self):
        return str(self.__dict__)