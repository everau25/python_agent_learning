"""
    编写一个程序，让用户输入一个1-9之间的整数n，然后使用for循环打印n的1~9乘法的结果。

    要求：

    1. 使用input()获取用户输入
    2. 将输入转换为整数类型
    3. 使用for循环和range()函数实现
    4. 使用格式化输出，格式为：n x i = result
    5. 程序应验证输入是否在1-9范围内，否则提示重新输入

"""
while True:
    try:
        num = int(input("请输入一个1-9之间的整数："))

        if 1 <= num <= 9:
            for i in range(1, 10):
                result = num * i
                print(f"{num} x {i} = {result}")
            break
        else:
            print("范围不对！数字应在1-9之间，请重新输入。")

    except ValueError:
        print("格式错误！您输入的不是整数，请重新输入。")

