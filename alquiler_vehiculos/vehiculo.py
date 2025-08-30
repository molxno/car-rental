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
from .persona import Propietario

class Vehiculo:
    """Clase base para todo tipo de vehículo."""
    def __init__(self, placa: str, marca: str, modelo: str, anio_fabricacion: int, propietario: Propietario, valor_dia: float) -> None:
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__anio_fabricacion = anio_fabricacion
        self.__propietario = propietario
        self.__valor_dia = float(valor_dia)

    # Encapsulamiento: getters / setters
    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def marca(self) -> str:
        return self.__marca
    @marca.setter
    def marca(self, value: str) -> None:
        self.__marca = value

    @property
    def modelo(self) -> str:
        return self.__modelo
    @modelo.setter
    def modelo(self, value: str) -> None:
        self.__modelo = value

    @property
    def anio_fabricacion(self) -> int:
        return self.__anio_fabricacion
    @anio_fabricacion.setter
    def anio_fabricacion(self, value: int) -> None:
        self.__anio_fabricacion = value

    @property
    def propietario(self) -> Propietario:
        return self.__propietario
    @propietario.setter
    def propietario(self, value: Propietario) -> None:
        self.__propietario = value

    @property
    def valor_dia(self) -> float:
        return self.__valor_dia
    @valor_dia.setter
    def valor_dia(self, value: float) -> None:
        self.__valor_dia = float(value)

    def __str__(self) -> str:
        return f"{self.__placa} - {self.__marca} {self.__modelo} ({self.__anio_fabricacion})"


class Motocicleta(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, anio_fabricacion: int, propietario: Propietario, valor_dia: float, cilindraje: int) -> None:
        super().__init__(placa, marca, modelo, anio_fabricacion, propietario, valor_dia)
        self.__cilindraje = cilindraje

    @property
    def cilindraje(self) -> int:
        return self.__cilindraje
    @cilindraje.setter
    def cilindraje(self, value: int) -> None:
        self.__cilindraje = value


class Automovil(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, anio_fabricacion: int, propietario: Propietario, valor_dia: float, carroceria: str) -> None:
        super().__init__(placa, marca, modelo, anio_fabricacion, propietario, valor_dia)
        self.__carroceria = carroceria  # sedán, hatchback, SUV, etc.

    @property
    def carroceria(self) -> str:
        return self.__carroceria
    @carroceria.setter
    def carroceria(self, value: str) -> None:
        self.__carroceria = value
