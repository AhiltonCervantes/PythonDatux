class animal():
    def __init__(self,name,raza,pelaje):
        self.name=name
        self.raza=raza
        self.pelaje=pelaje
    
class gato(animal):
    def __init__(self, name, raza, pelaje):
        super().__init__(name, raza, pelaje)
    def sonido(self,sound):
        return f"El gato produce un sonido {self.sonido}"

class perro(animal):
    def __init__(self, name, raza, pelaje):
        super().__init__(name, raza, pelaje)
    def sonido(self,sound):
        return f"El perro produce un sonido {self.sonido}"