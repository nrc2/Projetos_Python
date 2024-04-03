def dias_minutos(num_of_days, c_unit):
    if c_unit == "hours":
         return f"{num_of_days} dias são {num_of_days * 24} horas"
    elif c_unit == "minutes":
         return f"{num_of_days} dias são {num_of_days * 24 * 60} minutos"
    else:
         return "unidade nao suportada"
    

def validate_and_execute(days_and_unit_dictionary):

    try:
            user_input_nunber = int(days_and_unit_dictionary["days"])
            if user_input_nunber > 0:
                calculated_value = dias_minutos(user_input_nunber, days_and_unit_dictionary["c_unit"])
                print (calculated_value)
            elif user_input_nunber == 0:
                return "0 dias são 0 minutos"
                
    
    except ValueError:
        print("your input is not a valid number. Don't ruin ny program!")
    
user_input = ""

while user_input != "exit":
    user_input = input("Escreva um numero:\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "c_unit": days_and_unit[1]}

    validate_and_execute(days_and_unit_dictionary)

