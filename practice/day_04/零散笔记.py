import random
#  判断or 和 and 的输出效果
# print("11" or "12")
# print("11" and "12")
# print(0 or "11")
# print(0 and "11")

# 案例：法律规定，车辆驾驶员的血液酒精含量小于 20mg/100ml 不构成酒驾；
#       酒精含量大于或等于 20mg/100ml 为酒驾；酒精含量大于或等于 80mg/100ml 为醉驾。
# 编写 Python 程序判断是否为酒后驾车。

# mg = int(input('请输入血液酒精含量'))
#
# if mg < 20:
#     print('不构成酒驾')
# else:
#     if mg >= 80:
#         print('醉驾')
#     else:
#         print('酒驾')

# 猜数字案例

# rand_num =random.randint(1,100)
# print(rand_num)
# max_tries = 3
# for i in range(max_tries):
#     num = int(input('请输入您要猜的数字'))
#     if num == rand_num:
#         print('猜对了')
#         break
#     elif num > rand_num:
#         print('猜大了,', end='')
#     else:
#         print('猜小了,', end='')
#     left = max_tries - 1 - i
#     if left > 0:
#         print(f'还剩 {left} 次机会。')
#     else:
#         print(f'机会用光啦，正确答案是 {rand_num}')

#  案例：用while循环求1 到100的和
#
# num = 1
# total_num = 0
# while num < 101:
#
#     total_num += num
#     num += 1
#
# print(total_num)


# 举例：一共吃5个苹果，吃完第一个，吃第二个…，这里"吃苹果"的动作是不是重复执行？
#
# 场景一：如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第5个苹果，
# 即是吃苹果的动作停止，这里就是break控制循环流程，即终止此循环。
#
# 场景二：如果吃的过程中，吃到第三个吃出一个大虫子...,
# 是不是这个苹果就不吃了，开始吃第四个苹果，这里就是continue控制循环流程，即退出当前一次循环继而执行下一次循环代码。

# i = 1
# while i <6:
#     print(f'正在吃第{i}个苹果')
#     if i == 3:
#         break
#     i += 1


# i = 1
# while i <6:
#     print(f'正在吃第{i}个苹果')
#
#     if i == 3:
#         print(f'吃出一个大虫子，不吃了')
#         i +=1
#         continue
#
#     print(f'第{i}个苹果吃完了')
#     i += 1



