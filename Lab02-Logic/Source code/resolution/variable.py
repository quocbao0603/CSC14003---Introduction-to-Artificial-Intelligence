class Variable(object):
    def __init__(self, functor):
        self.functor = functor

    def match(self, functor):
        result = {}
        if self != functor:
            result[self] = functor
        return result

    def binding(self, matched):
        flag = matched.get(str(self))
        if flag:
            return flag.binding(matched)
        return self
        
    def __str__(self):
        return str(self.functor)        
        
    def __repr__(self):
        return str(self)

    