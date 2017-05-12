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
			break;
		result.append(i[0])
		count=count+1

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
	
	
	join=[]
	
	for j in Allfiles:
		output_temp=ngrams(open(j[0],j[1]).read(),n) # output_temp is dict
		join.append(output_temp) # join becomes list of dictionary
		sorted_elements=sort_ngrams(output_temp) #sorted_elements is list of tuples
		top30percent(sorted_elements)

	temp=[]
	final=[]

	for k in join: # seven times only
		for i in result: 
			flag=k.get(i,0) #O(1)time by get() function
			t=(i,flag)
			temp.append(t)
		final.append(temp)
		temp=[]
	
	index=0
	string_header=str(n)+"-grams feature vectors:\n\n"
	string_vector=""
	for i in final: # seven times only
		string1=""
		string2=""
		count=0
		for j in i:
			count=count+1
			string2+=str(j[1])+" "
			string1+="F"+str(count)+", "

		string1+="-----> " 
		string2+=name[index]+"\n\n"
		string_vector+=string1+string2
		index+=1
	
	final_vector=string_header+string_vector
	train_dataset.write(final_vector)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print(final_string) # apply one tab here to get optiized format but that will disturb formatting
	
main()
