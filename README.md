# Programa de Solução do Problema da Torre de Hanoi

Este programa consiste em uma implementação em Python da função recursiva para resolver o problema da Torre de Hanoi. O objetivo do programa é calcular o número mínimo de movimentos necessários para transferir todos os discos de uma torre de origem para uma torre de destino, seguindo as regras do jogo.


## Como funciona o programa

1 - A função hanoi(n, source, target, auxiliary, moves) é a função recursiva responsável por resolver o problema da Torre de Hanoi.

- n representa o número de discos.
- source é o nome do pino de origem.
- target é o nome do pino de destino.
- auxiliary é o nome do pino auxiliar.
- moves é o número de movimentos até o momento.

2 - A função hanoi() verifica se há discos para serem movidos. Se houver, executa os seguintes passos:

- Chama recursivamente a função hanoi() para mover n-1 discos do pino de origem para o pino auxiliar.
- Move o disco n do pino de origem para o pino de destino.
- Incrementa o contador de movimentos.
- Chama recursivamente a função hanoi() para mover os n-1 discos do pino auxiliar para o pino de destino.

3 - O usuário é solicitado a inserir o número de discos através do comando num_discs = int(input("Insira o número de discos: ")).

4 - Os nomes dos pinos de origem, destino e auxiliar são inicializados: source = 'Origem', target = 'Destino', auxiliary = 'Auxiliar'.

5 - A variável moves é inicializada com zero para contar o número total de movimentos.

6 - A função hanoi() é chamada, passando os parâmetros adequados, para resolver o problema da Torre de Hanoi. O resultado é armazenado na variável moves.

7 - O programa exibe na tela o número total de movimentos realizados: `print(f'Total de movimentos: {moves}').

## Como usar o programa

 - Certifique-se de ter o Python instalado em seu ambiente de desenvolvimento.

 - Clone o repositório contendo o programa ou copie o código para o seu projeto.

 - Abra um terminal e navegue até o diretório onde o programa está localizado.

- Execute o programa digitando o comando python nome_do_arquivo.py no terminal.

- Insira o número de discos quando solicitado.

- Aguarde o programa calcular o número mínimo de movimentos e exibir o resultado na tela.

## Observações

Certifique-se de que o ambiente Python esteja configurado corretamente e que todas as dependências necessárias estejam instaladas para executar o programa sem erros.

Este programa utiliza uma abordagem recursiva para resolver o problema da Torre de Hanoi, o que significa que pode apresentar problemas de desempenho para um número muito grande de discos. Tenha isso em mente ao utilizar o programa.

Aproveite a experiência de resolver o desafiante problema da Torre de Hanoi!

