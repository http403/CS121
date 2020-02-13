import functions


if __name__ == '__main__':
    total = functions.purchase()
    sale_discount = functions.big_spender_discount(total)
    loyalty_discount = functions.loyalty_discount(total)
    coupon_discount = functions.coupon_discount(int(input("How many coupons you got? > ")))
    functions.print_summary(total, sale_discount, loyalty_discount, coupon_discount)