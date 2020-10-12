def main():
    text = "this is a collection of words of nice words this is fun thing it is"
    wordlist = text.split()


    text_dictionary = dict()

    for word in wordlist:
            if word in text_dictionary:
                text_dictionary[word] = text_dictionary[word] + 1
            else:
                text_dictionary[word] = 1

    dict_list = list(text_dictionary.keys())
    dict_list.sort()
    for key in dict_list:
        print("{:{}} : {}".format(key, word_length(wordlist), text_dictionary[key]))



def word_length(wordlist):
    max_letters = 0
    for word in wordlist:
        if len(word) > max_letters:
            max_letters = len(word)
    return max_letters


main()
