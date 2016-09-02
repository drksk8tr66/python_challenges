import re


class PhoneCheck:

    def __init__(self, regex=None):
        if regex is None:
            self.regex = r"^[0-9]{10}|" \
                         r"[0-9]{3}-{1}[0-9]{3}-{1}[0-9]{4}|" \
                         r"[0-9]{3} {1}[0-9]{3} {1}[0-9]{4}|" \
                         r"[0-9]{3}\.{1}[0-9]{3}\.{1}[0-9]{4}|" \
                         r"\([0-9]{3}\) {0,1}[0-9]{3}-{1}[0-9]{4}|" \
                         r"[0-9]{3}-{1}[0-9]{4}"
        else:
            self.regex = regex

    def set_regex(self, regex=None):
        if regex is None:
            print('No Regex Provided. Will continue to use default {}'.format(self.regex))
        else:
            self.regex = regex

    def validate(self, phone):
        return True if re.match(self.regex, phone) else False


if __name__ == '__main__':
    p = PhoneCheck()
    print(p.regex)
    print(p.validate('1234567890'))
    print(p.validate('123-456-7890'))
    print(p.validate('123.456.7890'))
    print(p.validate('(123)456-7890'))
    print(p.validate('(123) 456-7890'))
    print(p.validate('456-7890'))
    print(p.validate('123-45-6789'))
    print(p.validate('123:4567890'))
    print(p.validate('123/456-7890'))
    print(p.validate('123-456.7890'))
    p.set_regex(r"\(?[0-9]{3}?(\-|\.|\\|\))? ?[0-9]{3}(\-| |\.)?[0-9]{4}|^[0-9]{3}\-?[0-9]{4}")
    print(p.regex)
    print(p.validate('1234567890'))
    print(p.validate('123-456-7890'))
    print(p.validate('123.456.7890'))
    print(p.validate('(123)456-7890'))
    print(p.validate('(123) 456-7890'))
    print(p.validate('456-7890'))
    print(p.validate('123-45-6789'))
    print(p.validate('123:4567890'))
    print(p.validate('123/456-7890'))
    print(p.validate('123-456.7890'))


