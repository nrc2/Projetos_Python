calculo_min = 24 * 60

def dias_minutos(num_of_days):
    return f"{num_of_days} dias são {num_of_days * calculo_min} minutos"
    

def validate_and_execute():

    try:
            user_input_nunber = int(user_input)
            if user_input_nunber > 0:
                calculated_value = dias_minutos(user_input_nunber)
                print (calculated_value)
            elif user_input_nunber == 0:
                return "0 dias são 0 minutos"
                
    
    except ValueError:
        print("your input is not a valid number. Don't ruin ny program!")
    

user_input = input("Escreva um numero:\n")
validate_and_execute()

