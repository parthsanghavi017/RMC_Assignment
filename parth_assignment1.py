#Question 1
sequence = input("Enter a DNA sequence:")
length =  len(sequence)
print(length)

#Question 2 
GCcont = 100 *((sequence.count("G")+ sequence.count("C")) / length)
print (GCcont, "percent is the GC cont")

#Question 3
mutated = sequence.replace("T" , "A")
print(mutated)

#Question 4 
half = length//2
A = sequence[half:]
B = sequence [:half]

print(A)
print(B)

#Question 5
seq = ("ATCGATAGATACAA") #Since ATA start from in POS 4
seq.find("ATA")


#Question 6 
seq_2 = {"UAAAAGGCGAGAUAAAUA"}
seq_2.find("UAG")
seq_2.find("UAA")
seq_2.find("UGA")

#Question 7 
delta = ("")
#delta.find('ACGTC')
#delta.find('CTAGT')
#delta.find('ATGCTA')

#Question 8 
input_seq = "ATGATAGATAGATGATATCGATAGTA"
len_input = len(input_seq)
input_half = len_input//2
second = input_seq[input_half:]
reversed_second = second[::-1]
print(reversed_second)

