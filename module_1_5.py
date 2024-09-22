immutable_var = 'ocean', 'sea', 24, 45
print(immutable_var)
#immutable_var[0]= 'island' # не заменятеся потому что в моем кортеже нет изменяемых объектов

mutable_list = ['ocean', 'sea', 24, 45]
print(mutable_list)
mutable_list[0] = 'apple'
print(mutable_list)