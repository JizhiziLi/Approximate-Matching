#
#   Bi-gram.py
#
#   Created by Jizhizi Li on 20/4/2015
#   The following codes reads content from two text file, treating one as queries,
#   the other as resources. It will go through all resources to check if there is
#   approximate queries in it. (Based on bi-gram algorithm.)
#   As a result, it will print out the ID of approximate items, and write it into file. 


#   This part opens the text file and turn it into array.
#   The third text file is used to write result in.

txtpath1 = r"queries.10K.txt"
txtpath2 = r"tweets.30K.txt"
txtpath3 = r"compare_of_bi_gram.txt"


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
#print(arrA[385])

#   This function delelte duplicate in one array

def deletedouble(arrany):
	arranynew=[]
	for i in arrany:
		if i not in arranynew:
			arranynew.append(i)
	arrany=arranynew		
	return arrany	

#   This function counts the bi-gram distance between two string.

def distance(a, b):
	a = a.upper()
	b = b.upper()
	arra = []
	arrb = []
	common = 0;
	

	for i in range(0,len(a)-1):
		arra.append(a[i]+a[i+1]);
		arra = deletedouble(arra);

	for j in range(0,len(b)-1):
		arrb.append(b[j]+b[j+1]);
		arrb = deletedouble(arrb);

	for i in range(0,len(arra)):
		for j in range(0,len(arrb)):
			if(cmp(arra[i],arrb[j])==0):
				common=common+1;
		distance = 0;
		distance = len(a)+len(b)-2-2*common;
	return distance;


#   The following code goes through text and write common part into the third text.

print("The following is the result of approximate matching based on two-gram, in which distance is smaller than one.")
fpc.write("\nThe following is the result of approximate matching based on two-gram, in which distance is smaller than one.\n\n\n")


wordOne = 0
wordTwo = 1
wordThree = 2
wordFour = 3
wordFive = 4


#   The range of lineOne means the line it will check.

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
					if(distance(arrA[lineOne].split()[wordOne],arrB[i].split()[j])<=1):
						#print(arrB[i].split()[j]);
						arrOne.append(arrB[i].split()[0])
			if(wordTwo<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordTwo])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(distance(arrA[lineOne].split()[wordTwo],arrB[i].split()[j])<=1):
						#print(arrB[i].split()[j]);
						arrTwo.append(arrB[i].split()[0])	
			if(wordThree<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordThree])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(distance(arrA[lineOne].split()[wordThree],arrB[i].split()[j])<=1):
						#print(arrB[i].split()[j]);
						arrThree.append(arrB[i].split()[0])
			if(wordFour<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordFour])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(distance(arrA[lineOne].split()[wordFour],arrB[i].split()[j])<=1):
						#print(arrB[i].split()[j]);
						arrFour.append(arrB[i].split()[0])	
			if(wordFive<len(arrA[lineOne].split())):
				if(len(arrA[lineOne].split()[wordFive])>2 and cmp(arrA[lineOne].split()[wordOne],'and')!=0):
					if(distance(arrA[lineOne].split()[wordFive],arrB[i].split()[j])<=1):
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
		











