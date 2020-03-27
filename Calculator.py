class Calculator(object):
    def Add(self, number):
        if number == "":
            return 0
        elif len(number) == 1:
            return int(number)
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
            return sum(int_list)