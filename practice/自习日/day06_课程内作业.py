"""
编写一个程序来统计缺失的数字并返回它们的总和。缺失的数字是指给定列表中两个极端（最大和最小数字）之间没有出现的数字。
例如，在集合{2, 5, 3, 7, 5, 7}中，两个极端（即2和7）之间缺失的数字是4和6。
"""

my_set = {2, 5, 3, 7, 5, 7}

# 求最大、最小值
max_num = None
min_num = None
for i in my_set:
    if max_num is None:
        max_num = i
        min_num = i
    else:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

# 遍历 range，找出缺失数字并求和
missing_nums = []
missing_sum = 0

for i in range(min_num, max_num + 1):
    if i not in my_set:
        missing_nums.append(i)
        missing_sum += i  # 顺便累加求和

print(f"最大值为：{max_num}，最小值为：{min_num}")
print(f"缺失的数字有：{missing_nums}")
print(f"缺失数字的总和为：{missing_sum}")






