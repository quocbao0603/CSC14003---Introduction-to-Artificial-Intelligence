
#list
import re

#return string res is a predicate
def convertPredicate(clause):
    isRule = False
    arr = []
    res = []
    tmp = []
    
    for i in range(len(clause)):
        c = clause[i]
        #end a predicate
        if (c == ')'):
            arr.append(''.join(tmp))
            tmp = []
            res.append(arr)
            arr = []
        elif(c == '-'):
            isRule = True
        elif(c.isalpha()):
            if (c.isupper()):
                tmp.append('?')
            tmp.append(c)
        elif(c != ' ' and len(tmp) > 0):
            arr.append(''.join(tmp))
            tmp = []
    #print("clause ", clause)
    if (isRule):
        tmp = res[0]
        for i in range(len(res) - 1):
            res[i] = res[i + 1]
        res[-1] = tmp
    #print(res)
    for i in range(len(res)):
        tmp = ""
        for j in res[i]:
            if (tmp == ""):
                tmp = tmp + j
            else:
                tmp = tmp + " " + j
        res[i] = tmp
    #print("test res ", res)
    return res, isRule


def convert_clause(clauses):
    #print("input ", clauses)
    element = []
    arr = []
    for clause in clauses:
        tmp, isRule = convertPredicate(clause)
        #check a statement
        relation = ""
        for i in tmp:
            if (len(relation) > 0): relation = relation + ' (' + i + ')'
            else: relation = relation + '(' + i + ')'
        relation = '(' + relation + ')'
        if (len(relation) > 0):arr.append(relation)
    #print("check Convert ", arr, sep = "\n")
    return arr

def convert_to_list(clause):
    arr = []
    for c in clause[1:-1]:
        if c == '(':
            sym = []
        elif c == ')':
            arr.append(''.join(sym).split(' '))
        else:
            sym.append(c)
    return arr

def parse_input(clause, goal=False):
    #print("check parse", clause)
    funcs = convert_to_list(clause)
    if len(funcs) > 1:
        res = [[x[0], x[1:], "&&"] for x in funcs]
        res[-1] = res[-1][:-1]
        if not goal:
            res[-2][-1] = "=>"
    else:
        res = [[x[0], x[1:]] for x in funcs]
    res = [x for y in res for x in y]
    #print("check parse1", res)
    return res
