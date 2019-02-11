from blastx_biopython import qblast

fname = raw_input("Enter .fasta file name : ")
fastafile=(open(fname,'r')).read()
result = qblast("blastx","nr",fastafile)

name=fname.split('.')[0]
save_file = open(name+"_x.xml",'w')
save_file.write(result)
save_file.close()
result.close()