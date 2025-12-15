import os
from datetime import datetime
import uuid

USUARIOS_DIR = "Usuarios"

# -------------------------------
# Utilidades de archivos
# -------------------------------
def asegurar_carpeta():
    if not os.path.exists(USUARIOS_DIR):
        os.makedirs(USUARIOS_DIR)

def ruta_usuario(rut):
    return os.path.join(USUARIOS_DIR, f"{rut}.txt")

# -------------------------------
# Carga y guardado de datos
# -------------------------------
def cargar_usuario(rut):
    try:
        with open(ruta_usuario(rut), "r", encoding="utf-8") as f:
            return eval(f.read())
    except FileNotFoundError:
        print("Usuario no existe.")
        return None

def guardar_usuario(rut, data):
    with open(ruta_usuario(rut), "w", encoding="utf-8") as f:
        f.write(str(data))

# -------------------------------
# Creación de usuario
# -------------------------------
def crear_usuario(rut):
    if os.path.exists(ruta_usuario(rut)):
        print("El usuario ya existe.")
        return None

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    usuario = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "cuentas": {}
    }

    guardar_usuario(rut, usuario)
    print("Usuario creado correctamente.")
    return usuario

# -------------------------------
# Cuentas bancarias
# -------------------------------
def crear_cuenta(usuario):
    tipo = input("Tipo de cuenta (vista/corriente/ahorro): ")
    numero = str(uuid.uuid4())[:8]

    usuario["cuentas"][numero] = {
        "tipo": tipo,
        "saldo": 0,
        "movimientos": []
    }
    print(f"Cuenta creada: {numero}")

def seleccionar_cuenta(usuario):
    if not usuario["cuentas"]:
        print("No existen cuentas.")
        return None

    for n, c in usuario["cuentas"].items():
        print(f"{n} - {c['tipo']} - Saldo: {c['saldo']}")

    return input("Seleccione número de cuenta: ")

# -------------------------------
# Movimientos
# -------------------------------
def registrar_movimiento(cuenta, tipo, monto, detalle=""):
    movimiento = {
        "fecha": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "tipo": tipo,
        "monto": monto,
        "detalle": detalle
    }
    cuenta["movimientos"].append(movimiento)
    cuenta["movimientos"] = cuenta["movimientos"][-20:]

# -------------------------------
# Operaciones bancarias
# -------------------------------
def depositar(usuario):
    num = seleccionar_cuenta(usuario)
    if num in usuario["cuentas"]:
        monto = int(input("Monto a depositar: "))
        cuenta = usuario["cuentas"][num]
        cuenta["saldo"] += monto
        registrar_movimiento(cuenta, "Depósito", monto)
        print("Depósito realizado.")

def retirar(usuario):
    num = seleccionar_cuenta(usuario)
    if num in usuario["cuentas"]:
        monto = int(input("Monto a retirar: "))
        cuenta = usuario["cuentas"][num]
        if monto <= cuenta["saldo"]:
            cuenta["saldo"] -= monto
            registrar_movimiento(cuenta, "Retiro", monto)
            print("Retiro realizado.")
        else:
            print("Saldo insuficiente.")

def transferir(usuario):
    print("Cuenta origen")
    origen = seleccionar_cuenta(usuario)
    print("Cuenta destino")
    destino = seleccionar_cuenta(usuario)

    if origen != destino:
        monto = int(input("Monto a transferir: "))
        c_origen = usuario["cuentas"][origen]
        c_destino = usuario["cuentas"][destino]

        if monto <= c_origen["saldo"]:
            c_origen["saldo"] -= monto
            c_destino["saldo"] += monto
            registrar_movimiento(c_origen, "Transferencia", monto, f"a {destino}")
            registrar_movimiento(c_destino, "Transferencia", monto, f"desde {origen}")
            print("Transferencia exitosa.")
        else:
            print("Saldo insuficiente.")

def ver_movimientos(usuario):
    num = seleccionar_cuenta(usuario)
    if num in usuario["cuentas"]:
        for m in usuario["cuentas"][num]["movimientos"]:
            print(m)

# -------------------------------
# Comprobante
# -------------------------------
def generar_comprobante(rut, detalle):
    nombre = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    archivo = f"{nombre}-{rut}.txt"

    with open(archivo, "w", encoding="utf-8") as f:
        f.write(detalle)

    print(f"Comprobante generado: {archivo}")
