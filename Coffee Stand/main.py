from math import ceil
from validate import valid_response


def product_choice() -> str:
    print("What drink you want?")
    print("  1) Tea")
    print("  2) House Coffee")
    print("  3) Premium Blend Coffee")

    return valid_response(
        returns={
            1: "Tea",
            2: "House Coffee",
            3: "Premium Blend Coffee"
        },
        error_responses=[
            "Sorry, we doesn't provide this drink at the moment."
        ]
    )


def product_size() -> int:
    print("What size you want?")
    print("  1) Short  (8  oz)")
    print("  2) Tall   (12 oz)")
    print("  3) Grande (16 oz)")

    return valid_response(
        returns={
            1: 8,
            2: 12,
            3: 16
        },
        error_responses=[
            "Sorry, we doesn't provide this size at the moment."
        ]
    )


def cost(choice: str, size: int) -> float:
    prices = {
        "Tea": 3.,
        "House Coffee": 3.5,
        "Premium Blend Coffee": 4.
    }
    size_factors = {
        8: 1,
        12: 1.25,
        16: 1.5
    }

    return prices[choice] * size_factors[size]


def charity(price: float) -> float:
    is_decent_human = input("Do you want to support a charity by rounding up the change? > ").lower()
    if is_decent_human == "yes" or is_decent_human == "y":
        return ceil(price)
    return price


if __name__ == '__main__':
    # Greeting
    print("Welcome to Half-Decent Coffee Stand. What do you want?")
    print("You total is ${:.2f}".format(charity(cost(product_choice(), product_size()))))
