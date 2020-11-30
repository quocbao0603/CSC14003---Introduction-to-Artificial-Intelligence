from fact import Fact
from unify import unify
from substitution import Substitution

class Rule:
   def __init__(self, head=Fact(), tails=[]):
      self.head = head        # Inferred fact
      self.tails = tails            # tails: list of facts

      self.tails.sort()
      self.dup_predicate = self.detect_dup_predicate()

   def __repr__(self):
      return '{} => {}'.format(' & '.join([str(cond) for cond in self.tails]), str(self.head))

   def copy(self):
      return Rule(self.head.copy(), self.tails.copy())

   def get_num_tails(self):
      return len(self.tails)


   def may_helpful(self, fact_functor):
      functors = set()
      for premise in self.tails:
         functors.add(premise.functor)
      return fact_functor in functors

   def may_triggered(self, new_facts):
      # Check if any fact pi in new_facts is unified with a premise in rule
      for new_fact in new_facts:
         for premise in self.tails:
            if unify(new_fact, premise, Substitution()):
               return True
      return False

   def detect_dup_predicate(self):
      num_tails = self.get_num_tails()
      for i in range(num_tails - 1):
         if self.tails[i].functor == self.tails[i + 1].functor:
            return True
      return False

   @staticmethod
   def parse_rule(rule_str):       
      # Example: daughter(Person, Parent) :- female(Person), parent(Parent, Person).
      rule_str = rule_str.strip().rstrip('.').replace(' ', '')
      sep_idx = rule_str.find(':-')

      # Get head (lhs) and tails (rhs) seperated by ':-'
      head = Fact.parse_fact(rule_str[: sep_idx])
      tails = []
      list_fact_str = rule_str[sep_idx + 2:].split('),')

      for idx, fact_str in enumerate(list_fact_str):
         if idx != len(list_fact_str) - 1:
            fact_str += ')'
         fact = Fact.parse_fact(fact_str)
         tails.append(fact)

      return Rule(head, tails)
