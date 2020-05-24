import os


class File:
    @staticmethod
    def _path_to_file(file_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", file_path))

    @staticmethod
    def _convert_to_integer(items_to_convert):
        result = []
        for item in items_to_convert:
            try:
                result.append(int(item))
            except ValueError:
                result.append(item)

        return result

    @staticmethod
    def _parse_file(file, separator):
        return [i.strip("\n").split(separator) for i in file]

    def read_file(self, file_path):
        with open(self._path_to_file(file_path), "r") as file:
            return file.readlines()

    def get_file_content(self, file_name, separator=","):
        raw_file_content = self.read_file(file_name)
        return [
            self._convert_to_integer(line)
            for line in self._parse_file(raw_file_content, separator)
        ]

    def add_line(self, line, file_name):
        with open(self._path_to_file(file_name), "a") as file:
            file.write(line + "\n")
