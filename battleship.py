import os

class Player:
    
    def __init__(self, name):
        self.name = name

    def play(self, my_board, enemy_board):
        my_board.display_game(my_board.player_moves, enemy_board.player_combinations)

        while True:
            field = input(f'\n{self.name} shoot the field: ').upper()

            if len(field) != 2:
                print('\nWrong field input!\n')
                continue
            elif field not in my_board.fields:
                print('\nWrong field input!\n')
                continue
            elif field in my_board.player_moves:
                print('\nField is already targeted!\n')
                continue
            else:
                my_board.player_moves.add(field)
                if any(field in fs for fs in enemy_board.player_combinations):
                    my_board.display_game(my_board.player_moves, enemy_board.player_combinations)
                    print(f'\nSuccessful hit on field {field}!')
                    if my_board.win_check(enemy_board):
                        print('\nAll fields are successfully hit')
                        print(f'\n-------- {self.name} won! --------\n')
                        exit()
                    else:
                        continue
                else:
                    my_board.display_game(my_board.player_moves, enemy_board.player_combinations)
                    print(f'\nNo hit.\n')
                    break


class Ships_board:
    
    def __init__(self):
        self.fields = [f'{i}{int(j)}' for i in 'ABCDEFG' for j in range(7)]
        self.board_matrix = [[' '] * 7 for i in range(7)]
        self.player_combinations = set()
        self.irregular_fields = set()
    
    def ship_input(self, ship_size):

        while True:
            fields = []
            lst = input(f'\nEnter {ship_size} field/s (comma separated): ').upper()
            lst = list(map(str.strip, lst.split(',')))

            if len(lst) != ship_size:
                    print('\nWrong field number!\n')
                    continue
            for i in lst:
                if len(i) != 2:
                    print('\nWrong entry!\n')
                    break
                elif i not in self.fields:
                    print('\nWrong entry!\n')
                    break
                elif len(lst) != len(set(lst)):
                    print('\nWrong entry!\n')
                    break
                elif any(i in fs for fs in self.player_combinations):
                    print(f'\nField {i} is occupied!\n')
                    break
                elif i in self.irregular_fields:
                    print(f'\nShips must no touch!\n')
                    break
                else:
                    fields.append(i)
            else:
                if self.connection_check(fields) == True:
                    return frozenset(fields)
                else:
                    print('\nEntered fields are not horizontally/vertically connected!\n')
                    continue
    
    def connection_check(self, positions):
        convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
        conv_positions = []

        for i in positions:
            for s,b in zip(i[0], i[1]):
                conv_positions.append((convert[s], int(b)))
        conv_positions.sort()
        if len(conv_positions) == 1:
            return True
        elif all((row, column + 1) in conv_positions for row, column in conv_positions[:-1]):
            return True
        elif all((row + 1, column) in conv_positions for row, column in conv_positions[:-1]):
            return True
        else:
            return False

    def ships_entry(self, player):
        print(f'------- {player.name} Entry fields for 1 submarine, 2 destroyers and 3 patrol boats -------')

        ship_sizes = [3, 2, 2, 1, 1, 1]
        for i in ship_sizes:
            self.input_display(list(self.player_combinations))
            ship = self.ship_input(i)
            self.player_combinations.add(ship)
        else:
            print('\n' * 100)  # alternative
            print(f'\n------- {player.name} successfully entered his ships! -------\n')
     
    def input_display(self, fields):
        convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
        rev_convert = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G'}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for i in fields:
            for j in i:
                for c,n in zip(j[0], j[1]):
                    self.board_matrix[convert[c]][int(n)] = '■'

        for i, row in enumerate(self.board_matrix):
            for j, elem in enumerate(row):
                if elem == '■':
                    for c_i, c_j in directions:
                        n_i, n_j = i + c_i, j + c_j
                        if 0 <= n_i < len(self.board_matrix) and 0 <= n_j < len(self.board_matrix[0]) and self.board_matrix[n_i][n_j] != '■':
                            self.board_matrix[n_i][n_j] = '/'
                            self.irregular_fields.add(rev_convert[n_i] + str(n_j))

        for i,j in zip(self.board_matrix, 'ABCDEFG'):
            print(f'{j} {i}')
        
        for i in range(7):
            print(f'    {i}', end='')
    

class Play_board:
    
    def __init__(self):
        self.fields = [f'{i}{int(j)}' for i in 'ABCDEFG' for j in range(7)]
        self.board_matrix = [[' '] * 7 for i in range(7)]
        self.player_moves = set()
          
    def display_game(self, fields, enemy_ships):
        convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}

        for i in fields:
            for c,n in zip(i[0], i[1]):
                if any(i in fs for fs in enemy_ships):
                    self.board_matrix[convert[c]][int(n)] = '■'
                else:
                    self.board_matrix[convert[c]][int(n)] = '×'

        for i,j in zip(self.board_matrix, 'ABCDEFG'):
            print(f'{j} {i}')
        
        for i in range(7):
            print(f'    {i}', end='')
    
    def win_check(self, enemy_ships):
        
        if all(subset.issubset(self.player_moves) for subset in enemy_ships.player_combinations):
            return True
        else:
            return False
        
def player_switch(current_option, options):

    return options[1 - options.index(current_option)]


player1 = Player(input('Player 1: '))
player2 = Player(input('Player 2: '))

print(f"\nFirst player is '{player1.name}'")
print(f"Second player is '{player2.name}'\n")

player1_ships = Ships_board()
player2_ships = Ships_board()

player1_ships.ships_entry(player1)
player2_ships.ships_entry(player2)

os.system('cls' if os.name == 'nt' else 'clear')

print('----- Players are succsessfully entered their ships! -----\n')

player1_board = Play_board()
player2_board = Play_board()

players = [player1, player2]
boards_of_players = [player1_board, player2_board]
ships = [player2_ships, player1_ships]

current_player = player1
player_board = player1_board
enemy_ships = player2_ships

while True:
    current_player.play(player_board, enemy_ships)
    
    current_player = player_switch(current_player, players)
    player_board = player_switch(player_board, boards_of_players)
    enemy_ships = player_switch(enemy_ships, ships)


