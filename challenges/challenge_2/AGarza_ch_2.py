# prompt user for cal mode
calc_mode = input('Please chose a calculation.\nForce (F)\nMass (M)\nAcceleration (A)\n')

# calc force
if calc_mode == 'F':
	m = float(input('Please enter mass (kg):'))
	a = float(input('Please enter acceleration (m/s/s):'))
	f = m*a
	print('Force is %f N' % f)

# calc mass
elif calc_mode=='M':
	f = float(input('Please enter force (N):'))
	a = float(input('Please enter acceleration (m/s/s):'))
	m = f/a 
	print('Mass is %f kg' % m)

# calc acceleration
elif calc_mode=='A':
	f = float(input('Please enter force (N):'))
	m = float(input('Please Enter mass (kg):'))
	a = f/m
	print('Acceleration is %f m/s/s' % a)

# exit if user makes any other parameter.
else: print('Please enter F (Force), M (Mass), A (Acceleration)')