import itertools

from fact import Fact
from unify import unify
from substitution import Substitution

def SUBST(facts_1, facts_2): #SUBST
   if len(facts_1) != len(facts_2):
      return False

   for f1, f2 in zip(facts_1, facts_2):
      if f1.get_functor() != f2.get_functor():
         return False

   return unify(facts_1, facts_2, Substitution())

def FOL_FC_ASK(kb, alpha):
   res = set()
   # check alpha in kb
   for fact in kb.facts:
      phi = unify(fact, alpha, Substitution())
      if phi:
         if phi.empty():
            res.add('true')
            return res
         res.add(phi)


   while True:
      new_facts = set()

      for rule in kb.rules:
         if not rule.may_triggered(kb.facts):
            continue

         num_tails = rule.get_num_tails()
         # Get facts in rule
         potential_facts = kb.get_potential_facts(rule)

         # Check if rule contains tails with the same predicate
         if not rule.dup_predicate:        
            potential_tails = itertools.combinations(sorted(potential_facts), num_tails)
         else:
            potential_tails = itertools.permutations(potential_facts, num_tails)

         for tuple_tails in potential_tails:
            tails = [tail for tail in tuple_tails]
            theta = SUBST(rule.tails, tails)
            if not theta:
               continue
                        
            new_fact = rule.head.copy()
            theta.substitute(new_fact)
            
            if new_fact not in new_facts and new_fact not in kb.facts:
               new_facts.add(new_fact)
               phi = unify(new_fact, alpha, Substitution())
               if phi:
                  if phi.empty():
                     kb.facts.update(new_facts)
                     res.add('true')
                     return res
                  res.add(phi)

      if not new_facts:
         if not res:
            res.add('false')
         return res
      kb.facts.update(new_facts)
