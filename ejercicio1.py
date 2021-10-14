class Animal:
    def __init__(self, age, name):
        self.age = age # public attribute
        self.name = name # public attribute

    def saluda(self, saludo='Hola', receptor = 'nuevo amigo'):
        print(saludo + " " + receptor)
    @staticmethod
    def add(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return " ".join((a, b))
        else:
            raise TypeError
    def mostrarNombre(self):
        print(self.nombre)
    def mostrarEdad(self):
        print(self.edad)