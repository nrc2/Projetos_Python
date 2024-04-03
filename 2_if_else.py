calculo_min = 24 * 60

def dias_minutos(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} dias são {num_of_days * calculo_min} minutos"
    elif num_of_days == 0:
        return "0 dias são 0 minutos"
    else:
        return "Número de dias não pode ser negativo"

user_input = input("Escreva um numero:\n")

if user_input.isdigit():
    user_input_nunber = int(user_input)
    calculated_value = dias_minutos(user_input_nunber)
    print (calculated_value)
else:
    print("your input is not a valid number.Don't ruin ny program!")