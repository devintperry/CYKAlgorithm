# simplified grammar to use for the cyk algorithm implemented as a dictionary
# These are the productions for the simplified grammar in CNF
# 
# S -> FB
# B -> CB | b
# C -> a
# D -> b
# E -> CD
# F -> HB | CD
# G -> IB | a
# H -> EG
# I -> CG 

# this is the dictionary that stores the above CFG in CNF
productions = {
     "S": ["FB"],
     "B": ["b"],
     "C": ["a"],
     "D": ["b"],
     "E": ["CD"],
     "F": ["HB", "CD"],
     "G": ["IB", "a"],
     "H": ["EG"],
     "I": ["CG"]
    }


def cyk_algorithm(w):

    # capture length of input string
    str_length = len(w)

    # create N x N table where n is length of input string
    # initial values of the table will be ""
    table = []
    table_row = []
    for i in range(str_length):
        table_row = []
        for j in range(str_length):
            table_row.append("")
        table.append(table_row)

    # build list of variables, full non terminal productions (two capital letters)
    # and also a list to store terminals
    variables = []
    full_non_terminals = []
    terminals = []
    for i in range(str_length):
        # go through rules of the grammar
        for lhs, transition in productions.items():
            # add variables to variable list if not there
            if lhs not in variables:
                variables.append(lhs)
            # iterate through rhs list of rules
            for j in range(len(transition)):
                # if length is one then we know it is a terminal
                if len(transition[j]) == 1 and transition[j] not in terminals:
                    terminals.append(transition[j])
                # if length is more than one then we know this is a non terminal rule consisting of two non_terminals
                elif len(transition[j]) != 1 and transition[j] not in full_non_terminals:
                    full_non_terminals.append(transition[j])

    # iterate through length of string
    for i in range(str_length):
        # iterate through the variables of the grammar
        for var in variables:
            # check if a production exists of the form A -> x
            # where A is any non_terminal of the grammar and x is any terminal
            for x in terminals:
                if x in productions[var] and x == w[i]:
                    table[i][i] += var

    # fill in the rest of the table above the diagonal with the produced variables
    for index in range(str_length):
        if index == 0:
            continue
        else:
            for j in range(str_length-index):
                l = j + index
                for k in range(j, l):
                    for var in variables:
                        for nt in full_non_terminals:
                            if nt in productions[var]:
                                str1 = table[j][k]
                                str2 = table[k+1][l]
                                if nt[0] in str1 and nt[1] in str2:
                                    table[j][l] += var

    # for testing purposes print the initial table
    # print(variables)
    # print(full_non_terminals)
    # print(terminals)
    
    # for testing print the productions from the grammar map
    # print(productions)


# This is the test string for our grammar in CNF
# Pass testString to the CYK Algorithm to test membership of grammar
# CNF Grammar is hardcoded from result/output from of cfgtocnf.py
testString = "abb"
cyk_algorithm(testString)
