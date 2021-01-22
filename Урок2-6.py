prm_value = ('название', 'цена', 'количество', 'ед')
i_row = 0
in_value = ""
list_rows = []
while in_value != 'Конец ввода':
    in_value = input('Введите инормацию 1, для ввода новой позиции, 2 для просмотра введенных данных, "Конец ввода" '
                     'для выхода из программы ')
    print(f'введен параметр {in_value}')
    if in_value == '1':
        d = {'one': 1}
        for p in prm_value:
            d[p] = input(f'{p} ')
        del d['one']
        i_row = i_row + 1
        row_value = [i_row, d]
        list_rows.append(row_value)
        print(d)
        print(row_value)
    elif in_value == '2':
        for p in list_rows:
            print(p)
        w = {}
        a_lists = []
        for k in prm_value:
            w_value = ""
            for p in list_rows:
                if w_value == "":
                    w_value = p[1][k]
                else:
                    w_value = w_value + ', ' + p[1][k]
            w = {k: w_value}
            a_lists.append(w)
        for l in a_lists:
            print(l)
    else:
        print("Конец программе") if prm_value == "Конец ввода" else print("Конец Программе")


