def main():
	string1="apple"
	string2="nokia"
	result=swap(string1,string2)
	print("before swap "+ 'String1:'+string1+' String2:'+string2)
	print("after swap "+'String1:'+result[0]+' String2:'+result[1])
	return None

def swap(string1,string2):
	
	string2=string1 + string2
	string1=string2[len(string1):(len(string1)+len(string2))]

	string2=string2[0:len(string1)]
	return string1,string2

if __name__=='__main__':
	main()
