from sentence import *
from term import Term
import itertools


class KB:
    def __init__(self, sentences):
        self.sentences = sentences

    def __str__(self):
        return ".\n".join(str(sentence) for sentence in self.sentences)
    
    def __repr__(self):
        return str(self)


    def resolution(self, alpha):
        state = False
        step = []
        alpha = alpha.negative()
        sentences = set(self.sentences)
        sentences.add(alpha)
        vars = dict()
        while True:
            new_sentences = set()
            for (ci, cj) in itertools.combinations(sorted(sentences), 2):
                resolver, cur_state, var = ci.resolve(cj)
                new_sentences.update(resolver)
                state |= cur_state
                if var is not None:
                    vars.update(var)
            
            generated_senteces = sorted(differences_sentences(new_sentences, sentences))
            step.append(generated_senteces)
            sentences.update(new_sentences)
            if state:
                return True, vars
            if not generated_senteces:
                return False, vars




