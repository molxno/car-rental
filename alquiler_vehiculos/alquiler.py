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

from __future__ import annotations
from datetime import datetime, timedelta
from .persona import Usuario
from .vehiculo import Vehiculo

class RegistroAlquiler:
    ESTADO_EN_PROCESO = "En Proceso"
    ESTADO_FINALIZADO = "Finalizado"

    def __init__(self, usuario: Usuario, vehiculo: Vehiculo, fecha_inicio: datetime) -> None:
        if vehiculo.propietario.cedula == usuario.cedula:
            raise ValueError("Un usuario no puede alquilar su propio vehículo.")
        self.__usuario = usuario
        self.__vehiculo = vehiculo
        self.__fecha_inicio = fecha_inicio
        self.__estado = RegistroAlquiler.ESTADO_EN_PROCESO

    # Encapsulamiento
    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def vehiculo(self) -> Vehiculo:
        return self.__vehiculo

    @property
    def fecha_inicio(self) -> datetime:
        return self.__fecha_inicio

    @property
    def estado(self) -> str:
        return self.__estado

    def calcular_dias(self, hasta: datetime | None = None) -> int:
        """Calcula la cantidad de días de alquiler entre fecha_inicio y 'hasta' (o ahora).
        Regla: mínimo 1 día. Se usa diferencia en días naturales.
        """
        ref = hasta or datetime.now()
        delta = (ref.date() - self.__fecha_inicio.date()).days
        return max(1, delta)

    def costo_total(self, hasta: datetime | None = None) -> float:
        dias = self.calcular_dias(hasta)
        return dias * self.__vehiculo.valor_dia

    def pagar(self) -> None:
        """Realiza el pago e imprime por consola el detalle, cambiando el estado a 'Finalizado'."""
        dias = self.calcular_dias()
        total = self.costo_total()
        print("===== PAGO DE ALQUILER =====")
        print(f"Cédula usuario: {self.__usuario.cedula}")
        print(f"Placa vehículo: {self.__vehiculo.placa}")
        print(f"Valor por día: {self.__vehiculo.valor_dia:.2f}")
        print(f"Total días: {dias}")
        print(f"Costo total: {total:.2f}")
        print("============================")
        self.__estado = RegistroAlquiler.ESTADO_FINALIZADO

    def __str__(self) -> str:
        return f"Alquiler de {self.__vehiculo.placa} por {self.__usuario.cedula} - Estado: {self.__estado}"
