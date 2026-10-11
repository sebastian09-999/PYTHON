class Vuelo:
    def __init__(self, numero, fecha, origen, destino):
        self.numero = numero
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.pasajeros = []

    def registrar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def listar(self):
        print("Número de vuelo:", self.numero)
        print("Fecha:", self.fecha)
        print("Ciudad origen:", self.origen)
        print("Ciudad destino:", self.destino)
        print("Pasajeros:", self.pasajeros)

vuelo = Vuelo(
    input("Número de vuelo: "),
    input("Fecha: "),
    input("Ciudad origen: "),
    input("Ciudad destino: ")
)

n = int(input("¿Cuántos pasajeros desea registrar? "))
for i in range(n):
    vuelo.registrar_pasajero(input("Nombre del pasajero: "))

vuelo.listar()