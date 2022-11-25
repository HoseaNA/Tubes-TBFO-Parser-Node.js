import sys, supportFunc

left, right = 0, 1

A, B, prod = [],[],[]

variablesJar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z",
                "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "W1", "X1", "Y1", "Z1",
                "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "W2", "X2", "Y2", "Z2",
                "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "W3", "X3", "Y3", "Z3",
                "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "W4", "X4", "Y4", "Z4",
                "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "W5", "X5", "Y5", "Z5",
                "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6", "O6", "P6", "Q6", "R6", "S6", "T6", "U6", "W6", "X6", "Y6", "Z6",]

# Memastikan apakah rule memiliki produksi satu variabel
def unitary(rule, var):
	if rule[left] in var and rule[right][0] in var and len(rule[right]) == 1:
		return True
	return False

# Memastikan apakah rule memiliki produksi satu terminal
def simple(rule):
	if rule[left] in B and rule[right][0] in A and len(rule[right]) == 1:
		return True
	return False

# Menambahkan simbol S0 sebagai start symbol
def start(prod, var):
	var.append('S0')
	return [('S0', [var[0]])] + prod

# Menghapus unitary production dari suatu produksi
def unit(prod, var):
	i = 0
	result = changeUnitary(prod, var)
	tmp = changeUnitary(result, var)
	while result != tmp and i < 1000:
		result = changeUnitary(tmp, var)
		tmp = changeUnitary(result, var)
		i+=1
	return result

# Menghapus produksi yang tidak menghasilkan simbol terminal
def delete(prod):
	newSet = []
	outlaws, prod = supportFunc.removeTargetProd(target='e', prod=prod)
	for outlaw in outlaws:
		for production in prod + [e for e in newSet if e not in prod]:
			if outlaw in production[right]:
				newSet = newSet + [e for e in  supportFunc.rewrite(outlaw, production) if e not in newSet]
	return newSet + ([prod[i] for i in range(len(prod)) 
							if prod[i] not in newSet])

# Memastikan produksi merupakan unitary dan bisa diganti
def changeUnitary(rules, var):
	unitaries, result = [], []
	for aRule in rules:
		if unitary(aRule, var):
			unitaries.append( (aRule[left], aRule[right][0]) )
		else:
			result.append(aRule)
	for uni in unitaries:
		for rule in rules:
			if uni[right]==rule[left] and uni[left]!=rule[left]:
				result.append( (uni[left],rule[right]) )
	
	return result

# Menghapus produksi simbol, terminal, dan variabel yang tergabung
def term(prod, var):
	newProductions = []
	dictionary = supportFunc.makeDict(prod, var, terms=A)
	for production in prod:
		if simple(production):
			newProductions.append(production)
		else:
			for term in A:
				for index, value in enumerate(production[right]):
					if term == value and not term in dictionary:
						dictionary[term] = variablesJar.pop()
						B.append(dictionary[term])
						newProductions.append( (dictionary[term], [term]) )						
						production[right][index] = dictionary[term]
					elif term == value:
						production[right][index] = dictionary[term]
			newProductions.append( (production[left], production[right]) )
	return newProductions

# Menghapus produksi yang menghasilkan lebih dari 2 variabel
def bin(prod, var):
	result = []
	for production in prod:
		k = len(production[right])
		if k <= 2:
			result.append( production )
		else:
			newVar = variablesJar.pop(0)
			var.append(newVar+'1')
			result.append( (production[left], [production[right][0]]+[newVar+'1']) )
			i = 1
			for i in range(1, k-2 ):
				var1, var2 = newVar+str(i), newVar+str(i+1)
				var.append(var2)
				result.append( (var1, [production[right][i], var2]) )
			result.append( (newVar+str(k-2), production[right][k-2:k]) ) 
	return result

# Memulai konversi
if __name__ == '__main__':
	if len(sys.argv) > 1:
		path = str(sys.argv[1])
	else:
		path = 'cfg.txt'
	
	A, B, prod = supportFunc.pathLoader(path)
    
	prod = start(prod, var=B)
	prod = term(prod, var=B)
	prod = bin(prod, var=B)
	prod = delete(prod)
	prod = unit(prod, var=B)
	
	open('cnf.txt', 'w').write(	supportFunc.convertForm(prod) )