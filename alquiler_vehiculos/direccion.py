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

class Direccion:
    """Representa una dirección física."""
    def __init__(self, pais: str, ciudad: str, barrio: str, via: str, numero: str) -> None:
        self.__pais = pais
        self.__ciudad = ciudad
        self.__barrio = barrio
        self.__via = via
        self.__numero = numero

    # Getters y setters (encapsulamiento)
    @property
    def pais(self) -> str:
        return self.__pais
    @pais.setter
    def pais(self, value: str) -> None:
        self.__pais = value

    @property
    def ciudad(self) -> str:
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, value: str) -> None:
        self.__ciudad = value

    @property
    def barrio(self) -> str:
        return self.__barrio
    @barrio.setter
    def barrio(self, value: str) -> None:
        self.__barrio = value

    @property
    def via(self) -> str:
        return self.__via
    @via.setter
    def via(self, value: str) -> None:
        self.__via = value

    @property
    def numero(self) -> str:
        return self.__numero
    @numero.setter
    def numero(self, value: str) -> None:
        self.__numero = value

    def __str__(self) -> str:
        return f"{self.__via} #{self.__numero}, {self.__barrio}, {self.__ciudad}, {self.__pais}"
