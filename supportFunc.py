import re
import itertools
from pathlib import Path

left, right = 0, 1

# Memisahkan rules
def alphabetCleanser(exp):
    return exp.replace('  ',' ').split(' ')

# Menggabungkan dua list tanpa duplikat
def unionOfList(list1, list2):
    final_list = list(set().union(list1, list2))
    return final_list

# Mengubah aturan (dictionary) menjadi list
def convertDictToArr(dict):
    result = []
    for key in dict:
        result.append( (dict[key], key) )
    return result

# Menyimpan aturan produksi sebagai key dan value
def makeDict(prod, var, terms):
    result = {}
    for production in prod:
        if production[left] in var and production[right][0] in terms and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result

# Mengelompokkan pembacaan file cfg menjadi terminal, variable, dan prod
def pathLoader(path):
    script_location = Path(__file__).absolute().parent
    file_location = script_location/path
    file = open(file_location).read()
    K = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
    V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n","").replace("\n",""))
    P = (file.split("Productions:\n")[1])
    return alphabetCleanser(K), alphabetCleanser(V), prodCleanser(P)

# Membersihkan ekspresi grammar dari format cfg dan dikelompokkan menjadi
# rules dan hasil produksi
def prodCleanser(exp):
    result = []
    rawRulse = exp.replace('\n','').split(';')
    for rule in rawRulse:
        leftSide = rule.split(' -> ')[0].replace(' ','')
        rightTerms = rule.split(' -> ')[1].split(' | ')
        for term in rightTerms:
            result.append( (leftSide, term.split(' ')) )
    return result

# Menghapus produksi non terminal
def removeTargetProd(target, prod):
    trash, ereased = [],[]
    for production in prod:
        if target in production[right] and len(production[right]) == 1:
            trash.append(production[left])
        else:
            ereased.append(production)
            
    return trash, ereased

# Mengolah ulang aturan produksi yang ada dan menghapus berdasarkan target
def rewrite(target, prod):
    result = []
    positions = [i for i,x in enumerate(prod[right]) if x == target]
    for i in range(len(positions)+1):
         for element in list(itertools.combinations(positions, i)):
             tadan = [prod[right][i] for i in range(len(prod[right])) if i not in element]
             if tadan != []:
                 result.append((prod[left], tadan))
    return result

# Mengubah bentuk aturan produksi menjadi string untuk dituliskan pada file
# output
def convertForm(rules):
    dict = {}
    for rule in rules:
        if rule[left] in dict:
            dict[rule[left]] += ' | '+' '.join(rule[right])
        else:
            dict[rule[left]] = ' '.join(rule[right])
    result = ""
    for key in dict:
        result += key+" -> "+dict[key]+"\n"
    return result