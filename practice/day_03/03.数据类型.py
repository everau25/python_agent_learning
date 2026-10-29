"""
    使用type(变量) 判断变量的类型
    当三个双引号和三个单引号 单独出现的时候 表示注释
    当三个双引号和三个单引号 赋值给了某个变量的时候  表示字符串 应用再多行文本的时候
    注意事项:中间不可以拼接三个单引号或者双引号
"""

# 数字
# 值: int 整型
a = 10
print(a , type(a) )
# 值: float  浮点型
b = 10.1
print(b , type(b) )

print("--------------------------------------------")
# 布尔 : boolean
# 值 : True  False
flag1 = True
print(flag1 , type(flag1) )
flag2 = False
print(flag2 , type(flag2) )
print("--------------------------------------------")
# 字符串
# 单引号  '内容'
str1 = ('张三')
# 双引号  "内容"
str2 = "张三"
# 三引号  '''内容 '''      """内容"""
str3 = """张

三"""
str4 = '''张!@#$%^三'''
print(str1 , type(str1) )
print(str2 , type(str2) )
print(str3 , type(str3) )
print(str4 , type(str4) )

print("---------------------------------------------")
'''
代码自上而下运行的 , 变量本身没有数据类型 , 所有的数据类型取决于 字面量
变量的定义 会覆盖的(变量名称一致的时候 后续的内容 会覆盖之前的内容)
建议 : 书写变量的时候 一定要见名知意
'''
name = 'zhangsan'
print(name , type(name))
# isinstance(参数1,参数2)  判断参数1 是不是参数2的数据类型  int float boolean string
print( isinstance(name , str) ) # 输出True
print( isinstance(name , int) ) # 输出False
name=18
print(name , type(name))
name= True
print(name , type(name))
