from bank_utils import *


def menu_usuario(usuario):
    while True:
        print("\n1.Crear cuenta 2.Depositar 3.Retirar 4.Transferir 5.Movimientos 6.Salir")
        op = input("Opción: ")

        if op == "1": crear_cuenta(usuario)
        elif op == "2": depositar(usuario)
        elif op == "3": retirar(usuario)
        elif op == "4": transferir(usuario)
        elif op == "5": ver_movimientos(usuario)
        elif op == "6": break
        else: print("Opción inválida")

        guardar_usuario(usuario["rut"], usuario)


def main():
    asegurar_carpeta()
    rut = input("Ingrese RUT: ")
    usuario = cargar_usuario(rut)

    if not usuario:
        crear = input("¿Crear usuario nuevo? (s/n): ").lower()
        if crear == "s":
            usuario = crear_usuario(rut)

    if usuario:
        menu_usuario(usuario)

if __name__ == "__main__":
    main()
