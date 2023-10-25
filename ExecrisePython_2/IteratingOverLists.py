class IterationsOverList():
    def generate_list_power_minus_2(self, elements):
        # result = []
        # if elements <= 0:
        #     return result
        #
        # result.append(1)
        # current = 1
        #
        # i = 1
        # while i < elements:
        #     current *= -2
        #     result.append(current)
        #     i += 1
        # return result

        result = []
        # 首先考虑边界条件
        # first consider the edge situations like 0
        if elements <= 0:
            return result

        # 其次把第一个数字先放进去
        # put the first number in the list
        result.append(1)
        current = 1

        # 利用for循环来实现不停连续乘-2的效果
        # use for loop to achieve the effect of times -2 consistently
        for i in range(1, elements):
            current *= -2
            result.append(current)
        return result

    def compute_list_average(self, lst):
        list_sum = 0
        list_length = len(lst)
        for element in lst:
            list_sum += element
        list_average = list_sum / list_length
        return list_average

    def reverse_list(self, lst):
        list_reversed = lst[::-1]
        return list_reversed


    # def is_palindrome(self, string):
    #     string_list = []
    #     for i in string:
    #         string_list.append(i)
    #     num = len(string_list)
    #     string2_list = []
    #     for i in range(num):
    #         string2_list.append(0)
    #     j = 0
    #     while j < num:
    #         string2_list[num-j-1] = string_list[j]
    #         j += 1
    #     return string_list == string2_list

    def check_palindrome(self, string):
        for i in range(len(string)//2):
            if string[i] != string[-1-i]:
                return False
        return True




    def is_palindrome_2(self, s):
        return s == s[::-1]



if __name__ == "__main__":
    iterations_over_list = IterationsOverList()
    print(iterations_over_list.reverse_list("have a nice day"))
    print(iterations_over_list.compute_list_average(iterations_over_list.generate_list_power_minus_2(5)))
    print(iterations_over_list.generate_list_power_minus_2(30))
    print(iterations_over_list.check_palindrome("tenet"))
    print(iterations_over_list.is_palindrome_2("tenet"))
