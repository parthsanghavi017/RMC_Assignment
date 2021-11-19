bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN","S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET","WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN" }
bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN","S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET","WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN" }
#Question 1
int = bcell_bepipred.intersection(bcell_iedb)
print('common epitopes', int) #common sentences

#Question 2
ideb_unique =  bcell_iedb - bcell_bepipred 
print("present in ideb" , ideb_unique)
length_ide = len(ideb_unique)

#Question 3 
bipepr_unique =  bcell_bepipred- bcell_iedb
length_bip = len(bipepr_unique)
print(bipepr_unique , ideb_unique)

#Question 4
print(length_bip + length_ide)



list = ("UAA" ,"UGC","AUAGCT","ATUA","UAG")
print('UAA' , list.count("UAA"))