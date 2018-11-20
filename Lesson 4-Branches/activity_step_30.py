# Activity

@classmethod
def distance(cls, unit, *args):
    distance = 0
    distance = reduce(lambda x, y: x*y, args)
    return "%s %s" %(distance, unit)
