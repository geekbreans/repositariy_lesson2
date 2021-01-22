my_list = [7, 5, 3, 3, 2]

rtg_value = input('Введите рейтинг - ')

if rtg_value.isnumeric():
    w_order = 0
    for w in my_list:
        w_order = w_order + 1
        rtg_value = int(rtg_value)
        if rtg_value >= w:
            my_list.insert(w_order-1, rtg_value)
            print(w)
            break

else:
    print("Необходимо ввести число")

for w in my_list:
    print(w)
