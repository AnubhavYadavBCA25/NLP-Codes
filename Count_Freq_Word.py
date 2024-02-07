def word_freq(sent):
    counts = dict()
    words = sent.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

text = str(input('Enter the sentence:'))
print(word_freq(text.lower()))