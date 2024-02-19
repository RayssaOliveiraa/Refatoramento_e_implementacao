# Refatoramento_e_implementacao

# Jogo de Estratégia - War

Este é um projeto baseado no famoso jogo de tabuleiro War. 
O código foi desenvolvido como parte de uma atividade, na qual também inclui a implementação do padrão de "projeto Observer", implementada por outra pessoa anteriomente.

## Objetivo da Atividade

1. **Identificar Code Smells:**
   - Identificar pelo menos 5 code smells no código fornecido.
   - Descrever esses code smells no arquivo `code-smells.txt`.

2. **Refatoração:**
   - Refatorar o código para eliminar pelo menos 3 code smells identificados.

3. **Implementação de Nova Funcionalidade:**
   - Implementar a seguinte história: "Como jogador eu gostaria de colocar exércitos nos meus territórios. A quantidade de exércitos é um número inteiro e, caso seja colocado em um território de outro jogador, a operação será negada."

## Code Smells Identificados

1. **Método com Responsabilidade Mista:**
   - O método `jogadorVence` realiza duas tarefas distintas: imprimir a mensagem de vitória e notificar os observadores.

2. **Acesso Direto a Variáveis:**
   - A variável `__observadores` é uma lista acessada diretamente fora da classe `JogoWar`.

3. **Método NotificarCampeao Imprime Diretamente:**
   - O método `notificarCampeao` na classe `Continente` imprime diretamente.

4. **Nomes Poco Descritivos:**
   - Algumas variáveis, como `vencedor`, podem ser mais descritivas.

5. **Falta de Validação de Entrada:** (Ajustado quando foi implementado a lógica para a nova Historia) 
   - O método `jogadorVence` aceita qualquer número inteiro como vencedor, incluindo valores negativos.

## Refatorações Realizadas

1. **Método com Responsabilidade Mista:**
   - Separado o método `jogadorVence` em dois: um para notificar os observadores e outro para imprimir a mensagem de vitória.

2. **Acesso Direto a Variáveis:**
   - Criado um método `observadores` para encapsular o acesso à variável `__observadores`.

3. **Método NotificarCampeao Imprime Diretamente:**
   - Modificado o método `notificarCampeao` para retornar a mensagem em vez de imprimir diretamente.

## Nova Funcionalidade Implementada

- Adicionada a capacidade de adicionar exércitos a regiões. A quantidade de exércitos é um número inteiro, e a operação é negada se tentar adicionar a um território de outro jogador.

## Exemplo de Uso

# Exemplo de uso do jogo e adição de exércitos
# (Veja main.py)

lINK CONTENDO A EXPLICAÇÃO DO CÓDIGO: <https://youtu.be/pyXNeUg6J6Q>

