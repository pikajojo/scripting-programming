class ErrorAndDebugging():
    # endless loos. However, I have no idea what it's supposed to do...

    # it is endless because after the first while loop, the value of the temp is -1
    # and the formula is temp = temp/2 -1, so temp will always remain as negative
    # which means temp will always satisfy the condition of the while loop: temp < 100
    # in this case, the while loop will be an infinite loop
    def run(self):
        counter = 0
        temp = 0
        while temp < 100:
            temp = temp/2-1
            print(temp)
            counter += 1
            if counter > 10:
                print("endless loop")
                break

if __name__ == "__main__":
    error_and_debugging = ErrorAndDebugging()
    print(error_and_debugging.run())