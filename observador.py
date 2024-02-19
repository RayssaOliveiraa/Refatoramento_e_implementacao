from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def notificarCampeao(self, vencedor):
        pass
