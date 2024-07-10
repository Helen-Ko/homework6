my_dict = {'Anna':1985, 'Dima':1988, 'Max':1983}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Helen'))
my_dict.update({'Kirill':1980,
                      'Sasha':1981})
print(my_dict)
a = my_dict.pop('Dima')
print(a)
print(my_dict)
my_set = {1,3,'apple', 3,5.5,7,5,'snow',7}
print(my_set)
print(my_set.add(6))
print(my_set)
print(my_set.add('True'))
print(my_set)
print(my_set.discard(3))
print(my_set)