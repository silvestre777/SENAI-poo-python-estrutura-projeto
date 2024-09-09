import os
from  models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
os.system("cls || clear")


pessoa_1 = Pessoa("Silvestre", 22, Sexo.MASCULIUNO, 
                  Endereco("Rua A",77))

print(pessoa_1)