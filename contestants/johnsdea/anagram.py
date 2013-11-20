
def get_ana_dict(word):
    word_list = list(word.lower())
    word_list.sort()
    return ''.join(word_list)

def main():
    words = open("real_words", "r")
    out = open("anagram_out", "w")

    word_list = words.read().split("\n")

    anagrams = {}
    all_anagrams = []
    for word in word_list:
        anagram = get_ana_dict(word)
        if anagram in anagrams:
            anagrams[anagram] = anagrams[anagram] + 1
        else:
            anagrams.update({anagram: 1})
    occurences = [anagrams[x] for x in anagrams]
    out.write(str(max(occurences)))

if __name__ == "__main__":
    main()
