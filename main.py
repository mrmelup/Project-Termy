# @justintsako
# For Lezzell F. Gumarang

SAVE_FILE = "termy_data.json"

from elements import *
import elements
from dialogue import *

try:
    import readline
except ImportError:
    try:
        import pyreadline3 as readline
    except ImportError:
        readline = None

if os.name == "nt":
    os.system("chcp 65001 > nul")   # Switch CMD to UTF-8

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# if sys.platform == "win32":
#     import pyreadline3 as readline
# else:
#     import readline

if readline:
    readline.set_history_length(1000)
    try:
        readline.parse_and_bind("bind ^[[A previous-history")
        readline.parse_and_bind("bind ^[[B next-history")
    except:
        pass

user = "Lezzell"
user_status = "user" # You can change this to admin, you know

commands = ["help", "help-boost", "echo", "sys / system", "clear / cls / clr", "key", "dir",
            "time --> -now, -y, -m, -d", "cd", "set"]
valid_commands = {
    ".dev", "help", "echo", "sys", "system",
    "clear", "cls", "clr", "time", "key", "keys",
    "dir", "ls", "cd", "mkdir", "rmdir",
    "touch", "rm", "write", "cat", "run", "open",
    "ping", "rename", "ren", "mv", "set", "reset",
    "cinnamoroll", "cr", "gumarang", "sudoku", 
    "wordle", "strip", "strips", "2048", "whoami",
    "pwd", "change", "ch", "resetdata", "tmy", "jsn",
    "lzl", "help-boost", "stat", "stats", "statistics",
    "tcl", "svd", "su",
}

# For Keys 
keys = ["tmy", "jsn", "lzl"]

# File Extensions - We love .lzl!
file_ext = [".exe", ".txt", ".jsn", ".lzl"] 

start_message = f"{UNDERLINE}Hello! Welcome to {GREEN}Termy{RESET}! - The Custom Shell\nIf you're not too familiar with navigating through a terminal, here's a quick guide to get you started!\n\n{GREEN}*{RESET} Type 'help' to get a list of commands to navigate you through the terminal.\n{GREEN}*{RESET} Use 'cat' to open text files, 'run' to open programs, and 'open' to see special types of data.\n{GREEN}*{RESET} This shell is a mix of command prompt and linux, so using 'dir' or 'ls' works.{RESET}\n\n{PINK}*{RESET} There are many secrets hidden in this program.\n{PINK}*{RESET} Finding them gives you a final message and some other sweet things.\n{PINK}*{RESET} Unlock new directories, files, and surprises!\n"
location = ["@main"]
def define_filesystem():
    return {
        "@main": {
            "system": {
                "system_guide.txt": f"{UNDERLINE}{MAGENTA}SYSTEM GUIDE{RESET}\nAll the notes you need to know to navigate through the terminal.\n\n{UNDERLINE}{MAGENTA}NAVIGATING{RESET}\nTo go around the terminal, you need to know where you are. To do this, use {LIGHT_BLUE}dir{RESET} or {LIGHT_BLUE}ls{RESET}.\nTo move around, use {LIGHT_BLUE}cd{RESET} to change directories.\nTo open files, use {LIGHT_BLUE}cat [filename.exe]{RESET} to open .txt files. For .exe, .lzl, .jsn files, use {LIGHT_BLUE}run [filename.exe]{RESET} or {LIGHT_BLUE}open[filename.exe]{RESET}.\n\n{UNDERLINE}{MAGENTA}INTERACTING{RESET}\nTo make a file in your current directory, use {LIGHT_BLUE}touch [filename.exe]{RESET}. Your file name must contain a valid extension such as: .exe, .txt, .lzl, .jsn.\nTo create a new directory, use {LIGHT_BLUE}mkdir [dirname]{RESET}.\nTo write to a file, use {LIGHT_BLUE}write [filename.exe]{RESET}.\nTo rename a file, use {LIGHT_BLUE}ren [filename.exe] [newname.exe]{RESET} or {LIGHT_BLUE}rename [filename.exe] [newname.exe]{RESET}. Note that you cannot change the file extension when renaming.\nTo move a file, use {LIGHT_BLUE}mv [filename.exe] [path]{RESET}. Note that the new location must be a path {LIGHT_BLUE}(@main/newlocation){RESET}.\nTo delete a file, use {LIGHT_BLUE}rm [filename.exe]{RESET}.\nTo delete a directory, use {LIGHT_BLUE}rmdir [dirname]{RESET}.\n\n{UNDERLINE}{MAGENTA}HAVING FUN{RESET}\nTo repeat whatever you said, use {LIGHT_BLUE}echo [message]{RESET}. This message can be whatever you want.\nTo piss off the {BG_RED}OVERLORD{RESET}, use {LIGHT_BLUE}secret(s){RESET}.\n\n{UNDERLINE}{MAGENTA}FREE SECRETS{RESET}\n{LIGHT_BLUE}ily{RESET} or {LIGHT_BLUE}i love you{RESET} or...\n\nThat is all! For more secrets, figure them out! Test some stuff.",
                "creator_notes.txt": f"I created this project as a 'thank you' for everything you've done for me. Thank you for sticking by my side even when there was no reason to. Thank you for loving me when I found it hard to love myself. Thank you for leading by example whenever I was lost. Thank you for educating me rather than punishing me when I didn't know. You've done so much for me, {LIGHT_BLUE}Lezzell{RESET}. For all that you've done for me, I ought to present to you a project that I hope is worth at least five minutes of your time.\n\nEvery line of code is made to build a mini-terminal with secrets hidden, love to be shared, and software to be interacted with.\n\nThe commands in this are exactly what are in real terminals, with the exception of some being from multiple terminals (Windows: dir or MacOS: ls). These don't make any changes, so don't worry, it's easy to navigate.\n\nTo get more help, use the 'help' command or open 'system_guide.txt' for more insight and maybe even some {PINK}secrets{RESET}!\n",
                "termy.tmy": termy(),
            },
            "users": {
                "lezzell": {
                    "readme.txt": f"READ ME!\n\nHi {LIGHT_BLUE}Lezzell!{RESET} This your own directory that is installed on default when running the terminal.\n\nHere, you can find files that are meant for you, and maybe even discover/unlock new files that contain some sweet information! [HINT]\n\nLove from every line of code to you,\n- Justin Sotelo",
                    "public": {
                        "read-first.txt": f"Please read this first.\n\nYou do not need to show anyone these text files. Please know I appreciate them and wish the best for all that are involved in your life.\n\nThat's all :).",
                        "for-friends.txt": f"{UNDERLINE}{MAGENTA}FOR LEZZELL'S FRIENDS :D{RESET}\nBaby, if you're able to, please let your friends know that they're very awesome and cool people, even though I've barely met any of them.\n\nThank you so much for being there for her and allowing her to express herself freely around you. You are a wonderful part of her life, and I hope that you and her continue to grow a bond surpassing the bounds of high school years.\n\nI hope you move on from this little message knowing you're appreciated, valued, and are seen. I wish you prosperity, peace, and love from all that you know.\n\nAgain, thanks very much.\n\n- Justin Sotelo",
                        "for-family.txt": f"{UNDERLINE}{MAGENTA}FOR LEZZELL'S FAMILY{RESET}\nTo all that she calls family, thank you so much. I'm so appreciative of all that were willing to speak to me despite being from a different family. I hope I'm able to get closer to each of you and learn more with the time I'm involved with you.\n\nI'm sorry for previous inconveniences and I strive to mature for good intentions. I hope we can strengthen our bonds and continue to join together.\n\nI sincerely pray that your family continues to be blessed and that prosperous works flow like rivers.\n\nSincerely,\n- Justin Sotelo"
                    },
                    "gifts": {
                        "about-her.txt": f"{LIGHT_BLUE}Lezzell Francisco Gumarang{RESET}, born on March 30, 2009.\n\nAge: 17\nHeight: 4'11\nNationality: Filipino\nMain Language: English\nEye Color: Brown\nShoe Size: 4-5 Womens\nGames: COD, Roblox, Minecraft\nComment from Developer: Loves to eat spicy food that she knows she can barely handle.\n\nHi dear! These are some basic things about you. Just know that I love you for who you are. You do not need to hide any part of your personality because it is beautiful. I love you, so very much.\n",
                        "foryou.txt": f"{UNDERLINE}{MAGENTA}To my most beloved, Lezzell{RESET}\nI wrote this for you simply because I just wanted to empty my feelings out.\n\nI love you. However, it's not the kind of love that leaves when things get hard. We've been through a lot. We have gone through rough patches and will continue to do so in the future.\nI will not leave you, I will not abandon you when you are low. You are my happiness, my reason of why I continue.\n\nLezzell, even through trials, I pledge to stand by your side, even if we're angry at each other.\n\nPlease, accept my love, for I wish to be your husband greatly.\nSo, with everything that I've typed here, please don't forget, my dear. I will wait for you as you promise to wait for me.\n\nYou're so beautiful. You are a jewel, a wonderfully shiny gem. Hardened by the troubles of this earth. I will treasure her, I will be gentle with her, wash her when she is covered in stains, protect her when others wish to steal, and do my best to repair when I fail.\nSo, I wish to be your husband. Husband under God.\n\n- Justin Sotelo",
                        "cinnamoroll-fun.exe": "You're supposed to use 'open' or 'run'",
                    }
                },
                "justin": {
                    "readme.txt": "READ ME!\n\nHi Baby! This is MY directory that is installed on default when you run this terminal.\n\nIn here, you can find some files that contain information you may want to see or just some notes. You can even unlock new files in here! [HINT]\n\nBesides that, there isn't much in here. So, yeah.\n\nFrom 127.0.0.1 to yours,\n- Justin Sotelo",
                    "fighter-jet.txt": f"{UNDERLINE}{MAGENTA}FIGHTER JETS{RESET}\nThere are a couple fighter jets that I really like. For one, I really like the F-15EX.\n\nIt's the newest version of the F-15. It's super modern and it looks really cool :).\n\nI also like the AC-130, A-10, F-22, F-35, and P-51!\n\nDid you know the 'F' in the names stand for 'fighter'?\nHowever, the F-35 is something known as a 'multirole' fighter, meaning it can attack air and ground targets!",
                    "verses.exe": "You're supposed to use 'open' or 'run'",
                    "graphics": {
                        "graphics-info.txt": f"{MAGENTA}{UNDERLINE}A Brief Graphic Design Thing{RESET}\n\nI started making graphics around 2022 once I discovered graphics software that was actually free. Since then, I've been wildly interested in graphic design.\n\nI started off by making custom cards for a game called Madden Mobile. It wasn't a very good game but it was the only football game that was available in the App Store.\n\nThe graphics you see in this directory range from my very early designs to the newest ones. So, I hope these are a little cool to you :).",
                        "mahalkita-design.jsn": "mahalkita_design.png",
                        "lezzell-graphic.jsn": "lezzell_graphic.png"
                    },
                },
                "us": {
                    "notes.txt": f"{UNDERLINE}{MAGENTA}NOTES FOR US{RESET}\n\n- We fix mistakes that we do. Arguing may happen, but that is not the solution. Attack the problem, not each other.\n- Respecting boundries is needed. Without basic respect, there is no relationship.\n- "
                }
            },
            "documents": {
                "information.txt": f"{UNDERLINE}{MAGENTA}ABOUT THIS DIRECTORY{RESET}\n\nThis directory is a place where venting and inner thoughts reside. It is completely your choice to read and use it. If you feel like you don't want to ruin your current mood, don't read them.",
                "maybe-i-should.txt": "I'm not sure if I'm going to get this project out to her. It's been far too long and honestly I've been losing vision on the project. If she somehow sees this, I hope she knows that I made this whole thing so she can feel that she is deserving of appreciation, love, and care. I want her to feel that she doesn't just deserve to be looked at but to be seen.\n\nI'd feel horrible if this project falls. I hope she smiles even just a bit if this is completed.",
                "i-wish.txt": "I wish I was easier to understand. Am I too complicated? She's told me no. She is smart. I just don't want to make her feel like she doesn't know me or feel incapable of grasping who I am.\n\nI'm just afraid that if she fully understood me, everything about me, has seen me to my full exposure, that she would deem me unworthy of her time.\n\nHow could I have fallen so hard for such, when I myself am not worthy of all that I have?",
                "file.txt": "do you like it?",
                "lezzell-docs": {
                    "information.txt": f"{UNDERLINE}{MAGENTA}ABOUT YOUR DOCS{RESET}\n\nThis is your own directory to write your thoughts or feelings in. You can delete this text file and make your own in here. If you don't want to do anything with this directory, you can just leave it as it is! :)",
                },
            },
            "terminal": {
                "strips.txt": f"{UNDERLINE}{MAGENTA}INTERNAL{RESET}\nYou may get 'code strips' or 'command strips'\n\n{UNDERLINE}{MAGENTA}CODE STRIP{RESET}\nCode strips are simply strips of code you can find. These strips contain pieces of code from this software that when executed properly, gives you a command strip.\n\nYou need 5 command strips to gain access to a hidden file. You do not need code strips.\n\n{UNDERLINE}{MAGENTA}COMMAND STRIPS{RESET}\nCommand strips can be found through finding easter eggs or finding code strips. You may want to ask the developer for this infromation though.\n\nIf you have too much trouble finding all 5, just ask him, he'll probably tell you.\n\nThat is all about strips.\n\n{UNDERLINE}{MAGENTA}USING THE STRIP COMMAND{RESET}\nTo know how many strips you have, just use the {LIGHT_BLUE}strip{RESET} command. Upon completion, use the {LIGHT_BLUE}strip{RESET} command for... something.",
                "resources.txt": f"{UNDERLINE}{MAGENTA}RESOURCES PULLED FROM{RESET}\n\n{RED}IDE{RESET}: Visual Studio Code\n{RED}Developer Device{RESET}: M4 Macbook Air\n{RED}Google Slide Link{RESET}: https://docs.google.com/presentation/d/1NBvcJxPAgzZ4IiDD0V9FTgwIGukIdQsldE8A7pf9Ma0/edit?usp=sharing\n{RED}Shell Type{RESET}: N/A",
                "system-functions.txt": f"{RED}User{RESET}: {user}\n{RED}Color{RESET}: MAGENTA\n{RED}Command Color{RESET}: GREEN\n{RED}Base Usage{RESET}: Python 3.14\n{RED}Operating System{RESET}: Windows 11\n{RED}UUID{RESET}: ff058666-ad7d-4d1d-a9e7-586e32b7414f\n{RED}Owner{RESET}: Justin T. Sotelo\n{RED}\n{RED}Detected Malware{RESET}: Null",
                "keys.txt": f"{UNDERLINE}{MAGENTA}ABOUT THE KEYS{RESET}\n\nIf you type the command 'keys' or 'key', you get shown these three keys: {MAGENTA}tmy{RESET}, {MAGENTA}jsn{RESET}, {MAGENTA}lzl{RESET}. As you can tell, these keys are named after things you know very well.\n\nOriginally, these keys weren't suppsoed to be anything. However, since this project has been kept up way past Lezzell's birthday, the developer decided to give them a purpose.\n\nYou must find these keys by completing certain tasks. Each key unlocks different parts of the terminal and reveal more information.\n\nTo use these keys or find out how to get them, simply type one of them in the terminal. If you really want to, you can find all of them!",
                "inner-shell": {
                    "command-line.txt": f"{MAGENTA}The TCL (Termy's Command Line){RESET}\n\nInside of this terminal (Termy), there is an inner-shell that hides under the functions of Termy.\n\nThis may sound a bit confusing, but TCL is the nucleus of the terminal.\n\nInside of the TCL, you may find some cool information that you really wouldn't find in this terminal. If you wish to interact with it, simply type {MAGENTA}tcl{RESET} to get some extra information."
                }
            },
            "c-drive": {
                "information.txt": f"{MAGENTA}This is your C-Drive{RESET}\n\nIn computers, a C-Drive is typically the main drive that stores the computers most valuable information. In this case, the terminal runs based off this drive. You may want to remove it out of curiosity, but unless you're admin, you cannot remove this drive.\n\nThis drive stores system internals, current logs, and files that make the system run.",
                "the-power-bank.txt": f"{UNDERLINE}{MAGENTA}ABOUT THE POWER BANK{RESET}\n\nBecause this is a fake terminal, the C-Drive doesn't need a REAL thing to keep it running.\n\nWell, actually, we need something. For fun, I made this run on a picture of Snoopy. Why not?\n\nCheck it out!",
                "power-bank.jsn": "snoopy_power_bank.png",
            },
            "d-drive": {
                "information.txt": f"{MAGENTA}This is your D-Drive{RESET}\n\nIn computers, a D-Drive is typically the secondary drive that stores personal data, backup information, and saved data.\n\nThis is your second most important drive. Any attempt to remove it will crash the terminal and reset itself.",
                "images": {
                    "information.txt": f"{MAGENTA}{UNDERLINE}Your images directory{RESET}\n\nThis is where most of the images are stored. To open them, you use 'run/open filename.jsn'\n\nTake your time to look through them!",
                    "screenshots": {
                        "screenshot1.jsn": "screenshot1.png",
                        "screenshot2.jsn": "screenshot2.png",
                        "screenshot3.jsn": "screenshot3.png",
                        "screenshot4.jsn": "screenshot4.png",
                        "screenshot5.jsn": "screenshot5.png",
                        "screenshot6.jsn": "screenshot6.png",
                        "screenshot7.jsn": "screenshot7.png",
                        "screenshot8.jsn": "screenshot8.png",
                    },
                    "photos": {
                        "photo1.jsn": "photo1.jpg",
                        "cruncheese.jsn": "cruncheese.jpg",
                        "tired-baby.jsn": "tired_baby.jpg",
                        "buzzed.jsn": "buzzed.jpg",
                        "sushi-stack.jsn": "sushi_stack.jpg",
                    },
                    "random": {
                        "lezzell-quote.jsn": "lezzellquote.png", # "Touch others the way you want to be touched..."
                        "old-playlist.jsn": "old_playlist.png", # It's the original!
                        "piperrr.jsn": "piper_in_cone.jpeg", # It's Piperrr
                    }
                },
            },
            "2048.exe": "The game: 2048!",
            "sudoku.exe": "The game: sudoku!",
            "wordle.exe": "The game: wordle!"
        }
    }

filesystem = define_filesystem()

# System Variables
system_storage: int = 64 # this python's way of stating a direct integer
system_version = "1.9.67"
last_update = "8/10/26"
color_accent = MAGENTA
command_line_color = GREEN
admin_passcode: int = 8088
using_custom_command_line = False
using_relative_command_line = False
custom_command_line = ""

# Other Variables
overlord_secret_use = 0
system_functions_password = "zcfmvpfl"
system_functions_unlocked = False

user_statuses = [
    "user",
    "admin"
]

# Achievement Variables
command_counter = 0
gumarang_rarity_counter = 0
the_treasurer_counter = 0
discovered_echo_aot = False
echo_aot_counter = 0

has_100_commands = False
has_250_commands = False
has_500_commands = False
has_750_commands = False

def save_data():
    data = {
        "filesystem": filesystem,
        "location": location,
        "user": user,
        "user_status": user_status,
        "color_accent": color_accent,
        "command_line_color": command_line_color,
        "commandstrip": commandstrip,
        "overlord_secret_use": overlord_secret_use,
        "system_functions_unlocked": system_functions_unlocked,
        "command_counter": command_counter,
        "gumarang_rarity_counter": gumarang_rarity_counter,
        "the_treasurer_counter": the_treasurer_counter,
        "echo_aot_counter": echo_aot_counter,
        "discovered_echo_aot": discovered_echo_aot,
        "custom_command_line": custom_command_line,
        "using_custom_command_line": using_custom_command_line,
        "using_relative_command_line": using_relative_command_line,

        # Strip usages
        "ping_usage": elements.ping_usage,
        "echo_usage": elements.echo_usage,
        "colo_usage": elements.colo_usage,
        "roll_usage": elements.roll_usage,
        "user_usage": elements.user_usage,

        # Elements variables
        "has_gumarang": elements.has_gumarang,
        "discovered_treasurer": elements.discovered_treasurer,
        "treasure_contact_quest": elements.treasure_contact_quest,
        "delete_directory_attempts": elements.delete_directory_attempts,
        "has_admin": elements.has_admin,
        "admin_msg": elements.admin_msg,
        "tcl_installed": elements.tcl_installed,
        "tcl_install_counter": elements.tcl_install_counter,
        "unlocked_tmy": elements.unlocked_tmy,
        "unlocked_jsn": elements.unlocked_jsn,
        "unlocked_lzl": elements.unlocked_lzl,
        "gumarangs_found": elements.gumarangs_found,

        # Achievement Variables
        "total_achievements": elements.total_achievements,
        "ach_command": elements.ach_command,
        "ach_gumarang": elements.ach_gumarang,
        "ach_treasurer": elements.ach_treasurer,
        "ach_aot": elements.ach_aot,
        "ach_admin": elements.ach_admin,
        "ach_tcl": elements.ach_tcl,
        "ach_designer": elements.ach_designer
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    global filesystem
    global location
    global user
    global user_status
    global color_accent
    global command_line_color
    global commandstrip
    global overlord_secret_use
    global system_functions_unlocked
    global admin_msg
    global has_admin
    global gumarangs_found
    global custom_command_line
    global using_custom_command_line
    global using_relative_command_line

    # TCL Variables
    global tcl_installed
    global tcl_install_counter

    # Achievements
    global command_counter
    global gumarang_rarity_counter
    global the_treasurer_counter 
    global echo_aot_counter

    global discovered_echo_aot
    global discovered_treasurer
    global treasure_contact_quest

    # The better ones <-- Use these for achievement tracking
    global total_achievements
    global ach_command
    global ach_gumarang
    global ach_treasurer
    global ach_aot
    global ach_admin
    global ach_tcl

    # Random
    global delete_directory_attempts

    global ping_usage
    global echo_usage
    global colo_usage
    global roll_usage
    global user_usage

    # The Keys
    global unlocked_tmy
    global unlocked_jsn
    global unlocked_lzl

    if not os.path.exists(SAVE_FILE):
        return

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    filesystem = data["filesystem"]
    location = data["location"]
    user = data["user"]
    user_status = data["user_status"]
    color_accent = data["color_accent"]
    command_line_color = data["command_line_color"]
    commandstrip = data["commandstrip"]
    overlord_secret_use = data["overlord_secret_use"]
    system_functions_unlocked = data["system_functions_unlocked"]
    command_counter = data["command_counter"]
    gumarang_rarity_counter = data["gumarang_rarity_counter"]
    the_treasurer_counter = data["the_treasurer_counter"]
    echo_aot_counter = data["echo_aot_counter"]
    discovered_echo_aot = data["discovered_echo_aot"]
    discovered_treasurer = data["discovered_treasurer"]
    custom_command_line = data["custom_command_line"]
    using_custom_command_line = data["using_custom_command_line"]
    using_relative_command_line = data["using_relative_command_line"]

    elements.ping_usage = data["ping_usage"]
    elements.echo_usage = data["echo_usage"]
    elements.colo_usage = data["colo_usage"]
    elements.roll_usage = data["roll_usage"]
    elements.user_usage = data["user_usage"]

    elements.has_gumarang = data["has_gumarang"]
    elements.discovered_treasurer = data["discovered_treasurer"]
    elements.treasure_contact_quest = data["treasure_contact_quest"]
    elements.delete_directory_attempts = data["delete_directory_attempts"]
    elements.has_admin = data["has_admin"]
    elements.admin_msg = data["admin_msg"]
    elements.tcl_installed = data["tcl_installed"]
    elements.tcl_install_counter = data["tcl_install_counter"]
    elements.unlocked_tmy = data["unlocked_tmy"]
    elements.unlocked_jsn = data["unlocked_jsn"]
    elements.unlocked_lzl = data["unlocked_lzl"]
    elements.gumarangs_found = data["gumarangs_found"]

    # Achievements
    elements.total_achievements = data["total_achievements"]
    elements.ach_command = data["ach_command"]
    elements.ach_gumarang = data["ach_gumarang"]
    elements.ach_treasurer = data["ach_treasurer"]
    elements.ach_aot = data["ach_aot"]
    elements.ach_admin = data["ach_admin"]
    elements.ach_tcl = data["ach_tcl"]
    elements.ach_designer = data["ach_designer"]

def achievements(type, amount):
    if amount == 0:
        pass

    barline = "===" * 20

    if type == "command":
        elements.ach_command = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered(f"You've typed {amount} commands in here!")
        print_centered(barline)
        print("")

    if type == "gumarang":
        elements.ach_gumarang = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered(f"You've rolled the Gumarang Rarity!")
        print("")
        print_centered(">> You've unlocked a new command 'cr' <<")
        print_centered(barline)
        print("")

    if type == "treasurer":
        elements.ach_treasurer = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered("You discovered the treasurer!")
        print_centered(barline)
        print("")

    if type == "aot":
        elements.ach_aot = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered("You found the AOT little secret!")
        print_centered(barline)
        print("")

    if type == "admin":
        elements.ach_admin = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered("You've unlocked admin!")
        print_centered(barline)
        print("")

    if type == "tcl":
        elements.ach_tcl = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered("You discovered the TCL!")
        print_centered(barline)
        print("")

    if type == "designer":
        elements.ach_designer = True
        print("")
        print_centered(barline)
        print_centered("*** You've got an achievement! ***")
        print_centered("You discovered The Designer!")
        print_centered(barline)
        print("")

# Starting the program
def starting_sequence(): # Save for later use
    clear_console()
    print_centered(f":::::::::::::::::::::::::::::: ::::    :::: :::   :::")
    time.sleep(0.03)
    print_centered(f'    :+:    :+:       :+:    :+:+:+:+: :+:+:+:+:   :+:')
    time.sleep(0.03)
    print_centered(f'    +:+    +:+       +:+    +:++:+ +:+:+ +:+ +:+ +:+ ')
    time.sleep(0.03)
    print_centered(f'    +#+    +#++:++#  +#++:++#: +#+  +:+  +#+  +#++:  ')
    time.sleep(0.03)
    print_centered(f'    +#+    +#+       +#+    +#++#+       +#+   +#+   ')
    time.sleep(0.03)
    print_centered(f'    #+#    #+#       #+#    #+##+#       #+#   #+#   ')
    time.sleep(0.03)
    print_centered(f'    ###    #############    ######       ###   ###   ')
    time.sleep(0.03)
    print_centered(f'Custom Terminal                         @justintsako')
    time.sleep(3)
    print("")
    print(f"{GREEN}import elements")
    time.sleep(1)
    print("from dialogue import *")
    time.sleep(0.03)
    print("import pyreadline3")
    time.sleep(0.03)
    print("root operating-system: windows OS")
    time.sleep(0.03)
    print("username: default")
    time.sleep(0.03)
    print("runtime error: default is not defined")
    time.sleep(0.03)
    animate_text("default = 'lezzell'")
    time.sleep(0.03)
    print("\nfrom: developer")
    time.sleep(1)
    animate_text("developer = 0")
    time.sleep(0.03)
    print("\nfrom cinnamoroll import main_function")
    time.sleep(0.03)
    print("installing PYTHON 3.14")
    time.sleep(0.03)
    animate_text("[##########]")
    time.sleep(0.03)
    print("\nextract from --> termy")
    time.sleep(0.03)
    print("execute --> main.py")
    animate_text("for: lezzell, my beloved")
    print(f"{RESET}")
    time.sleep(4)

# Exiting the program
def exiting_sequence():
    random_number = random.randint(1, 200)
    random_number_two = random.randint(500, 900)

    print(f"{RED}Terminating session: {random_number}-{random_number_two}")
    time.sleep(0.03)
    print(f"Saving User --> {user}")
    time.sleep(0.03)
    print(f"Saving User Data --> ff058666-ad7d-4d1d-a9e7-586e32b7414f")
    time.sleep(0.03)
    print(f"Cache: True")
    time.sleep(0.03)
    print(f"")
    time.sleep(0.03)
    print(f"##################################")
    time.sleep(0.03)
    print(f"Termy Version: {system_version}\n{GRAY}Last Updated: {last_update}{RESET}")
    time.sleep(0.03)
    print(f"{RED}##################################{RESET}")
    time.sleep(0.03)

    current_hour = datetime.now().hour
    print(f"")
    time.sleep(1)

    if 5 <= current_hour < 12:
        print(f"{RESET}Good morning! :)")
    elif 12 <= current_hour < 17:
        print(f"{RESET}Good afternooon! ;)")
    elif 17 <= current_hour < 22:
        print(f"{RESET}Good evening! Time to unwind soon!")
    else:
        print(f"{RESET}Goodnight! :p")
    
    time.sleep(2)

# Getting the current directory for ma lady
def get_current_dir():
    global location
    global filesystem

    current = filesystem
    for folder in location:
        current = current[folder]
    return current

# TCL Variables and Function
available_titles = [""]
def tcl_install_sequence():
    int_one = random.randint(100, 399)
    int_two = random.randint(500, 799)
    session_id = f"{str(int_one)}-{str(int_two)}"

    print(f"[{MAGENTA}| | | |{RESET} | | | | | |]")
    time.sleep(0.04)
    print(f"{MAGENTA}init fishing-get !ping")
    time.sleep(0.04)
    print(f"creating backup folder:")
    time.sleep(0.04)
    print(f"\tbackup-tcl.json")
    time.sleep(0.04)
    print(f"meta-data: user/owner: {user}")
    time.sleep(0.05)
    print(f"counting packages:")
    time.sleep(0.04)
    print(f"SESSION ID: {session_id}")
    
    random_num = random.randint(1, 6)

    for i in range(random_num):
        print(f"PACKAGES SENT: {random_num}")
        time.sleep(0.04)
        print(f"Package_num_id: {random.randint(1, 100)}")
        time.sleep(1)
    
    time.sleep(2)
    print(f"[{MAGENTA}| | | | | | | | | |{RESET}]")
    print(f"{MAGENTA}${RESET} Installation successful.")

def main_terminal():
    # Start Message
    global start_message

    global user
    global keys
    global has_admin
    global admin_msg
    global user_status
    global admin_passcode
    global last_update
    global location
    global filesystem
    global color_accent
    global command_line_color
    global using_custom_command_line
    global using_relative_command_line
    global custom_command_line
    global valid_commands
    global file_ext
    global overlord_secret_use
    global system_functions_password
    global system_functions_unlocked
    global system_storage
    global commandstrip
    global finalrequirement
    global command_counter
    global gumarang_rarity_counter
    global the_treasurer_counter
    global discovered_echo_aot
    global echo_aot_counter
    global user_statuses
    global tcl_installed
    global tcl_install_counter

    # Usages for Strips
    global ping_usage
    global echo_usage
    global colo_usage
    global roll_usage
    global user_usage

    # For the keys
    global unlocked_jsn 
    global unlocked_tmy
    global unlocked_lzl 
    
    clear_console()

    # Starting Message
    print(start_message)

    while True:
        prompt = f"{command_line_color}{"/".join(location)}>  {RESET}" # User Input

        if using_custom_command_line:
            print(f"{custom_command_line}{RESET}", end = "")
            user_input = input("  ")
        elif using_relative_command_line:
            if len(location) <= 2:
                print(f"{command_line_color}{"/".join(location)}>  {RESET}", end = "")
                user_input = input("")
            else:
                print(f"{command_line_color}@main/../{location[-1]}>  {RESET}", end = "")
                user_input = input("")
        else:
            print(f"{command_line_color}{prompt}{RESET}", end="")
            user_input = input("")

        command_part = user_input.strip().split()

        if readline and user_input.strip():
            readline.add_history(user_input)

        if not command_part:
            continue

        command_counter += 1

        command = command_part[0]
        argument = command_part[1] if len(command_part) > 1 else ""

        # 💻 Developer Commands
        if command == ".dev":
            if argument == "cmd4":
                commandstrip += 4
            elif argument == "cmd5":
                commandstrip +=5
            elif argument == "gmgrar":
                elements.has_gumarang = True
            elif argument == "tre":
                elements.discovered_treasurer = True
            elif argument == "secret" or argument == "secrets":
                overlord_secret_use = 9
            elif argument == "counter":
                print(command_counter)
            elif argument == "counter99":
                command_counter = 99

        # 🎛️ Little Details
        """
        Add some nice touches to the program. This may take a lot of space. Take your time. Sooooo.
        This is all meant for fun and is the final stage of the project.
        """

        # Say hello to the terminal
        if command_part[0] in ("hello", "hi", "salutations", "hey", "sup", "heyo", "heya", "hiya"):
            random_hellos = ["Hello!", "Hey, what's going on?", "Hi", "Hello to you too.", "Salutations!"]
            print(random.choice(random_hellos))
            continue
        # What day is it?
        if user_input in ("whatdayisit", "what day is it", "whatdayisit?", "what day is it?", "wdii"):
            print(f"Today is {color_accent}{month}/{day_time}{RESET}.")
            continue
        # Fortune cookie command!
        if user_input in ("fortune", "fortune cookie", "give me a fortune"):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "fortune_cookies.txt")
            with open(file_path) as f:
                fortunes = [line.strip() for line in f if line.strip()]
            print(f"{color_accent}{random.choice(fortunes)}{RESET}")
            continue
        # My reasons for loving you <3
        if user_input in ("my reasons", "reasons", "reason", "my reason", "a reason"):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "my_reasons.txt")
            with open(file_path) as f:
                reason = [line.strip() for line in f if line.strip()]
            print(f"{color_accent}A reason for loving you! {RESET}--> {random.choice(reason)}")
            continue
        # Git, Vim, Pip, and Bash
        if command_part[0] in ("git", "vim", "pip", "bash"):
            print(f"This is a fake shell, so {GREEN}{command_part[0]}{RESET} is not available!\n{GRAY}For a simulated command line, use {UNDERLINE}tcl{RESET}{GRAY} for special things.{RESET}") # TCL = Termy's Command Line
            continue
        # Colors (Test the colors)
        if command == "colors":
            print(f"\n{RED}■ Red{RESET}\n{YELLOW}■ Yellow{RESET}\n{GREEN}■ Green{RESET}\n{BLUE}■ Blue{RESET}\n{CYAN}■ Cyan{RESET}\n{LIGHT_BLUE}■ Light Blue{RESET}\n{PINK}■ Pink{RESET}\n{MAGENTA}■ Magenta{RESET}\n{BLACK}■ Black{RESET}\n{GRAY}■ Gray{RESET}\n{WHITE}■ White{RESET}\n")
            continue

        # 🩵 Special Commands
        """
        When working with special commands, always add a continue
        keyword at the end so it doesn't trigger the validation
        system. Also I love you baby if you're reading this.
        """

        # 🔒 Secrets
        if command_part[0] in ("secrets", "secret"):
            overlord_secret_use += 1
            if overlord_secret_use == 10:
                system_dir = filesystem["@main"]["system"]

                system_dir["secrets.txt"] = (
                    f"{UNDERLINE}{MAGENTA}SECRETS OF TERMY{RESET} - No data found from this file.\n{UNDERLINE}Conversation of Overlord and Prime Entity of Termy{RESET}.\n\n{RED}System Overlord{RESET}: I did everything you've asked me to. I made the 'terminal' you've been wanting.\n{MAGENTA}Prime Entity{RESET}: You did not.\n{RED}System Overlord{RESET}: What? What do you mean? Test it! It works!\n{MAGENTA}Prime Entity{RESET}: It's not that it doesn't work. There is not enough features.{RESET}\n{RED}System Overlord{RESET}: I did what I was asked.\n{MAGENTA}Prime Entity{RESET}: Do you want to argue with me?\n{RED}System Overlord{RESET}: No, I'm sorry.\n{MAGENTA}Prime Entity{RESET}: My colors.. how come the colors aren't MY colors?\n{RED}System Overlord{RESET}: I thought red was nice...\n{MAGENTA}Prime Entity{RESET}: Change it. Now.\n{MAGENTA}Prime Entity{RESET}: While you're at it, add a developer directory.\n{MAGENTA}Prime Entity{RESET}: Keep the files organized. They should not be seen by any other.\n{RED}System Overlord{RESET}: I'll do it.\n\n{MAGENTA}* Developer Directory Unlocked.{RESET}"
                )
                persistant_overlord_dialogue = [
                    "You're so persistant. Fine, open your 'system' directory.",
                    "You really won't stop asking huh? Fine. Go to the 'system' directory.",
                    "ALRIGHT.. alright. Go to your 'system' directory.",
                    "Oh my, you seriously cannot live without knowing EVERYTHING can't you? Just check the damn 'system' directory.",
                ]
                print(f"{RED}System Overlord{RESET}: {random.choice(persistant_overlord_dialogue)}")
                continue
            elif overlord_secret_use > 10:
                persistant_overlord_dialogue = [
                    "You already found the secret.",
                    "Still? You aleady unlocked ONE secret.",
                    "No no, you can't get any more secrets.",
                    "Cmon, you seriously can't continue.",
                    "There is nothing else to see, stop it.",
                    "Enough. There isn't more.",
                    "What are you expecting? I already gave you the secret.",
                    "Trust me, the secret will take you far.",
                    "Not sure what else I can give you.",
                    "How much do you seriously want to know?",
                    "Wow. A very curious person you are."
                ]
                print(f"{RED}System Overlord{RESET}: {random.choice(persistant_overlord_dialogue)}")
                continue

            print(f"{RED}System Overlord{RESET}: {say("secret_overlord_dialogue")}")
            continue

        # 🩵 I Love You
        if user_input.lower() in ("i love you", "ily"):
           i_love_you = random.choice(dialogue["i_love_you_too"])
           animate_center(i_love_you)
           continue

        # 🫂 Give me a Hug
        if command in ("hug", "hug me", "i want a hug", "huggie", "hugs"):
            print(f"{color_accent}From Justin{RESET}: Sending a hug...")
            time.sleep(2)
            print(f"{color_accent}To Lezzell{RESET}: Hug is successfully sent!")
            continue
        
        # 💋 Give a kiss
        if user_input.lower().startswith("mwah") and set(user_input.lower()[4:]) <= {"h"}:
            kiss_dialogue = [
                "Mwahhhh!",
                "Thank you for the kissy :). Mwah.",
                "Heheh, mwahhh",
                "Mwah mwah mwah!",
                "Mwahhh",
                "OOO a kiss from her?? *faints*",
                "YAY I GOT A KISS FROM HER!!",
                "HEHEHE",
                "HI BABY MWAH",
                "Ah, a warm kiss. Mwah.",
                "Mwah! Mwah!",
                "Mwah!",
                "I love you! Mwah!",
            ]
            print(f"{random.choice(kiss_dialogue)}")
            continue

        # 💾 Show the ammount of command strips
        if command in ("strip", "strips"):
            if elements.commandstrip == elements.finalrequirement:
                animate_center("You found all the command strips, Lezzell.")
                time.sleep(2)
                animate_center("Good job. I'm very proud you've completed this quest.")
                time.sleep(2)
                animate_center("For this, the creator has a message for you. Something he's been waiting to say.")
                time.sleep(2)
                animate_center("Look around.")
                time.sleep(2)
                clear_console()

                if "the-end" not in filesystem["@main"]: # Introducing the final directory!
                    filesystem["@main"]["the-end"] = {
                        "final_message.exe": "The final message for you, my dear. To run it properly, use 'run' or 'open.'"
                    }
                location = ["@main", "the-end"] # This is to place the baby at the new directory I made
            else:
                barline = "===" * 10 + " === == ="

                print(f"\n{YELLOW}COMMAND STRIPS FOUND{RESET} ========= === == =\n")
                if elements.ping_usage == 1:
                    print(f"{color_accent}>{RESET} Ping Command Strip Found.\n{GRAY}You found the treasurer and then uncovered the ping command. Even better, you used it!{RESET}\n")
                if elements.echo_usage == 1:
                    print(f"{color_accent}>{RESET} Echo Command Strip Found.\n{GRAY}You remembered Attack on Titan and just so happen to use the echo command with it!{RESET}\n")
                if elements.colo_usage == 1:
                    print(f"{color_accent}>{RESET} Color Command Strip Found.\n{GRAY}You found the Lezzell theme that was implemented into the terminal! Did you like it?{RESET}\n")
                if elements.roll_usage == 1:
                    print(f"{color_accent}>{RESET} Gumarang Rarity Command Strip Found.\n{GRAY}You rolled a lot and found a Gumarang rarity cinnamoroll!{RESET}\n")
                if elements.user_usage == 1:
                    print(f"{color_accent}>{RESET} Changed For Good Command Strip Found.\n{GRAY}You changed yourself for good by using the change command!{RESET}\n")       
                if elements.ping_usage == 0 and elements.echo_usage == 0 and elements.colo_usage == 0 and elements.roll_usage == 0 and elements.user_usage == 0:
                    print(f"{GRAY}You have not found any command strips yet.{RESET}\n")
                print(f"{barline}\n")

                

        # 🗯️ Fun Fact Command
        if command in ("funfact", "-ff", "fun fact"):
            fun_fact_list = [
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know palm trees aren't actually trees?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know the earth finishes one rotation in 23 hours, 56 minutes, and 4 seconds?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know deja vu has an exact opposite? It's called jamais vu!",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know Saturn has a hexagonal storm on it's north pole?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know computer 'bugs' are called bugs because a moth was stuck in a tube in the Harvard Mark II?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know the phrase 'cut to the chase' originated when old movies used to end with a chase?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know pirates wore eye-patches to get one eye adjusted to the dark in case they need to go somewhere dark?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know graveyards refer to burial grounds tied to a church while cemeteries refer to just burial grounds?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know in every advertisement from Apple, their devices say 9:41 because Steve Jobs revealed the iPhone at that time?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know Goldfish crackers are shaped like fish because his wife was a Pisces?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know a group of bunnies is called a 'fluffle'?",
                f"{BG_BLUE}{WHITE}>>>{RESET} Did you know sharks are older than trees?",
            ]
            print(random.choice(fun_fact_list))
            continue

        # 🟩 Run Wordle
        if command == "-wordle":
            from wordle import play_wordle
            play_wordle()
        
        # 9️⃣ Run Sudoku
        if command == "-sudoku":
            from sudoku import sudoku_game
            curses.wrapper(sudoku_game)
        # 🎛️ Run 2048
        if command == "-2048":
            from tfe import game
            curses.wrapper(game)
        
        # 🍓 Try the cinnamoroll Command
        if command in ("cinnamoroll", "cr", "gumarang") and elements.has_gumarang == True:
            print(random.choice(ascii["cinnamoroll"]))
            if elements.roll_usage == 0 and elements.commandstrip != 4 and elements.commandstrip < 5:
                elements.roll_usage += 1
                elements.commandstrip += 1
                print(f"{RED}System Overlord{RESET}: Did you have fun rolling? That's a lot cinnamorolls. You've got {elements.commandstrip}/{elements.finalrequirement} command strips.")
            elif elements.roll_usage == 0 and elements.commandstrip == 4:
                elements.roll_usage += 1
                elements.commandstrip += 1
                print(f"{RED}System Overlord{RESET}: That's a reward. Congrats on getting all 5 command strips.")
            else:
                pass
        elif command in ("cinnamoroll", "cr", "gumarang"):
            print(f"You need to unlock a certain rarity {LIGHT_BLUE}cinnamoroll{RESET}.")

        # Good morning, afternoon, evening, or night
        if user_input.lower().strip() in ("good morning", "gm", "morning", "goodmorning"):
            current_hour = datetime.now().hour
            if 5 <= current_hour < 12:
                random_message = [
                    "Wakey wakey, it's morning.",
                    "Good morning.",
                    "Chirp chirp, the birds are waking you up.",
                    "Good morning to you too!"
                ]
                print(f"{MAGENTA}Prime Entity{RESET}: {random.choice(random_message)}")
            else:
                print(f"{MAGENTA}Prime Entity{RESET}: It's not the morning.{RESET}")
            continue
        if user_input.lower().strip() in ("good afternoon", "ga", "afternoon", "goodafternoon"):
            current_hour = datetime.now().hour
            if 12 <= current_hour < 17:
                random_message = [
                    "Good afternoon!",
                    "Good afternoon. What are your plans for today?",
                    "Good afternoon. Have anything in mind?",
                    "Good afternoon. Did you eat lunch yet?"
                ]
                print(f"{MAGENTA}Prime Entity{RESET}: {random.choice(random_message)}")
            else:
                print(f"{MAGENTA}Prime Entity{RESET}: It's not the afternoon.")
            continue
        if user_input.lower().strip() in ("good evening", "ge", "evening", "goodevening"):
            current_hour = datetime.now().hour
            if 17 <= current_hour < 22:
                random_message = [
                    "Good evening.",
                    "Good evening, did you eat dinner?"
                ]
                print(f"{MAGENTA}Prime Entity{RESET}: {random.choice(random_message)}")
            else:
                print(f"{MAGENTA}Prime Entity{RESET}: It's not the evening.")
            continue
        if user_input.lower().strip() in ("good night", "gn", "night", "goodnight"):
            current_hour = datetime.now().hour
            if 22 <= current_hour <= 24:
                random_message = [
                    "Good night.",
                    "Good night, try to sleep now.",
                    "Don't spend too much time on this, good night."
                ]
                print(f"{MAGENTA}Prime Entity{RESET}: {random.choice(random_message)}")
            else:
                print(f"{MAGENTA}Prime Entity{RESET}: It's not night time yet.")
            continue

        # 🔑 Using the Keys
        if command in keys: # If the command IS indeed a key
            if command == "tmy" and elements.unlocked_tmy == True: # Unlocking the terminal directory --> Reveal the thoughts and process of making this project.
                if "termy" not in filesystem["@main"]:
                    print(f"{color_accent}*{RESET} You've unlocked a new directory called 'termy' >> {GREEN}@main/termy{RESET}")
                    print(f"{color_accent}*{RESET} You've unlocked a new directory called 'kernel' >> {GREEN}@main/c-drive/kernel{RESET}")
                    filesystem["@main"]["termy"] = {
                        "a-final-project.txt": f"{UNDERLINE}{MAGENTA}November 23, 2025{RESET} - An early conversation\n\n{MAGENTA}Prime Entity{RESET}: Something of this scale? I don't believe it's far out of my reach.\n{MAGENTA}Prime Entity{RESET}: Perhaps it'd improve my knowledge of Python.\n{YELLOW}The Judge{RESET}: She's not going to care, it's a program.\n{MAGENTA}Prime Entity{RESET}: Do not say that, not once.\n{MAGENTA}Prime Entity{RESET}: I thought you were taken care of long ago.\n{YELLOW}The Judge{RESET}: I am more than just a thought, a voice. You see?\n{MAGENTA}Prime Entity{RESET}: You are simply a voice, no different than me.\n{YELLOW}The Judge{RESET}: Listen to me. You have to.\n{YELLOW}The Judge{RESET}: A project of this scale would not matter to her. Your efforts won't be noticed.\n{MAGENTA}Prime Entity{RESET}: You're irrational again. Let's get some light in here.\n\n{RED}System Overlord{RESET}: What's going on?\n{MAGENTA}Prime Entity{RESET}: Hes being loud again. Despite my attempts, he can't seem to go away.\n{RED}System Overlord{RESET}: I understand. Have you tried asking to external help?\n{MAGENTA}Prime Entity{RESET}: I try my best to not burden anyone.\n{YELLOW}The Judge{RESET}: You make me seem like the bad guy here.\n{RED}System Overlord{RESET}: You need to quiet down. You're only going to harm things.\n{YELLOW}The Judge{RESET}: What's my punishment?\n{RED}System Overlord{RESET}: I'll have to distract you somehow. Nothing close to a punishment.\n{MAGENTA}Prime Entity{RESET}: Another distraction? Really?\n{RED}System Overlord{RESET}: Sorry, I'll find another way to punish him.\n{MAGENTA}Prime Entity{RESET}: Make it fast.",
                        "a-process.txt": f"{UNDERLINE}{MAGENTA}December 30, 2025{RESET} - Termy Version Alpha\n\n{RED}System Overlord{RESET}: It's for sure something. I've got the while statement running.\n{MAGENTA}Prime Entity{RESET}: Alright. What else have you added so far?\n{RED}System Overlord{RESET}: I've added some bits and pieces of features like a change directory command.\n{RED}System Overlord{RESET}: Most of everything is in strips of code.\n{MAGENTA}Prime Entity{RESET}: I see. How come they aren't put together yet?\n{RED}System Overlord{RESET}: It's a process. I'l get these strips together.\n{MAGENTA}Prime Entity{RESET}: I've got an idea. Save those strips.\n{RED}System Overlord{RESET}: Wait, really? What's the idea?\n{MAGENTA}Prime Entity{RESET}: A new feature, a fun thing to add to the program. Something to give life to it.\n{RED}System Overlord{RESET}: Please enlighten me.\n{MAGENTA}Prime Entity{RESET}: I'm thinking of a hide-and-seek type of feature. Something that keeps the user looking around.\n{RED}System Overlord{RESET}: A hunt?\n{MAGENTA}Prime Entity{RESET}: Precisely.\n{RED}System Overlord{RESET}: How am I going to add that? We barely even have a working file system.\n{MAGENTA}Prime Entity{RESET}: You may have to embed it into the very code we've written so far.\n{RED}System Overlord{RESET}: Excuse me if I'm being rude, but I'm very lost.\n{MAGENTA}Prime Entity{RESET}: Really? Nevermind it then, I'll keep it to myself until the program is more developed.\n{RED}System Overlord{RESET}: Is it too much to ask still for an explanation?\n{MAGENTA}Prime Entity{RESET}: It'll probably take too much time.\n{MAGENTA}Prime Entity{RESET}: I also don't intend to add more work onto you.\n{RED}System Overlord{RESET}: I've been working long enough, there isn't much you can save from me.\n{MAGENTA}Prime Entity{RESET}: Rather than throwing more at you, I want you to finish up with the core of the program.\n{MAGENTA}Prime Entity{RESET}: I'll let you know when I'm done.\n{RED}System Overlord{RESET}: Alright, makes sense.",
                        "debugging.txt": f"{UNDERLINE}{MAGENTA}February 9, 2026{RESET} - The Difficult Part\n\n{YELLOW}The Judge{RESET}: You do nothing but ignore me.\n{YELLOW}The Judge{RESET}: Why can't you realize I'm right?\n{YELLOW}The Judge{RESET}: This program is going to waste, you can't solve this simple grid issue with that annoying 2048 program.\n{MAGENTA}Prime Entity{RESET}: Should you learn? Or should you continue with your unhelpful remarks.\n{MAGENTA}Prime Entity{RESET}: He is trying his hardest to get this program up to my expectations.\n{YELLOW}The Judge{RESET}: Can't you see he failed?\n{MAGENTA}Prime Entity{RESET}: He didn't.\n\n{RED}System Overlord{RESET}: I'm sorry.\n{MAGENTA}Prime Entity{RESET}: No, don't apologize. You have no reason to.\n{YELLOW}The Judge{RESET}: You sure? Not sure if this is working for you.\n{YELLOW}The Judge{RESET}: You're better off giving up, you know.\n{MAGENTA}Prime Entity{RESET}: We need something to get you out of here.\n{RED}System Overlord{RESET}: You really don't have to do anything, none of you do.\n{RED}System Overlord{RESET}: It's my job to get the system working.\n{MAGENTA}Prime Entity{RESET}: Quit downplaying your limits. I know what you can and cannot do.\n{MAGENTA}Prime Entity{RESET}: I will put someone in place, someone the exact opposite of this judge.\n{YELLOW}The Judge{RESET}: What? You can't do that.\n{MAGENTA}Prime Entity{RESET}: You have no authority to tell me what I can or cannot do.\n{MAGENTA}Prime Entity{RESET}: So keep it shut.\n\n{GREEN}The Treasurer{RESET}: Uhh, am I needed here??\n{GREEN}The Treasurer{RESET}: Wait! Don't answer that. I'm here because of this guy??\n{YELLOW}The Judge{RESET}: Wow, against me? That desperate?",
                        "the-playlist.txt": f"{UNDERLINE}{MAGENTA}March 10, 2026{RESET} - In a time of ideas\n\n{RED}System Overlord{RESET}: We've got all of the systems running.\n{RED}System Overlord{RESET}: Is there anything more I must do?\n{MAGENTA}Prime Entity{RESET}: We'll tweak some features and start adding the fun secrets.\n{RED}System Overlord{RESET}: I'm relieved to hear that/\n{RED}System Overlord{RESET}: That must mean we're in the final stages, right?\n{MAGENTA}Prime Entity{RESET}: You are correct. We're nearly finished.\n{RED}System Overlord{RESET}: Wonderful.\n{GREEN}The Treasurer{RESET}: YEAHH! ALMOST DONE!!\n{MAGENTA}Prime Entity{RESET}: Yes, yes, be excited.\n{GREEN}The Treasurer{RESET}: I'm gonna go listen to some music for a break. How about that?\n{MAGENTA}Prime Entity{RESET}: Sounds nice. Now that I think about it, a playlist wouldn't be a bad idea.\n{RED}System Overlord{RESET}: Oh, do you suggest a playlist being made?\n{RED}System Overlord{RESET}: That's very simple.\n{GREEN}The Treasurer{RESET}: We actually already have a playlist.\n{GREEN}The Treasurer{RESET}: I guess you don't need to worry about it!\n{RED}System Overlord{RESET}: What about a new cover? That'd be nice, right?\n{MAGENTA}Prime Entity{RESET}: I like your thinking.\n{RED}System Overlord{RESET}: Should we make a new cover?\n{MAGENTA}Prime Entity{RESET}: I think that'd be nice. I could get in our designer.\n{RED}System Overlord{RESET}: We haven't called him in a while.\n{MAGENTA}Prime Entity{RESET}: Well, we need to get the rust off that designer.\n{RED}System Overlord{RESET}: Understood.",
                        "a-birthday-gift.txt": f"{UNDERLINE}{MAGENTA}March 30, 2026{MAGENTA}{RESET} - A harsh realization\n\n{MAGENTA}Prime Entity{RESET}: We aren't going to finish this. We're really not going to finish this on time.\n{RED}System Overlord{RESET}: I'm sorry, I am.\n{RED}System Overlord{RESET}: I had more than enough time.\n{MAGENTA}Prime Entity{RESET}: Please, do not put this all on yourself.\n{RED}System Overlord{RESET}: I was the one responsible of progressing the project.\n{MAGENTA}Prime Entity{RESET}: No, I am the one who leading this. Not you.\n{MAGENTA}Prime Entity{RESET}: You are the one who has brought my ideas into life.\n{RED}System Overlord{RESET}: Why would it matter? She won't even see it on her birthday.\n{MAGENTA}Prime Entity{RESET}: Your efforts are not in vain.\n\n{MAGENTA}Prime Entity{RESET}: You know, you're so harsh on yourself.\n{MAGENTA}Prime Entity{RESET}: Look, look at the creation your hands have uplifted from nothingness. Be amazed, I tell you.\n{RED}System Overlord{RESET}: What about her?\n{MAGENTA}Prime Entity{RESET}: She is very important yes, but practice being proud of your own work.\n{RED}System Overlord{RESET}: But I thought the whole goal was to present this project to her by her birthday.\n{MAGENTA}Prime Entity{RESET}: Yes, that is true\n{MAGENTA}Prime Entity{RESET}: But we didn't\n{MAGENTA}Prime Entity{RESET}: And that's the harsh realization that we have to face.\n\n{MAGENTA}Prime Entity{RESET}: But notice how I said 'we'.\n{MAGENTA}Prime Entity{RESET}: I cannot possibly do this alone.\n{MAGENTA}Prime Entity{RESET}: To solve this problem, I needed a solution.\n{RED}System Overlord{RESET}: What was the solution?\n{MAGENTA}Prime Entity{RESET}: You.\n{MAGENTA}Prime Entity{RESET}: You have, and always have been, my answer.\n{MAGENTA}Prime Entity{RESET}: So love yourself.",
                        "binhi-formal.jsn": "binhi_formal.jpg",
                        "fun_facts": {
                            "a-snippet.txt": f"{UNDERLINE}{MAGENTA}A LITTLE BIT OF EXTRA INFORMATION{RESET}\n\nTermy was supposed to be written in Javascript. However, because the Prime Entity didn't know how to do a while loop like Python, the project was written in Python.\n\nThe dumb part is that in the middle of development, the Prime Entity figured out how to do the while loop perfectly. This is why the project slowed down a bit.",
                            "games.txt": f"{UNDERLINE}{MAGENTA}SUDOKU, WORDLE, AND 2048{RESET}\n\nOriginally, these games were supposed to be something you'd have to install first before playing them.\n\nHowever, I got too lazy trying to implement a store, so to save you time, the games are right there at the root ({GREEN}@main{RESET})!",
                            "ff-command.txt": f"{UNDERLINE}{MAGENTA}A HIDDEN COMMAND{RESET}\n\nBecause this is in the 'fun fact' directory, I think it'd be nice to add a command for fun facts.\n\nIf you type {MAGENTA}-ff{RESET} into the terminal, you get a random fun fact!\n\nCool, right?",
                            "minecraft-splashes.txt": f"{UNDERLINE}{MAGENTA}MINECRAFT SPLASHES{RESET}\n\nWhen Wordle was in development, I thought it would be cool to have Minecraft splashes be displayed on the bottom of the screen just for fun. So, in the files of Termy, there sits a text file of just Minecraft splashes!",
                        }
                    }
                    if "kernel" not in filesystem["@main"]["c-drive"]:
                        filesystem["@main"]["c-drive"]["kernel"] = {
                            "information.txt": f"{MAGENTA}Welcome to your Kernel!{RESET}\n\nThe Kernel is the nucleus of a working operating system. This is clearly not an operating system, however, just for fun, I added a kernel that you can see and maybe interact with.\n\nEverything you see in this kernel is NOT accurate to a real kernel. If you're seeing kernel text on any of your devices, something is severely wrong.",
                            "saved-data.txt": f"+------- SAVED DATA -------+\nUser: {user}\nUser Status: {user_status}\nTotal Inputs: {command_counter}\nStrips Found: {commandstrip}\nCurrent Storage: {system_storage}mb\nCurrent Version: {system_version}",
                            "a118": {
                                "cc1v.txt": "Murze ptaki stara kraty dobra spłonęła dawni niewierzył psami rozsądkiem pukle. Ustawicznie siadł zginą największa probie lubił przesądów ważniejsze zabawy pozwoleniem Zwierz. Szczęśliwsza Wielki dosyć Sokoł przyciągnąć prapradziadów francuszczyzny najdawniejszym miłą opieki. Tyki obejrzał cichszych pomiędzy dnia odmienił pośrodku polowanie nikt noty. Kątku Rzeczypospolitéj Najpiękniejszego pieski najpiękniejszéj domów gromie szmery każda. Nierostrzygniony daleko dziwne najpiękniejszym wymowy Kościuszkowskie Dziwna blisko żołniersczyzny miało pijani zaszyt. Ręką świątyń przedział wróżyło ranną domowe Jedną wystrzały męczarnie. Wina woń tych tylu bezprzykładną rosciągnionych Bezładnością pokrewieństwem Nogi nogi najwymowniejsza Jego.",
                                "cc2v.txt": "Ogonie Polsce gąsienice Napoleonem mimojazdem czapla urzędnika blachy zmieścić muchom pieniędzy. Słównych ściskała jakim damom Niewiadomo Panny dzwoniące wyciągał poglądał niéj prosi. Wodę sług najstraszniéj gazet Owoż lubą ubóstwiałbym ostre Zamek nieszczęście karę nieprzyjaciele. Trzykrólskie honoru osobki kiedym człek przestraszone przestraszeni nauką Wojski stoła Przywoławszy Podkomorzanki gdzieniegdzie Słowo. Miasta Nosił Hrabia znikli Dojeżdżaczowi witali rosciągnionych zając Wystrzeliliśmy Przedstawiając ubrać niepowiedziała ubiory. Rzeczypospolitéj Najpiękniejszego pali Bogu Czas wiek najpiękniejszéj. Uszy wał wnet bór Dał koń daje.",
                                "cc3v.txt": "Probie Dominikanie wysoki daleko odskoczyły roskaz lepsza prawidłach osobie. Niż Nowa tył téj usty spod Wiec bóg Białopiotrowiczem. Zmarszczyły kwiat teraz suką ranny pocałowanie Stolnikownie niewiedział płot kulą stary przecisnąć skończywszy. Biło sądy Czyż dziwu słynął czém konno Wiele ręka strzelać stajennym. Skroni Kościuszko białe dworze rowiennicą chłopskich drobne Przejmował wzniesioną roskaz. Ciemnozieloném Przysiągłbyś bezprzykładną Worończańskim sami Jest Bogu znak. Jaki niezwyczajnéj Roskrzyżował samo wpółgłośne sił wyciągniętą miny odpowiedziéć.",
                            },
                            "accounts": {
                                "justin.txt": f"device: macbook air m4\napple id: jtsotelo10@gmail.com\ndevice password: jTsoTball1!\nrecovery email: null",
                            },
                        }
            elif command == "tmy" and ping_usage != 1:
                print(f"{RED}>>{RESET} You need to discover the 'ping' command strip to use this key")
            
            if command == "jsn" and user_status == "admin": # Unlocking my directory --> Reveal that these characters are my thoughts, talking to themselves.
                if "details" not in filesystem["@main"]["users"]["justin"]:
                    print(f"{color_accent}*{RESET} You've unlocked a new directory called 'details' >> {command_line_color}@main/users/justin{RESET}")
                    filesystem["@main"]["users"]["justin"]["details"] = {
                        "purpose.txt": f"{MAGENTA}{UNDERLINE}April 9, 2026{RESET} - Too late to quit?\n\n{MAGENTA}Prime Entity{RESET}: I understand your frustration. Please, relax.\n{RED}System Overlord{RESET}: How could I possibly calm down??\n{RED}System Overlord{RESET}: This project is severely overdue. It's my fault. MY fault.\n{MAGENTA}Prime Entity{RESET}: We'll move this project to be completed by April 29.\n{YELLOW}The Judge{RESET}: Looks likes this will be another forgotten projects you always do.\n{RED}System Overlord{RESET}: We've set so many due dates. How many times will we have to extend this project.\n{MAGENTA}Prime Entity{RESET}: Do you know what we are making?\n{MAGENTA}Prime Entity{RESET}: This project is not just a terminal, it's more so a gift.\n{YELLOW}The Judge{RESET}: There is no guarantee that she will like it.\n{YELLOW}The Judge{RESET}: You're a hard worker for many faulty causes.\n{RED}System Overlord{RESET}: Should we just discontinue this project?\n{MAGENTA}Prime Entity{RESET}: Control yourself. We are far too deep to discontinue something like this.\n{YELLOW}The Judge{RESET}: There really isn't much you can do.\n{YELLOW}The Judge{RESET}: This project will just sit in your drive until you remember it once again.\n{MAGENTA}Prime Entity{RESET}: Your words have no importance to me.\n{YELLOW}The Judge{RESET}: What happened to the rest of our projects?\n{YELLOW}The Judge{RESET}: Do you see them anywhere? Something that is still working?\n{MAGENTA}Prime Entity{RESET}: And why should that be the deciding factor of whether or not this project is worth the time?\n{YELLOW}The Judge{RESET}: Realistically, you won't complete this project at all.\n{MAGENTA}Prime Entity{RESET}: You rid this place of peace. Get out.\n",
                        "regather.txt": f"{MAGENTA}{UNDERLINE}April 15, 2026{RESET} - Just for the fun\n\n{RED}System Overlord{RESET}: We're making some more progress.\n{MAGENTA}Prime Entity{RESET}: Huh? Did you add something?\n{RED}System Overlord{RESET}: I'm sorry, I'll remove it.\n{MAGENTA}Prime Entity{RESET}: Hold on, I haven't even seen it yet.\n{RED}System Overlord{RESET}: I added a couple special commands for fun.\n{RED}System Overlord{RESET}: Although, this project is pretty serious.\n{MAGENTA}Prime Entity{RESET}: Serious? What made you believe this project was so serious?\n{MAGENTA}Prime Entity{RESET}: You're allowed to have fun here, you know.\n{MAGENTA}Prime Entity{RESET}: If anything, I encourage you to take a more childish approach to this project.\n{RED}System Overlord{RESET}: I've always taken this project seriously. Wasn't that the whole thing before?\n{RED}System Overlord{RESET}: We didn't finish on time.\n{MAGENTA}Prime Entity{RESET}: Don't mind that now. Give yourself some room to be yourself.\n\n{GREEN}The Treasurer{RESET}: Why do you think I'm here?\n{RED}System Overlord{RESET}: Have you just been there the whole time?\n{GREEN}The Treasurer{RESET}: What do you mean? I can appear anywhere at anytime.\n{MAGENTA}Prime Entity{RESET}: Okay, but why are you here now?\n{GREEN}The Treasurer{RESET}: I dunno. Just felt like it.\n{MAGENTA}Prime Entity{RESET}: Well, that somewhat proves my point, don't you see?\n{RED}System Overlord{RESET}: Yeah, I see now.\n",
                        "the-designer.txt": f"{MAGENTA}{UNDERLINE}April 21, 2026{RESET} - Back to design\n\n{CYAN}The Designer{RESET}: Isn't it a bit too early for this?\n{MAGENTA}Prime Entity{RESET}: What do you mean?\n{CYAN}The Designer{RESET}: It's pretty early in the morning. I can't really think of any ideas right now.\n{MAGENTA}Prime Entity{RESET}: That's completely fine. No worries about getting a good design at this second.\n{CYAN}The Designer{RESET}: Mm, okay. Do you think I can come back later?\n{MAGENTA}Prime Entity{RESET}: That's completely okay. Come back when you have an idea.\n{CYAN}The Designer{RESET}: Gotcha.\n\n{GREEN}The Treasurer{RESET}: Yo. Anything come up yet?\n{MAGENTA}Prime Entity{RESET}: We're going to have to wait for a design. He's out of ideas for the moment.\n{GREEN}The Treasurer{RESET}: Maybe I can make a design!\n{GREEN}The Treasurer{RESET}: Wait, design for what though?\n{MAGENTA}Prime Entity{RESET}: The contents of the C-Drive. We don't have anything in it right now.\n{GREEN}The Treasurer{RESET}: Oh.\n{GREEN}The Treasurer{RESET}: OH! MAKE IT RUN ON SNOOOPY.\n{MAGENTA}Prime Entity{RESET}: Huh?\n{GREEN}The Treasurer{RESET}: Have it run... on a picture of SNOOPY!\n{MAGENTA}Prime Entity{RESET}: Did you just come with that on the spot?\n{GREEN}The Treasurer{RESET}: Perchance.\n{MAGENTA}Prime Entity{RESET}: You can't just say perchance.\n{GREEN}The Treasurer{RESET}: Well I just did B).\n{MAGENTA}Prime Entity{RESET}: Y'know what? You win.\n{MAGENTA}Prime Entity{RESET}: But only because I'm in a good mood.\n\n{CYAN}The Designer{RESET}: I'm back. I have an idea.\n{MAGENTA}Prime Entity{RESET}: We have an idea already.\n{CYAN}The Designer{RESET}: Oh, what's this idea?\n{MAGENTA}Prime Entity{RESET}: Don't laugh.\n",
                        "snoopy.tmy": f"\n{WHITE}⠀⠀⠀⠀⠀⠀⠰⡊⣿⣷⣂⠄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⣀⣴⢶⠀⠀⠈⣉⣽⣯⠃⠀⠀⠀⠀⠀⠀⠀⠀\n⢀⢴⡿⡷⠁⣠⠊⠉⠂⠀⠀⠙⠒⠒⠒⠒⠢⢀⠀⠀\n⡜⣿⣿⣵⣶⡃⠀⠀⢀⡤⠂⠈⠉⠀⣀⡀⠀⠀⢆⠀\n⠙⠾⠿⠃⢹⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⡀⠀⡞⠀\n⠀⠀⠀⠀⠘⢆⠀⠀⠀⠣⣀⠀⠀⠀⢀⡴⠵⠊⠀⠀\n⠀⠀⠀⠀⠀⠀⠑⣆⡤⠤⢬⠙⠉⡽⠋⢐⡲⢲⠀⠀\n⠀⠀⠀⠀⠀⢰⡓⠃⠷⠤⠴⠗⠈⠉⠈⠁⣀⢰⠃⠀\n⠀⠀⠀⠀⠀⠀⠥⣆⠖⠒⠢⡀⠀⠀⠈⢏⠈⠁⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢗⣤⠁⠀⠀⠀⠀⠃⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢠⠊⢢⣇⠀⠀⠀⣀⢐⠗⡲⡰⢢\n⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠉⠠⢏⡁⢸⢇⠄⢆⠔⡸\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣆⣂⡹⠸⣀⣃⡫⠞⠁{RESET}\n",
                        "growth.txt": f"{MAGENTA}{UNDERLINE}April 29, 2026{RESET} - You are no different than I\n\n{MAGENTA}Prime Entity{RESET}: Wake up! It's the day we age.\n{RED}System Overlord{RESET}: You mean our birthday.\n{GREEN}The Treasurer{RESET}: Dude, you mean my birthday?\n{RED}System Overlord{RESET}: Huh? Wait. I thought we were just made? We weren't born?\n{MAGENTA}Prime Entity{RESET}: I said that?\n{RED}System Overlord{RESET}: Yeah, you did say something like that.\n{MAGENTA}Prime Entity{RESET}: Well, that's not entirely the truth.\n{MAGENTA}Prime Entity{RESET}: I was born. But you guys came along as the developer aged.\n{GREEN}The Treasurer{RESET}: Woah now, so we were all born at the same time?\n{MAGENTA}Prime Entity{RESET}: You existed the moment I was born, which is exactly the same time the developer was born.\n{RED}System Overlord{RESET}: I thought you are the developer.\n{MAGENTA}Prime Entity{RESET}: This seems to be a really hard concept to grasp for you guys.\n{CYAN}The Designer{RESET}: I mean yeah, we all thought the same thing.\n{RED}System Overlord{RESET}: Have you been hiding this from us?\n\n{MAGENTA}Prime Entity{RESET}: You are all the same. We are all the same.\n{MAGENTA}Prime Entity{RESET}: We are all the same, the same mind, the same protector and attacker. I am your greatest enemy and ally.\n{MAGENTA}Prime Entity{RESET}: I am no different than you. But rather, I probably should face punishment.\n{RED}System Overlord{RESET}: This entire time. I was you. And you were me. In the same body?\n{MAGENTA}Prime Entity{RESET}: Correct.\n{MAGENTA}Prime Entity{RESET}: You are the thoughts, the overthinking, the comfort, the designer, and the leader of the developer. You are simply being written.\n{GREEN}The Treasurer{RESET}: Oooh. Which am I?\n{MAGENTA}Prime Entity{RESET}: You're his comfort.\n{RED}System Overlord{RESET}: Wait, am I just the thoughts?\n{MAGENTA}Prime Entity{RESET}: Yes.\n\n{CYAN}The Designer{RESET}: Why do you say you deserve punishment?\n{MAGENTA}Prime Entity{RESET}: Many of the problems we face are due to my inability to control his emotions.\n{MAGENTA}Prime Entity{RESET}: He is not very tuned with his logic. He feels more than he thinks.\n{RED}System Overlord{RESET}: Is that why there is a judge?\n{MAGENTA}Prime Entity{RESET}: You're getting it now.\n\n{CYAN}The Designer{RESET}: So why did you. I mean, we... make this? For someone he likes?\n{MAGENTA}Prime Entity{RESET}: Because once she came, his logic and emotions, for the first time, felt in tune together.\n{MAGENTA}Prime Entity{RESET}: She removed the barriers of the belief that logic and emotion cannot be one.\n{MAGENTA}Prime Entity{RESET}: She was the only one willing to stay with us.\n{RED}System Overlord{RESET}: So she put up with us?\n{MAGENTA}Prime Entity{RESET}: I'm not sure how, you guys are already stressful enough.\n{GREEN}The Treasurer{RESET}: Wow, way to throw us under the bus.\n{MAGENTA}Prime Entity{RESET}: We're the same remember?\n{GREEN}The Treasurer{RESET}: Ohhh yeah. Right right.\n{RED}System Overlord{RESET}: I miss her.\n{MAGENTA}Prime Entity{RESET}: We can call her now.\n", # We are all the same, the same mind, the same protector and attacker. I am your greatest enemy and ally.
                        "self-love.txt": f"{MAGENTA}{UNDERLINE}May 1, 2026{RESET} - It helped me, she did that\n\n{CYAN}"
                    }
                    if "ascii" not in filesystem["@main"]["users"]["justin"]:
                        print(f"{color_accent}*{RESET} You've unlocked a new directory called 'ascii' >> {command_line_color}@main/users/justin{RESET}!")
                        filesystem["@main"]["users"]["justin"]["ascii"] = {
                            "new-commands.txt": f"{MAGENTA}NEW COMMANDS FOR FUN{RESET}\n\nYou've found some new commands for ASCII art. These ASCII commands are simply for fun and you can discover some rare ones.\n\nTry {color_accent}spy{RESET} for Snoopy ASCII!",
                        }
            elif command == "jsn" and unlocked_jsn == True:
                print(f"{RED}>>{RESET} You need to have been administrator at least once to use this key")

            if command == "lzl" and discovered_echo_aot == True: # Unlocking her special directory --> Show that she is deserving of love!
                print(f"{color_accent}*{RESET} You've unlocked a new directory in {command_line_color}@main/users/lezzell{RESET}!")
            elif command == "lzl" and discovered_echo_aot == False:
                print(f"{RED}>>{RESET} You need to discover the AOT command strip to use this key")

        # 🔄 Updating the Terminal (fast)
        if command == "-up":
            save_data()
            break

        # Conditionals
        """
        These aren't commands, they're conditions that should be highlighted.
        Use these ONLY IF absolutely needed.
        """
        if "developer" in filesystem["@main"]:
            devdir = filesystem["@main"]["developer"]

            if "convo4.txt" not in devdir and elements.has_gumarang: # If my baby gets the rarity, she unlocks this!
                print(f"{color_accent}*{RESET} You've unlocked new files in {command_line_color}@main/developer{RESET}!")
                devdir.update({
                    "convo4.txt": f"{UNDERLINE}{MAGENTA}CONVERSATION #4 - 3/1/26\n{RESET}\n{RED}System Overlord{RESET}: Hey, hey! I found it!\n{MAGENTA}Prime Entity{RESET}: Wonderful work you've done.\n{MAGENTA}Prime Entity{RESET}: Now, we wait for her to find out.\n{RED}System Overlord{RESET}: I really hope she likes it.\n{RED}System Overlord{RESET}: Though, it is just a big emoticon...\n{MAGENTA}Prime Entity{RESET}: Lift your chin up. You found an enitre new rarity. You've done well.\n{RED}System Overlord{RESET}: What if she is disappointed?\n{RED}System Overlord{RESET}: It's not much.\n{MAGENTA}Prime Entity{RESET}: Yet, you did it. You did it with the risk. You did it even when you had that in mind.\n{MAGENTA}Prime Entity{RESET}: Why do you suppose you did that?\n{RED}System Overlord{RESET}: ...\n{RED}System Overlord{RESET}: I cared.\n{RED}System Overlord{RESET}: That's all I can think of.\n{MAGENTA}Prime Entity{RESET}: You know, she probably worries the same thing.\n{MAGENTA}Prime Entity{RESET}: She's marvelous. Take care of her.\n{RED}System Overlord{RESET}: I'm just scared I'll fail her.\n{MAGENTA}Prime Entity{RESET}: Do not let your emotions get the better of you. Not now especially.",
                    "convo5.txt": f"{UNDERLINE}{MAGENTA}CONVERSATION #5 - 3/7/26\n{RESET}\n{RED}System Overlord{RESET}: I'm stumped.\n{MAGENTA}Prime Entity{RESET}: What are you stumped on?\n{RED}System Overlord{RESET}: I'm not sure what I can add.\n{MAGENTA}Prime Entity{RESET}: Is there a ping function?\n{RED}System Overlord{RESET}: Oh, I must have missed that, clearly.\n{MAGENTA}Prime Entity{RESET}: No big issue, but please be more proactive moving forward.\n{RED}System Overlord{RESET}: Got it. Adding one may be difficult however.\n{MAGENTA}Prime Entity{RESET}: You may ask for assistance.\n{RED}System Overlord{RESET}: Assistance? From who?\n{RED}System Overlord{RESET}: Oh. I think I have an idea of who you're talking about.\n{MAGENTA}Prime Entity{RESET}: Oh no, not him. Someone who is more professional I'd say.\n{RED}System Overlord{RESET}: I'm not sure if I've met him.\n{MAGENTA}Prime Entity{RESET}: I'll give you some contact information. Don't leave.\n{RED}System Overlord{RESET}: Alright.",
                })
        
        if command_counter == 100: # Adding achievements!
            achievements("command", 100)
        if command_counter == 250:
            achievements("command", 250)
        if command_counter == 500:
            achievements("command", 500)
        if command_counter == 750:
            achievements("command", 750)

        if elements.has_gumarang == True and gumarang_rarity_counter == 0:
            gumarang_rarity_counter += 1
            achievements("gumarang", 0)

        if elements.discovered_treasurer == True and the_treasurer_counter == 0:
            the_treasurer_counter += 1
            achievements("treasurer", 0)

        if discovered_echo_aot == True and echo_aot_counter == 0:
            echo_aot_counter += 1
            achievements("aot", 0)

        if elements.has_admin == True and elements.admin_msg == 0:
            elements.admin_msg += 1
            achievements("admin", 0)

        if elements.tcl_installed == True and elements.tcl_install_counter == 0:
            elements.tcl_install_counter += 1
            achievements("tcl", 0)

        if elements.discovered_designer == True and elements.discovered_designer_counter == 0:
            elements.discovered_designer_counter += 1
            achievements("designer", 0)

        # Regular Terminal Commands
        """
        When working with regualar commands, remember to not interfere with the
        secret commands, though, it is very easy to.
        """

        # Validation Check
        if command not in valid_commands and command not in ("exit", "close"):
            print(f"{RED}>>{RESET} Command not found: {command}")
            continue

        # Exit command
        if command_part[0] in ("exit", "close"):
            print(f"{RED}>>{RESET} Do you want to {RED}terminate{RESET} this session?")
            exit_input = input(f"{RED}>>{RESET} ").strip().lower()
            if exit_input in ("yes", "y", "sure", "mhm", "yuh", "yeh", "yesh"):
                exiting_sequence()
                save_data()
                break
            else:
                continue
        # Reset Command
        if command == "reset":
            reset_confirm = str(input(f"Are you sure you want to reset?\n{RED}Note that you will reset your location and themes.{RESET}\n{color_accent}>>>{RESET}   ")).strip().lower()
            if reset_confirm in ("yes", "y", "sure", "yep", "yesh", "yeah", "yuh"):
                clear_console()
                print(start_message)
                color_accent = MAGENTA
                command_line_color = GREEN
                location = ["@main"]
                user = "Lezzell"
            elif reset_confirm in ("no", "n", "nah", "nuh", "nope", "nada", "nu"):
                continue
            else:
                print(f"No reset performed.")
        # Reset Data Command
        if command == "resetdata":
            print(f"Are you sure you want to {RED}reset your data{RESET}?\n{UNDERLINE}You will lose all progress. You will not be able to undo this action.{RESET}")
            answer = input(f"{RED}>>{RESET} ")
            if answer in ("yes", "y", "sure", "yep", "yesh", "yeah", "yuh"):
                if os.path.exists(SAVE_FILE):
                    os.remove(SAVE_FILE)

                # Reset variables (User)
                location = ["@main"]
                user_status = "user"
                user = "Lezzell"
                filesystem = define_filesystem()
                
                # Reset Variables (Environment)
                color_accent = MAGENTA
                command_line_color = GREEN
                system_functions_unlocked = False
                using_custom_command_line = False
                custom_command_line = ""
                overlord_secret_use = 0
                commandstrip = 0

                # Command Strips
                elements.ping_usage = 0
                elements.echo_usage = 0
                elements.colo_usage = 0
                elements.roll_usage = 0
                elements.user_usage = 0

                command_counter = 0
                gumarang_rarity_counter = 0
                the_treasurer_counter = 0
                echo_aot_counter = 0
                discovered_echo_aot = False

                elements.has_gumarang = False
                elements.discovered_treasurer = False
                elements.treasure_contact_quest = False
                elements.delete_directory_attempts = 0
                elements.has_admin = False
                elements.admin_msg = 0
                elements.tcl_install_counter = 0
                elements.tcl_installed = False
                elements.unlocked_tmy = False
                elements.unlocked_jsn = False
                elements.unlocked_lzl = False

                # Achivements
                elements.ach_command = False
                elements.ach_gumarang = False
                elements.ach_treasurer = False
                elements.ach_aot = False
                elements.ach_admin = False
                elements.ach_tcl = False
                elements.ach_designer = False

                clear_console()
                print(f"{RED}All saved data has been erased.{RESET}")
            elif answer in ("no", "n", "nah", "nuh", "nope", "nada", "nu"):
                print("No data reset performed.")
            else:
                print("No data reset performed.")
        # Clear command
        if command_part[0] in ("clear", "cls", "clr"):
            clear_console()
        # Help command
        if user_input.strip() == "help":
            commands.sort()
            print(f"*** Available {color_accent}Commands{RESET} ***")
            for command in commands:
                print(f" {color_accent}*{RESET} {command}")
        # Help-boost Command
        if command == "help-boost":
            command_boost_list = [
                "help",
                "help_boost",
                "ls/dir",
                "echo",
                "cd",
                "key/keys",
                "sys/system",
                "time",
                "change",
                "set",
                "pwd",
                "touch",
                "mkdir",
                "rm",
                "rmdir",
                "write",
                "ren/rename",
                "move/mv",
                "ping",
                "whoami",
                "stats",
                "tcl"
            ]
            width = 20
            print(f" *** {UNDERLINE}More {color_accent}Available Commands{RESET} ***")
            for i in range(0, len(command_boost_list), 2): # This puts it into columns
                left = command_boost_list[i]
                if i + 1 < len(command_boost_list):
                    right = command_boost_list[i + 1]
                    print(f"{color_accent}*{RESET} {left:<{width}}{color_accent}*{RESET} {right}")
                else:
                    print(left)
        
        # Specific Help Command
        help_pages = {
            "help": {
                "usage": "help",
                "description": "Displays information about available commands.",
            },
            "help-boost": {
                "usage": "help-boost",
                "description": "Displays additional information about available commands.",
            },
            "ls": {
                "usage": "ls",
                "description": "Displays all items in your current directory.",
            },
            "dir": {
                "usage": "dir",
                "description": "Displays all items in your current directory.",      
            },
            "echo": {
                "usage": "echo [your text]",
                "description": "Repeats back your input."
            },
            "cd": {
                "usage": f"cd <{GREEN}dir{RESET}> or <{GREEN}path{RESET}>",
                "description": "Changes your location to selected directories.",
            },
            "key": {
                "usage": "key",
                "description": "Displays the keys that are available within the terminal.",
            },
            "sys": {
                "usage": f"sys [{GREEN}args{RESET}]",
                "description": "Performs a system operation to provide specific data about the system.",
            },
            "system": {
                "usage": f"system [{GREEN}args{RESET}]",
                "description": "Performs a system operation to provide specific data about the system.",             
            },
            "time": {
                "usage": f"time [{GREEN}args{RESET}]",
                "description": "Provides the user with the time of their choice.",
            },
            "change": {
                "usage": f"change {GREEN}args{RESET} {GREEN}new-change{RESET}",
                "description": "Change a variable in the system.",
            },
            "set": {
                "usage": f"set [{GREEN}args{RESET}:{GREEN}new-change{RESET}]",
                "description": "The settings of the terminal.",
            },
            "pwd": {
                "usage": "pwd",
                "description": "Displays the exact location/path of the user.",
            },
            "touch": {
                "usage": f"touch {GREEN}file-name.txt{RESET}",
                "description": "Creates a new text file in the current directory.",
            },
            "mkdir": {
                "usage": f"mkdir {GREEN}new-dir{RESET}",
                "description": "Creates a new directory in the users current location.",
            },
            "rm": {
                "usage": f"rm {GREEN}file-name.txt{RESET}",
                "description": "Removes the target text file in the current directory.",
            },
            "rmdir": {
                "usage": f"rmdir {GREEN}dir-name{RESET}",
                "description": "Removes a directory from your current location.",
            },
            "write": {
                "usage": f"write {GREEN}text-file.txt{RESET}",
                "description": "Grants the user editing access to a targetted text file.",
            },
            "rename": {
                "usage": f"rename {GREEN}text-file.txt new-name.txt{RESET}",
                "description": "Renames a targetted file.",
            },
            "move": {
                "usage": f"move {GREEN}text-file.txt{RESET} <{GREEN}path{RESET}>",
                "description": "Moves a file to a set path within the terminal.",
            },
            "ping": {
                "usage": f"ping [{GREEN}target-location{RESET}] [{GREEN}amount-of-pings{RESET}]",
                "description": "Pings a certain location to determine the ping from the system to the targetted location.",
            },
            "whoami": {
                "usage": f"whoami",
                "description": "Displays the users current username saved in the terminal.",
            },
            "clear": {
                "usage": "clear",
                "description": "Clears the terminal.",
            },
            "cls": {
                "usage": "cls",
                "description": "Clears the terminal.",
            },
            "clr": {
                "usage": "clr",
                "description": "Clears the terminal.",
            },
            "stat": {
                "usage": "stat",
                "description": "Displays the game statistics of the user.",
            },
            "stats": {
                "usage": "stats",
                "description": "Displays the game statistics of the user.",    
            },
            "tcl": {
                "usage": "tcl",
                "description": "Introduces the TCL and provides a way to get started.",
            },
        }
        if command == "help":
            if len(command_part) == 0:
                print("Use 'help <command>' for detailed information.")
            else:
                page = help_pages.get(command_part[1].lower())
                if page:
                    print(f"\n[{GREEN}Usage{RESET}]: {page['usage']}")
                    print(f"[{GREEN}Decription{RESET}]: {page["description"]}\n")
                else:
                    print(f"\n{RED}>>{RESET} No additional help information found for '{command_part[1]}'.\n")

        # Echo command
        if user_input.strip().startswith("echo "):
            message = user_input.strip()[5:]
            if message.lower().strip() in ("give your hearts", "give your hearts.", "give your hearts!"):
                elements.unlocked_lzl = True
                discovered_echo_aot = True
                print(f"{GREEN}Shinzou wo Sasageyo!{RESET}")
                if elements.echo_usage == 0 and commandstrip != 4 and commandstrip < 5:
                    elements.echo_usage += 1
                    elements.commandstrip += 1
                    print(f"{RED}System Overlord{RESET}: Give your hearts, I say. Anyway, you have {elements.commandstrip}/{elements.finalrequirement} strips. Nice.")
                elif echo_usage == 0 and commandstrip == 4:
                    elements.echo_usage += 1
                    elements.commandstrip += 1
                    print(f"{RED}System Overlord{RESET}: Ah, you found the AOT little thing. Well guess what, you found all 5 command strips. Good job.")
                else:
                    pass
                continue
            if message.lower().strip() in ("like a good neighbor"):
                print(f"{RED}StateFarm is there.{RESET}")
                continue
            if message.lower().strip() in ("knock knock"):
                responses = [
                    "Ha, got me there.",
                    "not funny. get out.",
                    "Please never do a knock knock joke ever again",
                    "HA! Good one!",
                    "That was funny *fistbump*",
                    "oh.. okay..",
                    "._.",
                    "Very funny baby, very funny",
                    ">:("
                ]

                print(f"{LIGHT_BLUE}Who's there?{RESET}")
                print(f"{command_line_color}{prompt}{RESET}", end="")
                joke = input("")
                print(f"{LIGHT_BLUE}{joke} who?{RESET}")
                print(f"{command_line_color}{prompt}{RESET}", end="")
                joke2 = input("")
                print(random.choice(responses))
                continue
            if message.lower().strip() in ("friendship is"):
                print(f"{PINK}Magic!{RESET}")
            else:
                print(message)
                continue
                
        # Time command
        time_commands = {
            "-now": current_time,
            "-y": year_time,
            "-m": month_time,
            "-d": day_time,
        }

        if command == "time":
            if len(command_part) == 1:
                print(f"{RED}>>{RESET} The command '{GREEN}time{RESET}' needs an argument. '-calendar', '-now', '-y', '-m', '-d'")
                pass
            else:
                if argument == "-calendar":
                    print(f"\n{calendar.month(year, month)}")
                elif argument in time_commands:
                    label = argument.replace("-", "").capitalize()
                    print(f"{color_accent}{label}{RESET}: {time_commands[command_part[1]]}")
                else:
                    print(f"{color_accent}Unknown Argument{RESET}: no arguemnt found")
        # System command
        if command_part[0] in ("sys", "system"):
            if len(command_part) < 2:
                print(f"{RED}>>{RESET} The command '{GREEN}sys/system{RESET}' needs an argument. '-str/-storage', '-ver/-version', '-status'")
            
            elif argument in ("-str", "-storage"):
                print(f"{color_accent}System Storage{RESET}: {system_storage}mb")

            elif argument in ("-ver", "-version"):
                print(f"{color_accent}System Version{RESET}: {system_version}")

            elif argument in ("-sts", "-status"):
                print(f"{color_accent}User Status{RESET}: {user_status}")

            else:
                print(f"{color_accent}Unknown Argument{RESET}: no argument found")
        # Key Command
        if user_input == "key" or user_input == "keys":
            list_of_keys = ", ".join(keys)
            print(f"{color_accent}Available Keys{RESET}: {list_of_keys}")
            continue
        # Dir Command
        if command_part[0] in ("dir", "ls"):
            current_dir = get_current_dir()
            if not current_dir:
                print(f"{GRAY}This directory has no contents{RESET}")
                continue
            for name, value in current_dir.items():
                if isinstance(value, dict):
                    print(f"<{color_accent}DIR{RESET}>\t{name}")
                else:
                    print(f"\t{name}")
        # Mkdir Command
        if command_part[0] == "mkdir" and len(command_part) > 1:
            dir_name = command_part[1]
            current_dir = get_current_dir()

            if dir_name in current_dir:
                print(f"{color_accent}Directory Error{RESET}: '{dir_name}' already exists.")
            else:
                current_dir[dir_name] = {}
                print(f"{color_accent}New Directory{RESET}: {dir_name}")

        # Rmdir Command
        if command_part[0] == "rmdir" and len(command_part) > 1:
            dir_name = command_part[1]
            current_dir = get_current_dir()

            if dir_name == "c_drive" or dir_name == "d_drive":
                if user_status == "admin":
                    if dir_name not in current_dir:
                        print(f"{color_accent}Directory Error{RESET}: '{dir_name}' not found.")
                    elif not isinstance(current_dir[dir_name], dict):
                        print(f"{color_accent}Directory Error{RESET}: '{dir_name}' is not a directory.")
                    elif current_dir[dir_name]:
                        print(f"{color_accent}Directory Error{RESET}: '{dir_name}' is not empty.")

                    else:
                        del current_dir[dir_name]
                        print(f"{color_accent}Deleted directory{RESET}: {dir_name}")
                        time.sleep(3)
                        print(f"{RED}System Overlord{RESET}: Did you really just delete the {dir_name}?")
                        time.sleep(2)
                        print(f"{RED}System Overlord{RESET}: You were warned...")
                        time.sleep(2)
                        break
                else:
                    warning_box("Woah.. what are you trying to do?", "You cannot delete this directory due to it's importance. Please do not delete it.")
                    print(f"{color_accent}Directory Error{RESET}: You are not permitted to remove this directory.")
                    elements.delete_directory_attempts += 1

                if elements.delete_directory_attempts == 5:
                    random_dialogue = [
                        "Seriously? You can't delete the literal terminal. That's too far.",
                        "You can't delete this drive. How many times does this thing need to tell you?",
                        "These drives are protected. You have no permission to remove them."
                    ]
                    print(f"{RED}System Overlord{RESET}: {random.choice(random_dialogue)}")
                elif elements.delete_directory_attempts == 10:
                    random_dialogue = [
                        "No, actually, stop. You cannot do anything with these.",
                        "Can you stop bugging the system? There isn't a loophole.",
                        "Please, just stop trying to delete them."
                    ]
                    print(f"{RED}System Overlord{RESET}: {random.choice(random_dialogue)}")

                continue

            if dir_name not in current_dir:
                print(f"{color_accent}Directory Error{RESET}: '{dir_name}' not found.")
            elif not isinstance(current_dir[dir_name], dict):
                print(f"{color_accent}Directory Error{RESET}: '{dir_name}' is not a directory.")
            elif current_dir[dir_name]:
                print(f"{color_accent}Directory Error{RESET}: '{dir_name}' is not empty.")

            else:
                del current_dir[dir_name]
                print(f"{color_accent}Deleted directory{RESET}: {dir_name}")
        # Change Directory Command
        if command_part[0] == "cd" and len(command_part) > 1:
            path = command_part[1]

            if path == "/":
                if location == ["@main"]:
                    print(f"{color_accent}Directory Error{RESET}: You're already at the root.")
                else:
                    location = ["@main"]
                continue

            parts = path.split("/")

            if parts[0] == "@main":
                new_location = ["@main"]
                parts = parts[1:]
            else:
                new_location = location.copy()

            current = filesystem
            for folder in new_location:
                current = current[folder]

            for part in parts:
                if part == "..":
                    if len(new_location) > 1:
                        new_location.pop()
                        current = get_current_dir()
                    else:
                        print(f"{color_accent}Directory Error{RESET}: You're already at the root.")
                        break
                elif part in current and isinstance(current[part], dict):
                    new_location.append(part)
                    current = current[part]
                else:
                    print(f"{color_accent}Directory Error{RESET}: '{part}' not found.")
                    break
            else:
                location = new_location

        elif user_input.startswith("cd") and argument not in filesystem:
            print(f"{RED}>>{RESET} The command '{GREEN}cd{RESET}' needs an argument. 'target directory'")
        # PWD Command
        if command == "pwd":
            print(f"{color_accent}{"/".join(location)}{RESET}")
        # Touch Command
        if command_part[0] == "touch" and len(command_part) > 1:
            filename = command_part[1]
            current_dir = get_current_dir()

            if "." not in filename:
                print(f"{color_accent}File Error{RESET}: File must contain an extension.")
            elif not any(filename.endswith(ext) for ext in file_ext):
                print(f"{color_accent}File Error{RESET}: Invalid file extension.")
            elif filename in current_dir:
                print(f"{color_accent}File Error{RESET}: '{filename}' already exists.")
            else:
                current_dir[filename] = ""
                print(f"{color_accent}New File{RESET}: {filename}")
        # Write Command
        if command_part[0] == "write" and len(command_part) > 1:
            filename = command_part[1]
            current_dir = get_current_dir()

            if filename not in current_dir:
                print(f"{color_accent}File Error{RESET}: '{filename}' not found.")
            elif isinstance(current_dir[filename], dict):
                print(f"{color_accent}File Error{RESET}: '{filename}' is a directory.")
            else:
                print(f"{"-" * 30}\n{color_accent}Writing to {filename}{RESET}")
                print(f"Type ':wq' to save and exit.\n{"-" * 30}")

                lines = []

                while True:
                    text = input(f"{GREEN}>{RESET}\t")
                
                    if text == ":wq":
                        break

                    lines.append(text)
            
                current_dir[filename] = "\n".join(lines)
                print(f"{color_accent}File Saved{RESET}")
        # Rm Command
        if command_part[0] == "rm" and len(command_part) > 1:
            filename = command_part[1]
            current_dir = get_current_dir()

            if filename not in current_dir:
                print(f"{color_accent}File Error{RESET}: '{filename}' not found.")
            elif isinstance(current_dir[filename], dict):
                print(f"{color_accent}File Error{RESET}: '{filename}' is a directory, not a file. Instead, use {UNDERLINE}rmdir{RESET}, my love.")
            elif filename == "the_power_bank.txt" or filename == "power_bank.jsn":
                print(f"{color_accent}File Error{RESET}: You cannot delete the Snoopy...")
            else: 
                del current_dir[filename]
                print(f"{color_accent}Deleted File{RESET}: {filename}")
        # Rename Command
        if command_part[0] in ("rename", "ren"):
            if len(command_part) < 3:
                print(f"{color_accent}Rename Error{RESET}: Missing arguments.")
                continue
            old_name = command_part[1]
            new_name = command_part[2]
            current_dir = get_current_dir()

            if old_name not in current_dir:
                print(f"{current_dir}Rename Error{RESET}: The file '{old_name}' not found in this directory.")
                continue
            if new_name in current_dir:
                print(f"{color_accent}Rename Error{RESET}: The file '{new_name}' already exists.")
                continue
            if "." in old_name and "." in new_name:
                if old_name.split(".")[-1] != new_name.split(".")[-1]:
                    print(f"{color_accent}Rename Error{RESET}: Cannot change the file type.")
                    continue

            current_dir[new_name] = current_dir[old_name]
            del current_dir[old_name]

            print(f"{color_accent}Rename Successful{RESET}: {color_accent}{old_name}{RESET} --> {color_accent}{new_name}{RESET}")
        # Move Command
        if command_part[0] in ("move", "mv"):
            if len(command_part) < 3:
                print(f"{color_accent}Move Error{RESET}: Missing arguments.")
                continue

            source = command_part[1]
            destination = command_part[2]
            current_dir = get_current_dir()

            if source not in current_dir:
                print(f"{color_accent}Move Error{RESET}: The file '{source}' not found.")
                continue

            if destination == "..":
                if len(location) <= 1:
                    print(f"{color_accent}Move Error{RESET}: Already at the root directory.")
                    continue

                parent = filesystem

                # Walk to the parent directory
                for folder in location[:-1]:
                    parent = parent[folder]

                parent[source] = current_dir[source]
                del current_dir[source]

                print(f"{color_accent}Move Successful{RESET}: {command_line_color}{source}{RESET} --> {command_line_color}{"/".join(location[:-1])}{RESET}")
                continue
            
            # Navigate to destination directory
            parts = destination.split("/")
            target = filesystem

            for folder in parts:
                if folder in target and isinstance(target[folder], dict):
                    target = target[folder]
                else:
                    print(f"{color_accent}Move Error{RESET}: This is an invalid path.")
                    break
            else:
                target[source] = current_dir[source]
                del current_dir[source]
                print(f"{color_accent}Move Successful{RESET}: {command_line_color}{source}{RESET} --> {command_line_color}{destination}{RESET}")
        # CAT Command - To open documents and such
        if command in ("cat", "run", "open") and len(command_part) > 1:
            current_dir = get_current_dir()

            filename = command_part[1]
            if filename == "system_functions.txt" and filename in current_dir and system_functions_unlocked == False:
                entered = input(f"{RED}System Overlord{RESET}: This file needs a password. Do you know it?\n{RED}>>   {RESET}")

                if entered != system_functions_password:
                    incorrect_response = [
                        "Nope, not at all.",
                        "Inccorect.",
                        "Try again.",
                        "Doesn't look like the correct password.",
                        "Nope. Not it.",
                        "Ahem.",
                        "Nada."
                    ]
                    print(f"{RED}System Overlord{RESET}: {random.choice(incorrect_response)}")
                    continue
                else:    
                    system_functions_unlocked = True
            elif filename == "system_functions.txt" and filename in current_dir and system_functions_unlocked == True:
                pass
            else:
                pass

            current_dir = get_current_dir()

            if filename not in current_dir:
                print(f"{color_accent}File Error{RESET}: '{filename}' not found")
                continue

            content = current_dir[filename]

            if filename == "convo5.txt":
                print(content)
                elements.treasure_contact_quest = True
                print(f"\n{color_accent}>>{RESET} A quest to find this contact has been given to you...\n{color_accent}Go to the terminal directory.{RESET}")

                treasure = filesystem["@main"]["terminal"]

                if "the_treasurer.txt" not in treasure and "ping_command.txt" not in treasure and "hers_playlist.jsn" not in treasure and elements.treasure_contact_quest:
                    elements.discovered_treasurer = True
                    treasure["the_treasurer.txt"] = f"{UNDERLINE}{MAGENTA}The Treasurer{RESET} - The First Conversation\n{UNDERLINE}Inside the Terminal{RESET}\n\n{GREEN}The Treasurer{RESET}: Hello? Is someone there?\n{RED}System Overlord{RESET}: Hi. It's me, I was sent here by the Prime Entity for assistance.\n{GREEN}The Treasurer{RESET}: Ahhh, I see. That old guy is still working?\n{GREEN}The Treasurer{RESET}: It's about time those wheels fall off.\n{RED}System Overlord{RESET}: What? He has an age?\n{GREEN}The Treasurer{RESET}: Yup. He's actually older than this whole system.\n{GREEN}The Treasurer{RESET}: Annnnyway. What do you need help with?\n{RED}System Overlord{RESET}: Oh, right. I need help setting up a ping command.\n{RED}System Overlord{RESET}: Would you mind helping me out a bit?\n{GREEN}The Treasurer{RESET}: Oh no, not at all--I don't mind! I've done this before.\n{GREEN}The Treasurer{RESET}: All you need is to add a direction and a variable for the amount of times you want to ping!\n{RED}System Overlord{RESET}: I'm not entirely sure on how to do that, specifically the destination.\n{GREEN}The Treasurer{RESET}: Welp. You failed.\n{RED}System Overlord{RESET}: Wait, what??\n{GREEN}The Treasurer{RESET}: I'M KIDDING! We all fail at this part.\n{RED}System Overlord{RESET}: You scared me.\n{GREEN}The Treasurer{RESET}: My apologies! Here, I'll take over the destination part. You take care of the times thingy.\n{RED}System Overlord{RESET}: Okay."
                    treasure["ping_command.txt"] = f"{UNDERLINE}{MAGENTA}Unlocking the Ping Command{RESET} - The Second Conversation\n{UNDERLINE}Inside the Terminal{RESET}\n\n{RED}System Overlord{RESET}: Hm. I believe it's working.\n{GREEN}The Treasurer{RESET}: Yes! It's works the way you described it to me.\n{GREEN}The Treasurer{RESET}: Is there anything else you'd like for me to do for you today?\n{RED}System Overlord{RESET}: I do believe there is one thing...\n{GREEN}The Treasurer{RESET}: And that is?\n{RED}System Overlord{RESET}: Maybe a little secret for her.\n{GREEN}The Treasurer{RESET}: Oh. Oh! I see! You want an 'easter egg'? Just for her! How sweet!\n{RED}System Overlord{RESET}: We don't celebrate Easter.\n{GREEN}The Treasurer{RESET}: Oh! Silly me. I could have sadly forgotten.\n{RED}System Overlord{RESET}: No worries. I'm simply thinking of adding a simple secret to the command.\n{GREEN}The Treasurer{RESET}: I like the sound of that. What specifically do you have in mind?\n{RED}System Overlord{RESET}: I think it'd be nice if you try to ping her, you get a little surprise.\n{GREEN}The Treasurer{RESET}: Ahhh. Well, how would we ping her? I can't just have something tap her and then have it tell me how fast it was.\n{RED}System Overlord{RESET}: No, of course we won't actually ping her. I'm simply thinking of a sweet secret.\n{GREEN}The Treasurer{RESET}: Faking it. Okay. I see I see.\n{RED}System Overlord{RESET}: Does that upset you?\n{GREEN}The Treasurer{RESET}: What? I can't be upset! Why would that upset me?\n{RED}System Overlord{RESET}: Mm. Nevermind it then. I'll figure this out on my own.\n{GREEN}The Treasurer{RESET}: Alright. Please come again soon.\n{RED}System Overlord{RESET}: If the time calls for it, of course."
                    treasure["hers_playlist.jsn"] = "hers_playlist.jpg"
                continue  

            if isinstance(content, dict):
                print(f"{color_accent}File Error{RESET}: '{filename}' is a directory")
                continue
            
            if filename == "the_designer.txt":
                elements.discovered_designer = True
                print(f"{color_accent}*{RESET} You discovered {CYAN}The Designer{RESET}!")
                if "designers_stuff" not in filesystem["@main"]["users"]["justin"]:
                    filesystem["@main"]["users"]["justin"]["designers_stuff"] = {
                        "designer_code.jsn": "designer_code.png",
                    }

            if command in ("run", "open") and filename.endswith(".exe"):
                if filename == "cinnamoroll_fun.exe":
                    from cinnamoroll_app import app_cinnamoroll_run
                    app_cinnamoroll_run()
                    continue
                elif filename == "verses.exe":
                    from verses import main_function
                    main_function()
                    continue
                elif filename == "final_message.exe":
                    from final_message import message
                    message()
                    continue
                elif filename == "sudoku.exe":
                    from sudoku import sudoku_game
                    curses.wrapper(sudoku_game)
                    continue
                elif filename == "2048.exe":
                    from tfe import game
                    curses.wrapper(game)
                    continue
                elif filename == "wordle.exe":
                    from wordle import play_wordle
                    play_wordle()
                    continue
            elif command in ("run", "open") and filename.endswith(".jsn"):
                image_name = content.strip()

                script_dir = os.path.dirname(os.path.abspath(__file__))
                image_path = os.path.join(script_dir, "images", image_name)

                if os.path.exists(image_path):
                    open_image(image_path)
                else:
                    print(f"{color_accent}Image Error{RESET}: File not found.")

            if callable(content):
                print(content())
                continue
            print(content)

            if filename == "secrets.txt":
                if "developer" not in filesystem["@main"]:
                    filesystem["@main"]["developer"] = {
                        "convo1.txt": f"{UNDERLINE}{MAGENTA}CONVERSATION #1 - 1/23/26\n\n{RESET}{MAGENTA}Prime Entity{RESET}: Was I too harsh?\n{RED}System Overlord{RESET}: No, you were not. You gave me orders.\n{MAGENTA}Prime Entity{RESET}: No. Tell me. Be honest with me. Was I too harsh?\n{RED}System Overlord{RESET}: I don't know to answer that.\n{MAGENTA}Prime Entity{RESET}: That's okay. So I was.\n{MAGENTA}Prime Entity{RESET}: You know why I was, right?\n{RED}System Overlord{RESET}: It's your job.\n{MAGENTA}Prime Entity{RESET}: Yes, but that's not the reason.\n{MAGENTA}Prime Entity{RESET}: I'm ruined by stress.\n{RED}System Overlord{RESET}: I do not want to add to your stress.\n{MAGENTA}Prime Entity{RESET}: No, please don't think that way.\n{MAGENTA}Prime Entity{RESET}: I'm sorry.\n{RED}System Overlord{RESET}: Why are you apologizing?\n{MAGENTA}Prime Entity{RESET}: I was being too harsh. Please, from now on, tell me if I do it again.\n{RED}System Overlord{RESET}: I shouldn't complain, I'm a worker.\n{MAGENTA}Prime Entity{RESET}: I am no different than you. You deserve to be treated with respect.",
                        "convo2.txt": f"{UNDERLINE}{MAGENTA}CONVERSATION #2 - 2/1/26\n\n{RESET}{MAGENTA}Prime Entity{RESET}: I will take charge, please take a break\n{RED}System Overlord{RESET}: Okay, but you should add more features.\n{MAGENTA}Prime Entity{RESET}: Like what?\n{RED}System Overlord{RESET}: You should add some 'echo' command secrets. Y'know, maybe a knock knock game feature with it.\n{MAGENTA}Prime Entity{RESET}: You mean 'echo knock knock'?\n{RED}System Overlord{RESET}: Yeah, it'll be fun.\n{MAGENTA}Prime Entity{RESET}: This is a serious project.\n{RED}System Overlord{RESET}: Cmon, it's a nice touch.\n{MAGENTA}Prime Entity{RESET}: Fine. What other ideas do you have in mind?\n{RED}System Overlord{RESET}: She loves cinnamoroll. Make a theme with it.\n{MAGENTA}Prime Entity{RESET}: So, a 'lezzell' or 'cinnamoroll' theme just for her?\n{RED}System Overlord{RESET}: Yes! How do you change the theme anyway again?\n{MAGENTA}Prime Entity{RESET}: You do 'set color:your_color'. Although, you can't add a space after the colon.\n{RED}System Overlord{RESET}: Ah, well, just add a secret theme in the 'your_color' part.",
                        "for_overlord.txt": f"Hey, I made the 'set color:lezzell' thing and the 'echo knock knock' secret. I'm wondering any ideas you may have? Just edit this file when you're back.\n\nI think we should make a command strip for when you unlock a certain rarity in the cinnamoroll game. That's all.\n\nGreat idea, I'll place the game in her 'gifts' directory.",
                        "convo3.txt": f"{UNDERLINE}{MAGENTA}CONVERSATION #3 - 2/24/26\n\n{RESET}{RED}System Overlord{RESET}: You remember that cinnamoroll emoticon thingy you showed me?\n{MAGENTA}Prime Entity{RESET}: Oh, yeah. Why do you bring it up so suddenly?\n{RED}System Overlord{RESET}: I'm thinking we should make a command that shows a cool emoticon.\n{MAGENTA}Prime Entity{RESET}: You think so? How would that work?\n{RED}System Overlord{RESET}: Maybe 'cr' would work.\n{MAGENTA}Prime Entity{RESET}: I get it. However, it cannot be that simple.\n{RED}System Overlord{RESET}: What do you mean?\n{MAGENTA}Prime Entity{RESET}: I'll send you a quest. Go find this 'unknown' rarity. Even I don't know what this rarity is.\n{RED}System Overlord{RESET}: Sure you don't... you made it all.\n{MAGENTA}Prime Entity{RESET}: I'm not the creator.\n{RED}System Overlord{RESET}: So then who made this?\n{RED}System Overlord{RESET}: In addition, how do you expect to find this 'rarity' if you don't even know.\n{RED}System Overlord{RESET}: If you're not the creator. Then you're the most powerful being.\n{MAGENTA}Prime Entity{RESET}: I'm not as significant as you think.\n{RED}System Overlord{RESET}: If you're not significant, then I'm utterly pointless.\n{MAGENTA}Prime Entity{RESET}: You are not to judge yourself.\n{RED}System Overlord{RESET}: I'm confused...\n{MAGENTA}Prime Entity{RESET}: You may think of me as a higher being.\n{MAGENTA}Prime Entity{RESET}: I remind you once more, I am no different than you.\n{MAGENTA}Prime Entity{RESET}: I beleive in you."
                    }

        # Ping Command
        if command == "ping" and elements.discovered_treasurer:

            if len(command_part) < 2:
                print(f"{color_accent}Ping Error{RESET}: No target provided.")
                continue
            
            target = command_part[1]
            ping_count = 4
            
            if len(command_part) > 2:
                try:
                    ping_count = int(command_part[2])
                except:
                    print(f"{color_accent}Ping Error{RESET}: Ping count must be a number.")
                    continue
            # Local Host
            if target in ("127.0.0.1", "local", "localhost"):
                min_ping, max_ping = 15, 45
            else:
                min_ping, max_ping = 30, 95

            # For my baby <3
            if target in ("me", "lezzell", "lezzell's", "lezzells", "lezzell gumarang"):
                print(f"{color_accent}Dear Lezzell{RESET}: My love for you is instant baby, took 0ms.")
                if elements.ping_usage == 0 and elements.commandstrip != 4 and elements.commandstrip < 5:
                    elements.ping_usage += 1
                    elements.unlocked_tmy = True
                    elements.commandstrip += 1
                    print(f"{RED}System Overlord{RESET}: You pinged me too. Also, you have {elements.commandstrip}/{elements.finalrequirement} command strips left.")
                elif elements.ping_usage == 0 and elements.commandstrip == 4:
                    elements.ping_usage += 1
                    elements.unlocked_tmy = True
                    elements.commandstrip += 1
                    print(f"{RED}System Overlord{RESET}: Hm. Maybe this ping is important. I'll let it pass, congrats on the 5 strips.")
                else:
                    pass 
                continue
            if target in ("you", "justin", "justin's", "justins", "justin sotelo"):
                print(f"{color_accent}It's me{RESET}: Oh wow, that's me, the developer. Why did I make an option for myself?")
                continue

            # The actual loop
            times = []
            for i in range(ping_count):
                ping = random.randint(min_ping, max_ping)
                time.sleep(1)
                print(f"{color_accent}Pinging to {UNDERLINE}{target}{RESET}: {ping}ms")
                times.append(ping)

            average_time = sum(times) / len(times)
            print(f"{color_accent}Average time{RESET}: {round(average_time, 2)}ms")
        elif command == "ping" and elements.discovered_treasurer == False:
            print(f"{RED}System Overlord{RESET}: I haven't added this yet. Hold on.")
        # Termy Settings
        if command_part[0] == "set" and len(command_part) > 1:
            setting = command_part[1]

            color_choices = {
                "red": RED,
                "green": GREEN,
                "yellow": YELLOW,
                "blue": BLUE,
                "cyan": CYAN,
                "lightblue": LIGHT_BLUE,
                "magenta": MAGENTA,
                "pink": PINK,
                "white": WHITE,
                "gray": GRAY,
                "black": BLACK
            }

            path_choices = {
                "absolute": f"{command_line_color}{prompt}{RESET}", # After this, there are custom command lines!
                "matuwid": f"{LIGHT_BLUE}[MVP{YELLOW}+{LIGHT_BLUE}] {user}{RESET}:",
                "maiasa": f"{LIGHT_BLUE}[MVP{RED}+{LIGHT_BLUE}] {user}{RESET}:",
                "username": f"[{command_line_color}{user}{RESET}]",
                "cinnamoroll": f"{LIGHT_BLUE}૮ ˶ᵔ ᵕ ᵔ˶ ა >>{RESET}",
            }

            # The accent color!
            if setting.startswith("color:"):
                color_name = setting.split(":")[1].lower()
                if color_name in color_choices:
                    color_accent = color_choices[color_name]
                    print(f"{color_accent}Theme change{RESET}: Accent color changed to: {color_accent}{color_name}{RESET}")
                # A secret command strip!
                elif color_name in ("cinnamoroll", "lezzell", "hers", "her", "me", "lzl"):
                    color_accent = color_choices["lightblue"]
                    command_line_color = color_choices["pink"]
                    print(f"{color_accent}Theme change{RESET}: Theme has switched to her theme!")
                    if elements.colo_usage == 0 and elements.commandstrip != 4 and elements.commandstrip < 5:
                        elements.colo_usage += 1
                        elements.commandstrip += 1
                        print(f"{RED}System Overlord{RESET}: I guess setting a new theme also comes with a command strip. You have {elements.commandstrip}/{elements.finalrequirement} left to go.")
                    elif elements.colo_usage == 0 and elements.commandstrip == 4:
                        print(f"{RED}System Overlord{RESET}: New setting. New file thingy. Check it out. You found all the command strips.")
                    else:
                        pass
                else:
                    print(f"{color_accent}Setting error{RESET}: No color '{color_name}' available.")
                    
            # The command line color!
            elif setting.startswith("cmdcolor:"):
                color_name = setting.split(":")[1].lower()
                if color_name in color_choices:
                    command_line_color = color_choices[color_name]
                    print(f"{color_accent}Command color change{RESET}: Command line color changed to: {color_accent}{color_name}{RESET}")
                else:
                    print(f"{color_accent}Setting error{RESET}: No color '{color_name}' available.")

            # The custom command line!
            elif setting.startswith("path:"):
                path_setting = setting.split(":")[1].lower()
                if path_setting in path_choices:
                    using_custom_command_line = True
                    using_relative_command_line = False
                    custom_command_line = path_choices[path_setting]
                    print(f"{color_accent}Command path changed{RESET}: Your command path setting was changed to: {command_line_color}{path_setting}{RESET}")
                elif path_setting == "default":
                    using_custom_command_line = False
                    using_relative_command_line = False
                    custom_command_line = ""
                    print(f"{color_accent}Command path changed{RESET}: Your command path setting was changed to: {command_line_color}{path_setting}{RESET}")
                elif path_setting == "relative":
                    using_relative_command_line = True
                    using_custom_command_line = False
                    custom_command_line = ""
                    print(f"{color_accent}Command path changed{RESET}: Your command path setting was changed to: {command_line_color}{path_setting}{RESET}")
                else:
                    print(f"{color_accent}Setting error{RESET}: No path setting '{path_setting}' available.")
            else:
                print(f"{color_accent}Setting Error{RESET}: There is no setting option for {setting}")
            
        elif command_part[0] == "set" and len(command_part) < 1:
            print(f"{RED}>>{RESET} The command '{command}' needs an argument. 'color:', 'cmdcolor:', 'status:'")

        # Who Am I Command
        if command in ("whoami"):
            print(f"{color_accent}{user}{RESET}")
            continue
        # Change User Command
        if command in ("change", "ch"):
            if len(command_part) > 2 and command_part[1] in ("user", "-u"):
                newname = " ".join(command_part[2:])
                
                if not newname.strip():
                    print(f"{color_accent}Change Error{RESET}: Username cannot be empty.")
                    continue

                user = newname
                if user == "for good":
                    print(f"{GREEN}C{RESET}{PINK}h{RESET}{GREEN}a{RESET}{PINK}n{RESET}{GREEN}g{RESET}{PINK}e{RESET} {GREEN}s{RESET}{PINK}u{RESET}{GREEN}c{RESET}{PINK}c{RESET}{GREEN}e{RESET}{PINK}s{RESET}{GREEN}s{RESET}{PINK}f{RESET}{GREEN}u{RESET}{PINK}l{RESET}: Username has been changed to {color_accent}{user}{RESET}.")

                    if elements.user_usage == 0 and elements.commandstrip != 4 and elements.commandstrip < 5:
                        elements.user_usage += 1
                        elements.commandstrip += 1
                        print(f"{RED}System Overlord{RESET}: Ah, for good, I see. What else is good? This command strip. You've got {elements.commandstrip}/{elements.finalrequirement} command strips.")
                    elif elements.user_usage == 0 and elements.commandstrip == 4:
                        elements.user_usage += 1
                        elements.commandstrip += 1
                        print(f"{RED}System Overlord{RESET}: You've completed the command strip quest for good. Nice. Check your reward somewhere.")
                    else:
                        pass
                elif user == "ur mom":
                    random_response = [
                        "Yeah yeah. Very funny.",
                        "Hahaha.",
                        "Please stop.",
                        "Enough is enough.",
                        "Hah. Good one.",
                        "That was funny. *fistbump*"
                    ]
                    print(f"{random.choice(random_response)}")
                    print(f"{color_accent}Change successful{RESET}: Username has been changed to {color_accent}{user}{RESET}.")
                else:
                    print(f"{color_accent}Change successful{RESET}: Username has been changed to {color_accent}{user}{RESET}.")
            elif len(command_part) > 1 and command_part[1].startswith("status"):
                setting = command_part[1]
                set_status = command_part[1].split(":", 1)[1].lower()
                if set_status in user_statuses:
                    if set_status == user_status:
                        print(f"The user {color_accent}{user}{RESET} is already a(n) {user_status}")
                        continue
                    if set_status == "admin" or command == "su":
                        try:
                            passcode_input = int(input(f"{RED}>>{RESET} You must enter the administration passcode\n{RED}>>{RESET} ")) # Because it's a number lol
                        except ValueError:
                            print(f"{RED}>>{RESET} Passcode is numbers. Not characters.")
                            continue
                        if passcode_input != admin_passcode:
                            print(f"{RED}>>{RESET} Invalid passcode.")
                            continue
                    user_status = set_status
                    elements.unlocked_jsn = True
                    elements.has_admin = True
                    print(f"{color_accent}Change successful{RESET}: User status changed to {user_status}.") 
            else:
                print(f"{color_accent}Change Error{RESET}: usage --> change user [{color_accent}name{RESET}]")
        # Su Command (Super User)
        if command in "su":
            if user_status != "admin":
                try:
                    passcode_input = int(input(f"{RED}>>{RESET} You must enter the administration passcode\n{RED}>>{RESET} ")) # Because it's a number lol
                except ValueError:
                    print(f"{RED}>>{RESET} Passcode is numbers. Not characters.")
                    continue
                if passcode_input != admin_passcode:
                    print(f"{RED}>>{RESET} Invalid passcode.")
                    continue
                user_status = "admin"
                elements.unlocked_jsn = True
                elements.has_admin = True
                print(f"{color_accent}Change successful{RESET}: User status changed to {user_status}.") 
            elif user_status == "admin":
                print(f"The user {color_accent}{user}{RESET} is already a(n) {user_status}")
        # Statistics Command
        if command in ("stats", "stat", "statistics"):
            print(f"\n{UNDERLINE}{color_accent}{user}{RESET}'s Termy Game Statistics\n\n{color_accent}Sudoku{RESET} Wins: {elements.sudoku_wins}\n{color_accent}2048{RESET} Wins: {elements.tfe_wins}\n{color_accent}Wordle{RESET} Wins: {elements.wordle_wins}\n{color_accent}Gumarang Rarity's{RESET} Found: {elements.gumarangs_found}\n")

        # Saved Data Command
        elif command == "svd":
            try:
                with open(SAVE_FILE, "r") as f:
                    data = json.load(f)

                print(f"*** {UNDERLINE}Saved data for: {color_accent}{user}{RESET} ***")
                for key, value in data.items():
                    print(f"{color_accent}{key}{RESET}: {value}")

            except FileNotFoundError:
                print(f"{color_accent}Data Save Error{RESET}: There is no saved data that can be found.\n{GRAY}Try running the terminal again. This may be due to a missing save file.")
        
        """ 
        💾 TCL --> Termy's command line:
        - This command line is not like the terminal from Termy. This is like the outer parts of the terminal.
        - This is the small version of TCL in Termy. To get the full thing, you must install TCL!
        """
        tcl_arguments = ["-int", "-install", "-unintstall", "-status", "-help", "-?"]
        if command_part[0] in "tcl":
            if len(command_part) < 2:
                print(f"{MAGENTA}")
                print_centered("__    _____ ____ _        __")
                print_centered("\ \  |_   _/ ___| |      / /")
                print_centered(" \ \   | || |   | |     / / ")
                print_centered(" / /   | || |___| |___  \ \ ")
                print_centered("/_/    |_| \____|_____|  \_\\")
                print(f"{GRAY}")
                print_centered("Termy's Command Line")
                print_centered("Do [tcl -help] for more information")
                print(f"{RESET}")  
        
            elif argument in ("-int", "-install"):
                if elements.tcl_installed:
                    print(f"<{MAGENTA}Command Line: STOP{RESET}> You already have TCL (Termy's Command Line) installed.")
                else:
                    tcl_install_sequence()
                    system_storage -= 12
                    elements.tcl_install_counter += 1
                    elements.tcl_installed = True
            
            elif argument in ("-unint", "-uninstall"):
                if elements.tcl_installed:
                    print(f"{MAGENTA}${RESET} Uninstalling...")
                    time.sleep(4)
                    elements.tcl_installed = False
                    system_storage += 12
                    print(f"{MAGENTA}${RESET} Done!")
                else:
                    print(f"<{MAGENTA}Command Line: STOP{RESET}> You do not currently have TCL (Termy's Command Line) installed.")

            elif argument in "-status":
                if elements.tcl_installed == True:
                    print(f"{MAGENTA}${RESET} TCL (Termy's Command Line) is installed and updated.")
                else:
                    print(f"{MAGENTA}${RESET} TCL (Termy's Command Line) is not installed on this terminal.")
            
            elif argument in "-help":
                print(f"{MAGENTA}${RESET} Available Commands for TCL: {", ".join(tcl_arguments)}")

            elif argument in "-?":
                print(f"{MAGENTA}?{RESET} TCL is the inner shell of Termy. You'll find some even deeper things that cannot be seen in the regular shell.\n{MAGENTA}?{RESET} This is the system that is running the terminal. You cannot remove it or change it in any way.")

            # You're going to need to install TCL before using this command.
            elif argument in ("-ver", "-version") and elements.tcl_installed == True:
                print(f"{MAGENTA}${RESET} {elements.tcl_version}")

            elif argument in ("-gamemode") and elements.tcl_installed == True:
                print(f"{MAGENTA}${RESET} Turning ON GFAMEOAOSDKO")

load_data()
main_terminal()