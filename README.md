# T2 de Estruturas Discretas 2016.1

# Questão 2

## Prova

`T(s, U) | s ∈ U e U é o conjunto de vértices` = Conseguimos achar o menor caminho da vértice `s` para qualquer `u ∈ U`.

### TCB
`T(s, U) | size(U) = 1`: O único caminho é entre `s` e ele mesmo, de custo 0

### TPI
`T(s, U) -> T(s, U') | U' = U ∪ v`: Se sabemos todos os caminhos de menor custo entre `s` e cada vértice de `U`, ao adicionar `v`, basta achar a aresta de menor custo entre `v` e qualquer vértice (ui) de `U`. Desse modo também conseguimos o menor caminho entre `s` e `v`: `s -> ui ∪ ui-> v`.

## Algorítimo

Ao ler o input, um grafo não direcionado é criado da seguinte maneira:
* Para cada estação um nó é criado guardando a zona e o número desta estação
* Para cada par duas estações pertencentes à uma mesma linha é criada uma aresta com os seguintes dados:
    * O custo: 1 se for uma linha de ônibus, e z*4 se for uma linha de trem z sendo o número de transferências de zonas entre essas duas estações
    * O tipo de transporte: Podendo ser ônibus ou trem
    * O número da linha

Em seguida o algoritimo de Dijkstra é rodado em cima desse grafo com o nó inicial sendo o da estação de partida

Fazemos um backtracking no output do Dijkstra para achar o menor caminho entre o nó inicial o e nó final (da estação de destino)

## Tempos de execução
| Z  | S   | T  | B  | X  | Y   | time    |
|----|-----|----|----|----|-----|---------|
| 2  | 100 | 50 | 50 | 1  | 100 | 2.21 ms |
| 10 | 100 | 5  | 50 | 71 | 95  | 240 ms  |
| 30 | 100 | 50 | 50 | 1  | 100 | 7945 ms |
