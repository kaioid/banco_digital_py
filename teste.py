from models.cliente import Cliente
from models.conta import Conta


maria: Cliente = Cliente('Maria Sousa', 'sousamaria@gmail.com', '123.456.789-01', '02/09/1987')
joao: Cliente = Cliente('Joao Gomes', 'jgomes@gmail.com', '234.567.890-02', '08/07/1978')

# print(maria)
# print(joao)

contaf: Conta = Conta(maria)
contaa: Conta = Conta(joao)

# print(contaf)
# print(contaa)

