class Space:
    def __init__(self, shape=(1,), dtype=float, name=None):
        self.name, self.shape, self.dtype = name, shape, dtype

    def __repr__(self):
        return "Space(%s, %s, %s)" % (self.name, str(self.shape), str(self.dtype).strip("<class>' "))


class Spec:
    def __init__(self, spaces, name=None):
        self.name, self.spaces = name, spaces

    def __repr__(self):
        return "Spec: %s\n%s" % (self.name, "\n".join(map(str, self.spaces)))