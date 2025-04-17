import random

def main():
    print("🔮 Welcome to Dhruv Pathak's Fortune Teller (21JE0311) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    
    happy_fortunes = [
        "✨ Your fortune: Amazing moments lie ahead, Dhruv Pathak! Stay cheerful. ✨",
        "✨ Your fortune: Your good vibes are opening doors to exciting possibilities today! ✨",
        "✨ Your fortune: The world feels brighter when you smile—keep shining, Dhruv! ✨"
    ]

    sad_fortunes = [
        "✨ Your fortune: Storms pass, and joy is on the horizon. Hold on, Dhruv Pathak. ✨",
        "✨ Your fortune: Even in the quietest times, Dhruv, your strength will guide you. ✨",
        "✨ Your fortune: This moment will fade—hope and happiness are already on their way. ✨"
    ]

    neutral_fortunes = [
        "✨ Your fortune: Steady steps bring lasting progress. Keep moving forward. ✨",
        "✨ Your fortune: Dhruv Pathak, your peaceful nature will unlock hidden truths today. ✨",
        "✨ Your fortune: Walking the middle path will lead you to unexpected rewards. ✨"
    ]


    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))   
    else:
        print("✨ Your fortune: I cannot read your mood, but Adesh Sinha's destiny is still bright! ✨")

if __name__ == "__main__":
    main()