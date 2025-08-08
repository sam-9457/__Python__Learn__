import random

def playGame():
    while True:
        key_in = input("請輸入剪刀/石頭/布（輸入 q 離開）：")
        if key_in == "剪刀":
            key_in = 0
            break
        elif key_in == "石頭":
            key_in = 1
            break
        elif key_in == "布":
            key_in = 2
            break
        elif key_in == "q":
            break
        else:
            print("輸入錯誤")
    return key_in
            
def result(key_in, target, Victory_or_defeat):
    if key_in - 1 == target or target - 2 == key_in:
        Victory_or_defeat["勝"] += 1
    elif key_in + 1 == target or target + 2 == key_in:
        Victory_or_defeat["敗"] += 1
    else:
        Victory_or_defeat["平手"] += 1
def main():
    main_key_in = ["剪刀", "石頭", "布"]
    Victory_or_defeat = {"勝":0, "敗":0, "平手":0}
    print("======猜拳遊戲=======\n")

    while True:
        player_key_in = playGame()
        if player_key_in != "q":
            target = random.randint(0,2)
            print(f"電腦出了{main_key_in[target]}")
            print(f"你出了{main_key_in[player_key_in]}")
            result(player_key_in, target, Victory_or_defeat)
            print(f"分數:\n勝:{Victory_or_defeat['勝']}\n敗:{Victory_or_defeat['敗']}\n平手{Victory_or_defeat['平手']}")
        else:
            print(f"遊戲結束\n分數:\n勝:{Victory_or_defeat['勝']}\n敗:{Victory_or_defeat['敗']}\n平手{Victory_or_defeat['平手']}")
            break
if __name__ == "__main__":
    main()