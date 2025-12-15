from datetime import datetime
import os

carrito = []

def leer_codigo_y_cantidad():
    try:
        codigo = int(input("Ingrese código de barras (6 dígitos): "))
        cantidad = int(input("Ingrese cantidad: "))
        if cantidad <= 0:
            raise ValueError
        return codigo, cantidad
    except ValueError:
        print("❌ Error: debe ingresar solo números positivos.")
        return None, None


def agregar_producto(productos, codigo, cantidad):
    if codigo not in productos:
        print("❌ Producto no existe.")
        return

    for item in carrito:
        if item["codigo"] == codigo:
            item["cantidad"] += cantidad
            return

    producto = productos[codigo]
    carrito.append({
        "codigo": codigo,
        "nombre": producto["Nombre"],
        "precio": producto["Precio"],
        "cantidad": cantidad
    })


def eliminar_producto(codigo):
    global carrito
    carrito = [p for p in carrito if p["codigo"] != codigo]


def modificar_cantidad(codigo, nueva_cantidad):
    if nueva_cantidad <= 0:
        print("❌ Cantidad inválida")
        return
    for item in carrito:
        if item["codigo"] == codigo:
            item["cantidad"] = nueva_cantidad
            return


def mostrar_carrito():
    print("\n🛒 PRODUCTOS EN CARRITO")
    total = 0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['nombre']} x{item['cantidad']} = ${subtotal}")
    print(f"TOTAL: ${total}")
    return total


def pagar(total):
    print("\n💳 MÉTODO DE PAGO")
    print("1. Efectivo")
    print("2. Tarjeta")
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        while True:
            try:
                monto = int(input("Monto con el que paga: "))
                if monto < total:
                    print("❌ Monto insuficiente")
                else:
                    vuelto = monto - total
                    generar_boleta(total, "Efectivo", vuelto)
                    break
            except ValueError:
                print("❌ Ingrese un número válido")

    elif opcion == "2":
        generar_boleta(total, "Tarjeta", 0)
    else:
        print("❌ Opción inválida")


def generar_boleta(total, medio_pago, vuelto):
    if not os.path.exists("Comprobantes"):
        os.makedirs("Comprobantes")

    fecha = datetime.now()
    nro_boleta = fecha.strftime("%Y%m%d%H%M%S")
    ruta = f"Comprobantes/boleta_{nro_boleta}.txt"

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("🛒 SUPERMERCADO PYTHON\n")
        f.write(f"Fecha: {fecha}\n")
        f.write(f"Boleta N°: {nro_boleta}\n\n")

        for item in carrito:
            f.write(f"{item['nombre']} x{item['cantidad']} = ${item['precio'] * item['cantidad']}\n")

        f.write(f"\nTOTAL: ${total}\n")
        f.write(f"Medio de pago: {medio_pago}\n")
        if medio_pago == "Efectivo":
            f.write(f"Vuelto: ${vuelto}\n")

        f.write("\nGracias por comprar 😊\n")

    print(f"\n✅ Boleta generada en {ruta}")
