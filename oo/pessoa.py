class Pessoa:
    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    andre = Pessoa(nome='André')
    wanderley = Pessoa(andre, nome='Wanderley')
    print(Pessoa.cumprimentar(wanderley))
    print(id(wanderley))
    print(wanderley.cumprimentar())
    print(wanderley.nome)
    print(wanderley.idade)
    for filho in wanderley.filhos:
        print(filho.nome)
