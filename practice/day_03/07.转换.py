# 类型转换案例
# 需求: 请键盘录入一个商品名称, 商品的价格, 商品的数量, 输出:  您购买了 xxx , 商品的单价为xxx,您购买了xx个, 总价为 xxx
# 键盘录入： input('提示词')
# 注意： 通过键盘录入的内容， 其数据类型都是字符串
produce = input("请输入商品名称")
produce_price = float(input("请输入商品价格"))
produce_num = int(input("请输入商品数量"))
total_price = produce_price * produce_num
print(f'您购买了{produce},商品的单价为{produce_price}，你购买了{produce_num}件，商品总价为{total_price}')

