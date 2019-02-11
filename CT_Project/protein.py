def GetProtein(string):
	string = string.split('\n')
	string = ''.join(string[1:])
	seq = list(string)
	
	def translate(seq):
		codontable = {
			'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
			'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
			'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
			'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
			'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
			'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
			'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
			'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*','TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
			}
	
		frame1=[]
		count=0
		while(len(seq)>3):
			codon=seq.pop(0)+seq.pop(0)+seq.pop(0)
			if codontable[codon] == 'M':
				count=1
			if count>0:
				if codontable[codon] == '*':
					count=0
				frame1.append(codontable[codon])
		
		return ''.join(frame1)
	
	def revcomp(seq):
		seq=seq[::-1]
		base={'A':'T','T':'A','G':'C','C':'G'}
		seq=map(lambda x : base[x], seq)
		return seq
	
	translated=[]
	for i in range(3):
		translated.extend(translate(seq[i:]).split('*'))
	seq = revcomp(seq)
	for i in range(3):
		translated.extend(translate(seq[i:]).split('*'))
	
	return max(translated,key=len)

#--------------------------------------------------------------------------------------#

def CompareProtein(seq1,seq2):
	results=[]
	for i in range(len(seq1)):
		if seq1[i]!=seq2[i]:
			result = seq2[i]+' is replaced by '+seq1[i]+' at position '+str(i+1)
			results.append(result)

	return '\n'.join(results)

#--------------------------------------------------------------------------------------#

# To search reference sequence in NCBI BLAST ##

from Bio.Blast import NCBIWWW,NCBIXML;
import os;from Tkinter import *

def blast(refseq,r1,r2,r3):

	seq=refseq.get('0.1',END)
	
	result = NCBIWWW.qblast("blastp","nr",seq)
	
	blast_records = NCBIXML.parse(result)
	
	blast_record = next(blast_records)
	r1.insert('1.0',str(blast_record.query_length))
	
	alignment = blast_record.alignments[0]
	r2.insert('1.0',((alignment.hit_def).split('>')[0]))
	
	r3.insert('1.0',str(alignment.accession))