
#import pdb
#pdb.set_trace() 
def main():
	a=[1,3,4,5,1,2]
	t=duplicates(a)
	print(t)
	

def duplicates(a):
	d=len(a)

	for i in range(0,d-1):
		a[i]=hash(a[i])
	for j in range(0,d-1):
		k=j
		key=a[j]
		for k in range(0,d-1):
			if a[k]==key:
				s=[a[k],a[j]]
				break

	return s                   

if __name__=='__main__':
	main()