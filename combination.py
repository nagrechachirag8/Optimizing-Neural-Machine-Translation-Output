#python comb.py eng-file h1-file h2-file h3-file h4-file google-op all-dic-file
import sys
ofile=open("temp_output.txt","a")
with open(sys.argv[1]) as f:
    e1 = f.readlines()

with open(sys.argv[2]) as f:
    h1 = f.readlines()

with open(sys.argv[3]) as f:
    h2 = f.readlines()

with open(sys.argv[4]) as f:
    h3 = f.readlines()

with open(sys.argv[5]) as f:
    h4 = f.readlines()

#with open(sys.argv[6]) as f:
 #   g = f.readlines()

with open(sys.argv[6]) as f:
    dic = f.readlines()
    dic1 = {}
    for wd1 in dic:
        wd = wd1.strip()
        key = wd.split(' ~ ')[0]
        val = wd.split(' ~ ')[1]
        if key in dic1:
            dic1[key] = dic1[key]+'/'+val
        else:
            dic1[key] = val



for (i,j,k,l,m) in zip(h1, h2, h3, h4,e1):
    wds1 = i.split()
    wds2 = j.split()
    wds3 = k.split()
    wds4 = l.split()
    ewds = m.split()
 

    wds_list = [wds1,wds2,wds3,wds4]
    len_list = [len(wds1),len(wds2),len(wds3), len(wds4)]
    index_max = max(range(len(len_list)), key=len_list.__getitem__)
    index_min = min(range(len(len_list)), key=len_list.__getitem__)

    h1_l = wds_list[0]
    h2_l = wds_list[1]
    h3_l = wds_list[2]
    h4_l = wds_list[3]

    h_longest = wds_list[index_max]
    h_smallest=wds_list[index_min]
    temp=[]
    comb_sent = []
    synonyms=[]
    comparison=[]
    
    #get syn wds for the longest sent
    for i in range(0,len(h_longest)):
        owd = h_longest[i]
        comb_sent.append(owd)
        if owd in dic1:
            syn_wds = dic1[owd].split('/')
            syn_wds_u = list(set(syn_wds))
        else:
            syn_wds_u = owd
        for swd in syn_wds_u:
            if swd in h1_l + h2_l + h3_l + h4_l and (swd != owd):
                #comb_sent[i] = comb_sent[i]+'/'+swd
                if(h_longest[i] in comb_sent):
                     comb_sent.remove(h_longest[i])
                comb_sent.append(h_longest[i]+'/'+swd)
                synonyms.append(swd)
                if (swd+"/0" in comb_sent):
                	comb_sent.remove(swd+"/0")   
               
        
        if (i< len(h1_l)):
            temp.append(h1_l[i])
        if (i< len(h2_l)):
            temp.append(h2_l[i])
        if (i< len(h3_l)):
            temp.append(h3_l[i])
        if (i< len(h4_l)):
            temp.append(h4_l[i])
       

        a=list(dict.fromkeys(temp))
        counter=0
        if(i+1 < len(h_smallest)):        
	        if ((h1_l[i+1]==h2_l[i+1]) and (h2_l[i+1]==h3_l[i+1]) and (h3_l[i+1]==h4_l[i+1])):
		        comparison=[h1_l[i] ,h2_l[i],h3_l[i],h4_l[i]]
        		comparison=list(dict.fromkeys(comparison))
		        stri=""
		        if(len(comparison)>1):
			        if(owd in comb_sent):
			                comb_sent.remove(owd)
		        	for i in comparison:
				        stri=i+"/"+stri
		        counter=1		
	        	comb_sent.append(stri.strip("/"))	
	                  
        if(counter==0):
        	for k in a:
        		if((k not in h_longest) and (k not in comb_sent) and (k not in synonyms)):
        			comb_sent.append( str(k)+"/0")
       
        temp.clear() 
    
   
    comb_sent = ' '.join(comb_sent).split()   
    b=list(dict.fromkeys(comb_sent))
    copy=(' '.join(b)) 
    ofile.write(str(copy))
    ofile.write("\n")

ofile.close()    







