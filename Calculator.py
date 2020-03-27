class Calculator(object):
    def Add(self, number):
        if number == "":
            return 0
        elif len(number) == 1:
            return int(number)
        else:
            my_list = number.split(",")
            int_list = [int(x) for x in my_list]
            return sum(int_list)