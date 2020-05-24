def main(grapher, file, inputer, file_name: str) -> None:
    routes = file.get_file_content(file_name, separator=",")
    graph = grapher(routes)

    while True:
        source, destination = inputer.get_input("Please enter the route (*-*): ")
        best_route, price = graph.calculate(source, destination)
        print(f"Best route: {best_route} > {price}")

        print()


if __name__ == "__main__":
    import argparse

    from domain.dijsktra import Dijsktra
    from services.file import File
    from services.input import Input

    parser = argparse.ArgumentParser(description="Find the least expensive path")
    parser.add_argument(
        "-f",
        "--file_name",
        dest="file_name",
        type=str,
        help="relative path to the file",
    )

    args = parser.parse_args()

    main(Dijsktra, File(), Input(), args.file_name)
