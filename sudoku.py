import curses
import random
import copy

def valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                nums = list(range(1,10))
                random.shuffle(nums)
                for num in nums:
                    if valid(board,i,j,num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_board(remove=40):
    board = [[0]*9 for _ in range(9)]
    solve(board)
    board_copy = copy.deepcopy(board)
    removed = 0
    while removed < remove:
        i, j = random.randint(0,8), random.randint(0,8)
        if board[i][j] != 0:
            board[i][j] = 0
            removed += 1
    return board, board_copy

def sudoku_game(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    
    # Color pairs
    curses.init_pair(1, curses.COLOR_CYAN, -1)   # original numbers
    curses.init_pair(2, curses.COLOR_GREEN, -1)  # correct check
    curses.init_pair(3, curses.COLOR_RED, -1)    # wrong check
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE) # cursor highlight

    def draw_board(board, user_board, wrong_cells, row, col):
        stdscr.clear()
        for i in range(9):
            for j in range(9):
                val = user_board[i][j]
                y, x = i*2, j*4
                display_val = str(val) if val != 0 else '.'

                if (i,j) in wrong_cells:
                    color = curses.color_pair(3)
                elif i == row and j == col:
                    color = curses.color_pair(4)
                elif board[i][j] != 0:
                    color = curses.color_pair(1)
                else:
                    color = curses.color_pair(0)

                try:
                    stdscr.addstr(y, x, f" {display_val} ", color)
                except curses.error:
                    pass

        # Grid lines
        for i in [2,5]:
            for x in range(37):
                try: stdscr.addch((i+1)*2-1, x, '-')
                except curses.error: pass
        for i in [2,5]:
            for y in range(19):
                try: stdscr.addch(y, (i+1)*4-1, '|')
                except curses.error: pass

        stdscr.refresh()

    def game_loop():
        board, solution = generate_board()
        user_board = copy.deepcopy(board)
        row, col = 0, 0
        wrong_cells = set()
        game_over = False

        while True:
            draw_board(board, user_board, wrong_cells, row, col)

            if game_over:
                max_y, max_x = stdscr.getmaxyx()
                message = "Press 'r' to retry or 'q' to quit."
                try:
                    stdscr.addstr(min(18, max_y-1), 0, message[:max_x-1])
                except curses.error:
                    pass
                key = stdscr.getch()
                if key == ord('r'):
                    return True  # restart
                elif key == ord('q'):
                    return False
                else:
                    continue

            key = stdscr.getch()

            # Move cursor
            if key in [curses.KEY_UP, ord('w')]:
                row = (row-1) % 9
            elif key in [curses.KEY_DOWN, ord('s')]:
                row = (row+1) % 9
            elif key in [curses.KEY_LEFT, ord('a')]:
                col = (col-1) % 9
            elif key in [curses.KEY_RIGHT, ord('d')]:
                col = (col+1) % 9

            # Enter number
            elif ord('1') <= key <= ord('9') and not game_over:
                if board[row][col] == 0:
                    user_board[row][col] = int(chr(key))
                    wrong_cells.discard((row,col))
            elif key in [ord('0'), ord(' ')] and not game_over:
                if board[row][col] == 0:
                    user_board[row][col] = 0
                    wrong_cells.discard((row,col))

            # Check cell
            elif key == ord('c') and not game_over:
                if board[row][col] == 0 and user_board[row][col] != 0:
                    if user_board[row][col] != solution[row][col]:
                        wrong_cells.add((row,col))
                    else:
                        wrong_cells.discard((row,col))

            # Solve
            elif key == ord('v') and not game_over:
                user_board = copy.deepcopy(solution)
                wrong_cells.clear()
                game_over = True

            # Quit
            elif key == ord('q'):
                return False

            # Auto end if board complete
            if user_board == solution:
                game_over = True

    # Main loop to allow retry
    while True:
        restart = game_loop()
        if not restart:
            break

# Enjoy the sudoku baby!
curses.wrapper(sudoku_game)