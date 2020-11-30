from kb import KB
from parser import *
import sys


def main():
    if len(sys.argv) > 3:
        return None
    
    with open(sys.argv[1], "r") as file:
        kb = parse_file(file)
        query_str = open(sys.argv[2], "r").readlines()

        for line in query_str:
            line = line.strip().replace("\n", "")
            query = parse_sentence(line)
            a , result = kb.resolution(query)
            print(line)
            if not a:
                print("False.\n")
                continue
            result_var = parse_result(query, result)
            if len(result_var) == 0:
                print("True.\n")
                continue
            for key, value in result_var.items():
                print(key + " = " + str(value))
            print('.\n')
        

if __name__ == "__main__":
    main()
