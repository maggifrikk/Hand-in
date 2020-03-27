class Calculator(object):
    def Add(self, number, number2=""):
        if number == "":
            return 0
        elif number2 == "":
            return number
        else:
            return number + number2