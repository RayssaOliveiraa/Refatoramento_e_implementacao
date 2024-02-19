from observador import Observador

class JogoWar:
    def __init__(self):
        self.__observadores = []

    @property  #CodeSmell 2
    def observadores(self):
        return self.__observadores

    def adicionarObservador(self, observador):
        self.__observadores.append(observador)

    def removerObservador(self, observador):
        self.__observadores.remove(observador)

    def notificarObservadores(self, vencedor):
        for observador in self.__observadores:
            observador.notificarCampeao(vencedor)
    #codesmell 1 
    def jogadorVence(self, vencedor):
        mensagem_vitoria = f"Jogador {vencedor} venceu o jogo!"
        self.notificarObservadores(vencedor)
        return mensagem_vitoria
    
    #antes de ajustar
    '''def jogadorVence(self, vencedor):
        print(f"Jogador {vencedor} venceu o jogo!")
        self.notificarObservadores(vencedor)'''
