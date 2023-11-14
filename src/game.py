class Game:
	def __init__(self, initial_state):
		self.state = initial_state
		self.goal_state = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 0]
		]
    
	# Verificar se chegou no estado final
	def is_goal_state(self):
		return self.state == self.goal_state
	
	# Pegar a posição vazia
	def get_empty_position(self):
		for i, row in enumerate(self.state):
			if 0 in row:
				return i, row.index(0)
	
	# Verificar os movimentos válidos
	def get_valid_moves(self):
		empty_row, empty_col = self.get_empty_position()
		valid_moves = []
		
		# Esquerda
		if empty_col > 0:
			valid_moves.append((empty_row, empty_col - 1))

		# Direita
		if empty_col < 2:
			valid_moves.append((empty_row, empty_col + 1))

		# Cima
		if empty_row > 0:
			valid_moves.append((empty_row - 1, empty_col))

		# Baixo
		if empty_row < 2:
			valid_moves.append((empty_row + 1, empty_col))

		return valid_moves
	
	# Realizar movimento
	def make_move(self, move):
		empty_row, empty_col = self.get_empty_position()
		new_row, new_col = move

		self.state[empty_row][empty_col], self.state[new_row][new_col] = (
			self.state[new_row][new_col],
			self.state[empty_row][empty_col]
		)
	
	# Imprimir o tabuleiro na tela
	def display_board(self):
		print("Estado atual:")
		for row in self.state:
			row_str = " ".join(f"[ {elem if elem != 0 else ' '} ]" for elem in row)
			print(row_str)
