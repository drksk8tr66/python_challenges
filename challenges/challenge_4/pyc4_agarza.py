import string
import random

print_all = list(string.printable[:94])
print_num = list(string.printable[:10])
print_lc = list(string.printable[10:36])
print_uc = list(string.printable[36:62])
print_sc = list(string.printable[62:94])

pw_distinct = int(input('How many passwords would you like to generate?'))
pw_length = int(input('Password Length:'))

for x in range(1,pw_distinct):

	pw = random.sample(print_all,pw_length)
	pw_string = ''.join(pw)
	pw_score = 0

	if any(j in pw for j in print_lc): pw_score +=1
	if any(j in pw for j in print_uc): pw_score +=1
	if any(j in pw for j in print_num): pw_score += 1
	if any(j in pw for j in print_sc): pw_score += 1

	if pw_score <= 2: pw_strength = 'LOW'
	elif pw_score == 3: pw_strength = 'MODERATE'
	elif pw_score == 4: pw_strength = 'STRONG'
	else: pw_strength = 'ERROR'	

	print(pw_string + '  -  PASSWORD STRENGTH: ' + pw_strength)