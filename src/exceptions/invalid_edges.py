from exceptions.internal_exception import InternalException


class InvalidEdges(InternalException):
    def __init__(self, message):
        self.message = message
        self.code = 500
        super(InvalidEdges, self).__init__()

    def __repr__(self):
        return self.message
