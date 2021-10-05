import string

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