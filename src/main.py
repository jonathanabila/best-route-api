from src.services.graph import Graph

if __name__ == "__main__":
    import timeit

    graph = Graph(
        [
            ("GRU", "BRC", 10),
            ("BRC", "SCL", 5),
            ("GRU", "CDG", 75),
            ("GRU", "SCL", 20),
            ("GRU", "ORL", 56),
            ("ORL", "CDG", 5),
            ("SCL", "ORL", 20),
        ]
    )

    print(graph.dijkstra("GRU", "CDG"))

    print(
        timeit.timeit(
            "graph=Graph([('GRU', 'BRC', 10),('BRC', 'SCL', 5),('GRU', 'CDG', 75),('GRU', 'SCL', 20),('GRU', 'ORL', 56),('ORL', 'CDG', 5),('SCL', 'ORL', 20)]); graph.dijkstra('GRU', 'CDG')",
            setup="from src.services.graph import Graph",
        )
    )
