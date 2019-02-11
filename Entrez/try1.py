from Bio.EUtils import HistoryClient
def omim_snp_search(dnsnp_id):
	client = HistoryClient.HistoryClient()
	articles = client.search(dnsnp_id, "omim")
	result = articles.efetch("summary")
	# how to parse the result??
	return result

print omim_snp_search("613766").read()

# https://openwetware.org/wiki/Harvard:Biophysics_101/2007/Notebook:Xiaodi_Wu/2007-3-20#Perform_OMIM_search