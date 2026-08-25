# wordle_app_fixed.py
import random
import sys
import os
import shutil
import re
from elements import print_centered

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "w.txt")

def random_note(): 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "minecraft_splash.txt")
    with open(file_path) as f:
        splash = [line.strip() for line in f if line.strip()]
    print_centered(random.choice(splash))

def play_wordle():
    # ---------------- OS & ANSI Setup ----------------
    WINDOWS = os.name == "nt"
    if WINDOWS:
        import msvcrt
    else:
        import tty, termios

    BLACK_BG = '\033[40m'   # empty space
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    WHITE = '\033[47m'
    BLACK_TEXT = '\033[30m'
    RESET = '\033[0m'

    # ---------------- Game Data ----------------
    with open(file_path) as f:
        word_list = [line.strip() for line in f if len(line.strip()) == 5]

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    grid = [[" "]*WORD_LENGTH for _ in range(MAX_ATTEMPTS)]
    colors = [[BLACK_BG]*WORD_LENGTH for _ in range(MAX_ATTEMPTS)]
    secret_word = random.choice(word_list)

    ansi_escape = re.compile(r'\x1b\[.*?m')

    def get_term_width():
        try:
            return shutil.get_terminal_size().columns
        except:
            return 80

    def center_text(text):
        text_stripped = ansi_escape.sub('', text)
        width = get_term_width()
        pad = (width - len(text_stripped)) // 2
        return ' ' * pad + text

    def clear_screen():
        os.system('cls' if WINDOWS else 'clear')

    def get_key():
        if WINDOWS:
            return msvcrt.getwch()
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    def print_grid(current_row, current_guess="", message=""):
        clear_screen()
        print(center_text("TERMY WORDLE"))
        for r in range(MAX_ATTEMPTS):
            row_display = ""
            for c in range(WORD_LENGTH):
                letter = grid[r][c].upper()
                color = colors[r][c]
                if r < current_row:
                    row_display += f"[{color} {letter} {RESET}] "
                elif r == current_row:
                    if c < len(current_guess):
                        row_display += f"[{BLACK_BG} {current_guess[c].upper()} {RESET}] "
                    else:
                        row_display += f"[{BLACK_BG}   {RESET}] "
                else:
                    row_display += f"[{BLACK_BG}   {RESET}] "
            print(center_text(row_display))
        if message:
            print("\n" + center_text(message))
        print("\n")
        print(center_text("Type letters. Simply press Backspace to delete and Ctrl + C to exit the game!"))
        random_note()

    # ---------------- Correct coloring for duplicates ----------------
    def color_guess(guess, secret):
        result_colors = [""] * WORD_LENGTH
        secret_counts = {}

        # Count letters in secret word
        for ch in secret:
            secret_counts[ch] = secret_counts.get(ch, 0) + 1

        # First pass: green
        for i in range(WORD_LENGTH):
            if guess[i] == secret[i]:
                result_colors[i] = GREEN
                secret_counts[guess[i]] -= 1

        # Second pass: yellow/white
        for i in range(WORD_LENGTH):
            if result_colors[i] == "":
                if guess[i] in secret_counts and secret_counts[guess[i]] > 0:
                    result_colors[i] = YELLOW
                    secret_counts[guess[i]] -= 1
                else:
                    result_colors[i] = WHITE + BLACK_TEXT

        return result_colors

    # ---------------- Main Loop ----------------
    current_row = 0
    while current_row < MAX_ATTEMPTS:
        current_guess = ""
        while True:
            print_grid(current_row, current_guess)
            key = get_key()

            if key in ('\r', '\n'):
                continue
            elif key in ('\x08', '\x7f'):
                current_guess = current_guess[:-1]
            elif key.isalpha() and len(current_guess) < WORD_LENGTH:
                current_guess += key.lower()
            elif key == '\x03':
                print("\n" + center_text("You quit :("))
                return 

            if len(current_guess) == WORD_LENGTH:
                if current_guess not in word_list:
                    current_guess = ""
                    continue
                # fill grid
                for i in range(WORD_LENGTH):
                    grid[current_row][i] = current_guess[i]
                # assign colors with duplicate handling
                colors[current_row] = color_guess(current_guess, secret_word)
                current_row += 1
                break

        print_grid(current_row)
        if current_guess == secret_word:
            victory_dialogue = [
                "You did it baby!",
                "Mwah, I'm so proud of you",
                "YUHHHH",
                "I love you so much, you smart girl",
                "YEAHHHH",
                "WOOO YEAH",
                "MWAH!",
                "TRY PLAYING AGAIN. YOU'RE VERY SMART.",
                "YESSS"
            ]
            print(f"\n{center_text(random.choice(victory_dialogue))}")
            return
    else:
        print("\n" + center_text(f"The word was '{secret_word.upper()}'"))

play_wordle()