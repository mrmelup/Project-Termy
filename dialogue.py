import random

dialogue = {
    "secret_overlord_dialogue": [
        "You're not going to find anything.",
        "Secret? You're not going to find anything, you know.",
        "Nice attempt. Really, you're not going to find anything interesting.",
        "Mhm, nothing to be seen. You can go now.",
        "Stop. You're wasting your time.",
        "Sure, try again. Nothing.",
        "Hey, you're not going to find anything.",
        "How did you even figure this out?",
        "Ignore this. Please.",
        "Don't continue, you're not some special wizard.",
        "...You think you're going to get a response?",
        "Gonna need a key for some secrets.", 
        "Really? You wanted to type 'secret'? Funny.",
        "What makes you think you're going to find anything?",
        "Nope. Nothing here.",
        "Why did you type 'secrets'? Doesn't seem like theres anything here.",
        "No, don't think there is anything here."
    ],
    "i_love_you_too": [
        "I love you most, my darling.",
        "I love you very much as well, my dear.",
        "All the love back to you.",
        "Mwah. I love you too.",
        "You deserve it baby :)",
        "Guess what? I love you most.",
        "I love you so very much.",
        "I love you eeeeeven more.",
        "I love you most. I win.",
        "I LOVE YOU MOST.",
        "I love you and you are mine."
    ]
}

def say(category):
    return random.choice(dialogue[category])