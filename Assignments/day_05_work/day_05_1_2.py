### 综合题目二：元组、列表与控制流的综合应用

# **【需求描述】** 已知某学习小组5名成员的成绩信息，使用**列表嵌套元组**的方式存储如下：
# `members = [("张三", 85), ("李四", 52), ("王五", 90), ("赵六", 78), ("钱七", 40)]`
#
# 请编写程序完成以下功能：
#
# 1. **筛选及格名单**：遍历数据，找出所有及格（>=60分）的成员，将其**姓名**添加到一个新的空列表 `pass_names` 中，最后打印该列表。
# 2. **不及格提醒**：遍历数据，找出不及格的成员，直接打印提示：“`[姓名]`同学成绩为`[分数]`，不及格，仍需努力！”。
# 3. **计算平均分**：计算该小组的平均分并打印。
# 4. **姓名查询**：使用 `input()`
# 让用户输入一个姓名，判断该姓名是否在小组中。如果在，输出其成绩；如果不在，输出“查无此人”。
# （*提示：可以利用 `for` 循环遍历比对，或者提取姓名后用 `in` 关键字判断*）。

members = [("张三", 85), ("李四", 52), ("王五", 90), ("赵六", 78), ("钱七", 40)]
pass_names = []
count = 0
total_score = 0
for i in members:
    my_tuple = i
    name = my_tuple[0]
    score = my_tuple[1]
    count += 1
    total_score += my_tuple[1]
    if my_tuple[1] >= 60:
        pass_names.append(name)
    else:
        print(f'{name}同学成绩为{score}，不及格，仍需努力！')


average_score = total_score / count

print(pass_names)
print(f'平均分为{average_score}')

search_name = input('请输入您要查询的姓名')
for name,score in members:
    if search_name == name:
        print(f'{name}成绩为{score}')
        break
else:
    print('查无此人')

