from random import choice


def gen_order(flavors: dict) -> tuple:
    flavor: str = choice(list(flavors.keys()))
    if flavors[flavor]["stock"] > 0:  # We have stock left
        flavors[flavor]["stock"] -= 1
        flavors[flavor]["hit"] += 1
        return True, flavor
    else:  # We have none left
        flavors[flavor]["miss"] += 1
        return False, flavor


if __name__ == '__main__':
    flavors: dict = {}
    flavors_to_add = ["Vanilla", "Chocolate", "Cookies N'Cream", "Mint chocolate chip", "Chocolate Chip Cookie Dough"]
    for flavor in flavors_to_add:
        flavors[flavor] = {
            "stock": 10,
            "hit": 0,
            "miss": 0
        }

    for i in range(30):
        order_success, flavor_name = gen_order(flavors)
        print("Order {} is for {}".format(i + 1, flavor_name))
        if not order_success:
            print("Sorry! We're all out of {}".format(flavor_name))

        # Attempt Required Fun #5, buggy as counting changed order as failed order (technically doesn't count) and
        #   does not perform on repeated failed order (e.g Vanilla -> Vanilla). More ideal will be removing the flavor
        #   when it is out of stock or check beforehand.
        # success = False
        # while not success:
        #     success, flavor_name = gen_order(flavors)
        #     print("Order {} is for {}".format(i+1, flavor_name))
        #     if not success:
        #         print("Sorry! We're all out of {}".format(flavor_name))
        #         success, flavor_name = gen_order(flavors)
        #         print("Order {} is changed to {}".format(i+1, flavor_name))

    total_sold = sum(f['hit'] for f in flavors.values())
    total_miss = sum(f['miss'] for f in flavors.values())

    # Generate Summary
    print()
    print("===== SALES REPORT =====")
    print("Final Sales:")
    for name, flavor in flavors.items():
        if flavor['hit'] > 0:
            print("{}: {} Order{} ({:.1f}%)".format(name, flavor['hit'], "s" if flavor['hit'] > 1 else "",
                                                    flavor['hit'] / total_sold * 100))

    print()
    print("Missed Orders")
    if total_miss == 0:
        print("There're no missed orders.")
    else:
        for name, flavor in flavors.items():
            if flavor['miss'] > 0:
                print("{}: {} Order{}".format(name, flavor['miss'], "s" if flavor['miss'] > 1 else ""))

    # most_sold = []

    # List Version
    # for fid, sale in enumerate(sales):
    #     if sale == max(sales):
    #       most_sold.append(fid)
    # most_sold = [fid for fid, sale in enumerate(sales) if sale == max(sales)]

    # Dictionary Version
    # Find most popular, deal with duplicate later
    # m = max(f['hit'] for f in flavors.values())
    # Find all duplicate
    # for name, flavor in flavors.items():
    #     if flavor["hit"] == m:
    #         most_sold.append(name)

    # I know this is very complicated. Please reference those working prototype above.
    most_sold = [name for name, flavor in flavors.items() if flavor['hit'] == max(f['hit'] for f in flavors.values())]

    most_sold_text = most_sold[0]
    if len(most_sold) > 1:
        for i in most_sold[1:-1]:
            most_sold_text += ", {}".format(most_sold[i])
        most_sold_text += ", and {}".format(most_sold[-1])

    print()
    print(most_sold_text, end=" ")
    print("{} the most popular ice cream of choice.".format("was" if len(most_sold) == 1 else "were"))
    print("=======================")
