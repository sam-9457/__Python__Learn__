import argparse
import random
def parse_name()->str:
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-ho", "--host",type=str, help = "姓名")
    parser.add_argument("-ch", "--challenger",type=str, help = "姓名")
    args = parser.parse_args()

    if not args.host:
        player1 = input("請輸入玩家1的名字: ")
        print(f"玩家1:{player1}")
    else:
        player1 = args.host
    if not args.challenger:
        player2 = input("請輸入玩家2的名字: ")
        print(f"玩家2:{player2}")
    else:
        player2 = args.challenger
    
    return player1, player2

def play_game(player1, player2):
    count1 = 0
    print(f"""========猜數字遊戲開始=========\n\n
這是{player1}的回合""")
    min = 1
    max = 100
    target = random.randint(min,max)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count1 += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{player1}你共猜了{count1}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
                print(f"{player1}已經猜{count1}次\n")
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
                print(f"{player1}已經猜{count1}次\n")
        else:
            print("請輸入提示範圍內的數字\n")
    count2 = 0
    print(f"""========猜數字遊戲開始=========\n\n
這是{player2}的回合""")
    min = 1
    max = 100
    target = random.randint(min,max)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count2 += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{player2}你共猜了{count2}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
                print(f"{player2}已經猜{count2}次\n")
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
                print(f"{player2}已經猜{count2}次\n")
        else:
            print("請輸入提示範圍內的數字\n")
    return count1, count2
def main():    
    Player1, Player2 = parse_name()
    Count1, Count2 = play_game(Player1, Player2)
    print(f"遊戲結束，{Player1}和{Player2}的猜數字次數分別為{Count1}和{Count2}")
    if Count1 < Count2:
        print(f"{Player1}獲勝!")
    elif Count1 > Count2:
        print(f"{Player2}獲勝!")
    else:
        print("平手!")

if __name__ == '__main__':
    main()