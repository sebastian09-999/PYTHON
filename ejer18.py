class Carro:
    def __init__(self, placa, marca, modelo, color):
        self._placa = placa
        self.marca = marca
        self._modelo = modelo
        self.color = color

    def getplaca(self):
        return self._placa

    def setplaca(self, placa):
        self._placa = placa

    def getmodelo(self):
        return self._modelo

    def setmodelo(self, modelo):
        self._modelo = modelo

class Libro:
    def __init__(self, titulo, autor, numeroPaginas):
        self._titulo = titulo
        self._autor = autor
        self._numeroPaginas = numeroPaginas

    def gettitulo(self):
        return self._titulo

    def getautor(self):
        return self._autor

    def getnumeroPaginas(self):
        return self._numeroPaginas

    def settitulo(self, titulo):
        self._titulo = titulo

    def setautor(self, autor):
        self._autor = autor

    def setnumeroPaginas(self, numeroPaginas):
        self._numeroPaginas = numeroPaginas

carro = Carro("ABC123", "Toyota", 2020, "Rojo")
libro = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

print(carro.getplaca(), carro.marca, carro.getmodelo(), carro.color)
print(libro.gettitulo(), libro.getautor(), libro.getnumeroPaginas())