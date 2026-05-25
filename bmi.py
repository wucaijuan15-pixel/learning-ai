# bmi.py

def calculate_bmi():
    print("====== 欢迎使用 BMI 健康计算器 ======")
    
    try:
        # 1. 获取用户输入
        weight = float(input("请输入你的体重 (单位: kg): "))
        height = float(input("请输入你的身高 (单位: m，例如 1.65): "))
        
        # 2. 计算 BMI 
        bmi = weight / (height ** 2)
        
        # 3. 打印计算结果（保留两位小数）
        print(f"\n你的 BMI 指数：{bmi:.2f}")
        
        # 4. 判断健康状态
        if bmi < 18.5:
            status = "体重过轻 🦴"
        elif 18.5 <= bmi < 24.0:
            status = "正常范围 👑（太棒了，继续保持！）"
        elif 24.0 <= bmi < 28.0:
            status = "体重超重 🍎"
        else:
            status = "过度肥胖 🍗"
            
        print(f"健康评估结果：{status}")
        
    except ValueError:
        print("输入错误！请输入正确的数字（例如体重输入 60，身高输入 1.7）。")

if __name__ == "__main__":
    calculate_bmi()


#我就是测试下更新的上传上去是怎样的