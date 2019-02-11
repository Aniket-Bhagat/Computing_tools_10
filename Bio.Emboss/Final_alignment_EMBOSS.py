import os

QueryF = 'alpha.faa'
RefF = 'beta.faa'
command = 'needle -outfile=temp.txt -asequence='+QueryF+' -bsequence='+RefF+' -gapopen=10 -gapextend=0.5'
os.system(command)

file = open('temp.txt','r')
file = (file.read()).splitlines()
os.remove('temp.txt')

alignment = file[31:-4]

query=[]
match=[]
ref=[]
for i in range(0,len(alignment),4):
	query.append((alignment[i])[21:-7])

for i in range(1,len(alignment),4):
	match.append((alignment[i])[21:])

for i in range(2,len(alignment),4):
	ref.append((alignment[i])[21:-7])


query = ''.join(query)
match = ''.join(match)
ref = ''.join(ref)

# print query
# print match
# print ref

for i in range(len(match)):
	if match[i]=='.':
		index=i
		print ref[index],'is replaced by',query[index],'at position',str(index+1)