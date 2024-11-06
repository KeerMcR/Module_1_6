my_dict = {'Kirill': 1997,
           'Anton': 1998,
           'Ilya': 1999}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Kirill'])
print('Not existing value: ', my_dict.get('Masha', 'Нет информации о годе рождения.'))
my_dict.update({'Misha': 2000,
                'Anna': 1998})
a = my_dict.pop('Ilya')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict, end = '\n\n')

my_set = {3, 3, 6, 7, 'Hello', 'Goodbye', (1, 3), True, 4.2, 2.4, 'Hello'}
print('Set: ', my_set)
my_set.update('byebye')
my_set.discard('Hello')
print('Modified set: ', my_set)