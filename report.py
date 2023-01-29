def main(args):    
    products = get_products(args.product_master)
    print(products)

    sales = get_sales(args.sales)
    print(sales)

    teams = get_teams(args.team_map)
    print(teams)


def get_teams(path):
    mylist = []
    teams = open(path, "r")
    for t in teams:
        item = t.split(",")
        my_team = Team(item[0],item[1])
        mylist.append(my_team)
    mylist.pop(0)
    return mylist

def get_products(path):
    mylist = []
    products = open(path, "r")
    for p in products:
        item = p.split(",")
        my_product = Product(item[0],item[1],item[2],item[3])
        mylist.append(my_product)
    return mylist

def get_sales(path):
    mylist = []
    sales = open(path, "r")
    for s in sales:
        item = s.split(",")
        my_sales = Sale(item[0],item[1],item[2],item[3],item[4])
        mylist.append(my_sales)
    return my_sales
class Product:
    def __init__(self,id,name,price,lotsize):
        self.id = id
        self.name = name
        self.price = price
        self.lotsize = lotsize

class Team:
    def __init__(self,id,name):
        self.id = id
        self.name = name


class Sale:
    def __init__(self,sale_id,product_id,team_id,quantity,discount):
        self.sale_id = sale_id
        self.product_id = product_id
        self.team_id = team_id
        self.quantity = quantity
        self.discount = discount


import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t","--team-map",help="Path to the team map file", type=str)
parser.add_argument("-p","--product-master",help="Path to the product master file",type=str)
parser.add_argument("-s","--sales",help="Path to the sales file",type=str)
parser.add_argument("-tr","--team-report",help="Path to the team report",type=str)
parser.add_argument("-pr","--product-report",help="Path to the product report",type=str)
#parser.add_argument("-h","--help",help="Display help")

args = parser.parse_args()

main(args)




