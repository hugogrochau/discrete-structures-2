# T2 de Estruturas Discretas 2016.1

## Authors
* Hugo Grochau
* Gabriel Maia

# Questão 2

## Prova
`T(start, finish, map<V, E>)` = É possível achar o todos os possíveis caminhos e seus custos entre start e finish pelo map.

### TCB
`T(start, finish, map<V, E>) | num_V = 1`: Estamos já no nosso destino, só existe um caminho e seu custo foi zero

### TPI
`T(start, finish, map<V, E>) | num_V = n -> T(start, finish, map<V, E>) | num_V = n+1`: Se sabemos todos os caminhos e seus custos de `T(start, finish, map) | num_V = n`, ao adicionar mais um nó (VN) precisamos pegar todos os caminhos que passam por nós visinhos de VN (VVs) e gerar novos caminhos a partir desses, calculando o custo adicional a partir das arestas entre os VVs e VN.

## Algorítimo

```
Ao ler o input, um grafo é criado da seguinte maneira:
* Para cada estação um nó é criado guardando a zona e o número desta estação
* Para cada conexão entre duas estações é criada uma aresta, guardando o número e tipo de linha (ônibus ou trem).
Após terminar de montar o gráfico, inicie as seguintes váriaveis:
* lowest_cost = INF
* lowest_cost_path = []

Começando do nó (estação) inicial, executa-se o seguinte recursivamente:

Adicione o nó corrente ao caminho

Se estamos na estação final:
    Se o custo total é menor do que lowest_cost_path:
        lowest_cost <- custo total
        lowest_cost_path <- caminho
    Termine

Para cada edge (conexão) que começa do nó corrente e não está no caminho:
    Se for uma transferência entre ônibuses:
        adicione 1 ao custo
        nó corrente <- conexão.destino
        inicie outra recursão

    Se for uma transferência entre um trem para um ônibus:
        adicione 1 ao custo
        nó corrente <- conexão.destino
        inicie outra recursão

    Se for uma mudança de zona numa lina de trem:
        adicione 4 ao custo
        nó corrente <- conexão.destino
        inicie outra recursão

    Se não for nenhum desses:
        nó corrente <- conexão.destino
        inicie outra recursão

No final de toda recursão o lowest_cost será o menor custo e o lowest_cost_path será o menor caminho
```
