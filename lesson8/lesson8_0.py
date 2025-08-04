def checkHealthy(Bmi):
    if Bmi < 18.5:
        return "體重過輕"
    elif Bmi < 24:
        return "體重正常"
    elif Bmi < 27:
        return "過重"
    elif Bmi < 30:
        return "輕度肥胖"
    elif Bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"
def suggestWeight(height):
    min_Weight = 18.5 * (height / 100) ** 2
    max_Weight = 24 * (height / 100) ** 2
    return min_Weight, max_Weight
def Main():
    try:
        while (True):
            height = int(input("請輸入身高"))
            if height <= 50 or height >= 250:
                print("範圍錯誤,請重新輸入")
                continue
            else:
                break
        while(True):
            weight = int(input("請輸入體重"))
            if weight <= 10 or weight >= 200:
                print("範圍錯誤,請重新輸入")
                continue
            else:
                break
    except ValueError:
        print("值出錯了")
    except Exception as e:
        print(f"出錯了:{e}")
    BMI = weight / (height / 100) ** 2
    print(f"你的身高為:{height}\n你的體重為:{weight}\n你的BMI為:{BMI:.1f}")
    health = checkHealthy(BMI)
    print(health)
    min_Weight, max_Weight = suggestWeight(height)
    print(f"您的標準體重是{min_Weight:.1f}~{max_Weight:.1f}之間")
if __name__ == "__main__":
     Main()