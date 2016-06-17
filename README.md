# T2 de Estruturas Discretas 2016.1

## Authors
* Hugo Grochau
* Gabriel Maia

# Questão 2
## Algorítimo

Ao ler o input, um grafo é criado da seguinte maneira:
* Para cada estação um nó é criado guardando a zona dessa estação
* Para cada conexão entre duas estações é criada uma aresta, guardando o número e tipo de linha (ônibus ou trem).

Após terminar de montar o gráfico, ini os seguintes váriaveis:
* lowest_cost = INF
* lowest_cost_path = []

Começando do nó (estação) inicial, executa-se o seguinte recursivamente:

Se estamos na estação final:
    Se o custo total é menor do que lowest_cost_path:
        lowest_cost <- custo total
        lowest_cost_path <- caminho
    Para

Para cada edge (conexão) que começa do nó corrente:
    Se for uma transferência entre ônibuses:
        inicie outra recursão com o custo <- custo + 1 e o nó corrente sendo a próxima estação

    Se for uma transferência entre um trem para um ônibus:
        inicie outra recursão com o custo <- custo + 1 e o nó corrente sendo a segunda estação

    Se for uma mudança de zona numa lina de trem:
        inicie outra recursão com o custo <- custo + 4 e o nó corrente sendo a segunda estação

    Se não for nenhum desses:
        inicie outra recursão com o nó corrente sendo a segunda estação

No final de toda recursão o lowest_cost será o menor custo e o lowest_cost_path será o menor caminho
