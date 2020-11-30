class Fact:
   def __init__(self, functor='', arguments=[]):
      self.functor = functor               # Relation or function
      self.arguments = arguments           # Varibles and constants

   def __repr__(self):
      return '{}({})'.format(self.functor, ', '.join(self.arguments))

   def __lt__(self, rhs):
      if self.functor != rhs.functor:
         return self.functor < rhs.functor
      return self.arguments < rhs.arguments

   def __eq__(self, rhs):
      if self.functor != rhs.functor:
         return False
      return self.arguments == rhs.arguments

   def __hash__(self):
      return hash(str(self))
   
   def copy(self):
      return Fact(self.functor, self.arguments.copy())

   def get_arguments(self):
      return self.arguments

   def get_functor(self):
      return self.functor

   @staticmethod
   def parse_fact(fact_str):
      fact_str = fact_str.strip().rstrip('.').replace(' ', '')
      sep_idx = fact_str.index('(')

      functor = fact_str[:sep_idx]
      arguments = fact_str[sep_idx + 1 : -1].split(',')
      return Fact(functor, arguments)
