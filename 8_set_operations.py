my_set = {"Naneiro", "Fevereiro"}
#não podemos acesar um eemento pelo seu índice somente usando loop
for element in my_set:
    print(element)

my_set.add("March")
print(my_set)#adiciona em uma posição aleatória
my_set.remove("March")
print(my_set)