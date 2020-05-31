class Authentication(object):
    def __init__(self, input_value=''):
        self.input_value = input_value

    def __lower(self):
        lower = any(c.islower() for c in self.input_value)
        return lower

    def __upper(self):
        upper = any(c.isupper() for c in self.input_value)
        return upper

    def __digit(self):
        digit = any(c.isdigit() for c in self.input_value)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        value_len = len(self.input_value)

        report_name = lower and upper and digit and value_len >= 6

        if report_name:
            print("Username and password validated.")
            return True

        elif not lower:
            print("You didn't use a lower case letter.")
            return False

        elif not upper:
            print("You didn't use a upper case letter.")
            return False

        elif value_len < 6:
            print("Your username and password should have at least 6 characters")
            return False

        elif not digit:
            print("You didn't use a digit")
            return False
        else:
            pass




