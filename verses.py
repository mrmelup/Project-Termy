from elements import *

verses = {
    "happy": [
        ("Psalm 30:5", "For his anger is but for a moment, and his favor is for a lifetime. Weeping may tarry for the night, but joy comes with the morning."),
        ("Zephaniah 3:17", "The Lord your God is in your midst, a mighty one who will save he will rejoice over you with gladness; he will quiet you by his love he will exult over you with loud singing."),
        ("John 16:22", "Just so, I tell you, there will be more joy in heaven over one sinner who repents than over ninety-nine righteous persons who need no repentance."),
        ("John 16:24", "Until now you have asked nothing in my name. Ask, and you will receive, that your joy may be full."),
        ("Romans 12:12", "Rejoice in hope, be patient in tribulation, be constant in prayer"),
        ("Romans 15:13", "May the God of hope fill you with all joy and peace in believing, so that by the power of the Holy Spirit you may abound in hope."),
        ("1 Thessalonians 5:16-18", "Rejoice always, pray without ceasing,  give thanks in all circumstances; for this is the will of God in Christ Jesus for you."),
        ("1 Peter 4:13", "Instead, be very glad—for these trials make you partners with Christ in his suffering, so that you will have the wonderful joy of seeing his glory when it is revealed to all the world.")
    ],
    "love": [
        ("1 Peter 4:8", "Above all, love each other deeply, because love covers over a multitude of sins."),
        ("1 Corinthians 16:14", "Let all that you do be done in love."),
        ("Romans 12:9-10", "Love must be sincere. Hate what is evil; cling to what is good. Be devoted to one another in brotherly love. Honor one another above yourselves."),
        ("Ephesians 5:2", "Live a life of love, just as Christ loved us and gave himself up for us as a fragrant offering and sacrifice to God."),
        ("1 Timothy 1:7", "For God did not give us a spirit of timidity, but a spirit of power, of love, and of self-discipline."),
        ("1 Corinthians 13:4-7", "Love is patient, love is kind. It does not envy, it does not boast, it is not proud.  It is not rude, it is not self-seeking, it is not easily angered, it keeps no record of wrongs.  Love does not delight in evil but rejoices with the truth.  It always protects, always trusts, always hopes, always perseveres.  Love never fails…"),
        ("1 John 4:10-12", "This is love: not that we loved God, but that he loved us and sent his Son as an atoning sacrifice for our sins. Dear friends, since God so loved us, we also ought to love one another. No one has ever seen God; but if we love one another, God lives in us and his love is made complete in us."),
        ("Song of Solomon 8:3", "I am my beloved’s and my beloved is mine."),
        ("Ecclesiastes 4:9-12", "Two are better than one, because they have a good return for their labor: If either of them falls down, one can help the other up. But pity anyone who falls and has no one to help them up. Also, if two lie down together, they will keep warm. But how can one keep warm alone? Though one may be overpowered, two can defend themselves. A cord of three strands is not quickly broken."),
        ("Song of Solomon 8:16", "Place me like a seal over your heart, like a seal on your arm; for love is as strong as death, its jealousy unyielding as the grave. It burns like blazing fire, like a mighty flame. Many waters cannot quench love; rivers cannot sweep it away. If one were to give all the wealth of one’s house for love, it would be utterly scorned."),
        ("Proverbs 10:12", "Hate stirs up trouble, but love forgives all offenses.")
    ],
    "hope": [
        ("Romans 8:24", "For in this hope we were saved. Now hope that is seen is not hope. For who hopes for what he sees?"),
        ("1 Peter 1:3", "Blessed be the God and Father of our Lord Jesus Christ! According to his great mercy, he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead."),
        ("Romans 15:4", "For whatever was written in former days was written for our instruction, that through endurance and through the encouragement of the Scriptures we might have hope."),
        ("Psalm 39:7", "And now, O Lord, for what do I wait? My hope is in you."),
        ("1 Corinthians 13:13", "So now faith, hope, and love abide, these three; but the greatest of these is love."),
        ("Romans 5:5", "And hope does not put us to shame, because God's love has been poured into our hearts through the Holy Spirit who has been given to us."),
        ("Titus 3:7", "So that being justified by his grace we might become heirs according to the hope of eternal life.")
    ],
    "strength": [
        ("Joshua 1:9", "Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the LORD your God is with you wherever you go."),
        ("Psalm 73:26", "My flesh and my heart may fail, but God is the strength of my heart and my portion forever."),
        ("Philippians 4:13", "I can do all things through him who strengthens me."),
        ("Deuteronomy 31:6", "Be strong and courageous. Do not fear or be in dread of them, for it is the LORD your God who goes with you. He will not leave you or forsake you."),
        ("Psalm 46:1-2", "God is our refuge and strength, a very present help in trouble. Therefore we will not fear though the earth gives way, though the mountains be moved into the heart of the sea."),
        ("1 Corinthians 16:13", "Be watchful, stand firm in the faith, act like men, be strong."),
        ("Isaiah 40:29-31", "He gives power to the faint, and to him who has no might he increases strength. Even youths shall faint and be weary, and young men shall fall exhausted; but they who wait for the LORD shall renew their strength; they shall mount up with wings like eagles; they shall run and not be weary; they shall walk and not faint."),
        ("Isaiah 41:10", "Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.")
    ],
    "closure": [
        ("John 3:16", "For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life."),
        ("Matthew 5:18", "For truly, I say to you, until heaven and earth pass away, not an iota, not a dot, will pass from the Law until all is accomplished."),
        ("Luke 21:33", "Heaven and earth will pass away, but my words will never pass away"),
        ("Proverbs 3:6", "In all your ways acknowledge Him, And He will make your paths straight."),
        ("Malachi 1:1", "When you lie down, you will not be afraid. When you lie down, your sleep will be sweet.")
    ],
    "fear": [
        ("2 Timothy 1:7", "For God has not given us a spirit of fear, but of power and of love and of a sound mind."),
        ("Psalm 56:3-4", "When I am afraid, I put my trust in you. In God, whose word I praise, in God I trust; I shall not be afraid. What can flesh do to me?"),
        ("Isaiah 43:1", "But now, this is what the Lord says — he who created you, Jacob, he who formed you, Israel: 'Do not fear, for I have redeemed you; I have summoned you by name; you are mine.'"),
        ("Psalm 23:4", "Even though I walk through the darkest valley, I will fear no evil, for you with me; your rod and your staff, they comfort me."),
        ("Psalm 27:1", "The LORD is my light and my salvation; whom shall I fear? The LORD is the stronghold of my life; of whom shall I be afraid?"),
        ("Psalm 46:1", "God is our refuge and strength, a very present help in trouble."),
        ("John 14:27", "Peace I leave with you; my peace I give to you. Not as the world gives do I give to you. Let not your hearts be troubled, neither let them be afraid."),
        ("Philippians 4:6", "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God."),
        ("1 Peter 5:7", "Cast all your anxieties on Him, because He cares for you.")
    ],
    "struggle": [
        ("Revelation 21:4", "He will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain anymore, for the former things have passed away."),
        ("Matthew 5:4", "Blessed are those who mourn, for they shall be comforted."),
        ("Psalm 23:4", "Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me."),
        ("Psalm 73:26", "My flesh and my heart may fail, but God is the strength of my heart and my portion forever."),
        ("2 Corinthians 1:3-4", "Blessed be the God and Father of our Lord Jesus Christ, the Father of mercies and God of all comfort, who comforts us in all our affliction, so that we may be able to comfort those who are in any affliction, with the comfort with which we ourselves are comforted by God."),
        ("1 Peter 5:10", "And after you have suffered a little while, the God of all grace, who has called you to his eternal glory in Christ, will himself restore, confirm, strengthen, and establish you."),
        ("2 Corinthians 4:17", "For this light momentary affliction is preparing for us an eternal weight of glory beyond all comparison."),
        ("Isaiah 43:2", "When you pass through the waters, I will be with you; and through the rivers, they shall not overwhelm you; when you walk through fire you shall not be burned, and the flame shall not consume you."),
    ],
    "guilt": [
        ("1 John 1:9", "If we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness."),
        ("Romans 3:23", "For all have sinned and fall short of the glory of God"),
        ("James 4:7", "Submit yourselves therefore to God. Resist the devil, and he will flee from you."),
        ("1 John 2:1", "My little children, I am writing these things to you so that you may not sin. But if anyone does sin, we have an advocate with the Father, Jesus Christ the righteous."),
        ("2 Corinthians 7:10", "For godly grief produces a repentance that leads to salvation without regret, whereas worldly grief produces death."),
        ("Isaiah 6:7", "And he touched my mouth and said: 'Behold, this has touched your lips; your guilt is taken away, and your sin atoned for.'"),
        ("Hebrews 10:22", "Let us draw near with a true heart in full assurance of faith, with our hearts sprinkled clean from an evil conscience and our bodies washed with pure water."),
        ("Acts 3:19", "Repent therefore, and turn back, that your sins may be blotted out,"),
        ("Isaiah 1:18", "'Come now, let us settle the matter,' says the LORD. 'Though your sins are like scarlet, they shall be as white as snow; though they are red as crimson, they shall be like wool.'")
    ],
    "anger": [
        ("Proverbs 15:1", "A soft answer turns away wrath, but a harsh word stirs up anger."),
        ("James 1:19-20", "Know this, my beloved brothers: let every person be quick to hear, slow to speak, slow to anger; for the anger of man does not produce the righteousness of God."),
        ("Colossians 3:8", "But now you must put them all away: anger, wrath, malice, slander, and obscene talk from your mouth."),
        ("Proverbs 22:24-25", "Make no friendship with a man given to anger, nor go with a wrathful man, lest you learn his ways and entangle yourself in a snare."),
        ("Psalm 37:8", "Refrain from anger, and forsake wrath! Fret not yourself; it tends only to evil.")
    ]
}

usage = 0
category = ["happy", "love", "hope", "strength", "closure", "fear", "struggle", "guilt", "anger"]

def make_line():
    print(f"{WHITE}={RESET}" * 55 + f"{WHITE}=== == ={RESET}")

def random_verse():
    category = random.choice(list(verses.keys()))
    reference, text = random.choice(verses[category])

    return f"A verse for: {LIGHT_BLUE}{category}{RESET}.\n\n{reference}\n    \"{text}\""

def selected_verse(verse):
    reference, text = random.choice(verses[verse])

    return f"A verse for: {LIGHT_BLUE}{verse}{RESET}.\n\n{reference}\n    \"{text}\""

def make_bar(usage, date):
    make_line()
    usage += 1
    print(f"Welcome to the Verses App! {WHITE}|{RESET} Usages: {usage} {WHITE}|{RESET} Date: {date}\n[ {RED}Q{RESET} ] Quit | [ {GREEN}R{RESET} ] Random Verse | [ {WHITE}S{RESET} ] Select Category")
    make_line()

    return usage

def display_verse(text):
    print(text)
    make_line()

def format_categories():
    formatted = []
    for cat in verses.keys():
        formatted.append(f"{cat.capitalize()}")
    return "  ".join(formatted)

def main_function():
    while True:
        clear_console()
        global usage
        global category
        date = f"{month}/{day_time}/{year}"

        usage = make_bar(usage, date)

        user_input = input(f"\n:::   ")

        # User Input
        if user_input in ("q", "quit", "leave", "exit"):
            break
        if user_input == "r":
            clear_console()
            usage = make_bar(usage, date)
            display_verse(random_verse())
            input(f"\nPress enter to continue or type exit to leave. ")

        if user_input == "s":
            clear_console()
            usage = make_bar(usage, date)

            verse = input(f"::: {UNDERLINE}Select a category{RESET}\n" + format_categories() + "\n:::  ").lower()
            
            if verse in verses:
                clear_console()
                usage = make_bar(usage, date)
                display_verse(selected_verse(verse))
                input(f"\nPress {LIGHT_BLUE}enter{RESET} to continue. ")
            else:
                print("That's not a category :(")
                input(f"\nPress {LIGHT_BLUE}enter{RESET} to continue. ")

main_function()