#Função recursiva para resolver o problema da torre de hanoi
def hanoi(n, source, target, auxiliary, moves):
    if n > 0:
        # Move os discos n-1 do pino de origem para o pino auxiliar
        moves = hanoi(n-1, source, auxiliary, target, moves)
        # Move o disco n do pino de origem para o pino de destino
        print(f'Mover disco {n} de {source} para {target}')
        moves += 1
        # Move os discos n-1 do pino auxiliar para o pino de destino
        moves = hanoi(n-1, auxiliary, target, source, moves)
    return moves

# Pedir ao usuário o número de discos
num_discs = int(input("Insira o número de discos: "))

# Inicializar os pinos de origem, destino e auxiliar
source = 'Origem'
target = 'Destino'
auxiliary = 'Auxiliar'

# Inicializar a variável de contagem de movimentos
moves = 0

# Chamar a função hanoi para resolver o problema
moves = hanoi(num_discs, source, target, auxiliary, moves)

# Imprimir o número total de movimentos
print(f'Total de movimentos: {moves}')
