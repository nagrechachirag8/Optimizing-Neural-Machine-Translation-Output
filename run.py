afile = open('eng.txt','r')
bfile = open('h1','r')
cfile = open('h2','r')
dfile = open('h3','r')
efile = open('h4','r')
ffile = open('temp_output.txt','r')
gfile=open("temp_output_utf8","r")

ofile = open('news_temp_result.txt','a')

stri = ' '

c = 0

while True:
	if(c%7 == 0):
		a=afile.readline()
		if(a==""):
			break
		ofile.write(a)
		ofile.write("\n")
	elif(c%7 == 1):
		a=bfile.readline()
		if(a==""):
			break
		ofile.write(a)
		
	elif(c%7 == 2):
		a=cfile.readline()
		if(a==""):
			break
		ofile.write(a)
		
	elif(c%7 == 3):
		a=dfile.readline()
		if(a==""):
			break
		ofile.write(a)
		
	elif(c%7 == 4):
		a=efile.readline()
		if(a==""):
			break
		ofile.write(a)
		ofile.write("\n")
		
	elif(c%7 == 5):
		a=ffile.readline()
		if(a==""):
			break
		ofile.write(a)
		
	elif(c%7 == 6):
		a=gfile.readline()
		if(a==""):
			break
		ofile.write(a)
		ofile.write("-------------------------------------------------------------------------------------------------\n")
		
	c+=1
		


		
		
