# 类型(变量)   float int str

# str - >  float
a = '175.5'
b = float(a)
print( type(b) , b )

# str - >  int
a = '175'
b = int(a)
print( type(b) , b )

# int  - > str
a = 175
b = str(a)
print( type(b) , b )

# int - >  float
a = 175
b = float(a)
print( type(b) , b )



# float - > str
a = 175.5
b = str(a)
print( type(b) , b )

# float - > int
a = 175.5
b = int(a)
print( type(b) , b )


print("------------------------------------------------")
# 注意: 字符串如果直接转换成整型 有可能会报错 字符串转换成整型的时候 不能有小数位
# 解决方案: 先将字符串转换float  再将float转换成int  保留整数位
a = '175.5'
b = int(  float(a)  )
print( type(b) , b )