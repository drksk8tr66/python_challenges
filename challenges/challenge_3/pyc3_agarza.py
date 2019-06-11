import itertools

cipher = {'A':'Y','B':'P','C':'L','D':'T','E':'A','F':'V',
		  'G':'K','H':'R','I':'E','J':'Z','K':'G','L':'M',
		  'M':'S','N':'H','O':'U','P':'B','Q':'X','R':'N',
		  'S':'C','T':'D','U':'I','V':'J','W':'F','X':'Q',
		  'Y':'O','Z':'W',' ':' '}

decode = {'Y':'A','P':'B','L':'C','T':'D','A':'E','V':'F',
		  'K':'G','R':'H','E':'I','Z':'J','G':'K','M':'L',
		  'S':'M','H':'N','U':'O','B':'P','X':'Q','N':'R',
		  'C':'S','D':'T','I':'U','J':'V','F':'W','Q':'X',
		  'O':'Y','W':'Z',' ':' '}

cipher_op = input('Would you like to encode (E) or decode (D) your message?')

if cipher_op.upper() =='E':
	msg = input('Please enter the string you want to encode:').upper()
	s = ''
	for x in itertools.chain(msg):
		s = s + cipher[x]
	print('Your encoded string is:\n'+s)

elif 	cipher_op.upper() =='D':
		msg = input('Please enter the string you want to decode:').upper()
		s = ''
		for x in itertools.chain(msg):
			s = s + decode[x]
		print('Your decoded string is:\n'+s)	