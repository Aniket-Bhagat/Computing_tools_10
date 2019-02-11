from Bio.Emboss.Applications import NeedleCommandline
needle_cline = NeedleCommandline(asequence="alpha.faa", bsequence="beta.faa",gapopen=10, gapextend=0.5, outfile="needle.txt")
# print(needle_cline)

# aseq = "acgtggcc"
# bseq = "aaatttccggtt"
# needle_cline = NeedleCommandline(asequence="asis:"+aseq, bsequence="asis:"+bseq, gapopen=10, gapextend=0.5, outfile="needle.txt")
stdout, stderr = needle_cline()
# print stdout + stderr

print needle_cline


# from Bio import AlignIO
# alignments = list(AlignIO.parse("needle.txt", "emboss"))
# print(alignments[0])