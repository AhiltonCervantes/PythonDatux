class Producto:
    def __init__(self,name,tipo,añoProduc) -> None:
        self.name=name
        self.tipo=tipo
        self.añoProduc=añoProduc
    def __str__(self) -> str:
        return f"El autoparte {self.name} es de tipo {self.tipo} producido en el año {self.añoProduc}"

class Catalogo:
    listaAutopartes=[]
    def __init__(self,autoparte):
        self.listaAutopartes.append(autoparte)
    def agregar(self, c):
        self.listaAutopartes.append(c)
    def mostrar(self):
        for c in self.listaAutopartes:
            print(c)