import module as m ##lembrando que podemos in=mportar só a função

import os
print(os.name)

user_input = ""

while user_input != "exit":
    user_input = input("Escreva um numero:\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "c_unit": days_and_unit[1]}

    m.validate_and_execute(days_and_unit_dictionary)
