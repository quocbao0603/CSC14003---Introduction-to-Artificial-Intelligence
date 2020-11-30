#How to use:
#python3 backward_chaining.py hoanggia.kb "((husband ?x queenelizabethii))" 
#Output: ((husband pricephillip queenelizabethii))
#python3 backward_chaining.py hoanggia.kb "((husband princephillip queenelizabethii))"
#Output: True

import sys,getopt
import re
import uuid
import copy
import Utils
visited = []
operators = ['&&', '=>']
queries_vars = {}

#present Knowledge base
class KB:
    def __init__(self):
        self.clauses = {}

    def tell(self, clause):
        index_clauses(self,clause, clause)

    def ask(self, query):
        res = FOL_BC_ASK(self, query)
        return res
    def __repr__(self):
        return repr(self.clauses)

#contain array of predicate
#op-code is hashed for optimal memory
class Statement:
    def __init__(self, op, args = []):
        self.op = op
        self.args = list(map(make_class_statement, args))

    def __repr__(self):
        return  str(self.op) + " ".join([str(x) for x in self.args])

    def __hash__(self):
        temp=hash(self.op) ^ hash(tuple(self.args))
        return  temp

    def __eq__(self, other):
        return isinstance(other, Statement) and self.op == other.op and \
        self.args == other.args

#============================================================================#
#This Main part of Backward Algorithm
def FOL_BC_ASK(kb, query):
    #print(queries_vars)
    return FOL_BC_OR(kb, query, {})


def FOL_BC_OR(kb, goal, theta):

    if goal in visited: return
    visited.append(goal)
    #print(goal)
    rules_for_goal = fetch_rules_for_goal(kb, goal)
    for rule in rules_for_goal:
        standardized_rule = STANDARDIZE_VARIABLES(rule, copy.deepcopy(queries_vars))
        #*****
        lhs, rhs = lhs_rhs(standardized_rule)
        #print(lhs, rhs)
        unify_solution = UNIFY(rhs, goal, theta)

        for thetadash in FOL_BC_AND(kb, lhs, unify_solution):
            if goal in visited:
                visited.remove(goal)
            yield thetadash
    if goal in visited:
        visited.remove(goal)
        if visited != []:
            visited.pop()



temp_list = []
def FOL_BC_AND(kb, goals, theta):
    if theta is None:
        pass
    elif isinstance(goals, list) and len(goals) == 0:
        yield theta
    else:
        if goals.op == '&&':
            first = goals.args[0]
            second = goals.args[1]
            if first.op == '&&':
                while not is_predicate(first):
                    firstarg=first.args[1]
                    secondarg=second
                    temp=[firstarg, secondarg]
                    second = Statement('&&', temp)
                    first = first.args[0]
        else:
            first = goals
            second = []
        for thetadash in FOL_BC_OR(kb, SUBST(theta, first), theta):
            for thetaddash in FOL_BC_AND(kb, second, thetadash):
                if goals in visited:
                    visited.remove(goals)

                yield thetaddash

#end main part
#===========================================================================#

is_predicate = lambda clause: clause.op not in operators and clause.op[0] != '?'
is_variable = lambda clause: isinstance(clause, Statement) and clause.op[0] == '?'


def SUBST(theta, clause):
    if(isinstance(clause, Statement)):
        if is_variable(clause):
            if clause in theta:
                temp=theta[clause]
                return temp
            else:
                return clause
        else:
            temp=Statement(clause.op, (SUBST(theta, arg) for arg in clause.args))
            return temp
    else:
        return

def UNIFY(x, y, theta):

    if theta is None: return None
    elif x == y: return theta
    elif is_variable(x): return UNIFY_VAR(x, y, theta)
    elif is_variable(y): return UNIFY_VAR(y, x, theta) 
    elif isinstance(x, Statement) and isinstance(y, Statement):
        temp1 = UNIFY(x.op, y.op, theta)
        
        temp = UNIFY(x.args, y.args,temp1)
        if temp is visited:
            print("unify")
        return temp
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        #print("check(x, y)", x, y)
        temp1 = UNIFY(x[0], y[0], theta)
        temp = UNIFY(x[1:], y[1:], temp1)

        return temp

    return None

def UNIFY_VAR(var, x, theta):
    #print("================================")
    #print("var, x, theta", var, x, theta)
    if var in theta:
        thetavar = theta[var]
        temp = UNIFY(thetavar, x, theta)
        return temp
    else:
        theta_copy = theta.copy()
        theta_copy[var] = x

        return theta_copy

def index_clauses_predicate(kb,precedent,antecedent):
    if antecedent.op in kb.clauses:
        if precedent not in kb.clauses[antecedent.op]:
            kb.clauses[antecedent.op].append(precedent)
    else:
        kb.clauses[antecedent.op] = [precedent]

def index_clauses(kb, precedent, antecedent):
    if is_predicate(antecedent):
        index_clauses_predicate(kb,precedent,antecedent)

    elif antecedent.op in operators:
        index_clauses(kb,precedent, antecedent.args[0])
        index_clauses(kb,precedent, antecedent.args[1])


def fetch_rules_for_goal(kb, goal):
    all_clauses = []
    #print("TEST KB", kb)
    try:
        predicate = getclause(kb,goal)
        #print(predicate)
        if predicate in kb.clauses:
            temp=kb.clauses[predicate]
            #print(temp)
            return temp
    except:
        for key in kb.clauses.keys():
            all_clauses = all_clauses + kb.clauses[key]
        #print(all_clauses)
        return list(set(all_clauses))
    print("TEST all ", allClauses)

def getclause(kb, goal):
    if is_predicate(goal):
        goal_op=goal.op
        return goal_op
    else:
        firstarg=goal.args[0]
        temp=getclause(kb,firstarg)
        return temp


def imp_func(clause):
    implication_index = clause.index('=>')
    lhs = clause[:implication_index]
    rhs = clause[implication_index+1:]
    value = [lhs, rhs]
    return Statement('=>',value)


def and_func(clause):
    and_index = clause.index('&&')
    lhs = clause[:and_index]
    rhs = clause[and_index + 1:]
    value=[lhs, rhs]
    #print("Left ", lhs, 'Right ', rhs)
    return Statement('&&', value)

def make_class_statement(clause):
    #print("Check make ", clause)
    if isinstance(clause, Statement):
        return clause
    if '=>' in clause:
        return imp_func(clause)
    elif '&&' in clause:
        return and_func(clause)
    elif isinstance(clause, str):
        return Statement(clause)
    first = clause[0]
    last = clause[1:][0]
    #print( " check(first, last) " , first, last)
    return Statement(first,last)
    
def lhs_conversion(clause):
    if clause.op =='&&':
        first = lhs_conversion(clause.args[0])
        last = lhs_conversion(clause.args[1])
        value1= [first, last]
        value=Statement(clause.op,value1)
        return value
    else:
       return clause

    
def STANDARDIZE_VARIABLES(clause, standardized = None):
    if standardized is None:
        standardized = {}
    if not isinstance(clause, Statement):
        return clause
    if is_variable(clause):
        if clause in standardized:
            return standardized[clause]
        else:
            temp = Statement('?' + str(uuid.uuid4()))
            standardized[clause] = temp
            return temp
    else:
        return Statement(clause.op, (STANDARDIZE_VARIABLES(arg, standardized) for arg in clause.args))
        
def lhs_rhs(clause):
    if clause.op == '=>':
        arg1 = clause.args[0]
        temp = lhs_conversion(arg1)
        temp1 = clause.args[1]
        return temp, temp1
    else:
        emptylist=[]
        return emptylist, clause

if __name__ == "__main__":  
    clauses = open(sys.argv[1]).readlines()
    tmp_clauses = []
    for i in range(len(clauses)):
        #parse clause from command
        clauses[i] = re.sub(r"#.*", "", clauses[i])
        clauses[i] = re.sub(r"\s+", " ", clauses[i])
        if clauses[i].strip() != '':
            clauses[i] = clauses[i].strip() 
        else:
            continue
        #print("i", clauses[i])
        tmp_clauses.append(clauses[i])
    
    #convert clause from Prolog-Stardard
    clauses = Utils.convert_clause(tmp_clauses)

    queries_original = re.sub(r"\s+", " ", sys.argv[2]).strip()
    #print(queries_original)
    
    queries = Utils.convert_to_list(queries_original)
    
    for query in queries:
        for i in range(1, len(query)):
            if query[i][0] == '?':
                if not query[i] in queries_vars:
                    queries_vars[query[i]] = '?' + str(uuid.uuid4())
                    #print("{} --> {}".format(query[i], queries_vars[query[i]]))
                query[i] = queries_vars[query[i]]
    queries = [[x[0], x[1:]] for x in queries]
    #print(queries, sep = '\n')
    
    
    #print('\n'.join(clauses))
    #print("-----")
    #print(queries)
    #print("-----")
    
    kb=KB()
    #ok
    #print('==============================')
    for clause in clauses:
        tmp = Utils.parse_input(clause)
        #print("check tmp ", tmp, clause)
        x = make_class_statement(tmp)
        #print("Check clause ", x)
        kb.tell(x)
    
    
    #print("KB=\n{}".format(kb))
    visited=[]

    possible_solutions = []
    solution_exists = True
    
    #print(queries_vars)
    for i in range(len(queries)):
        possible_solutions.append([])
        #print("Query = {}".format(queries[i]))
        solutions = kb.ask(make_class_statement(queries[i]))
        #print("Test sol: ", solutions)
        current_result = False
        for ans in solutions:
            ans = {str(x):str(ans[x]) for x in ans.keys()}
            possible_solutions[-1].append(ans)
            #print("ans ", ans)
            current_result = True
        solution_exists &= current_result
        solution_exists &= all(x != [] for x in possible_solutions)
    #print("After")
    #print(possible_solutions, sep = '\n')
    '''
    In this part, we combine solutions for each subquery.
    e.x: 
    for ((P ?x ?y) (Q ?y ?z))
    (P ?x ?y) have 2 statements: (P X1 Y1) and (P X2 Y2) 
    (Q ?y ?z) also have 2 statements: (Q Y2 Z1), (Q Y3 Z2)
    the solution is: (P X2 Y2) (Q Y2 Z1) 
    '''
    if solution_exists:
        while len(possible_solutions) > 1 and possible_solutions[-1] != []:
            new_solutions = []
            for sol_1 in possible_solutions[-1]:
                for sol_2 in possible_solutions[-2]:
                    success = True
                    sol = {}
                    for x in sol_1.keys():
                        if not x in sol_2.keys() or sol_2[x] == sol_1[x]:
                            sol[x] = sol_1[x]
                        else:
                            success = False
                            break
                    if success:
                        for x in sol_2.keys():
                            sol[x] = sol_2[x]
                    if success:
                        new_solutions.append(sol)
            possible_solutions.pop()
            possible_solutions.pop()
            possible_solutions.append(new_solutions)
    solution_exists &= all(x != [] for x in possible_solutions)
    isYNQuestion = True
    if solution_exists:
        for ans in possible_solutions[-1]:
            substitution = queries_original
            for x in queries_vars.keys():
                if queries_vars[x] in ans.keys():
                    substitution = substitution.replace(x, ans[queries_vars[x]])
                    if isYNQuestion == True:
                        isYNQuestion = False
            if (isYNQuestion):print("True") 
            else: print(substitution)
        #print(possible_solutions)
    else:
        if (isYNQuestion): print("False")
        else: print("No solution")
    