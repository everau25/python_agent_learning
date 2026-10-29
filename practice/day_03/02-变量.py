# 在python中 字符串是需要用单引号 或者 双引号 包裹起来的

age1 = 18
age2 = 19
age3 = 20
height = 172.5
name1 = '张三'
name2 = "李四"
# 程序中 有时候有多个单词组成  下划线区分单词
user_name = '王五'
# 或者使用驼峰式命名规则  每一个单词连接的首字母 是大写
userName = '赵六'
# 在python中 有一些关键单词 不允许作为变量的名称
# 下划线 本质上有特殊的意义存在 _name = 'xxx'
help('keywords')


# 程序的代码 自上而下运行的  变量先定义 后使用
# '' 表示字符串
print(name1)  # 输出一个变量值  使用变量即可
print('name1') # 输出一个固定值  使用单引号
print(name2)
print(name1,name2,height)