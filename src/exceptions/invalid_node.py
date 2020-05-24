from exceptions.internal_exception import InternalException


class InvalidNode(InternalException):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super(InvalidNode, self).__init__()

    def __repr__(self):
        return self.message
