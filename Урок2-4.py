big_word = input("Введите слова:")

big_words = big_word.split()

w_order = 0
for w in big_words:
    w_order = w_order + 1
    print(w_order, w[0:10] if len(w) > 10 else w)
