#
#   Soundex.py
#
#   Created by Jizhizi Li on 20/4/2015
#   The following codes reads content from two text file, treating one as queries,
#   the other as resources. It will go through all resources to check if there is
#   approximate queries in it. (Based on soundex algorithm.)
#   As a result, it will print out the ID of approximate items, and write it into file. 


#   This part opens the text file and turn it into array.
#   The third text file is used to write result in.
#   It also imports groupby from itertools, which is used in the soundex algorithm.


from itertools import groupby
txtpath1 = r"queries.1K.txt"
txtpath2 = r"tweets.3K.txt"
txtpath3 = r"compare_of_soundex.txt"


fpa = open(txtpath1)
fpb = open(txtpath2)
fpc = open(txtpath3,"a")

arrA = []
for linea in fpa.readlines():
	arrA.append(linea)


arrB = []
for lineb in fpb.readlines():
	arrB.append(lineb)

#   Print one detail array


#   This function delelte duplicate in one array

def deletedouble(arrany):
	arranynew=[]
	for i in arrany:
		if i not in arranynew:
			arranynew.append(i)
	arrany=arranynew		
	return arrany	


#   This function operates two string in soundex way, 
#   return 1 if the soundex description of two words are same.

def soundexCompare(a,b):
   codes = ("bfpv","cgjkqsxz", "dt", "l", "mn", "r")
   soundDict = dict((ch, str(ix+1)) for ix,cod in enumerate(codes) for ch in cod)
   cmap2 = lambda kar: soundDict.get(kar, '9')

   sdxa =  ''.join(cmap2(kar) for kar in a.lower())
   sdxb =  ''.join(cmap2(kar) for kar in b.lower())
   sdxfora2=a[0].upper() + ''.join(k for k,g in list(groupby(sdxa))[1:] if k!='9')
   sdxfora=sdxfora2[0:4].ljust(4,'0')
   sdxforb2=b[0].upper() + ''.join(k for k,g in list(groupby(sdxb))[1:] if k!='9')
   sdxforb=sdxforb2[0:4].ljust(4,'0')

   if(cmp(sdxfora,sdxforb)==0):
       return 1;




#for i in range(0,len(arrB)-1):
#	print(len(arrB[i].split())-1)


def deletedouble(arrany):
	arranynew=[]
	for i in arrany:
		if i not in arranynew:
			arranynew.append(i)
	arrany=arranynew		
	return arrany	


#   The following code goes through text and write common part into the third text.

print("The following is the result of approximate matching based on soundex algorithm.")
fpc.write("\nThe following is the result of approximate matching based on soundex algorithm.\n\n\n")


wordOne = 0
wordTwo = 1
wordThree = 2
wordFour = 3
wordFive = 4


for lineOne in range(1,100):
	print(lineOne)
	arrOne = [];
	arrTwo = [];
	arrThree = [];
	arrFour = [];
	arrFive = [];
	arrFinal = [];
	for i in range(0,len(arrB)):
		for j in range(0,len(arrB[i].split())):
			if(wordOne<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordOne])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(soundexCompare(arrA[lineOne].split()[wordOne],arrB[i].split()[j])==1):
						#print(arrB[i].split()[j]);
						arrOne.append(arrB[i].split()[0])
			if(wordTwo<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordTwo])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(soundexCompare(arrA[lineOne].split()[wordTwo],arrB[i].split()[j])==1):
						#print(arrB[i].split()[j]);
						arrTwo.append(arrB[i].split()[0])	
			if(wordThree<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordThree])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(soundexCompare(arrA[lineOne].split()[wordThree],arrB[i].split()[j])==1):
						#print(arrB[i].split()[j]);
						arrThree.append(arrB[i].split()[0])
			if(wordFour<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordFour])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(soundexCompare(arrA[lineOne].split()[wordFour],arrB[i].split()[j])==1):
						#print(arrB[i].split()[j]);
						arrFour.append(arrB[i].split()[0])	
			if(wordFive<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordFive])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(soundexCompare(arrA[lineOne].split()[wordFive],arrB[i].split()[j])==1):
						#print(arrB[i].split()[j]);
						arrFive.append(arrB[i].split()[0])					
				#print(arrB[i].split()[0]+arrB[i].split()[j]+ " and " +arrA[lineOne].split()[wordOne]);
				#print(arrB[i].split()[0]+arrB[i].split()[j]+ " and " +arrA[lineOne].split()[wordTwo]);
	#arrFinal.append("this is line"+str(lineOne)+" in queries: ");
	fpc.write("\nThis is line"+str(lineOne)+" in queries: ");
	arrOne = deletedouble(arrOne);
	arrTwo = deletedouble(arrTwo);
	arrThree = deletedouble(arrThree);
	arrFour = deletedouble(arrFour);
	arrFive = deletedouble(arrFive);
	#print(arrOne);
	#print(arrTwo);
	#print(arrThree);
	#print(arrFour);
	for i in range(0,len(arrOne)):
		for j in range(0,len(arrTwo)):
				if(cmp(arrOne[i],arrTwo[j])==0):
				#print(arrOne[i]);
				#arrFinal.append(arrOne[i]);
					fpc.write("No. ");
					fpc.write(arrOne[i]);
					print(arrOne[i]);
					fpc.write(" ");






