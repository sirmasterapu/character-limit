f = open("Characterlimit.txt",'r')
contents = f.readlines()
f.close()
f = open("output.txt","w")

for item in contents:
	item = item[0:10]
	item = item.strip("\n")
	f.write(item + "\n")



	
	
	
		