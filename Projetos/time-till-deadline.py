import datetime


entrada_usuario = input("Escreva sua meta e data final separadas por ':'\n")

input_list = entrada_usuario.split(":")

meta = input_list[0]
data_final = input_list[1]

datafinal_data = datetime.datetime.strptime(data_final, "%d.%m.%Y")

data_hoje = datetime.datetime.today()
tempo_ate = datafinal_data - data_hoje

print(f"Caro usuario! O tempo restante para sua meta: {meta} é {tempo_ate}")
