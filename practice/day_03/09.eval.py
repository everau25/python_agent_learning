
str = 1 + 1  # 计算
print(str)

#str = 1+ "1"  报错 整型和字符串不可以相加
#print(str)

str = "1" + "1"  # 字符串拼接
print(str)

str = eval( "1" + "1" ) # 没有变化  执行的效果 "1"+"1" = 11   eval(11) -> 输出11
print(str)

# eval 可以将一个字符串变成可执行的代码片段
str = '1+1'
str = eval('1+1') # 整个结果就是 '1+1'  eval('1+1') -> 计算 1+1的结果
print(str)

