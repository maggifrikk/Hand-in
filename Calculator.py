class NegativeNumber(Exception):
    def __init__(self, message):
        self.message = message

class Calculator(object):
    def Add(self, number):
        if number == "":
            return 0
        if len(number) == 1:
            return int(number)
        else:
            if "/" in number:
                new_delimiter = number[2]
                my_list = number[4:].split("{}".format(new_delimiter))
            else:
                my_list = number.split(",")
            new_list = []
            for element in my_list:
                if "\n" in element:
                    for elem in element.split("\n"):
                        new_list.append(elem)
                else:
                    new_list.append(element)
            int_list = [int(x) for x in new_list]
            for element in int_list:
                if element > 1000:
                    int_list.remove(element)
            negative_list = []
            for elem in int_list:
                if elem < 0:
                    negative_list.append(elem)
            try:
                if len(negative_list) > 0:
                    raise NegativeNumber("Negatives not allowed: {}".format(",".join([str(x) for x in negative_list])))
            except NegativeNumber as e:
                return e.message
            return sum(int_list)