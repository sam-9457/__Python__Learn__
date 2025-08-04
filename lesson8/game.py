import random

def play_game()->None:
    """猜數字遊戲
    這個函數實現了一個簡單的猜數字遊戲，玩家需要在指定範圍內猜一個隨機生成的數字。
    玩家每次猜測後，系統會提示猜的數字是太大還是太小，直到猜中為止。
    遊戲結束後會顯示玩家猜測的次數。
    如果玩家猜對了，會詢問是否要繼續遊戲。
    如果玩家選擇繼續，遊戲會重置並開始新一輪遊戲。
    如果玩家選擇結束，遊戲會顯示總玩次數並結束遊戲。
    """
    print("========猜數字遊戲=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"你共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
                print(f"您已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")