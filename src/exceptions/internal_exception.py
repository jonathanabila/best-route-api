class InternalException(Exception):
    def __init__(self, message, code):
        self._set_error_code(message, code)
        super(InternalException, self).__init__()

    def _set_error_code(self, message, code):
        if ":" in message:
            self.code = int(message.split(":")[0])
            self.message = message.split(":")[1]
        else:
            self.code = code
