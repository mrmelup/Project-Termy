from elements import *
import curses
import random

SIZE = 4
counted_tiles = set()

def new_board():
    board = [[0]*SIZE for _ in range(SIZE)]
    add_tile(board)
    add_tile(board)
    return board

def add_tile(board):
    empty = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.9 else 4

def compress(row):
    return [x for x in row if x != 0]

def merge(row):
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    new = []
    for row in board:
        row = compress(row)
        row = merge(row)
        row = compress(row)
        row += [0]*(SIZE - len(row))
        new.append(row)
    return new

def reverse(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_right(board):
    return reverse(move_left(reverse(board)))

def move_up(board):
    return transpose(move_left(transpose(board)))

def move_down(board):
    return transpose(move_right(transpose(board)))

def boards_equal(b1, b2):
    return all(b1[i][j] == b2[i][j] for i in range(SIZE) for j in range(SIZE))

def can_move(board):
    for row in board:
        if 0 in row:
            return True
    for i in range(SIZE):
        for j in range(SIZE-1):
            if board[i][j] == board[i][j+1]:
                return True
    for j in range(SIZE):
        for i in range(SIZE-1):
            if board[i][j] == board[i+1][j]:
                return True
    return False


def init_colors():
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

def get_color(val):
    if val == 0:
        return curses.color_pair(0)
    elif val == 2:
        return curses.color_pair(1)
    elif val == 4:
        return curses.color_pair(2)
    elif val == 8:
        return curses.color_pair(3)
    elif val == 16:
        return curses.color_pair(4)
    elif val == 32:
        return curses.color_pair(5)
    elif val == 64:
        return curses.color_pair(6)
    elif val == 128:
        return curses.color_pair(7)
    else:
        return curses.color_pair(8)

def draw_board(stdscr, board):
    stdscr.clear()

    tile_h = 3
    tile_w = 8

    for i in range(SIZE):
        for j in range(SIZE):
            val = board[i][j]
            color = get_color(val)

            y = i * tile_h
            x = j * tile_w

            for dy in range(tile_h):
                stdscr.addstr(y + dy, x, " " * tile_w, color)

            if val != 0:
                text = str(val)
                stdscr.addstr(
                    y + 1,
                    x + (tile_w - len(text)) // 2,
                    text,
                    color | curses.A_BOLD
                )

    stdscr.addstr(SIZE * tile_h + 1, 0, "Arrows or WASD | Q = quit")
    stdscr.refresh()

def get_move(key):
    # Arrow keys
    if key == curses.KEY_LEFT:
        return "LEFT"
    elif key == curses.KEY_RIGHT:
        return "RIGHT"
    elif key == curses.KEY_UP:
        return "UP"
    elif key == curses.KEY_DOWN:
        return "DOWN"

    # WASD keys
    elif key in (ord('a'), ord('A')):
        return "LEFT"
    elif key in (ord('d'), ord('D')):
        return "RIGHT"
    elif key in (ord('w'), ord('W')):
        return "UP"
    elif key in (ord('s'), ord('S')):
        return "DOWN"

    return None

def game(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    init_colors()

    board = new_board()

    while True:
        draw_board(stdscr, board)

        if not can_move(board):
            stdscr.addstr(SIZE * 3 + 2, 0, "Game Over! Press Q to quit.")

        key = stdscr.getch()

        if key in (ord('q'), ord('Q')):
            break

        move = get_move(key)
        if not move:
            continue

        old_board = [row[:] for row in board]

        if move == "LEFT":
            board = move_left(board)
        elif move == "RIGHT":
            board = move_right(board)
        elif move == "UP":
            board = move_up(board)
        elif move == "DOWN":
            board = move_down(board)

        if not boards_equal(old_board, board):
            add_tile(board)
            for row in board:
                for val in row:
                    if val > 2048 and val not in counted_tiles:
                        counted_tiles.add(val)
                        elements.tfe_wins += 1

# Running the Game :D ENJOY BABY!

if __name__ == "__main__":
    curses.wrapper(game)