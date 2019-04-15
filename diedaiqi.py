from collections.abc import Iterable,Iterator


class Good():
    def __init__(self, _addr):
        self.addr = _addr

    def __iter__(self):
        return self

    def __next__(self):
        pass


g = Good()
print(isinstance(iter("g"), Iterator))