from enum import Enum

class Sexo(Enum):

    MASCULIUNO = ("Masculino","M")
    FEMININO = ("Feminino","F")

    def __init__(self, texto : str, caracter : str) -> None:
        self.texto = texto
        self.caracter = caracter