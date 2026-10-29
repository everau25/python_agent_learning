# ## 3- 完成猜数字小游戏案例(while)
#
# 编写一个Python程序，随机生成一个1到100之间的整数，用户通过输入猜测的数字，程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。用户可以无限次猜测，直到猜对为止。猜对后，程序会提示用户并结束游戏。
#
# 实现思路
#
# ① 编写一个循环，满足条件后停止。
#
# ② 要从1 ~ 100之间选择一个随机数
#
# ③ if分支判断

import random

# 1- 让计算机随机出一个随机数 (1~100之间)
computer_random_num = random.randint(1,100)


while True:
    guess_num = int(input("请输入您要猜的数字"))
    if guess_num >= computer_random_num:
        print("猜大了，继续猜")
    elif guess_num < computer_random_num:
        print("猜小了，继续猜")
    else:
        print("恭喜你，猜对了！")
        break  # 猜对后直接跳出循环，结束游戏



