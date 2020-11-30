from kb import KB
from fact import Fact
import sys
if __name__ == "__main__":

   inp_file = sys.argv[1]
   query = sys.argv[2]
   query.strip('"')
   
   kb = KB()
   with open(inp_file, 'r') as f_in:
      list_sentences = f_in.readlines()
      KB.declare(kb, list_sentences)
   
   print(query)
   
   alpha = Fact.parse_fact(query)
   substs = set(kb.query_forward_chaining(alpha))
   substs_str = ' ;\n'.join([str(subst) for subst in substs]) + '.\n'
   print(substs_str)


