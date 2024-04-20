
comida = ["pan", "queso", "jamon", "pasta", "camisa"]

print(comida)

print(comida[0])

# los comandos son insert, remove, append, pop
# insert necesita colocar primero el indice en el que se va a colocar, y luego el elemento que se coloca (1, 24)
# con remove se necesita escribir el objeto tal como se encuentra escrito
# con append se agrega el elemento al final de la lista
# para eliminar con pop se debe colocar el indice del elemento que se desea remover

lista_de_compras = ["harina", "perejil", "huevos", "pan", "tomates", "levadura"]

running = True
while running:
    print("1. Agregar\n2. Ver lista\n3. Borrar\n4. Salir")
    opt = int(input("Ingrese una opcion: "))

    if opt == 1:
        cosa = input("\nAgregue algo al carrito: ")
        lista_de_compras.append(cosa.lower())
    elif opt == 2:
        print(lista_de_compras)
    elif opt == 3:
        indx = input("\nIngrese el numero del elemento que desee eliminar: ")
        lista_de_compras.remove(indx.lower())
    elif opt == 4:
        print("\nDe nada, vuelva pronto")
        running = False
    else:
        print("\nPor favor, limitese a uno de los numeros de las opciones ofrecidas")
    print("\n")
