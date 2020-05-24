### Exceptions
To facilitate error handling, all errors that have some information about the application have their description below 
and which code accompanies it. Thus, messages can be improved or changed, but the code will never be replaced or 
changed if its meaning is not exactly as described.

1. Wrong edges data - The information used to build the graphic contains invalid information.
2. Edge n1 n2 already exists - The edge n1 and n2 is already registered.
3. Such source node doesn't exist - The source node is not registered.
4. Such destination node doesn't exist - The destination node is not registered.
5. Such nodes don't connect -Such nodes don't connect.

### Algoritmos considerados

1. [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
2. [A*](https://en.wikipedia.org/wiki/A*_search_algorithm)
3. [Greedy Best-First-Search](https://www.mygreatlearning.com/blog/best-first-search-bfs/)

### Bibliografia

##### Introduction to A*
https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
https://www.redblobgames.com/pathfinding/a-star/introduction.html

### Observações

O tópico `## Explicando ##` no desafio contém um exemplo incorreto, a rota mais barata que deveria ser exibida é **1**.
