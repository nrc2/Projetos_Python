#set é uma lista que só permite valores únicos
calculo_min = 24 * 60

def dias_minutos(num_of_days):
    return f"{num_of_days} dias são {num_of_days * calculo_min} minutos"
    

def validate_and_execute():

    try:
            user_input_nunber = int(num_of_days_element)
            if user_input_nunber > 0:
                calculated_value = dias_minutos(user_input_nunber)
                print (calculated_value)
            elif user_input_nunber == 0:
                return "0 dias são 0 minutos"
                
    
    except ValueError:
        print("your input is not a valid number. Don't ruin ny program!")
    
user_input = ""

while user_input != "exit":
    user_input = input("Escreva um numero:\n")

    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))
    
    for num_of_days_element in user_input.split(","):
        validate_and_execute()

