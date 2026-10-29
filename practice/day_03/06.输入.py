# 输出: 从程序往外打印内容   print()
# 输入: 从外部输入一定的数据  变量 = input(prompt 提示信息)
name = input('请输入您的姓名:')
age = input('请输入您的年龄:')
height = input('请输入您的身高:')

# 输入的内容是什么类型的?  input接收到用户输入的所有内容都叫字符串
print( type(name) )
print( type(age) )
print( type(height) )

# 输出
print(f'用户输入的名称为:{name} 输入的年龄为:{age} 输入的身高为:{height}')