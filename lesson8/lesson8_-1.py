def get_player_ai(main):
    return main["player"], main["ai"]

def answer(main):
    while True:
        player, ai = main, key=get_player_ai
        player_question = input("")
        if player_question == player:
            print(ai)
            continue
        else:
            print("Failed")
            break
def Main():
    main = [{"player1": "Hi", "ai": "Hi"},
            {"player2": "How are you?", "ai": "I`m fine"}]
    answer(main)
Main()