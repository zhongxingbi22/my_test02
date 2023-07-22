def calculator():
    # 获取用户输入的两个数字
    number1 = float(input("请输入第一个数字："))
    number2 = float(input("请输入第二个数字："))

    # 获取用户输入的运算符
    operator = input("请输入运算符：")

    # 执行运算
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    else:
        print("不支持该运算符！")
        return

    # 输出结果
    print("计算结果为：", result)


if __name__ == "__main__":
    calculator()
