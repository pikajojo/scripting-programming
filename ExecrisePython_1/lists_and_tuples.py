def list_and_tuple():
    mylist = "abcde"
    mylist_list = []
    for element in mylist:
        mylist_list.append(element)
    mylist_list[2] = "z"
    mylist = mylist_list
    mylist2 = ["Yajing", "Wang", 26]
    mylist3 = mylist + mylist2
    print(mylist)
    print(mylist2)
    print(mylist3)


if __name__ == "__main__":
    list_and_tuple()