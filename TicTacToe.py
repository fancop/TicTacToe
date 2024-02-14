import random


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.board[i * 3], '|', self.board[i * 3 + 1], '|', self.board[i * 3 + 2], '|')
            print('-------------')

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            return False

    def check_winner(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                return self.board[i]

        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                return self.board[i]

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]

        return None

    def is_board_full(self):
        return ' ' not in self.board

    def play_game(self, is_single_player):
        print('Игрок 1 - X, Игрок 2 - O')
        if is_single_player:
            print('Вы играете против бота!')
        else:
            print('Вы играете против другого игрока!')

        while True:
            self.print_board()

            if self.current_player == 'O' and is_single_player:
                if self.board[4] == ' ':
                    position = 4
                else:
                    position = random.choice([i for i, val in enumerate(self.board) if val == ' '])
            else:
                print(f"Ходит игрок {self.current_player}")
                position = int(input('Выберите позицию (1 - 9): ')) - 1

            if position < 0 or position >= 9:
                print('Такой клетки не существует, напишите число от 1 до 9')
                continue

            if not self.make_move(position):
                print('Эта клетка уже занята, выберите другую')
                continue

            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f'Игрок {winner} победил!')
                break

            if self.is_board_full():
                self.print_board()
                print('Это ничья!')
                break

            self.switch_player()


if __name__ == '__main__':
    choice = input("Выберите режим: \n1 - игра с ботом\n2 - игра с другим игроком\n")

    if choice == '1':
        game = TicTacToe()
        game.play_game(is_single_player=True)
    elif choice == '2':
        game = TicTacToe()
        game.play_game(is_single_player=False)