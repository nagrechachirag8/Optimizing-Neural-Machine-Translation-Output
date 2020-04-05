ofile=open("temp_output_wx",'r')
afile=open("removed_matra.txt",'a')
stri=" "
temp=[]
while stri:
	a=ofile.readline()
	if (a==""):
		break
	r=a.split(" ")
	#print(r)
	for i in range(len(r)):
		b=r[i].upper()
		if(b[-1]=='0'):
			if(r[i-1].upper()==b[:-2]):
				
				st=r[i].strip("/0")
				item=r[i-1]+"/"+st
				temp.append(item)
				temp.pop(i-1)

			elif(r[i-1].upper().strip("/0")==b[:-2]):
				
				st=r[i].strip("/0")
				prev=r[i-1].strip("/0")
				item=prev+"/"+st
				temp.append(item)
				temp.remove(r[i-1])
						
			else:
				temp.append(r[i])
		
		elif(r[i].upper()==r[i-1].upper().strip("/0")):
			prev=r[i-1].strip("/0")
			item=prev+"/"+r[i]
			temp.append(item)
			temp.remove(r[i-1])
			
		else:
			temp.append(r[i])
	
	# for lengh between 3,4 to 6
	for i in range(len(temp)):
		item=temp[i].upper().strip("/0")
		for j in range(i+1,len(temp)):
			if( 4<= len(temp[i].strip("/0")) <= 6):
				wrd=temp[j][:3].upper().strip("/0")
				full_wrd=temp[j].upper().strip("/0") #paso
				count=len(list(set(item).intersection(full_wrd)))
				if((item[:3]==wrd) or ((count>len(item)-2) and (item[:1]==full_wrd[:1]))):
					temp[i]=temp[i].strip("/0")+"/"+temp[j].strip("/0")
					temp[j]="_"
			elif((len(temp[i].strip("/0"))==3) and (len(temp[j].strip("/0"))==3)): # ala ela
				wrd=temp[j].upper().strip("/0")
				if((item[:2]==wrd[:2]) or (item[1:]==wrd[1:])):
					temp[i]=temp[i].strip("/0")+"/"+temp[j].strip("/0")
					temp[j]="_"
	for k in temp:
		if(k=="_"):
			temp.remove(k)	
	counter=[] # for length > 5 and difference of 0 or 1
	for i in range(len(temp)):
		if ("/" in temp[i] and '0' not in temp[i]):
			pass
		else:
			wrd=temp[i].upper().strip("/0")
			if(len(wrd) > 5):
				for k in range(i+1 ,len(temp)):
					wrd2=temp[k].upper().strip("/0")
					diff=abs(len(wrd)-len(wrd2))
					if(diff in [0,1]):
						count=len(list(set(wrd).intersection(wrd2)))
						if((len(list(wrd))-2  <= count <=len(list(wrd)) or(len(list(wrd2))-2  <= count <=len(list(wrd2)))) and wrd[:2]==wrd2[:2]):
							temp[i]=temp[i].strip("/0") + "/" + temp[k].strip("/0")
							counter.append(k)
					elif(diff == 2):
						count=len(list(set(wrd).intersection(wrd2)))
						if(count==len(wrd)):
							temp[i]=temp[i].strip("/0") + "/" + temp[k].strip("/0")
							counter.append(k)
					
					else:
						pass
	

	for k in range(len(temp)):
		if(k in counter):
			temp[k]="_"
	for k in temp:
		if(k=="_"):
			temp.remove(k)	
	#print(temp)			
		
	copy=(' '.join(temp)) 
	#print(copy)
	
	afile.write(str(copy))
	#afile.write("\n")
	temp.clear()
	counter.clear()	
	
afile.close()
