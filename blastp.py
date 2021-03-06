# To search query sequence in NCBI BLAST and alignment ##

from Bio.Blast import NCBIWWW,NCBIXML

seq="MADKVLKEKRKLFIRSMGEGTINGLLDELLQTRVLNKEEMEKVKRENATVMDKTRALIDSVIPKGAQACQICITYICEEDSYLAGTLGLSADQTSGNYLNMQDSQGVLSSFPAPQAVQDNPAMPTSSGSEGNVKLCSLEEAQRIWKQKSAEIYPIMDKSSRTRLALIICNEEFDSIPRRTGAEVDITGMTMLLQNLGYSVDVKKNLTASDMTTELEAFAHRPEHKTSDSTFLVFMSHGIREGICGKKHSEQVPDILQLNAIFNMLNTKNCPSLKDKPKVIIIQACRGDSPGVVWFKDSVGVSGNLSLPTTEEFEDDAIKKAHIEKDFIAFCSSTPDNVSWRHPTMGSVFIGRLIEHMQEYACSCDVEEIFRKVRFSFEQPDGRAQMPTTERVTLTRCFYLFPGH"
result = NCBIWWW.qblast("blastp","nr",seq)

blast_records = NCBIXML.parse(result)


blast_record = next(blast_records)
print 'Length of sequence :'
print blast_record.query_length

alignment = blast_record.alignments[0]
print '\nSeq details:'
print (alignment.hit_def).split('>')[0]

print '\nAccession no.'
print alignment.accession