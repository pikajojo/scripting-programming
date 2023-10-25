class NestedList():
    def get_longest_list(self, lst):
            max = 0
            for ele in lst:
                length = len(ele)
                if length > max:
                    max = length
            return max

    def compute_averages_element_wise(self, lst):
        res_list = []
        lst_length = self.get_longest_list(lst)
        num = len(lst)


        #先把同一序号的元素放到一个数组中，比直接计算它们的sum要好得多，因为数组不仅可以计算和，还可以计算长度
        #考试难度！！！！！！！！！！！
        for i in range(lst_length):
            L = []
            for ele in lst:
                if len(ele) > i:
                    L.append(ele[i])
            res_list.append(sum(L)/len(L))
        return res_list



#     Write a function that has a nested list as an argument and calculates the averages of the jth
# elements in each sub-list. Beware: the length of the list of averages should be as long as the
# longest sub-list! For example [[1,2,3], [4,5], [6,7,8,9], [10]] should return [5.25, 4.67, 5.5, 9.0]
# (calculated as follows [(1+4+6+10)/4, (2+5+7)/3, (3+8)/2 ,9/1]).


if __name__ == "__main__":
    nestedlist = NestedList()
    lst = [[1,2,3],[4,5],[6,7,8,9],[10]]
    print(nestedlist.get_longest_list(lst))
    print(nestedlist.compute_averages_element_wise(lst))