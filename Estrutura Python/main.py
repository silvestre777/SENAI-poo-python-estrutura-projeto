import os
from  models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidadefederativa import Unidade_Federativa
os.system("cls || clear")


pessoa_1 = Pessoa (7,"Silvestre", "08/07/2000", "71983169204","silvestrefelix071@gmail.com", Sexo.MASCULIUNO, 
                  Endereco("Rua A",77,"Portao preto","41180110","Salvador", Unidade_Federativa.BAHIA))
pessoa_2 = Pessoa(7,"Julia", "01/03/2006","71983169204","julia99@gmail.com",Sexo.FEMININO, 
                  Endereco("Rua A",7,"casa","41881220","Salvador",Unidade_Federativa.BAHIA))
print(pessoa_1)
print(pessoa_2)