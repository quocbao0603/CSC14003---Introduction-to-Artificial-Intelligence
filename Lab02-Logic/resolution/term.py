from variable import Variable
from utils import *
class Term(object):
    def __init__(self, functor, arguments = [], negative = False):
        self.functor = functor
        self.arguments = arguments
        self.negative = negative

    def match(self, term):
        if isinstance(term, Variable):
            return term.match(self)
        
        if isinstance(term, Term):
            if self.functor != term.functor or len(self.arguments) != len(term.arguments):
                return None
            matching = list(zip(self.arguments, term.arguments))

            matched = [
                argument[0].match(argument[1])
                for argument in matching
            ]
            result = {}
            for dic in matched:
                if dic is None:
                    return None
                for key, value in dic.items():
                    result[str(key)] = value
            
            return result

    def binding(self, variables):
        return Term(self.functor, [argument.binding(variables) for argument in self.arguments], self.negative)

    def compliment(self, other):
        return self.functor == other.functor and len(self.arguments) == len(other.arguments) and self.negative != other.negative

    def is_pointless(self, other):
        return self.functor == other.functor and len(self.arguments) == len(other.arguments) and self.negative != other.negative

    def is_same_term(self, other):
        return self.functor == other.functor and len(self.arguments) == len(other.arguments)
    
    def clone(self):
        return Term(self.functor + '', self.arguments[:], self.negative == True)

    

    def notterm(self):
        return Term(self.functor, self.arguments, not self.negative)
    
    def var_to_constant(self, var, constant):
        for idx, i in enumerate(self.arguments):
            if i == var:
                self.arguments[idx] = Term(constant)

    def __str__(self):
        neg = ""
        if self.negative == True:
                neg  = "~"
        if len(self.arguments) == 0:
            return neg + str(self.functor)
        else:
            return neg + str(self.functor) + "(" + ", ".join(str(argument) for argument in self.arguments) + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.functor == other.functor and self.arguments == other.arguments and self.negative == other.negative

    def __lt__(self, other):
        if(self.functor[0] != other.functor[0]):
            return self.functor[0] < other.functor[0]
        for i, j in zip(self.arguments,other.arguments):
            if i != j:
                return i.functor[0] < j.functor[0]
        if self.negative == other.negative:
            return False
        else:
            return self.negative

def main():
    knownTerm = Term('father_child', [Term('eric'), Term('thorne'), Term('a')])
    x = Variable('X')
    y = Variable('Y')
    goal = Term('father_child', [Term('eric'), Term('a'), Term('a')])
    bindings = goal.match(knownTerm)
    print(bindings)
    term = goal.binding(bindings)
    print(term)

if __name__ == "__main__":
    main()

