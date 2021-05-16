#q1-1 reverse words
def reverse_word(word):
    word_list = list(word)
    word_reverse = word_list.reverse()
    return ''.join(word_list)

#q1-2 reverse text
def reverse_text(text):
    text_list = text.split(' ')
    reverse_text = []
    for w in text_list:
        reverse_text.append(reverse_word(w))
    return ' '.join(reverse_text)

word = "hello"
print(reverse_word(word))
text = "hello I am LJ"
print(reverse_text(text))