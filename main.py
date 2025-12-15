from proyecto_supermercado.productos import productos
from proyecto_supermercado.funciones import *

while True:
    print("\n🛍 MENÚ SUPERMERCADO")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar cantidad")
    print("4. Ver carrito")
    print("5. Pagar")
    print("6. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        codigo, cantidad = leer_codigo_y_cantidad()
        if codigo and cantidad:
            agregar_producto(productos, codigo, cantidad)

    elif opcion == "2":
        codigo = int(input("Código a eliminar: "))
        eliminar_producto(codigo)

    elif opcion == "3":
        codigo = int(input("Código a modificar: "))
        cantidad = int(input("Nueva cantidad: "))
        modificar_cantidad(codigo, cantidad)

    elif opcion == "4":
        mostrar_carrito()

    elif opcion == "5":
        total = mostrar_carrito()
        pagar(total)
        break

    elif opcion == "6":
        print("👋 Gracias por su visita")
        break

    else:
        print("❌ Opción inválida")
