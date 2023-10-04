def methods():
    mylist = [100,200,400,500]
    mylist.insert(2, 300)
    print(mylist)
    mylist.append(1000)
    print(mylist)
    mylist.sort()
    print(mylist)



sentence_example = "Zeven Zottegemse zotten zullen zes zomerse zondagen zwemmen zonder zwembroek."


def count_sentence(sentence):
    sentence_split = sentence.split()
    length = len(sentence_split)
    return length


def replace_sentence(sentence):
    new_sentence = ""
    sentence_split = sentence.split()
    for word in sentence_split:
        new_word = word.replace(word[0], "p")
        new_sentence += new_word + " "
    return new_sentence


if __name__ == "__main__":
    methods()
    print(count_sentence(sentence_example))
    print(replace_sentence(sentence_example))
