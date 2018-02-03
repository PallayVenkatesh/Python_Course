def middle(Sentence):
    s = Sentence.split()
    l = len(s)
    print('Middle words are :')
    print(*[s[int(l / 2)] if (l % 2 != 0) else s[int(l / 2):int(l / 2 + 1)] if (l % 2 == 0) else s[:]])


def reverseWordSentence(Sentence):
    words = Sentence.split(" ")

    newWords = [word[::-1] for word in words]

    newSentence = " ".join(newWords)

    return newSentence


def find_longest_word(Sentence):
    words = Sentence.split(" ")
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print('Longest Word is: '+longest_word)

Sentence = input('Enter Sentence?')

middle(Sentence)
find_longest_word(Sentence)

print('Sentence with Reverse  words is :'+reverseWordSentence(Sentence))
