from unittest import TestCase, main
import os
from challenges.challenge_1.dustin_ch_1 import gather_info, print_info, write_to_file, read_from_file


class MyTestCase(TestCase):
    def setUp(self):
        # the setup is the first thing to run during the unit test
        # create any persistent objects like files here
        if not os.path.isfile("Ch #1 - Dustin.txt"):
            f = open("Ch #1 - Dustin.txt", 'w', newline='')
            f.close()

    def test_gather_basic_info(self):
        params = ['Dustin', 30, 'dust7667']
        self.assertEqual(gather_info(name=params[0], age=params[1], username=params[2]), ['Dustin', 30, 'dust7667'])

    def test_gather_string_info(self):
        params = ['Dustin', '30', 'dust7667']
        self.assertEqual(gather_info(name=params[0], age=params[1], username=params[2]), ['Dustin', '30', 'dust7667'])

    def test_gather_wrongType_info(self):
        params = [30, 'Dustin', True]
        self.assertEqual(gather_info(name=params[0], age=params[1], username=params[2]), [30, 'Dustin', True])

    def test_print_basic_info(self):
        params = ['Dustin', 30, 'dust7667']
        ans = "Your name is {0}, you are {1} years old, and your username is {2}".format(params[0], params[1], params[2])
        self.assertEqual(print_info(params), ans)

    def test_print_no_info(self):
        params = None
        ans = "You have not supplied the correct type of info"
        self.assertEqual(print_info(params), ans)

    def test_print_blank_info(self):
        params = []
        ans = "You have not supplied the correct type of info"
        self.assertEqual(print_info(params), ans)

    def test_write_basic_info(self):
        params = ['Dustin', 30, 'dust7667']
        ans = "info saved"
        self.assertEqual(write_to_file(params), ans)

    def test_read_basic_info(self):
        f_name = "Ch #1 - Dustin.txt"
        params = ['Dustin', 30, 'dust7667']
        ans = ['Dustin', '30', 'dust7667']
        write_to_file(params)
        self.assertEqual(read_from_file(f_name), ans)

    def test_print_read_basic_info(self):
        f_name = "Ch #1 - Dustin.txt"
        params = ['Dustin', 30, 'dust7667']
        ans = "Your name is {0}, you are {1} years old, and your username is {2}".format(params[0], params[1],
                                                                                         params[2])
        write_to_file(params)
        self.assertEqual(print_info(read_from_file(f_name)), ans)

    def tearDown(self):
        # the teardown is the last thing to run in the unit test
        # be sure to remove anything created in the setup process
        f_name = "Ch #1 - Dustin.txt"
        if os.path.isfile(f_name):
            os.remove(f_name)


if __name__ == '__main__':
    main()
