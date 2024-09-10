import os
from  models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidadefederativa import Unidade_Federativa
os.system("cls || clear")


pessoa_1 = Pessoa("Silvestre", 22, Sexo.MASCULIUNO, 
                  Endereco("Rua A",77),Unidade_Federativa.BAHIA)

print(pessoa_1)