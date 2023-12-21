from auxiliaradm import AuxiliarAdministrativo
from gerente import Gerente
from rh import Rh

novaFolha = Rh()

gerente = Gerente("Thiago", 36, "879.383.003-76")
auxiliar = AuxiliarAdministrativo("Nicolas", 22, "631.772.106-40")

gerente.gerenciaPessoal = novaFolha

gerente.gerenciaPessoal.registraFuncionario(gerente)
gerente.gerenciaPessoal.registraFuncionario(auxiliar)

novaFolha.mostraFuncionarios()