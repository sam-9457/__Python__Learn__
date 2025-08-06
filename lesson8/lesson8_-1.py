import random

def AI_guess():
    print(f"========猜數字遊戲=========\n\n")
    while(True):
        min = 1
        max = 5
        count1 = 0
        count2 = 0
        target = random.randint(min, max)
        keyin = random.randint(min, max)
        count1 += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(keyin)
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"你共猜了{count1}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!")
                print(f"AI已經猜{count1}次")
                print(keyin)
            else:
                print(f"猜錯了!")
                print(f"AI已經猜{count1}次")
                print(keyin)
        else:
            print("請輸入提示範圍內的數字\n")
    print(f"========猜數字遊戲=========\n\n")
    while(True):
        min = 1
        max = 5
        count1 = 0
        count2 = 0
        target = random.randint(min, max)
        keyin = random.randint(min, max)
        count2 += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(keyin)
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"你共猜了{count2}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!")
                print(f"AI已經猜{count2}次")
                print(keyin)
            else:
                print(f"猜錯了!")
                print(f"AI已經猜{count2}次")
                print(keyin)
        else:
            print("請輸入提示範圍內的數字\n")
    print(f"遊戲結束")
AI_guess()