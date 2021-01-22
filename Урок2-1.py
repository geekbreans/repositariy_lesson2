sample_list = [10, '1', [111, 222, 333, 444], 'Tom', None, True, ('assa', 'bass',), range(17), {1: 'aaa', 2: 'bbb',3: 'ddd'}]

for k, item in enumerate(sample_list, 1):
    print(f'{k} - {item}  type is {item}')

for s in sample_list:
    print(s, type(s))
