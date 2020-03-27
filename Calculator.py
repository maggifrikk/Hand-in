class Calculator(object):
    def Add(self, number):
        if number == "":
            return 0
        elif len(number) == 1:
            return int(number)
        else:
            return int(number[0]) + int(number[-1])