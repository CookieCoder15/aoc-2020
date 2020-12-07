file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


class Bag:
    def __init__(self, adj, color, bags, quantity):
        self.adj = adj
        self.color = color
        self.bags = bags
        self.quantity = quantity


def process_data():
    bags = []
    for i in content:
        rule = i.split(" ")
        quantity = 1
        adj = rule[0]
        color = rule[1]
        contains = []
        if rule[4] != "no":
            x = 4
            while x < len(rule):
                cont_quantity = int(rule[x])
                cont_adj = rule[x+1]
                cont_color = rule[x+2]
                cont_contains = ["fill_me"]
                contains.append(
                    Bag(cont_adj, cont_color, cont_contains, cont_quantity))
                x += 4
        bags.append(Bag(adj, color, contains, quantity))
    for i in bags:
        fill_contains(i.bags, bags)
    return bags


def fill_contains(bags, all_bags):
    for x in bags:
        if x.bags == ["fill_me"]:
            for y in all_bags:
                if y.adj == x.adj and y.color == x.color:
                    x.bags = y.bags
                    break


def count_valid_bags(bags, adj, color, layer):
    amount = 0
    for x in bags:
        if layer != 0 and x.adj == adj and x.color == color:
            amount += 1
            break
        else:
            for y in x.bags:
                if y.adj == adj and y.color == color:
                    amount += 1
                else:
                    if count_valid_bags(y.bags, adj, color, layer+1) > 0:
                        amount += 1
                        break
    return amount


def sum_bags(bags, adj, color, initial_bag):
    amount = 0
    if initial_bag == None:
        for x in bags:
            if x.adj == adj and x.color == color:
                initial_bag = x
    for x in initial_bag.bags:
        amount += x.quantity + x.quantity * sum_bags(bags, adj, color, x)
    return amount


bags = process_data()
print(count_valid_bags(bags, "shiny", "gold", 0))
print(sum_bags(bags, "shiny", "gold", None))
