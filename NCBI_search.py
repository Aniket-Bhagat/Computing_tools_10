# To search query sequence in NCBI BLAST and alignment ##

from Bio.Blast import NCBIWWW,NCBIXML

fname = raw_input("Enter .fasta file name : ")
fastafile=(open(fname,'r')).read()
result = NCBIWWW.qblast("blastn","nt",fastafile)

name=fname.split('.')[0]
save_file = open(name+".xml",'w')
save_file.write(result.read())
save_file.close()
result.close()

'''
# result = open(name+".xml")
result = open("blast.xml")
blast_records = NCBIXML.parse(result)


blast_record = next(blast_records)
# print blast_record.query_id
# print blast_record.query_length


alignment = blast_record.alignments[0]
# print alignment.title
gi = (alignment.hit_id).split('|')[1]
print gi
# print alignment.hit_def
# print alignment.accession


hsp = alignment.hsps[0]
# print hsp.expect
# print hsp.query
# print hsp.match
# print hsp.sbjct
'''