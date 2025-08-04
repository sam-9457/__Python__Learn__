from Tools import calculate_bmi, classify_bmi, suggest_weight_range
"""
lesson9/lesson9_1.py
計算BMI值並分類體重狀態
"""

def main():
    """主函數，執行BMI計算和分類
    :raises ValueError: 如果輸入的體重或身高無效
    """
    print("✷" * 7, "計算BMI", "✷" * 7)
    try:
        weight:float = float(input("輸入體重 (kg): "))
        height:float = float(input("輸入身高 (cm): "))
        bmi:float = calculate_bmi(weight, height)

        print("\n======= 結果 =======")
        print(f"體重: {weight:.1f} kg")
        print(f"身高: {height:.1f} cm")
        print(f"BMI: {bmi:.2f}")

        status:str = classify_bmi(bmi)
        print(f"判定: {status}")

        if not (18.5 <= bmi < 24):
            min_w, max_w = suggest_weight_range(height)
            print(f"建議健康體重範圍: {min_w:.1f}kg ~ {max_w:.1f}kg")

    except ValueError as ve:
        print(f"錯誤: {ve}")
        
if __name__ == "__main__":
     main()