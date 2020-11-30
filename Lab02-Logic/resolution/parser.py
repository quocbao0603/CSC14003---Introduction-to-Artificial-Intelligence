from term import Term
from kb import KB
from sentence import Sentence
from variable import Variable


def parse_term(termstr):
    termstr = termstr.strip().rstrip('.').replace(' ', '')
    sep_idx = termstr.find("(")
    if termstr[0] == '~':
        negative = True
        termstr = termstr[1:]
        sep_idx-= 1
    else:
        negative = False
    functor = termstr[0:sep_idx]
    argsstr = termstr[sep_idx + 1: - 1].split(",")
    args = []
    for arg in argsstr:
        arg = arg.strip()
        if arg[0].isupper():
            args.append(Variable(arg))
        else:
            args.append(Term(arg))
    
    
    return Term(functor, args, negative)


def parse_sentence(sentencestr):
    terms = []
    sentencestr = sentencestr.strip().rstrip('.').replace(' ', '')
    sep_idx = sentencestr.find(':-')

    if sep_idx != -1:
        terms.append(parse_term(sentencestr[:sep_idx]))
        listtermstr = sentencestr[sep_idx + 2:].split("),")
        for idx, termstr in enumerate(listtermstr):
            termstr = termstr.strip()
            if idx != len(listtermstr) - 1:
                termstr = '~' + termstr + ')'
            else:
                termstr = '~' + termstr
            term = parse_term(termstr)
            terms.append(term)
    else:
        terms.append(parse_term(sentencestr))

    sentence = Sentence(terms)
    #print(str(sentence) + '\n')
    return sentence

def parse_file(file):
    lines = file.readlines()

    cmt_flag = 0
    rule_flag = 0
    rulestr = ""

    sentences = []

    for inp_line in lines:
        inp_line = inp_line.strip()
        if cmt_flag == 1 or inp_line.startswith("%"):
            continue
        if inp_line.startswith("/*"):
            cmt_flag = 1
            continue
        if inp_line.endswith("*/"):
            cmt_flag = 0
            continue

        if ":-" in inp_line:
            if(inp_line.endswith(".")):
                sentences.append(parse_sentence(inp_line))
                continue
            rulestr += inp_line
            rule_flag = 1
            continue


        if inp_line.endswith("."):
            if rule_flag == 1:
                rulestr += inp_line
                sentences.append(parse_sentence(rulestr))
                rulestr = ""
                rule_flag = 0
                continue
            sentences.append(parse_sentence(inp_line))
            
        if rule_flag == 1 and inp_line != "\n":
            rulestr += inp_line
            continue

        cmt_flag = 0
        rule_flag = 0
        rulestr = ""
        
    return KB(sentences)


def parse_result(query, result):
    var_flag = 0
    temp_query = query.arguments[0]
    for term in query.arguments[0].arguments:
        if isinstance(term, Variable):
            var_flag = 1
            break
    if var_flag == 0:
        return dict()
    while True:
        res_query = query.copy()
        for idx, arg in enumerate(res_query.arguments[0].arguments):
            if str(arg) in result:
                res_query.arguments[0].arguments[idx] = result[str(arg)]

        if res_query == query:
            return temp_query.match(res_query.arguments[0])
        query = res_query
def main():
    with open("first.txt", "r") as file:
        kb = parse_file(file)
        
        query = parse_sentence("vochong(tranthuantong, lethanhngau).")
        
        a, b = kb.resolution(query)
        
        print(b)
        print(a)
        print(parse_result(query, b))
        

if __name__ == "__main__":
    main()
