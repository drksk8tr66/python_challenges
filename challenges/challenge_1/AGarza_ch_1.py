
import os

nm = input('Please enter your name:')
age = input('Please enter your age:')
unm = input('Please ente your username:')

n_string = 'Your name is %s.  Your age is %s.  Your username is %s.\n' % (nm, age, unm)
print(n_string)

# if the log files already exists, append to the list
# otherwirse write new
if os.path.exists('name_log.txt'):
	write_mode = 'a'	
else: 
	write_mode = 'w'

n_log = open('name_log.txt',write_mode)
n_log.write(n_string)
n_log.close()