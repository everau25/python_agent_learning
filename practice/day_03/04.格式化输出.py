name = '张三'
age = 18
height = 175
# print('我的名字是name') # 错误
# print('我的名字是'+name +'年龄是' + age +'身高是' + height) # 字符串拼接(纯字符串)
# 格式化: 字符串 加上 变量 = 某种特殊的格式   浮点型自带小数位
# 方案1 : 不常用
print("我的名字是:%s,年龄是:%d,身高是:%.1f" % (name,age,height)  )
# 方案2: format 不常用 {} 表示占位
print("我的名字是:{},年龄是:{},身高是:{}".format(name,age,height))
# 了解 掌握 必须会 面试...
# 方案3: 格式化
print(f"我的名字是:{name},年龄是:{age},身高是:{height}")
