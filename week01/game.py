#COURSE: CSE210
#ASSINGMENT: Tic-Tac-Toe
# AUTHOR: Emanuel Valencia
# INSTRUCTOR: Brad Lythgoe

import math


def main():
    start_game()


def start_game():
    print("Welcome to Tic Tac Toe !!!")
    table = table_builder(3, 3)
    whose_turn = 1

    while True:
        print_message(whose_turn)
        draw_table(table)
        selected_square = get_square_input()
        perform_move(table, selected_square, whose_turn)
        did_win = verify(table, whose_turn)

        if did_win:
            break

        if is_playable(table) and whose_turn == 1:
            whose_turn = 2
        elif is_playable(table) and whose_turn == 2:
            whose_turn = 1
        else:
            whose_turn = 0
            break

    print_winning_message(whose_turn)
    draw_table(table)


def print_winning_message(player):
    if player == 1:
        print("Player X won !!! ")
        return
    if player == 2:
        print("Player O won !!!")
        return
    print("It's a draw !!!")


def print_message(player):
    if player == 1:
        print("x's turn to choose square (1-9)")
    if player == 2:
        print("o's turn to choose square (1-9)")


def get_square_input():
    return int(input())


def is_playable(table):
    for i in range(len(table)):
        for k in range(len(table[i])):
            if table[i][k] == 0:
                return True

    return False


def table_builder(height, width):
    table = [[0 for k in range(width)] for i in range(height)]

    return table


def verify(table, player):
    height = len(table)
    width = len(table[0])
    for i in range(height):
        temp = True
        for j in range(width):
            if table[i][j] != player:
                temp = temp and False

        if temp:
            return True

    for i in range(height):
        temp = True
        for j in range(width):
            if table[j][i] != player:
                temp = temp and False
        if temp:
            return True

    temp = True
    for i in range(height):
        if table[i][i] != player:
            temp = temp and False
    if temp:
        return True

    temp = True
    for i in range(height):
        if table[i][width - i - 1] != player:
            temp = temp and False
    if temp:
        return True

    return False


def draw_table(table):
    height = len(table)
    width = len(table[0])
    for i in range(height):
        print("----------")
        line = ""
        for j in range(width):
            position = (i * 3) + j + 1
            if table[i][j] == 0:
                line = line + f'|{position}|'
            elif table[i][j] == 1:
                line = line + "|X|"
            elif table[i][j] == 2:
                line = line + "|O|"
        print(line)


def perform_move(table, selectedSquare, player):
    i = math.ceil(selectedSquare / 3) - 1
    j = ((selectedSquare - 1) % 3)
    table[i][j] = player


if __name__ == "__main__":
    main()
