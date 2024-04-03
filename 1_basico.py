'''print ("20 dias são " + str(50) + " minutos")
print (f"20 dias são {50} minutos")
print( 20 + 24 + 60)'''

#Variáveis
#Python is dynamically typed
to_seconds =  24 * 60 * 60

#print (f"30 dias são {30 * to_seconds} segundos")

#Funções E PARÂMETROS
def days_to_unit(num_of_days):
    return f"{num_of_days} dias são {num_of_days * to_seconds} segundos"

"""days_to_unit(30)
days_to_unit(35)
days_to_unit(24)"""

#Variáveis globais e locais
#Se você criar variáveis dentro de funções elas serão locais e não poderão ser usadas por outra função

#User Input
user_input = input("Escreva o numero de dias:\n")
number = int(user_input)

valor = days_to_unit(number)
print(valor)