sample_list = []
el_count = 0

sample_list = input('Введите элементы с пробелами -').split()
el_count = len(sample_list)


for i in range(0, el_count, 2):

    if i + 1 < el_count:
        m1_value = sample_list[i]
        m2_value = sample_list[i+1]
        sample_list[i] = m2_value
        sample_list[i + 1] = m1_value


for s in sample_list:

    print(s)


