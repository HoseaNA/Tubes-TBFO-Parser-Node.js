import re
import itertools
from pathlib import Path

left, right = 0, 1

# Menggabungkan dua list tanpa duplikat
def union(lst1, lst2):
    final_list = list(set().union(lst1, lst2))
    return final_list

# Mengelompokkan pembacaan file cfg menjadi terminal, variable, dan productions
def loadModel(modelPath):
    script_location = Path(__file__).absolute().parent
    file_location = script_location/modelPath
    file = open(file_location).read()
    K = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
    V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n","").replace("\n",""))
    P = (file.split("Productions:\n")[1])
    return cleanAlphabet(K), cleanAlphabet(V), cleanProduction(P)

# Membersihkan ekspresi grammar dari format cfg dan dikelompokkan menjadi
# rules dan hasil produksi
def cleanProduction(expression):
    result = []
    rawRulse = expression.replace('\n','').split(';')
    for rule in rawRulse:
        leftSide = rule.split(' -> ')[0].replace(' ','')
        rightTerms = rule.split(' -> ')[1].split(' | ')
        for term in rightTerms:
            result.append( (leftSide, term.split(' ')) )
    return result

# Memisahkan rules
def cleanAlphabet(expression):
    return expression.replace('  ',' ').split(' ')

# Menghapus produksi non terminal
def seekAndDestroy(target, productions):
    trash, ereased = [],[]
    for production in productions:
        if target in production[right] and len(production[right]) == 1:
            trash.append(production[left])
        else:
            ereased.append(production)
            
    return trash, ereased

# Menyimpan aturan produksi sebagai key dan value
def setupDict(productions, variables, terms):
    result = {}
    for production in productions:
        if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result

# Mengolah ulang aturan produksi yang ada dan menghapus berdasarkan target
def rewrite(target, production):
    result = []
    positions = [i for i,x in enumerate(production[right]) if x == target]
    for i in range(len(positions)+1):
         for element in list(itertools.combinations(positions, i)):
             tadan = [production[right][i] for i in range(len(production[right])) if i not in element]
             if tadan != []:
                 result.append((production[left], tadan))
    return result

# Mengubah aturan (dictionary) menjadi list
def dict2Set(dictionary):
    result = []
    for key in dictionary:
        result.append( (dictionary[key], key) )
    return result

# Mengubah bentuk aturan produksi menjadi string untuk dituliskan pada file
# output
def prettyForm(rules):
    dictionary = {}
    for rule in rules:
        if rule[left] in dictionary:
            dictionary[rule[left]] += ' | '+' '.join(rule[right])
        else:
            dictionary[rule[left]] = ' '.join(rule[right])
    result = ""
    for key in dictionary:
        result += key+" -> "+dictionary[key]+"\n"
    return result