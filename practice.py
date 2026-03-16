#1.函数定义：逻辑封装
def assess_priority(age, stress_level, user_identity):
    """
    根据年龄和压力水平评估优先级
    """
    #2.逻辑判断（If-else语句）
    if stress_level > 8 and user_identity == "学生":
        return "紧急：建议立即转接人工心理干预"
    elif 18 <= age <= 25:
        return "普通：适合参加‘大学生心理健康’专题辅导"
    else:
        return "普通：安排常规AI辅助评估"
    #3.输入与数据转换
try:
    user_age = int(input("请输入您的年龄："))
    user_stress = int(input("请输入您的压力分值（1-10）："))
    user_identity = input("请输入您的身份（学生/教职工）：")

    #4.调用函数并打印结果
    result = assess_priority(user_age, user_stress, user_identity)
    print(f"\n评估结果：{result}")

except ValueError:
    print("错误：请输入数字，不要输入文字。")
    