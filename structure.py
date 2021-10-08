from tabulate import *
import string
import itertools

count = 0

variable = "ABCDGHIJKLORSTUVWXYZ"

steps = "abcdghijklorstuvwxyz"

formcount = 0

formvar = "EFQPMN"

showSteps = True



values = {
	# "A" : [0,1,0,...1]
	# "B" : [1,1,0,....0]
	# "c" : [0,1,0,....1]
	# "d" : [1,1,0,....0]
	# "F" : [0,0,1,....1]
}

formulas = {
	# "c" : "(AvB)"
	# "d" : "(C>B)"
	# "F" : "(c^d)"
}

table = {
	# "A" : [0,1,0,...1]
	# "B" : [1,1,0,....0]
	# "(AvB)" : [0,1,0,....1]
	# "(C>B)" : [1,1,0,....0]
	# "(AvB)^(C>B)" : [0,0,1,....1]
}

def calculate():
	for name in formulas:
		formula = calc[name]

		values[name] = []

		if "n" in formula:
			for i in values[formula[formula.find("n") + 1]]:
				if i == 0:
					values[name].append(1)
				else:
					values[name].append(0)
			continue
		
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

def getVariables(vcount):
	
	global count
	count = 0
	variables = {}

	#create matrix in the form of [[0,1],[1,0],[1,1],[0,0]]
	data = list(map(list, itertools.product([0, 1],repeat=vcount)))


	#Generate Variables: A, B, C, D .....
	for i in range(vcount):
		variable = string.ascii_uppercase[count]
		count += 1
		
		variables[variable] = []

		for b in data:
			variables[variable].append(b[i])
	
	return variables

def getStruct(struct):
	global count
	global formcount
	global steps
	global formula
	maxdephth = 0

	samedephth = None

	

	while True:
		print(struct)
		print(formulas)

		if "n" in struct:
			#search for not operands in formula
			operant = "n"
			positions = [pos for pos, char in enumerate(struct) if char == operant]

			for i in positions:
				if struct[i + 1] == "(":
					continue
				name = steps[count]
				count += 1
				
				#add formula to dic
				formulas[name] = struct[i] + struct[i + 1]
				struct = struct.replace(formulas[name], name)
		
		

		if "(" not in struct:
			name = formvar[formcount]
			formcount += 1

			formulas[name] = struct
			break


		for i in range(len(struct)):
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
				cont = False

				for y in formulas:
					if formulas[y] == formula[1:-1]:
						for name in formulas: 
							struct = struct.replace("(" + formulas[name] + ")", name)
						cont = True
				
				if cont == True:
					break

						
				Identifier = steps[count]
				formulas[Identifier] = formula
				samedephth=None
				count +=1

	
		for name in formulas:
			struct = struct.replace(formulas[name], name)

#get variableCount
while True:
	try:
		variableCount = int(input("How Many Variables does your System need? \n"))
		break
	except ValueError:
		print("\n ------------------ \n\n\n pleease enter an integer \n\n\n ------------------ \n\n\n")


#starting manual
values = getVariables(variableCount)
print(tabulate(values, headers="keys", tablefmt='orgtbl'))

print("\n...... 'help' for command list ......\n")

#main window
while True:
	
	command = input()

	if command == "help":
		print("variable [number]              :   change variable number")
		print("[new formula]                  :   make new formulas")
		print("[variable = new formula]       :   make new formulas")
		print("steps [bool]                   :   show steps on/ off")
	

	elif "variable" in command:
		vcount = command[9:]

		try:
			vcount = int(vcount)
		except ValueError:
			print("\nERROR: \n enter integer \n")
		values = getVariables(vcount)

	elif "steps" in command:

		if command[7:] == "True":
			showSteps = True
		else:
			showSteps = False

	else:
		if "=" in command:
			var = command[0]
			formulas[var] = command[2:]

		else:
			formula = command
			print(formula)
			getStruct(formula)
			print(formulas)

	calc = {}

	for i in formulas:
		calc[i] = formulas[i].replace("(", "")
		calc[i] = calc[i].replace(")", "")

	if showSteps:
		step = formulas
	else:
		for i in formulas:
			if string.isupper(i):
				step[i] = formulas[i]
	
	print(calc)

	calculate()

	

					
	


	print(tabulate(values, headers="keys", tablefmt='orgtbl'))
