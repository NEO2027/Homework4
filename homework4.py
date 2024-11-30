immutable_var = (123, "Artem", 3.10, True)
print(immutable_var)
try:
    immutable_var[0] = 456
except TypeError as error:
    print(error)
    print("Элементы кортежа изменить нельзя, так как кортеж - это неизменяемый тип данных.")

mutable_list = [19, "Urban", 6.6, False]
print(mutable_list)
mutable_list[0] = 100
mutable_list[1] = "Hello"
mutable_list.append("New")
print(mutable_list)