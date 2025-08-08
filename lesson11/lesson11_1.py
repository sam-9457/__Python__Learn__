import random

def input_gesture():#剪刀=0,石頭=1,布=2
    """
    Prompts the user to input a gesture ("剪刀", "石頭", "布") or "q" to quit.

    Returns:
        int or str: Returns 0 for "剪刀", 1 for "石頭", 2 for "布", or "q" if the user chooses to quit.
    """
    while True:
        gesture = input("輸入剪刀/石頭/布(輸入q退出):")
        if gesture == "剪刀":
            gesture = 0
            break
        elif gesture == "石頭":
            gesture = 1
            break
        elif gesture == "布":
            gesture = 2
            break
        elif gesture == "q":
            break
        else:
            print("請輸入正確選項")
    return gesture

def compare(player_gesture,opponent_gesture,record):
    """
    Compares the gestures of the player and the opponent in a game (e.g., rock-paper-scissors),
    updates the record dictionary with the result, and prints the outcome.
    Args:
        player_gesture (int): The gesture chosen by the player, represented as an integer.
        opponent_gesture (int): The gesture chosen by the opponent, represented as an integer.
        record (dict): A dictionary tracking the number of wins ("勝"), draws ("平"), and losses ("敗").
    Returns:
        None
    """

    if player_gesture - 1 == opponent_gesture or opponent_gesture - 2 == player_gesture:
        print("你贏了!")
        record["勝"] += 1
    elif player_gesture == opponent_gesture:
        print("平手!")
        record["平"] += 1
    else:
        print("你輸了!")
        record["敗"] += 1

def input_gesture():#剪刀=0,石頭=1,布=2
    while True:
        gesture = input("輸入剪刀/石頭/布(輸入q退出):")
        if gesture == "剪刀":
            gesture = 0
            break
        elif gesture == "石頭":
            gesture = 1
            break
        elif gesture == "布":
            gesture = 2
            break
        elif gesture == "q":
            break
        else:
            print("請輸入正確選項")
    return gesture

def compare(player_gesture,opponent_gesture,record):
    if player_gesture - 1 == opponent_gesture or opponent_gesture - 2 == player_gesture:
        print("你贏了!")
        record["勝"] += 1
    elif player_gesture == opponent_gesture:
        print("平手!")
        record["平"] += 1
    else:
        print("你輸了!")
        record["敗"] += 1

def main():
    gestures = ["剪刀","石頭","布"]
    record = {"勝":0,"敗":0,"平":0}
    print("\n=======猜拳遊戲=======\n")

    while True:
        player_gesture = input_gesture()
        if player_gesture != "q":
            opponent_gesture = random.randint(0,2)
            print(f"你出了{gestures[player_gesture]}")
            print(f"電腦出了{gestures[opponent_gesture]}")
            compare(player_gesture,opponent_gesture,record)
            print(f"目前成績:{record['勝']}勝,{record['敗']}敗,{record['平']}平\n")
        else:
            print(f"遊戲結束,你的成績是:{record['勝']}勝,{record['敗']}敗,{record['平']}平")
            break

if __name__ == "__main__":
    main()