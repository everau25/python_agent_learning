# ## 4- 完成用户登录案例(for)
#
# 案例：用for循环实现用户登录
#
# ① 输入用户名和密码
#
# ② 判断用户名和密码是否正确（username='admin'，password='admin888'）
#
# ③ 登录仅有三次机会，超过3次会报错
#
#
#
# 分析：用户登陆情况有3种:
#
# ① 用户名错误(此时便无需判断密码是否正确)  -- 登陆失败
#
# ② 用户名正确 密码错误 --登陆失败
#
# ③ 用户名正确 密码正确 --登陆成功



for i in range(3):
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    if username == "admin" and password == "admin888":
        print("登录成功")
        break
    elif username != "admin":
        print(f"用户名错误，登录失败,你还剩{2-i}次机会")
    else:
        print(f"用户名正确，密码错误，登录失败,你还剩{2-i}次机会")