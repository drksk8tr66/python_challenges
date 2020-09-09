if __name__ == '__main__':
    file = 'Jordan CH1.txt'
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    user = input('Please enter your username: ')
    file_object_write = open(file, 'w')
    file_object_write.write(
        'your name is {0} you are {1} years old, and your username is {2}'.format(name, age, user))
    file_object_write.close()
    file_object_read = open(file, 'r')
    print(file_object_read.read())
    file_object_read.close()


class File:
    def __init__(self, name):
        self.name = name

    def write_file(self, name, age, user):
        file_object_write = open(self.name, 'w')
        file_object_write.write(
            'your name is {0} you are {1} years old, and your username is {2}'.format(name, age, user))
        file_object_write.close()

    def read_file(self):
        file_object_read = open(self.name, 'r')
        print(file_object_read.read())
        file_object_read.close()


if __name__ == '__main__':
    file = File('Jordan CH1.txt')
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    user = input('Please enter your username: ')
    file.write_file(name, age, user)
    file.read_file()
