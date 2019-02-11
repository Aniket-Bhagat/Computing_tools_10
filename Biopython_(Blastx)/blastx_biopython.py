from urllib import urlencode as _urlencode
from urllib2 import urlopen as _urlopen, Request as _Request
from io import StringIO


NCBI_BLAST_URL = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

def _as_bytes(s):
		"""Turn a (byte) string or a unicode string into a (byte) string."""
		return str(s)

_as_string = _as_bytes

def _parse_qblast_ref_page(handle):
	"""Extract a tuple of RID, RTOE from the 'please wait' page (PRIVATE).

	The NCBI FAQ pages use TOE for 'Time of Execution', so RTOE is probably
	'Request Time of Execution' and RID would be 'Request Identifier'.
	"""
	s = _as_string(handle.read())
	i = s.find("RID =")
	if i == -1:
		rid = None
	else:
		j = s.find("\n", i)
		rid = s[i + len("RID ="):j].strip()

	i = s.find("RTOE =")
	if i == -1:
		rtoe = None
	else:
		j = s.find("\n", i)
		rtoe = s[i + len("RTOE ="):j].strip()

	if not rid and not rtoe:
		# Can we reliably extract the error message from the HTML page?
		# e.g.  "Message ID#24 Error: Failed to read the Blast query:
		#		Nucleotide FASTA provided for protein sequence"
		# or	"Message ID#32 Error: Query contains no data: Query
		#		contains no sequence data"
		#
		# This used to occur inside a <div class="error msInf"> entry:
		i = s.find('<div class="error msInf">')
		if i != -1:
			msg = s[i + len('<div class="error msInf">'):].strip()
			msg = msg.split("</div>", 1)[0].split("\n", 1)[0].strip()
			if msg:
				raise ValueError("Error message from NCBI: %s" % msg)
		# In spring 2010 the markup was like this:
		i = s.find('<p class="error">')
		if i != -1:
			msg = s[i + len('<p class="error">'):].strip()
			msg = msg.split("</p>", 1)[0].split("\n", 1)[0].strip()
			if msg:
				raise ValueError("Error message from NCBI: %s" % msg)
		# Generic search based on the way the error messages start:
		i = s.find('Message ID#')
		if i != -1:
			# Break the message at the first HTML tag
			msg = s[i:].split("<", 1)[0].split("\n", 1)[0].strip()
			raise ValueError("Error message from NCBI: %s" % msg)
		# We didn't recognise the error layout :(
		# print s
		raise ValueError("No RID and no RTOE found in the 'please wait' page, "
						 "there was probably an error in your request but we "
						 "could not extract a helpful error message.")
	elif not rid:
		# Can this happen?
		raise ValueError("No RID found in the 'please wait' page."
						 " (although RTOE = %s)" % repr(rtoe))
	elif not rtoe:
		# Can this happen?
		raise ValueError("No RTOE found in the 'please wait' page."
						 " (although RID = %s)" % repr(rid))

	try:
		return rid, int(rtoe)
	except ValueError:
		raise ValueError("A non-integer RTOE found in "
						 "the 'please wait' page, %s" % repr(rtoe))

def qblast(program, database, sequence, url_base=NCBI_BLAST_URL,
			auto_format=None, composition_based_statistics=None,
			db_genetic_code=None, endpoints=None, entrez_query='(none)',
			expect=10.0, filter=None, gapcosts=None, genetic_code=None,
			hitlist_size=50, i_thresh=None, layout=None, lcase_mask=None,
			matrix_name=None, nucl_penalty=None, nucl_reward=None,
			other_advanced=None, perc_ident=None, phi_pattern=None,
			query_file=None, query_believe_defline=None, query_from=None,
			query_to=None, searchsp_eff=None, service=None, threshold=None,
			ungapped_alignment=None, word_size=None,
			alignments=500, alignment_view=None, descriptions=500,
			entrez_links_new_window=None, expect_low=None, expect_high=None,
			format_entrez_query=None, format_object=None, format_type='XML',
			ncbi_gi=None, results_file=None, show_overview=None, megablast=None,
			):
	
	import time
	assert program in ['blastn', 'blastp', 'blastx', 'tblastn', 'tblastx']

	parameters = [
		('AUTO_FORMAT', auto_format),
		('COMPOSITION_BASED_STATISTICS', composition_based_statistics),
		('DATABASE', database),
		('DB_GENETIC_CODE', db_genetic_code),
		('ENDPOINTS', endpoints),
		('ENTREZ_QUERY', entrez_query),
		('EXPECT', expect),
		('FILTER', filter),
		('GAPCOSTS', gapcosts),
		('GENETIC_CODE', genetic_code),
		('HITLIST_SIZE', hitlist_size),
		('I_THRESH', i_thresh),
		('LAYOUT', layout),
		('LCASE_MASK', lcase_mask),
		('MEGABLAST', megablast),
		('MATRIX_NAME', matrix_name),
		('NUCL_PENALTY', nucl_penalty),
		('NUCL_REWARD', nucl_reward),
		('OTHER_ADVANCED', other_advanced),
		('PERC_IDENT', perc_ident),
		('PHI_PATTERN', phi_pattern),
		('PROGRAM', program),
		# ('PSSM',pssm), - It is possible to use PSI-BLAST via this API?
		('QUERY', sequence),
		('QUERY_FILE', query_file),
		('QUERY_BELIEVE_DEFLINE', query_believe_defline),
		('QUERY_FROM', query_from),
		('QUERY_TO', query_to),
		# ('RESULTS_FILE',...), - Can we use this parameter?
		('SEARCHSP_EFF', searchsp_eff),
		('SERVICE', service),
		('THRESHOLD', threshold),
		('UNGAPPED_ALIGNMENT', ungapped_alignment),
		('WORD_SIZE', word_size),
		('CMD', 'Put'),
		]
		
	query = [x for x in parameters if x[1] is not None]
	message = _as_bytes(_urlencode(query))

	request = _Request(url_base,message,{"User-Agent": "BiopythonClient"})
	handle = _urlopen(request)

	rid, rtoe = _parse_qblast_ref_page(handle)
	parameters = [
		('ALIGNMENTS', alignments),
		('ALIGNMENT_VIEW', alignment_view),
		('DESCRIPTIONS', descriptions),
		('ENTREZ_LINKS_NEW_WINDOW', entrez_links_new_window),
		('EXPECT_LOW', expect_low),
		('EXPECT_HIGH', expect_high),
		('FORMAT_ENTREZ_QUERY', format_entrez_query),
		('FORMAT_OBJECT', format_object),
		('FORMAT_TYPE', format_type),
		('NCBI_GI', ncbi_gi),
		('RID', rid),
		('RESULTS_FILE', results_file),
		('SERVICE', service),
		('SHOW_OVERVIEW', show_overview),
		('CMD', 'Get'),]
	query = [x for x in parameters if x[1] is not None]
	message = _as_bytes(_urlencode(query))

	# Poll NCBI until the results are ready.  Use a backoff delay from 2 - 120 second wait
	delay = 2.0
	previous = time.time()
	while True:
		current = time.time()
		wait = previous + delay - current
		if wait > 0:
			time.sleep(wait)
			previous = current + wait
		else:
			previous = current
		if delay + .5 * delay <= 120:
			delay += .5 * delay
		else:
			delay = 120

		request = _Request(url_base,message,{"User-Agent": "BiopythonClient"})
		handle = _urlopen(request)
		results = _as_string(handle.read())

		# Can see an "\n\n" page while results are in progress,
		# if so just wait a bit longer...
		if results == "\n\n":
			continue
		# XML results don't have the Status tag when finished
		if "Status=" not in results:
			break
		i = results.index("Status=")
		j = results.index("\n", i)
		status = results[i + len("Status="):j].strip()
		if status.upper() == "READY":
			break

	return (results)