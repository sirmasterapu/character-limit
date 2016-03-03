f = open("Characterlimit.txt",'r')
contents = f.readlines()#Gets contents of File
f.close()
f = open("output.txt","w")

for item in contents:
	item = item[0:10]#Counts characters
	item = item.strip("\n")#Gets rid of extra \n
	f.write(item + "\n")

f.close()

	
	
	
		