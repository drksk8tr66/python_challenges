import itertools

# cipher dicts
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


if cipher_op.upper() =='E': # ecnode a message
	msg = input('Please enter the string you want to encode:').upper()
	s = ''
	for x in itertools.chain(msg):  # iterate over each character and map it using cipher
		s = s + cipher[x]  # add each character to the end of the string.
	print('Your encoded string is:\n'+s)

elif 	cipher_op.upper() =='D': # decode a message
		msg = input('Please enter the string you want to decode:').upper()
		s = ''
		for x in itertools.chain(msg): # iterate same as before
			s = s + decode[x]
		print('Your decoded string is:\n'+s)	