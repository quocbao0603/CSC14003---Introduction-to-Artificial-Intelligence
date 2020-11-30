from term import Term
class Sentence():
    def __init__(self, arguments = []):
        if len(arguments) == 0:
            self.arguments = []
        self.arguments = arguments
        self.arguments.sort()

    def binding(self, variable):
        self.arguments = [argument.binding(variable) for argument in self.arguments]
        self.arguments.sort()
    
    def clone_except(self, term):
        clone = Sentence([])
        for i in self.arguments:
            if i != term:
                clone.arguments.append(i.clone())
        return clone

    def is_pointless(self):
        for i in range(len(self.arguments) - 1):
            if self.arguments[i].is_pointless(self.arguments[i + 1]):
                return True
        return False
    
    def copy(self):
        arguments = [argument.clone() for argument in self.arguments]
        return Sentence(arguments)

    def __eq__(self, other):
        if len(self.arguments) != len(other.arguments):
            return False
        sorted(self.arguments)
        sorted(other.arguments)
        for idx, argument in enumerate(self.arguments):
            if argument != other.arguments[idx]:
                return False
        return True
    
    def is_in(self, term):
        for argument in self.arguments:
            if argument.is_same_term(term):
                return True
        return False

    def add(self, term):
        self.arguments.append(term)

    def negative(self):
        return Sentence([argument.notterm() for argument in self.arguments])

    def __len__(self):
        return len(self.arguments)
    
    def __str__(self):
        return " or ".join(str(argument) for argument in self.arguments)
    
    def __hash__(self):
        return id(self)

    def __lt__(self, other):
        if len(self.arguments) != len(other.arguments):
            return len(self.arguments) < len(other.arguments)
        else:
            for idx, arg in enumerate(self.arguments):
                if arg != other.arguments[idx]:
                    return arg < other.arguments[idx]
        return False
   

    def merge(self, sentences):
        for argument in sentences.arguments:
            if not self.is_in(argument):
                self.arguments.append(argument)
        sorted(self.arguments)
    

    def __repr__(self):
        return str(self)

    def resolve(self, other): 
        resolve_flag = False
        result = set()
        result_sentence = set()
        matches = dict()
        for argi in self.arguments:
            for argj in other.arguments:
                neg = argi.compliment(argj)
                matched = argi.match(argj.notterm())
                if matched is not None and neg:
                    clone_other = other.clone_except(argj)
                    result_sentence = self.clone_except(argi)
                    result_sentence.merge(clone_other)
                    if result_sentence.is_pointless():
                        continue
                    if len(result_sentence) == 0:
                        resolve_flag = True
                    vara = dict()
                    for k,v in matched.items():
                        if k != str(v):
                            vara[k] = v
                    matched = vara
                    if len(matched) != 0:
                        result_sentence.binding(matched)
                    result.add(result_sentence)
                    matches.update(matched)


        return result, resolve_flag, matches



def differences_sentences(sen1, sen2):
    result = set()
    for seni in sen1:
        flag = 1
        for senj in sen2:
            if seni == senj:
                flag = 0
                break
        if flag == 1:
            result.add(seni)
    return result
