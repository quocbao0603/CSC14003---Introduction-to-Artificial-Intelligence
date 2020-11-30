from sentence import Sentence
from fact import Fact
from rule import Rule
from FOL_FC_ASK import FOL_FC_ASK

class KB:
   def __init__(self):
      self.facts = set()
      self.rules = []

   def add_fact(self, fact):
      self.facts.add(fact)

   def add_rule(self, rule):
      self.rules.append(rule)

   def query_forward_chaining(self, alpha):
      return FOL_FC_ASK(self, alpha)

   def get_potential_facts(self, rule):
      facts = []
      for fact in self.facts:
         if rule.may_helpful(fact.functor):
            facts.append(fact)
      return facts

   @staticmethod
   def declare(kb, list_sent_str):
      while list_sent_str:
         sent_str, list_sent_str = Sentence.next(list_sent_str)
         sent_type = Sentence.categorize(sent_str)
         if sent_type == 'fact':
            fact = Fact.parse_fact(sent_str)
            kb.add_fact(fact)
         elif sent_type == 'rule':
            rule = Rule.parse_rule(sent_str)
            kb.add_rule(rule)
