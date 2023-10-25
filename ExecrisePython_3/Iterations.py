class Iterations:
    def while_loop(self,start):
        k = start
        while k > 0:
            print("k=",k)
            k -= 1

    def max_and_min(self, list):
        max = list[0]
        min = list[0]
        for i in range(1, len(list)):
            if list[i] > max:
                max = list[i]
            if list[i] < min:
                min = list[i]
        return max, min

if __name__ == "__main__":
    iterations = Iterations()

    print(iterations.while_loop(9))
    print(iterations.max_and_min([3,5,75,24,21,67,43,7,9,22]))