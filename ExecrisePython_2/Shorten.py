def Shorten(string):
    result = ""

    if len(string) < 2:
        return result
    else:
        result = string[:2] + string[-2] + string[-1]
        # the multiple adds can be in one line
        return result

# def alter_string(astring):
#     if(len(astring) < 2):
#         return ""
#     return astring[:2]+astring[-2:]
# a good way to select the last 2 char [-2:]



# very good idea
def replace_char(word):
    replaced = word.replace(word[0], "$")
    return word[0] + replaced[1:]

# def change_char(astring):
#     first = astring[0]
#     second = astring[1:]
#     return first + second.replace(first, '$')

if __name__ == "__main__":
    shorten = Shorten("ww")
    print(shorten)
    print(replace_char("zzz"))

