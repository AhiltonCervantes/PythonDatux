class problema1():
    def __init__(self,fullname,dni,edad):
        self.fullname=fullname
        self.dni=dni
        self.edad=edad
    def __str__(self) -> str:
        return f"{self.fullname} con identificacion N°{self.dni} tiene {self.edad} años"
