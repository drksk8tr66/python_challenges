import re


def validate(t_num):
    if not t_num:
        return False
    if type(t_num) is not str:
        return False
    if re.match("[0-9]{10}|[0-9]{7}|([0-9]{3}-)?[0-9]{3}-[0-9]{4}|[0-9]{3}\.[0-9]{3}\.[0-9]{4}|"
                "\([0-9]{3}\) ?[0-9]{3}-[0-9]{4}", t_num):
        return True
    else:
        return False

if __name__ == '__main__':
    print(validate('1234567890'))
