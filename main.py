from continente import Continente
from jogo_war import JogoWar

if __name__ == "__main__":
    
    america_do_norte = Continente("América do Norte")
    asia = Continente("Ásia")

    
    jogo = JogoWar()
    jogo.adicionarObservador(america_do_norte)
    jogo.adicionarObservador(asia)

  
    jogador1 = 1
    america_do_norte.adicionarExercitos(10, jogador1)

    
    jogador2 = 2
    america_do_norte.adicionarExercitos(5, jogador2)

    
    mensagem_vitoria = jogo.jogadorVence(jogador1)
    print(mensagem_vitoria)

    
    asia.adicionarExercitos(8, jogador2)

   
    mensagem_vitoria2 = jogo.jogadorVence(jogador2)
    print(mensagem_vitoria2)
