from observador import Observador

class Continente(Observador):
    def __init__(self, nome):
        self.nome = nome
        self.exercitos = 0
        self.proprietario = None

    #CodeSmell 3
    def notificarCampeao(self, vencedor):
        return f"Região {self.nome}: Jogador {vencedor} conquistou esta região com {self.exercitos} exércitos!"
    
    #ANTES
    '''def notificarCampeao(self, vencedor):
        print(f"Região {self.nome}: Jogador {vencedor} conquistou esta região!")'''
    

#Implementação da historia a baixo
    '''"Como jogador eu gostaria de colocar exércitos nos meus territórios. A quantidade de exércítos é um número inteiro e, 
    caso seja coloca em um território de outro jogador, a operação será negada."'''

    def adicionarExercitos(self, quantidade, jogador):
        if isinstance(quantidade, int) and quantidade > 0:
            if self.proprietario is None or jogador == self.proprietario:
                self.exercitos += quantidade
                self.proprietario = jogador
                print(f"{quantidade} exércitos adicionados à região {self.nome}. Total: {self.exercitos}")
            else:
                print("Operação negada: A região pertence a outro jogador.")
        else:
            print("Quantidade inválida de exércitos. Deve ser um número inteiro positivo.")

