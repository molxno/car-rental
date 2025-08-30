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
from datetime import date
from .direccion import Direccion

class Persona:
    """Clase base para Propietario y Usuario."""
    def __init__(self, cedula: str, nombres: str, apellidos: str, telefono: str, direccion: Direccion, fecha_nacimiento: date) -> None:
        self.__cedula = cedula
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__telefono = telefono
        self.__direccion = direccion
        self.__fecha_nacimiento = fecha_nacimiento

    # Encapsulamiento: getters / setters
    @property
    def cedula(self) -> str:
        return self.__cedula

    @property
    def nombres(self) -> str:
        return self.__nombres
    @nombres.setter
    def nombres(self, value: str) -> None:
        self.__nombres = value

    @property
    def apellidos(self) -> str:
        return self.__apellidos
    @apellidos.setter
    def apellidos(self, value: str) -> None:
        self.__apellidos = value

    @property
    def telefono(self) -> str:
        return self.__telefono
    @telefono.setter
    def telefono(self, value: str) -> None:
        self.__telefono = value

    @property
    def direccion(self) -> Direccion:
        return self.__direccion
    @direccion.setter
    def direccion(self, value: Direccion) -> None:
        self.__direccion = value

    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value: date) -> None:
        self.__fecha_nacimiento = value

    def nombre_completo(self) -> str:
        return f"{self.__nombres} {self.__apellidos}"

    def __str__(self) -> str:
        return f"{self.nombre_completo()} (CC {self.__cedula})"


class Propietario(Persona):
    """Propietario de vehículos."""
    pass


class Usuario(Persona):
    """Usuario que alquila vehículos."""
    pass
