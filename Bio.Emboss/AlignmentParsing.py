file = open('needle.txt','r')
file = (file.read()).splitlines()
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

print query
print match
print ref