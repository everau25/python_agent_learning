"""
编写一个程序，让用户输入一个正整数n，然后计算1到n之间（包含n）所有整数的和、积

要求：

1. 使用input()获取用户输入的数字
2. 将输入转换为整数类型
3. 使用while循环实现累加和累乘功能
4. 使用格式化输出显示这二个计算结果
"""

num = int(input("请输入一个正整数"))
i = 1
total_sum = 0
total_product = 1
while i <= num:
    total_sum += i
    total_product *= i
    i += 1
print(f"1 到 {num} 的累加和为：{total_sum}")
print(f"1 到 {num} 的累乘积为：{total_product}")







