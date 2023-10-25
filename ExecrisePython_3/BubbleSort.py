
def BubbleSort(mylist):
    length = len(mylist)
    for i in range(1, length):
        for j in range(0,length-i):
            if mylist[j+1]<mylist[j]:
                tmp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = tmp
    return mylist

if __name__ == "__main__":
    print(BubbleSort([23,43,12,4,54,21,5,10]))

