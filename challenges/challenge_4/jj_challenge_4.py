import string
import random

class PasswordGenerator():
    ''' A simple wrapper for our password generator'''
    GOOD = 'GOOD'
    BAD = 'BAD'
    def __init__(self):
        self.alphabet = string.digits + string.ascii_letters + string.punctuation

    def generate_pass(self,  l: int = 8):
        '''
        :param: l is the length of the password, the min acceptable range is 8
        :returns: A random password made up of the alphabet
        :raises: An exception if the password is not long enough
        '''
        if l < 8:
            raise Exception("You're gonna get hacked...")
        p = ''.join(random.choice(self.alphabet) for i in range(0, l))
        return p

    def check_pass(self, password=''):
        '''
        This function only checks to make sure the password meets the basic requirements
        :param: password to be checked, it should be at least 8 characters
        :returns: an int, sepcifying the quality
        '''
        numbers = sum(c.isdigit() for c in password)
        upper_case = sum(c.isupper() for c in password)
        lower_case = sum(c.islower() for c in password)
        symbols = sum(PasswordGenerator.ispunct(c) for c in password)
        if (symbols > 0 and upper_case > 0 and lower_case > 0 and numbers > 0) \
                or len(password) < 0:
            return self.GOOD
        else:
            return self.BAD

    @staticmethod
    def ispunct(letter):
        return letter in string.punctuation

if __name__ == '__main__':
    p = PasswordGenerator()
    try:
        pd = p.generate_pass(10)
        print("Password: "+pd)
        print("Quality: "+p.check_pass(pd))
    except Exception as e:
        print(e)