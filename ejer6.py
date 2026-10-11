tipo = input("¿Desea pizza vegetariana? si/no: ").lower()
if tipo == "si":
    print("Ingredientes vegetarianos: pimiento, tofu")
    ingrediente = input("Elija un ingrediente: ").lower()
    print("Pizza vegetariana")
    print("Ingredientes: mozzarella, tomate,", ingrediente)
else:
    print("Ingredientes no vegetarianos: peperoni, jamón, salmón")
    ingrediente = input("Elija un ingrediente: ").lower()
    print("Pizza no vegetariana")
    print("Ingredientes: mozzarella, tomate,", ingrediente)