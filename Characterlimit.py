f = open("Characterlimit.txt".'r')
contents = f.readlines()
f.close()
f = open("output.txt","w")

for item in contents:
	item = item[0:10]
	f.write(item + "\n")



	
	
	
		