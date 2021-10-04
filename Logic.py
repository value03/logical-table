from tabulate import *
import string

import itertools

title = []

data = []

values = {}




alphabet = 0


	

def getStruct(struct, alphabet):
	alph = alphabet
	
	#
	structure = {}
	
	maxdephth = 0
	
	samedephth = None
	
	
	while True:
		
		#when to stop simplifying
		if '(' not in struct:
			identifier = string.ascii_lowercase[alph]
			structure[identifier] = "(" + struct + ")"
			alph += 1
			break
		
		
		#iterate trough input string z.B. (AvB)^(C>A)
		for i in range(len(struct)):
			
			#Identify lowest brackets
			
	#		(AvB)^(C>(A^B))
	#maxd.  111100111222210
	#samed. 0000nn0001111n
	#			 ^	  ^
	
	#			 |	  |
			
			#increase debth 
			if struct[i] == "(":
				samedephth = maxdephth
				start = i + 1
				maxdephth += 1
				
			
			elif struct[i] == ")":
				maxdephth -= 1
				
			#at index where the bracket closes add 'new var' : '(formula)' to structure
			if maxdephth == samedephth:
				Identifier = string.ascii_lowercase[alph]
				structure[Identifier] = struct[start-1:i+1]
				samedephth=None
				alph +=1
				
		
		#replace Identified formulas with variables
		#(AvB)^(C>(A^B))
		#  |        |
		#  d  ^(C>  e)    	
		for name in structure:
			struct = struct.replace(structure[name], name)
			
		
		print(struct)
		print('/n-----/n')
		print(structure)
			
			
			
		
			
	return structure, alph
	
	
	


def computeLogic(formula, name):
	
	variable1 = formula[0]
	operand = formula[1]
	variable2 = formula[2]

	values[name] = []
	title.append(name + ' = '  + formula)
	
	for i in range(len(values[variable1])):
		
		value1 = values[variable1][i]
		value2 = values[variable2][i]
		
		#logic operators
		if operand == 'v':
			if  value1 == 0 and value2 == 0:
				values[name].append(0)
				data[i].append(0)
				
			else:
				values[name].append(1)
				data[i].append(1)
					
					
		if operand == '^':
			if value1 == 1 and value2 == 1:
				values[name].append(1)
				data[i].append(1)
			else:
				values[name].append(0)
				data[i].append(0)
	
		
		if operand == '>':
			if value1 == 1 and value2 == 0:
				values[name].append(0)
				data[i].append(0)
			else:
				values[name].append(1)
				data[i].append(1)
					
					
	
#get variableCount
while True:
	try:
		variableCount = int(input("How Many Variables does your System need? \n"))
		break
	except ValueError:
		print("\n ------------------ \n\n\n pleease enter an integer \n\n\n ------------------ \n\n\n")
		
		
		
#create matrix in the form of [[0,1],[1,0],[1,1],[0,0]]
data = list(map(list, itertools.product([0, 1],repeat=variableCount)))



#Generate Variables: A, B, C, D .....
for i in range(variableCount):
	variable = string.ascii_uppercase[alphabet]
	alphabet += 1
	
	title.append(variable)
	values[variable] = []
	for b in data:
		values[variable].append(b[i])



print(tabulate(data, headers=title, tablefmt='orgtbl'))


while True:
	cycle = 0
	
	input2 = input("Add formula, type 'no' to abbort\n")
	
	if input2 == 'no':
		break

	#getting Sorted Bracket Dictonary
	structure, alphabet = getStruct(input2, alphabet)
	
	
	
	#compute logic tree
	for i in structure:
		#cut Brackets
		structure[i] = structure[i][1:len(structure[i]) - 1]
		
		computeLogic(structure[i], i)
		
		
		
	#variables[-1] = 'F-' + str(cycle) + ' = ' + input2
		
		
	print(tabulate(data, headers=title, tablefmt='orgtbl'))
	print(data)
	print(values)
		
	
		



