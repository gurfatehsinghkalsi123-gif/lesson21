def match_words(words):
    count = 0
    list=[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            count = count+1
            list.append(word)
    print("the numbers of words that have matched = ", count)
    print("matched words are:", list)
match_words(['12', '121', '6556', '98879', '4554343'])