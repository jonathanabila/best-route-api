from exceptions.internal_exception import InternalException


class InvalidEdges(InternalException):
    def __init__(self, message):
        self.message = message
        super(InvalidEdges, self).__init__(message, 500)

    def __repr__(self):
        return self.message
