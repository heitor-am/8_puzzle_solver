# Pegar a entrada do usuário para cada linha
def get_input_row(prompt):
	while True:
		try:
			row = input(prompt)
			row = list(map(int, row.split(" ")))

			if all(0 <= elem <= 8 for elem in row):
				return row
			else:
				print("Por favor, insira apenas números inteiros entre 0 e 8.")

		except ValueError:
			print("Por favor, insira apenas números inteiros.")

# Pegar o estado inicial
def get_initial_state():
	print("Digite abaixo os valores do estado inicial:")
	print("OBS: Utilize o 0 (zero) para representar o espaço vazio!")

	initial_state = []
	for i in range(3):
		row = get_input_row(f"Informe a {i+1}ª linha: ")
		initial_state.append(row)

	return initial_state

# Imprimir o estado inicial
def print_initial_state(initial_state):
	print("\nEstado inicial:")
	for row in initial_state:
		row_str = " ".join(f"[ {elem if elem != 0 else ' '} ]" for elem in row)
		print(row_str)

initial_state = get_initial_state()
print_initial_state(initial_state)
