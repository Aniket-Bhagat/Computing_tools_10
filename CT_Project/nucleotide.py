import os
from Tkinter import *

def DoEmboss(check):
	QueryF = 'alpha.faa'
	RefF = 'beta.faa'
	command = 'needle -outfile=temp.txt -asequence='+QueryF+' -bsequence='+RefF+' -gapopen=10 -gapextend=0.5'
	os.system(command)

	file = open('temp.txt','r')
	file = (file.read()).splitlines()
	
	if check==0:
		os.remove('temp.txt')
	else:
		os.rename('temp.txt','alignment.txt')


	os.remove('beta.faa')
	os.remove('alpha.faa')
	
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

	results = []
	for i in range(len(match)):
		if match[i]=='.':
			result = ref[i]+' is replaced by '+query[i]+' at position '+str(i+1)
			results.append(result)
	return '\n'.join(results)

#----------------------------------------------------------------------------------#

def SeqStats(refseq,r1,r2,r3,r4,r5,r6,r7,r8):
	data=refseq.get('0.1',END)
	data = ''.join(data.split()[1:])

	r1.insert('1.0', str(len(data))+' basepairs')

	r2.insert('1.0', str(data.count('G'))+' in Reference Sequence')

	r3.insert('1.0', str(data.count('C'))+' in Reference Sequence')

	r4.insert('1.0', str(data.count('T'))+' in Reference Sequence')

	r5.insert('1.0', str(data.count('A'))+' in Reference Sequence')
	
	GC = (data.count('G')+data.count('C'))*100
	r6.insert('1.0', str(float(GC)/float(len(data)))+' %')

	r7.insert('1.0', str(data.count('ATG')))

	r8.insert('1.0', str(data.count('TAA')+data.count('TAG')+data.count('TGA')))