class Input:
    @staticmethod
    def _get_input(message):
        return input(message)

    def get_input(self, message, separator="-"):
        raw_input = self._get_input(message)
        return raw_input.strip().split(separator)
