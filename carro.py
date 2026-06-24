class Carro:
    def __init__(self, marca, modelo, placa, valorD):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.valorD = valorD
        self.__quilometragem = 0 
        self.disponivel = True

    def exibir(self):
        text_aparente = "Disponível" if self.disponivel == True else "Alugado"
        print(f"INFORMAÇÕES DO CARRO\nMarca: {self.marca}\nModelo: {self.modelo}\nPlaca: {self.placa}\nValor da diária: {self.valorD}\nQuilometragem: {self.__quilometragem}\nDisponibilidade: {text_aparente}")
    
    def alugar(self):
        if (self.disponivel == True):
            self.disponivel = False
            print("O carro foi alugado")
        else:
            print("O carro não está disponível para alugar")

    def devolver(self, quilometros_percorridos):
        if (self.disponivel == False and quilometros_percorridos > 0):
            self.disponivel = True
            self.__quilometragem = self.__quilometragem + quilometros_percorridos
            print("O carro foi devolvido com", quilometros_percorridos, "km a mais de quilometragem")
        else:
            print("Não é possível executar essa ação. Verifique se o carro já não foi devolvido ou se a quilometragem digitada é um número positivo!")
