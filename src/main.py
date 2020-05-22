def main(grapher, file, file_name: str) -> None:
    routes = file.get_file_content(file_name, separator=",")
    graph = grapher(routes)

    while True:
        best_route, price = graph.calculate("ORL", "BRC")
        print(f"Best route: {best_route} > {price}")
        break


if __name__ == "__main__":
    import argparse

    from methods.dijsktra import Dijsktra
    from services.file import File

    parser = argparse.ArgumentParser(description="Find the least expensive path")
    parser.add_argument(
        "-f",
        "--file_name",
        dest="file_name",
        type=str,
        help="relative path to the file",
    )

    args = parser.parse_args()

    main(Dijsktra, File(), args.file_name)
