def PI(accuracy:int = 0):
    '''
    Leibniz formula for π implemented in Python
    1 - 1/3 + 1/5 - 1/7 + 1/9 ... = PI/4
    :param: digits - the number of digits in our pi result
    :return: the irrational number PI as a float
    '''
    x = 0.0
    for n in range(0, accuracy):
         x += (-1)**n / (2*n+1)
    return x * 4


if __name__ == '__main__':
    print(PI(900001))


