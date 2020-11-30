from term import Term

class Rule:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    
    def __str__(self):
        return str(self.head) + ":- " + str(self.tail)

    def __repr__(self):
        return str(self)   