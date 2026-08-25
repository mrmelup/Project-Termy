from elements import *
import elements

rarity_emotes = {
    "Common": "૮ ˶ᵔ ᵕ ᵔ˶ ა",
    "Rare": "૮₍ ˃ ⤙ ˂ ₎ა",
    "Musical": "♪(๑ᴖ◡ᴖ๑)♪",
    "Iconic": "૮ ˶˃ ᵕ ˂˶ ა ✨",
    "Legendary": "🌟(˶˃ ᵕ ˂˶)",
    "Gumarang": "💖૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა💖"
}

prompt_dialogue = ["What's the idea?", "Hi Lezzell! What's your move?", "Next move?", "What is she going to do?", "I wonder what she'll say.", "Hi!", "Hi baby! What are you going to do?", "Have any plans?", "We should hangout sometime!", "I really miss you.", "I'm hungry..."]

main_color = LIGHT_BLUE
secondary_color = PINK
dotted_note = f"{main_color}*{RESET}   "

player_inventory = []
credit = 5
chance_boost = 0.0

def dash_line():
    print(f"{main_color}{'=' * 25} === == ={RESET}")

def pulled_cinnamoroll(rarity_display, rarity_clean):
    emote = rarity_emotes.get(rarity_clean, "")

    dash_line()
    print(f"You obtained a(n) {rarity_display} cinnamoroll! {emote}")
    if rarity_clean in ("Legendary"):
        good_pull_dialogue = [
            "Nice baby! It's hard to get these.",
            "Wowwww, thats nice :)",
            "Mwah! A good pull!",
            "Woooo :) Save that"
        ]
        print(random.choice(good_pull_dialogue))
    if rarity_clean in ("Gumarang"):
        elements.has_gumarang = True
        elements.gumarangs_found += 1
        gumarang_pull_diaglogue = [
            "YOO THATS THE RAREST ONE",
            "NICE BABY!",
            "DANG, YOU MAY HAVE UNLOCKED SOMETHING I THINK",
            "MWAHHH"
        ]
        print(random.choice(good_pull_dialogue))
    dash_line()

def app_cinnamoroll_run():
    global has_gumarang
    global credit 

    clear_console()
    print(f"You found the game --> 'Roll a {LIGHT_BLUE}cinnamoroll{RESET}!'\n{dotted_note}Roll a cinnamoroll is a minigame that only requires very few commands to play.\n{dotted_note}For commands, simply type 'help' to display all the commands you need to know.\n{dotted_note}This game is very small, but there are different rarities of cinnamorolls; the rarest of these being the Gumarang Roll :).")

    while True: 

        prompt = random.choice(prompt_dialogue)
        print(f"\n{secondary_color}⬇   {RESET}{main_color}{prompt}{RESET} | {RED}Love Credit{RESET}: {credit}\n", end = "")
        gameroll = input()

        if gameroll in ("exit", "leave"):
            break
        
        if gameroll == "help":
            print(f"\n{main_color}All the commands you need to know.{RESET}\n{dotted_note}{secondary_color}roll{RESET} Rolls just once and gives you a cinnamoroll!\n{dotted_note}{secondary_color}inv{RESET}  Check how many cinnamorolls you have or some other items!\n{dotted_note}{secondary_color}ily{RESET}  Sending an 'ily' gives you credits!\n{dotted_note}{secondary_color}cls{RESET}  Clears the screen to clean the mess.\n{dotted_note}{secondary_color}doc{RESET}  Open up a document that contains a message!")

        if gameroll.startswith("roll"):
            parts = gameroll.split()

            roll_count = 1
            if len(parts) > 1 and parts[1].isdigit():
                roll_count = int(parts[1])

            roll_count = min(roll_count, 50)

            cinnamoroll_rarity = [
                {"name": "Common", "color": GREEN, "weight": 60},
                {"name": "Rare", "color": BLUE, "weight": 45},
                {"name": "Musical", "color": WHITE, "weight": 30},
                {"name": "Iconic", "color": YELLOW, "weight": 20},
                {"name": "Legendary", "color": MAGENTA, "weight": 10},
                {"name": "Gumarang", "color": LIGHT_BLUE, "weight": 1}
            ]

            if credit >= roll_count:
                credit -= roll_count

                results = []
                summary = {}

                # 🎬 play animation ONCE
                for i in range(2):
                    clear_console()
                    print(f"{main_color}/{RESET}")
                    time.sleep(0.1)
                    clear_console()
                    print(f"{main_color}-{RESET}")
                    time.sleep(0.1)
                    clear_console()
                    print(f"{main_color}\\{RESET}")
                    time.sleep(0.1)
                    clear_console()
                    print(f"{main_color}|{RESET}")

                # 🎲 do all rolls
                for _ in range(roll_count):
                    roll = random.choices(
                        cinnamoroll_rarity,
                        weights=[c["weight"] for c in cinnamoroll_rarity],
                        k=1
                    )[0]

                    rarity_name = roll["name"]
                    elements.has_gumarang = True
                    rarity_display = f"{roll['color']}{rarity_name}{RESET}"

                    results.append((rarity_name, rarity_display))

                    # track summary
                    if rarity_name not in summary:
                        summary[rarity_name] = 0
                    summary[rarity_name] += 1

                    player_inventory.append({
                        "name": rarity_name,
                        "display": rarity_display
                    })

                # Print results
                dash_line()
                print(f"{main_color}You rolled {roll_count} time(s)!{RESET}")

                for rarity_name, rarity_display in results:
                    emote = rarity_emotes.get(rarity_name, "")
                    print(f"- {rarity_display} {emote}")

                dash_line()

                # 📊 summary
                print(f"{secondary_color}Summary:{RESET}")
                rarity_order = ["Common", "Rare", "Musical", "Iconic", "Legendary", "Gumarang"]

                for rarity in rarity_order:
                    if rarity in summary:
                        emote = rarity_emotes.get(rarity, "")
                        print(f"{rarity}: x{summary[rarity]} {emote}")

                dash_line()

            else:
                print(f"{RESET}You don't have enough credits!")

        if gameroll == "inv":
            random_note = ["I think she likes cinnamoroll, not sure though.",
                           "I can't really see what she has.",
                           "I miss you.",
                           "I love you <3"
                           ]
            dash_line()
            print(f"{main_color}Lezzell's{RESET} inventory of cinnamorolls. {main_color}{random.choice(random_note)}{RESET}")
            if len(player_inventory) == 0:
                print("Nothing in here for now.")  
            elif len(player_inventory) > 0:
                inventory = {}

                for item in player_inventory:
                    rarity = item["name"]

                    if rarity not in inventory:
                        inventory[rarity] = 0

                    inventory[rarity] += 1

                rarity_order = ["Common", "Rare", "Musical", "Iconic", "Legendary", "Gumarang"]

                for rarity in rarity_order:
                    if rarity in inventory:
                        emote = rarity_emotes.get(rarity, "")
                        print(f"{secondary_color}{rarity}{RESET}: x{inventory[rarity]} {emote}")
            dash_line()
            
        if gameroll == "ily":
            credit += 1
            i_love_you_message = [
                "I love you too baby!",
                "I love you so so so much!",
                "Mwah! I love you too.",
                "I love you most btw.",
                "I love you very, very much.",
                "I love you SUPER!"
            ]
            print(f"{RESET}{random.choice(i_love_you_message)} {PINK}+1 Credit{RESET}")
        if gameroll in ("i love you.", "i love you", "i love you very much", "i love you more", "i love you most"):
            credit += 5
            i_love_you_message = [
                "I love you even more, my dear",
                "I adore everything about you.",
                "The love missed the moon. It now runs through space to the stars, for my love is greater than the distance of the moon from the earth.",
                "I love you so much more, even if you say otherwise.",
                "I want to spend the rest of my life with you, my love.",
                "I want you to be the last glimpse of God's blessings before I pass.",
                "You eyes join the beauties of the sky down to my own.",
                "Yes, I can be your Discord to your Fluttershy. You help me wash off my former mistakes.",
                "Please be the Ria to my Senn",
                "I'll love you like Ephesians 5:25.",
                "I'm not helplessly in love, for I do not ask for help. I am where I want to be.",
                "There is no amount of lines of code that can accurately represent my love for you",
                "Not all flowers bloom in spring, for I found one still flowing beautifully despite the years of hardship.",
                "Lend me your fears, your mistakes, for I will love them as much as your beauties.",
                "Philippians 1:3.",
                "You are my pride, my joy, my reason."
            ]
            print(f"{RESET}{random.choice(i_love_you_message)} {PINK}+5 Credit{RESET}")
        if gameroll == "cls":
            clear_console()
        if gameroll == "doc":
            print(f"{UNDERLINE}{MAGENTA}ABOUT THIS APP{RESET}\nThis is a silly little app for you to roll different rarities of cinnamorolls. I know you love cinnamoroll and I plan to expand on a project about a game just like this!\n\nThe game is very simple: Just roll and hope for the best cinnamoroll using the credits you've been given.\n\nThere are 6 different types of cinnamorolls in this little game: common, rare, musical, iconic, and the other two you can discover for yourself.\n\nIf you discover the rarest one, you unlock a new command in the terminal!\n\nWhen getting more credits, you use 'ily' because that's simple. But you if you add a little more love into it: 'I love you', you may get more credits!")

app_cinnamoroll_run()