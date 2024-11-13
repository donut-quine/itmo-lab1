class NotPositiveLengthException(Exception):
    def __init__(self, length, *args):
        super().__init__("Length cannot be negative or zero! Given length: {length}", *args)
