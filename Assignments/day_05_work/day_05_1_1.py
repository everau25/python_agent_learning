## 课程外作业题：【完成当日内容后尝试做】

### 综合题目一：字符串与列表的综合应用
#
# **【需求描述】**
#
# 1. 提示用户输入一串以逗号 `,` 分隔的学生考试成绩（例如输入：`85,92,78,60,45,95`）。
# 2. 使用字符串的 `split()` 方法将输入的内容切割成列表。
# 3. 遍历该列表，将字符串类型的成绩转换为整数（`int`）。
# 4. 在遍历过程中，统计并计算以下数据：
#    - 总人数
#    - 及格人数（>=60分）
#    - 优秀人数（>=90分）
#    - 所有成绩的总和
# 5. 计算平均分，并使用 `f-string` 格式化输出最终的统计报告（平均分保留1位小数）。

student_scores = input('请以逗号为间隔输入学生的考试成绩')
student_scores_list = student_scores.split(',')
student_scores_list_int = []
count = 0
pass_scores = 0
excellent_scores = 0
total_score = 0
for i in student_scores_list:
    score = int(float(i))
    student_scores_list_int.append(score)
    count += 1
    total_score += score
    if score >= 60:
        pass_scores += 1
    if score >= 90:
        excellent_scores += 1

print(student_scores_list_int)
average_score = total_score / count
print(f'学生的总人数为{count},及格人数为{pass_scores},优秀人数为{excellent_scores},成绩总和为{total_score},平均分为{average_score:.1f}')




