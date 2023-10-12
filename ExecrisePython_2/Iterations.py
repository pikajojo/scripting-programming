class Iterations():
    def print_bla_forloop(self, times):
        result = ""
        for i in range(times):
            result += "bla"
        print(result)
    def print_arrow_forloop(self, size):
        picture = ""
        for i in range(1,size):
            picture += i * "*"
            picture += "\n"
        for i in range(size, 0, -1):
            picture += i * "*"
            picture += "\n"
        print(picture)

    def print_bla_whileloop(self, times):
        result = ""
        i = 0
        while i < times:
            result += "bla"
            i += 1
        print(result)

    def print_arrow_whileloop(self, size):
        picture = ""
        i = 1
        while i < size+1:
            picture += "*" * i
            picture += "\n"
            i += 1
        i = 3
        while i > 0:
            picture += "*" * i
            picture += "\n"
            i -= 1
        print(picture)

    def my_division(self, dividend, divisor):
        if divisor == 0:
            return

        quotient = 0
        remainder = 0
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        while dividend_abs > divisor_abs:
            dividend_abs -= divisor_abs
            quotient += 1
            remainder = dividend_abs
        if (divisor>0 and dividend>0) or (divisor<0 and dividend<0):
            return quotient, remainder
        elif divisor>0 and dividend<0:
            return -quotient, -remainder
        elif divisor<0 and dividend>0:
            return -quotient, remainder

if __name__ == "__main__":
    iterations = Iterations()
    iterations.print_bla_whileloop(4)
    iterations.print_arrow_whileloop(4)
    iterations.print_bla_forloop(4)
    iterations.print_arrow_forloop(4)
    print(iterations.my_division(75, -9))