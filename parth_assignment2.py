# Q1. Write a program to find the second maximum GC value from the list also find the median GC value.
#     Gc values are as follows 30.5,12,54,23,84
#from typing import Sequence


GC = [30.5,12,54,23,84]
GC.sort()
length = len(GC)
print(GC)
last_second = length - 2 

print(GC[last_second])

# Q3. Check the presence of all the stop codons in the list ["UAA","UGC","AUAGCT","ATUA","UAG"]
List = ("UAA" ,"UGC","AUAGCT","ATUA","UAG")
print ("UAG" ,List.count("UAG"))
print ('UAA', List.count("UAA"))
print ('UGA', List.count("UGA"))

#Q4 Write a program to transcribe the sequence "ATGCTCGCGTAA"
sequence = ("ATGCTCGCGTAA")
A_trans = sequence.replace("T" , "U")
print(A_trans)

#Q5 Concatenate two lists of GC Values [30.5,12,54,23,84] and [12,45,54,32] 
#     and find the maxium and minum GC Values.
A = {30.5,12,54,23,84}
B = {12,45,54,32}

combined = A.union(B)
list_2 = list(combined)
list_2.sort()
print(list_2)
length_ = len(list_2)
maximum = list_2[length_ -1]
minimum = list_2[0]
print('maximum' , maximum)
print('minimum' , minimum)

