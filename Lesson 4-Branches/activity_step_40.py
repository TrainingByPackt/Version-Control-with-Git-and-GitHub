# Activity

@classmethod
def time(cls, unit, *args):
    time = 0
    time = reduce(lambda x, y: x/y, args)
    return time
