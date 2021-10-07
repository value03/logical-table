from tabulate import *
import string

import itertools

values = {}

formulas = {}



numbers = 0

alphabet = 0


	

def getStruct(struct, alphabet):
	
	alph = alphabet
	
	maxdephth = 0
	
	samedephth = None


	matches = ["v", "^", ">"]

	
	
	while True:
		
		#when to stop simplifying
		if '(' not in struct:
			if "n" in struct:
				formula = struct
				operand = "n"
				positions = [pos for pos, char in enumerate(formula) if char == operand]

				for i in positions:
					if any(x in struct for x in matches):
						print("found operand")
						name = string.ascii_lowercase[alph]
					else:
						name = string.ascii_uppercase[alph]
					alph += 1

					#add formula to dic
					formulas[name] = "(" + formula[i] + formula[i + 1] + ")"
					struct = struct.replace(formula[i] + formula[i + 1], name)
				
				
			if any(x in struct for x in matches):
				identifier = string.ascii_uppercase[alph]
				formulas[identifier] = "(" + struct + ")"
				alph += 1
				break
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
				formula = struct[start-1:i+1]
				if "n" in formula:
					#search for not operands in formula
					operand = "n"
					positions = [pos for pos, char in enumerate(formula) if char == operand]

					for i in positions:
						name = string.ascii_lowercase[alph]
						alph += 1
						
						#add formula to dic
						formulas[name] = formula[i] + formula[i + 1]
						
				else:
					Identifier = string.ascii_lowercase[alph]
					formulas[Identifier] = formula
					samedephth=None
					alph +=1
				
		
		#replace Identified formulas with variables
		#(AvB)^(C>(A^B))
		#  |        |
		#  d  ^(C>  e)    	
		for name in formulas:
			struct = struct.replace(formulas[name], name)
			
		
		print(struct)
		print('/n-----/n')
		print(formulas)
			
			
			
		
			
	return alph
	


def computeLogic(formula, name):

	values[name] = []

	if "n" in formula:
		for i in values[formula[1]]:

			if i == 0:
				values[name].append(1)
			else:
				values[name].append(0)
		return
	
	variable1 = formula[0]
	operand = formula[1]
	variable2 = formula[2]
	
	for i in range(len(values[variable1])):
		
		value1 = values[variable1][i]
		value2 = values[variable2][i]
		
		#logic operators
		if operand == 'v':
			if  value1 == 0 and value2 == 0:
				values[name].append(0)
				
			else:
				values[name].append(1)
					
					
		if operand == '^':
			if value1 == 1 and value2 == 1:
				values[name].append(1)
			else:
				values[name].append(0)
	
		
		if operand == '>':
			if value1 == 1 and value2 == 0:
				values[name].append(0)
			else:
				values[name].append(1)
					
	
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
	
	values[variable] = []
	for b in data:
		values[variable].append(b[i])



print(tabulate(values, headers="keys", tablefmt='orgtbl'))

showSteps = False

while True:
	cycle = 0
	
	input2 = input("Add formula, type 'no' to abbort\n")
	
	if input2 == 'no':
		break

	input2 = input2.replace(" ", "")


	if input2 == 'showSteps=True':
		showSteps = True
		continue
	elif input2 == 'showSteps=False':
		showSteps = False
		continue

	


	#getting Sorted Bracket Dictonary
	alphabet = getStruct(input2, alphabet)
	
	print(formulas)
	
	
	#compute logic tree
	for i in formulas:
		#cut Brackets
		holder = formulas[i].replace("(", "") 
		holder = holder.replace(")", "")

		print(i + "\n" + holder)
		
		computeLogic(holder, i)
		
		
		
	#variables[-1] = 'F-' + str(cycle) + ' = ' + input2

	print(values)
	copy = values
	print(copy)

	tablediv = {}

	for i in values:
		tablediv[i] = values[i]
	

	if showSteps == False:
		for i in list(tablediv):
			if i in string.ascii_lowercase:
				del tablediv[i]
	
	for i in range(20):
		print("\n - \n")
		print(tablediv)
		print("\n - \n")
		found = False
		for y in list(tablediv):
			print("checking {}".format(y))
			for x in list(y):
				print("---  checking {}".format(x))
				for z in formulas:
					if z == x:
						print("found")
						print("bevore")
						print(str(tablediv) + "         " + str(values))
						try:
							tablediv[y.replace(z, formulas[z])] = tablediv.pop(y)

							print("after")
							print(str(tablediv) + "         " + str(values))
							found = True
							continue
						except:
							pass

		
		if found == False:
			break

	print(copy)
	print(values)
	values = copy
		
		
	 

	


		
	print(tabulate(tablediv, headers="keys", tablefmt='orgtbl'))
	print(tabulate(values, headers="keys", tablefmt="fancy_grid"))
	print(formulas)
	print(values)
	print(tablediv)
		
	
		



