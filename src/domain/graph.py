from domain.dijsktra import Dijsktra
from services.file import File


class Graph(Dijsktra):
    def __init__(self):
        routes = File().get_file_content("../dist/input-file.txt")
        super().__init__(routes)
