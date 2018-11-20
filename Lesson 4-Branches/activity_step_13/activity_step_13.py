    # Activity
    
    @classmethod
    def speed(cls, unit, *args):
        speed = 0
        speed = reduce(lambda x, y: x*y, args)
        return "%s %s" %(speed, unit)
