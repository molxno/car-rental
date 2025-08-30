# =============================================================
# Momento Evaluativo 1 - Estructura de Datos y Laboratorio
# Sistema de Alquiler de Vehículos
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# =============================================================

from datetime import date, datetime, timedelta
from alquiler_vehiculos import (
    Direccion, Propietario, Usuario,
    Automovil, Motocicleta, RegistroAlquiler
)

def crear_datos_demo():
    # Direcciones
    d1 = Direccion("Colombia", "Medellín", "Laureles", "Cra 80", "12-34")
    d2 = Direccion("Colombia", "Medellín", "El Poblado", "Calle 10", "45-67")
    d3 = Direccion("Colombia", "Bogotá", "Chapinero", "Av 7", "89-10")
    d4 = Direccion("Colombia", "Cali", "San Antonio", "Calle 5", "11-22")

    # Personas
    p1 = Propietario("10101234", "Ana", "Gómez", "3001234567", d1, date(1990, 5, 21))
    p2 = Propietario("20202345", "Luis", "Pérez", "3007654321", d2, date(1985, 8, 12))

    u1 = Usuario("30303456", "Sofía", "López", "3111111111", d3, date(1998, 1, 10))
    u2 = Usuario("40404567", "Carlos", "Ramírez", "3222222222", d4, date(1995, 3, 15))

    # Vehículos (2 autos y 2 motos)
    a1 = Automovil("ABC123", "Toyota", "Corolla", 2020, p1, 120000.0, "sedán")
    a2 = Automovil("XYZ987", "Kia", "Rio", 2019, p2, 100000.0, "hatchback")

    m1 = Motocicleta("MOT001", "Yamaha", "FZ", 2021, p1, 80000.0, 150)
    m2 = Motocicleta("MOT002", "Honda", "CBR", 2022, p2, 90000.0, 250)

    return p1, p2, u1, u2, a1, a2, m1, m2

def flujo_principal():
    p1, p2, u1, u2, a1, a2, m1, m2 = crear_datos_demo()

    # Crear al menos dos registros de alquiler
    # Caso 1: u1 alquila a1 desde ayer
    alquiler1 = RegistroAlquiler(u1, a1, datetime.now() - timedelta(days=2))

    # Caso 2: u2 alquila m2 desde hoy
    alquiler2 = RegistroAlquiler(u2, m2, datetime.now())

    # Mostrar y pagar
    print(alquiler1)
    alquiler1.pagar()
    print(alquiler1)  # estado debe quedar en Finalizado

    print(alquiler2)
    alquiler2.pagar()
    print(alquiler2)

    # Intento inválido: usuario alquila su propio vehículo (descomentar para ver excepción)
    # alquiler_invalido = RegistroAlquiler(u1, m1, datetime.now())  # m1 es de p1, u1 != p1 así que es válido
    # alquiler_invalido2 = RegistroAlquiler(Usuario(p1.cedula, p1.nombres, p1.apellidos, p1.telefono, p1.direccion, p1.fecha_nacimiento), a1, datetime.now())

if __name__ == "__main__":
    flujo_principal()
