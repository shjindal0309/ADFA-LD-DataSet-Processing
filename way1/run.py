import operator
import time
result=[]
def ngrams(input, n):
	input = input.split(' ')
	output = {}
	for i in range(len(input)-n+1):
		g = ' '.join(input[i:i+n])
		output.setdefault(g, 0)
		output[g] += 1
	return output
# https://docs.python.org/3/library/operator.html
# Source for itemgetter() function
# Return a callable object that fetches item from its operand 
# using the operands __getitem__() method. 
# If multiple items are specified, returns a tuple of lookup values. For example:
# After f = itemgetter(2), the call f(r) returns r[2].
# After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
# def itemgetter(*items):
#     if len(items) == 1:
#         item = items[0]
#         def g(obj):
#             return obj[item]
#     else:
#         def g(obj):
#             return tuple(obj[item] for item in items)
#     return g
def sort_ngrams(output): 
	input=sorted(output.items(),key=operator.itemgetter(1),reverse=True)
	return input

def top30percent(x):
	  length=len(x)*3/10
	  count=1
	  for i in x:
	  	if(count>length):
	  		break
	  	result.append(i[0])
	  	count+=1
def main(): 
	n=input("Enter n-gram value: ")

	#This assumes that your program takes at least a tenth of second to run.
	start_time = time.time() +0.1
	
	Allfiles=[]
	Adduser=("Adduser.txt","r")
	Hydra_FTP=("Hydra_FTP.txt","r")
	Hydra_SSH=("Hydra_SSH.txt","r")
	Java_Meterpreter=("Java_Meterpreter.txt","r")
	Meterpreter=("Meterpreter.txt","r")
	Web_Shell=("Web_Shell.txt","r")
	NormalData=("Normaldata.txt","r")

	Allfiles.append(Adduser)
	Allfiles.append(Hydra_FTP)
	Allfiles.append(Hydra_SSH)
	Allfiles.append(Java_Meterpreter)
	Allfiles.append(Meterpreter)
	Allfiles.append(Web_Shell)
	Allfiles.append(NormalData)

	train_dataset=open("output.txt","w")

	name=["Adduser","Hydra_FTP","Hydra_SSH","Java_Meterpreter","Meterpreter","Web_Shell","Normal"]
	
	names=["Adduser","Hydra_FTP","Hydra_SSH","Java_Meterpreter","Meterpreter","Web_Shell"]
	
	Adduser=[]
	Hydra_FTP=[]
	Hydra_SSH=[]
	Java_Meterpreter=[]
	Meterpreter=[]
	Web_Shell=[]
	Normal=[]

	Adduser_vector=[]
	Hydra_FTP_vector=[]
	Hydra_SSH_vector=[]
	Java_Meterpreter_vector=[]
	Meterpreter_vector=[]
	Web_Shell_vector=[]
	Normal_vector=[]

	Adduser_vector_final=[]
	Hydra_FTP_vector_final=[]
	Hydra_SSH_vector_final=[]
	Java_Meterpreter_vector_final=[]
	Meterpreter_vector_final=[]
	Web_Shell_vector_final=[]
	Normal_vector_final=[]

	count=0
	for i in range(1,65):
		count+=1
		s="Adduser"+str(count)+".txt"
		Adduser.append(s)
		s=""
	count=0
	for i in range(1,115):
		count+=1
		s="Hydra_FTP"+str(count)+".txt"
		Hydra_FTP.append(s)
		s=""
	count=0
	for i in range(1,124):
		count+=1
		s="Hydra_SSH"+str(count)+".txt"
		Hydra_SSH.append(s)
		s=""
	count=0
	for i in range(1,88):
		count+=1
		s="Java_Meterpreter"+str(count)+".txt"
		Java_Meterpreter.append(s)
		s=""
	count=0
	for i in range(1,54):
		count+=1
		s="Meterpreter"+str(count)+".txt"
		Meterpreter.append(s)
		s=""
	count=0
	for i in range(1,84):
		count+=1
		s="Web_Shell"+str(count)+".txt"
		Web_Shell.append(s)
		s=""
	count=0
	for i in range(1,834):
		count+=1
		s="Normaldata"+str(count)+".txt"
		Normal.append(s)
		s=""
	
	for j in Allfiles:
		output_temp=ngrams(open(j[0],j[1]).read(),n) # output_temp is dict
		sorted_elements=sort_ngrams(output_temp) #sort is list of tuples
		top30percent(sorted_elements)

	for i in Adduser:	
		output_temp=ngrams(open(i,"r").read(),n)
		Adduser_vector.append(output_temp)
	for i in Hydra_FTP:	
		output_temp=ngrams(open(i,"r").read(),n)
		Hydra_FTP_vector.append(output_temp)
	for i in Hydra_SSH:	
		output_temp=ngrams(open(i,"r").read(),n)
		Hydra_SSH_vector.append(output_temp)
	for i in Java_Meterpreter:	
		output_temp=ngrams(open(i,"r").read(),n)
		Java_Meterpreter_vector.append(output_temp)
	for i in Meterpreter:	
		output_temp=ngrams(open(i,"r").read(),n)
		Meterpreter_vector.append(output_temp)
	for i in Web_Shell:	
		output_temp=ngrams(open(i,"r").read(),n)
		Web_Shell_vector.append(output_temp)
	for i in Normal:	
		output_temp=ngrams(open(i,"r").read(),n)
		Normal_vector.append(output_temp)

	temp=[]
	for k in Adduser_vector:
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Adduser_vector_final.append(temp)
		temp=[]

	for k in Hydra_FTP_vector:
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Hydra_FTP_vector_final.append(temp)
		temp=[]

	for k in Hydra_SSH_vector:
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Hydra_SSH_vector_final.append(temp)
		temp=[]

	for k in Java_Meterpreter_vector:
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Java_Meterpreter_vector_final.append(temp)
		temp=[]

	for k in Meterpreter_vector:
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Meterpreter_vector_final.append(temp)
		temp=[]

	for k in Web_Shell_vector: 
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Web_Shell_vector_final.append(temp)
		temp=[]

	for k in Normal_vector: 
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		Normal_vector_final.append(temp)
		temp=[]

	feature_vector=[]
	feature_vector.append(Adduser_vector_final)
	feature_vector.append(Hydra_FTP_vector_final)
	feature_vector.append(Hydra_SSH_vector_final)
	feature_vector.append(Java_Meterpreter_vector_final)
	feature_vector.append(Meterpreter_vector_final)
	feature_vector.append(Web_Shell_vector_final)
	feature_vector.append(Normal_vector_final)
	
	index=0
	string_header=str(n)+"-grams feature vectors:\n\n"
	string_vector_final=""
	for k in feature_vector:
		for i in k:
			string2=""
			count=0
			for j in i:
				string2+=str(j[1])+" "
			string2+=name[index]+"\n\n"
			string_vector_final+=string2
		index+=1

	final_vector=string_header+string_vector_final
	train_dataset.write(final_vector)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print(final_string) # apply one tab here to get optiized format but that will disturb formatting
	
main()
