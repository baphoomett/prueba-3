dispensador_6 = 0
dispensador_10 = 0
dispensador_20 = 0
opcion = 0


var_pedido = []

def menu_principal():
    while True:
        print("Registro de pedido")
        print("Listar los pedidos")
        print("Imprimir hoja de ruta")
        print("Buscar pedido por ID")
        print("Salir del programa")
        opcion == input("Seleccione una opcion :")

        if opcion == "1":
             registrar_pedido()
        elif opcion == "2":
             listar_pedido()



def registrar_pedido():
    while True:
        nombre = input("Ingrese nombre")
        apellido = input("Ingrese apellido")
        comuna = input("Ingrese comuna")





        pedidos = {
                "nombre": nombre,
                "apellido": apellido,
                "comuna": comuna,


                }



def listar_pedido():
    while True:


       #no hay necesidad de revisar esta inmundicia, en el examen vengo modo insano