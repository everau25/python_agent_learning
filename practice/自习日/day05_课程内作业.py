# ### 作业1:  字符串的案例:
#
# 案例1 给定一个图片的名称为"avatar.png"，代码实现获取这个图片的名称(avatar)以及这个图片的后缀(.png)。
#
# - 分析：
#   - ① 建议先获取点号的位置（目前还未学习，只能一个一个数）
#   - ② 从开头切片到点号位置，得到的就是文件的名称
#   - ③ 从点号开始切片，一直到文件的结尾，则得到的就是文件的后缀

# pic_name = 'avatar.png'
#
# print(pic_name[:6])
# print(pic_name[6:])

# ### 作业2: 列表
#
# 需求1: 求相邻元素最大值.编写一个程序，求一个正整数数组中每对相邻元素的最大值。
#  例如, 输入: [7 8 9 5 6 7 2 3] 输出: [8, 9, 9, 6, 7, 7, 3]

# num_1 = [7, 8, 9, 5, 6, 7, 2, 3]
# len_num_1 =len(num_1) - 1
# result = []
# for i in range(len_num_1):
#     if num_1[i] > num_1[i+1]:
#         max_val = num_1[i]
#     else:
#         max_val = num_1[i+1]
#     result.append(max_val)
# print(result)

# 需求2: 给定列表original_list其中包含1, 2, 2, 3, 4, 4, 5, 6, 6, 7元素，现在通过编写程序对列表中的数据进行去重
# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# original_list = list(set(original_list))
# print(original_list)

# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# update_list = []
# for i in original_list:
#     if i not in update_list:
#         update_list.append(i)
# print(update_list)

# 案例需求1
#
# 编写一个程序来提取嵌套元组中的唯一元素。
# 例如: 在嵌套元组((1,2,3),(2,4,6),(2,3,5))中, 2重复出现了3次，3重复出现了2次，但我们的输出列表只会包含2、3一次。
# 即：[1, 2, 3, 4, 5, 6]

# my_tuple = ((1, 2, 3),(2, 4, 6),(2, 3, 5))
# my_list = []
# for i in my_tuple:
#     my_tuple_1 = i
#     for j in my_tuple_1:
#         if j not in my_list:
#             my_list.append(j)
# print(my_list)


# 案例需求2:
#
# 给定一个元组my_tuple，里面包含1, 2, 3, 4, 5, 6, 7, 8, 9元素，要求统计数字元组中, 奇数的个数

# my_tuple =(1, 2, 3, 4, 5, 6, 7, 8, 9,)
# sub_list = []
# for i in my_tuple:
#     if i % 2 == 1:
#         sub_list.append(i)
# my_count = len(sub_list)
# print(my_count)


