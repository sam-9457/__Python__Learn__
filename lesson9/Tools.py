def calculate_bmi(weight:float, height:float) -> float:
    """計算BMI值   
    :param weight: 體重 (kg)
    :param height: 身高 (cm)
    :return: BMI值
    :raises ValueError: 如果體重或身高小於等於0"""
    if weight <= 0 or height <= 0:
        raise ValueError("輸入的體重與身高需為大於 0")
    bmi = weight / ((height / 100) ** 2)
    return  bmi

def classify_bmi(bmi:float)->str:
    """根據BMI值分類體重狀態
    :param bmi: BMI值
    :return: 體重狀態描述
    :raises ValueError: 如果BMI值小於0"""
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return  "體重正常"
    elif bmi < 27:
        return  "過重"
    elif bmi < 30:
        return  "輕度肥胖"
    elif bmi < 35:
        return  "中度肥胖"
    else:
        return  "重度肥胖"

def suggest_weight_range(height:float)->tuple[float]:
    """根據身高建議健康體重範圍
    :param height: 身高 (cm)
    :return: 建議的健康體重範圍 (最小值, 最大值)
    :raises ValueError: 如果身高小於等於0
    """
    min_bmi = 18.5
    max_bmi = 24
    min_weight = min_bmi * ((height / 100) ** 2)
    max_weight = max_bmi * ((height / 100) ** 2)
    return min_weight, max_weight
