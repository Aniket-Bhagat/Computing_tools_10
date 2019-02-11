from Bio import Entrez
Entrez.email = "aniket.bhagat@students.iiit.ac.in"

'''
handle = Entrez.einfo()
# result = handle.read()
# print record.keys()
record = Entrez.read(handle)
handle.close()

print record[record.keys()[0]]
'''

# handle = Entrez.esearch(db="omim", term="huntington")
# record = Entrez.read(handle)

# print record

handle = Entrez.efetch(db="omim",id="613766")
print(handle.read())