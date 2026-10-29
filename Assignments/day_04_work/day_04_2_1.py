"""
编写一个程序，让用户输入商品原价和购买数量，然后计算总金额并应用以下折扣规则：

- 购买数量为1-2件，无折扣
- 购买数量为3-5件，享受9折优惠
- 购买数量超过5件，享受8折优惠
要求：

1. 使用input()获取用户输入的商品原价和数量
2. 将输入转换为适当的数值类型
3. 使用if判断应享受几折
4. 使用算术运算符计算折扣后的总金额
5. 使用格式化输出（f-string）显示结果，保留2位小数

"""
price = float(input("请输入您要买的商品原价："))
num = int(input("请输入您要买的商品数量："))


if price < 0 or num <= 0:
    print("输入有误！商品原价和购买数量必须大于 0。")
else:
    total_price = num * price

    if 1 <= num <= 2:
        discount_info = "无折扣"
    elif 3 <= num <= 5:
        total_price *= 0.9
        discount_info = "享受9折优惠"
    else:
        total_price *= 0.8
        discount_info = "享受8折优惠"

    print(f"您购买了 {num} 件商品，{discount_info}，最终总价为：{total_price:.2f} 元")

