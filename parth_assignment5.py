#Question 1
start, end = 1, 20
for number in range(start, end):
    if number % 2 !=0:
        print(number, end= " " )


#Question 2
start, end = 1, 20
for numbr in range(start, end):
    if numbr % 2 ==0:
        x= reversed(str(numbr))
        print(x, end= " " )

#Question 3 
def factorial(n): 
	fact=1 
	for i in range(1,n+1): 
		fact=fact*i 
	return fact 
 
n=int(input("Enter number 'N': ")) 
f=factorial(n) 
print('Factorial is: ',f) 

#question 4 
def Gc_content(seq):
    length = len(seq)
    GC_count = (seq.count("G") + seq.count("C"))
    GC_content = 100 * (GC_count / length)
    return GC_content

seq=["ATAGTAAAA","ATGATAGATAAT","ATAGATGATA","ATAAAATAGGCCGA","ATAGCCAGCTAGATA","AGCTAGCA"]
for i in seq:
    print(Gc_content(i))

#Question 5 
list1 = [Gc_content(i) for i in seq]
print(list1)
print("Most GC content is is:", max(list1))

#Question 6
ids=["YC1","YC2","YC1","YC3","YC2"]
# using naive method to get count 
# of each element in string 
ids_freq = {}
  
for i in ids:
    if i in ids_freq:
        ids_freq[i] += 1
    else:
        ids_freq[i] = 1
print ("Count of all characters in GeeksforGeeks is :\n " +  str(ids_freq))