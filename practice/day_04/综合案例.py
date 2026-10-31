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
# ③ 用户名正确 密码正确 --登陆成功 break


# for i in range(3):
#     username = input('请输入用户名')
#     password = input('请输入密码')
#     if username == 'admin' and password == 'admin888':
#         print('登录成功')
#         break
#     elif username != 'admin':
#         print('用户名错误',end='')
#     else:
#         print('密码错误',end='')
#     left = 3 - i -1
#     if left > 0:
#         print(f'，还剩{left}次机会')
#     else:
#         print('错误次数过多，已锁定账户')



# for循环做99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}*{i}={i * j}", end="\t")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print()
# for i in range(1, 6):         # 管5行
#     for j in range(1,6):     # 管每行固定5个
#         print("*", end=" ")   # 打星星
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# for i in range(1,9):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={j*i}',end='\t')
#     print()

#  正三角形案例
'''
    *
   ***
  ******
 *********
************
'''
# for i in range(1,6):
#      for j in range(6-i):
#          print(' ',end='')
#      for k in range(i*2 - 1):
#          print('*',end='')
#      print()

#  数字阶梯
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

#  平行四边形
# for i in range(1,6):
#     for j in range(6-i):
#         print(' ',end='')
#     for j in range(6):
#         print('*',end='')
#     print()

#  续99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={j*i}',end='\t')
#     print()

#  倒99乘法表
# for i in range(1,10):
#     for j in range(10-i):
#         print(f'{j+1}*{10-i}',end='\t')
#     print()

#  倒正三角形
# for i in range(1,6):
#     for j in range(i-1):
#         print(' ',end='')
#     for k in range(6-i):
#         print('* ',end='')
#     print()