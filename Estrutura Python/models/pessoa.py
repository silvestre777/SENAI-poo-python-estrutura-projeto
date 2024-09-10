from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidadefederativa import Unidade_Federativa


class Pessoa:
    def __init__(self, nome:str, idade:int, sexo: Sexo, endereco: Endereco, unidadefederativa : Unidade_Federativa) -> None:
        self.nome =nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        self.unidadefederativa = unidadefederativa

    def __str__(self) -> str:
        return (f"\n== Dados ==="
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                f"\n {self.endereco}"
                f"\n UF: {self.unidadefederativa.value}")