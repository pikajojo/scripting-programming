def farenheitToCelsius(self, fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


def isFreezing(self, fahrenheit):
    if farenheitToCelsius(fahrenheit) <= 0:
        return True
    else:
        return False


def find(self, mylist, element):
    for i in range(mylist):
        if list[i] == element:
            return i
    return 'Element not found in list'


def reverseList(self, mylist):
    reversed = []
    for i in range(len(list) - 1, -1, -1):
        reversed.append(list[i])
    return reversed

def bla(self, amount):  # returns "bla" amount times
    i = 0
    resultString = ""
    while i < amount:
        resultString += "bla"
        i += 1
    return resultString

def is_sorted(self, my_list):
    for i in range(len(my_list)-1):
        first_element = my_list[i]
        second_element = my_list[i+1]
        if first_element > second_element:
            return False
    return True


def f_original(self, lst, range, divider, start_index=0):
    a = 0
    b = range
    if start_index + range <= len(lst):
        while b > 0:
            index = range - b + start_index
            if lst[index] % divider == 0 and lst[index] != 0:
                a += 1
            b -= 1
    return a

    # you can try to rewrite the program here.
def f_rewritten(self, lst, myrange, divider, start_index=0):
    res = 0
    if myrange <= len(lst):
        for i in range(0, myrange+1):
            if lst[i] % divider == 0 and lst[i] != 0:
                res += 1
    return res
