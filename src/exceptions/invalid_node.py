from exceptions.internal_exception import InternalException


class InvalidNode(InternalException):
    def __init__(self, message):
        self.message = message
        super(InvalidNode, self).__init__(message, 400)

    def __repr__(self):
        return self.message
