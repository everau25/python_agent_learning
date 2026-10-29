# ## 2- 求1~100的奇数和
#
# 奇数: 对2取余数, 得 1 为奇数
#
# 要求: 分别使用 for 和 while实现

for i in range(1,101):
    if i % 2 == 1:
        print(i)
    i += 1