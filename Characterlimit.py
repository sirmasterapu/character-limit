f = open("Characterlimit.txt".'r')
contents = f.readlines()
f.close()
character = 0
characterList = []

for item in contents:
	character = 0
	
	for letter in item:
		character += 1
		
		while character <= 10:
			characterList.append(letter)
	characterList.append('\n')


output = ''
for item in characterList:
	output += item
	
f = open("output.txt",'w')

	
	
		