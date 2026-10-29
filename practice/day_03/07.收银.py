'''
    输入 商品的名称  商品的价格 商品的数量
    输出: 应付款总价
'''
# 商品的名称
product_name = input("请输入商品的名称:")
product_price = input("请输入商品的价格:")
product_num = input("请输入商品的数量:")

# 先将字符串转换成数字类型 再进行计算   类型(变量)
product_price = float(product_price)
product_num = int(product_num)
# 商品的总价格计算: 数量*单价   报错: 字符串不可以进行计算
total_price = product_price * product_num

print(f"您购买了{product_name},商品的价格是{product_price}元,数量是{product_num}个,您应付的价格为:{total_price}元")