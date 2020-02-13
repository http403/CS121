from jinja2 import Template

from math import sqrt
from random import uniform


def purchase() -> float:
    """
    Simulated Purchase Action

    :return: amount spent
    """
    spent = uniform(200, 2000)
    print("You just spent ${:.2f} in the store!".format(spent))
    return spent


def big_spender_discount(price: float) -> float:
    """
    Bulk discount logic

    :param price: amount spent
    :return: percentage discount
    """
    if price < 250:
        return 0.05
    elif price < 500:
        return 0.1
    elif price < 1000:
        return 0.15
    elif price >= 1000:
        return 0.2
    return 0


def loyalty_discount(price: float) -> float:
    """
    Loyalty discount calculator
    This will break when one buy over $10,000. After that the company
    need to pay the customer for buy things. LOL.

    :param price: amount spent
    :return: percentage discount
    """
    return sqrt(price)/100


def coupon_discount(coupons: int) -> float:
    """
    Coupon discount calculator
    Again, this will bankrupt the company.

    :param coupons: The number of coupons to apply
    :return: percentage discount
    """
    return coupons * 0.005


def print_summary(total: float, bulk_discount: float, vip_discount: float, coupon_discount: float) -> None:
    bulk_save = total * bulk_discount
    loyalty_save = total * vip_discount
    coupon_save = total * coupon_discount
    saved = total - bulk_save - loyalty_save - coupon_save

    receipt = Template("""****** CUSTOMER DISCOUNT SUMMARY ******
---------------------------------------
Total purchase amount:       $ {{ "%.2f"|format(total) }}
{{ bulk_discount|round|int }} % Discount:               -$ {{ "%.2f"|format(bulk_save) }}
Loyalty Discount:           -$ {{ "%.2f"|format(loyalty_save) }}
Coupon Discount:            -$ {{ "%.2f"|format(coupon_save) }}
---------------------------------------
TOTAL AFTER DISCOUNT         $ {{ "%.2f"|format(discounted_total) }}
---------------------------------------
You Saved                    $ {{ "%.2f"|format(saved) }}
---------------------------------------
    """)

    print(receipt.render(
        total=total,
        bulk_discount=bulk_discount*100,
        bulk_save=bulk_save,
        loyalty_save=loyalty_save,
        coupon_save=coupon_save,
        discounted_total=saved,
        saved=total - saved
    ))
