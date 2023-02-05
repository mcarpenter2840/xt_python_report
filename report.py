def main(args):    
    products = get_products(args.product_master)
    myproducts = ProductList()
    for x in products:
        #print(x.getproducts())
        myproducts.addproduct(x)

    sales = get_sales(args.sales)    
    # for x in sales:
    #    print(x.getsale())
    
    teams = get_teams(args.team_map)
    for x in teams:        
        for s in sales:
            if s.team_id == x.id:
                x.addsales(s)
        #print(x.getsales())
        TeamReport(x,myproducts).getreport()
    
    for p in myproducts.getproducts():
        report = ProductReport(p,sales)
        report.printreport()

    
def get_teams(team_path):
    mylist = []
    teams = open(team_path, "r")
    for t in teams:
        item = t.strip().split(",")
        my_team = Team(item[0],item[1])        
        mylist.append(my_team)
    mylist.pop(0)
    return mylist

def get_products(path):
    mylist = []
    products = open(path, "r")
    for p in products:
        item = p.strip().split(",")
        my_product = Product(item[0],item[1],item[2],item[3])
        mylist.append(my_product)
    return mylist

def get_sales(path):
    mylist = []
    sales = open(path, "r")
    for s in sales:
        item = s.strip().split(",")
        my_sales = Sale(item[0],item[1],item[2],item[3],item[4])
        mylist.append(my_sales)
    return mylist
class Product:
    def __init__(self,id,name,price,lotsize):
        self.id = id
        self.name = name
        self.price = float(price)
        self.lotsize = int(lotsize)
    
    def getlotprice(self):
        return int(self.lotsize) * float(self.price)

    def getproducts(self):
        print(f"id:  {self.id}\tname:  {self.name}\tprice:  {self.price}\tlotsize:  {self.lotsize}\ttotal:  {self.getlotprice()}")

class ProductList:
    def __init__(self):
        self.product_list = []
    
    def addproduct(self,product):
        self.product_list.append(product)
    
    def getproduct(self,id):
        for p in self.product_list:
            if p.id == id:
                return p
    
    def count(self):
        return len(self.product_list)

    def getproducts(self):
        return self.product_list

class Team:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.sales_list = []
    
    def getteam(self):
        print(f"id:  {self.id}\tname:  {self.name}")
    
    def getsales(self):
        print(self.name)
        for x in self.sales_list:
            x.getsale()
    
    def addsales(self,mysale):
        self.sales_list.append(mysale)

class Sale:
    def __init__(self,sale_id,product_id,team_id,quantity,discount):
        self.sale_id = sale_id
        self.product_id = product_id
        self.team_id = team_id
        self.quantity = int(quantity)
        self.discount = float(discount)
    
    def getsale(self):
        print(f"sale_id:  {self.sale_id}\tproduct_id:  {self.product_id}\tteam_id:  {self.team_id}\tqty:  {self.quantity}\tdiscount:  {self.discount}")

class TeamReport:
    def __init__(self, myteam, product_list):
        self.team = myteam
        self.prod_list = product_list
        self.grossrevenue = 0
    
    def calcgross(self):
        for s in self.team.sales_list:
            p = self.prod_list.getproduct(s.product_id)
            self.grossrevenue += int(s.quantity) * p.getlotprice()
    
    def getreport(self):
        self.calcgross()
        print(f"Team:  {self.team.name}\tGross:  {self.grossrevenue}")

class ProductReport:
    def __init__(self,product,sales):
        self.id = product.id
        self.name = product.name
        self.grossrevenue = 0
        self.totalunits = 0
        self.discountcost = 0

        for s in sales:
            if s.product_id == product.id:
                self.addsale(s,product)
    
    def addsale(self,sale,product):
        self.grossrevenue += (sale.quantity * product.getlotprice()) * (1 + sale.discount)
        self.totalunits += sale.quantity
        self.discountcost += product.getlotprice() * sale.discount
    
    def printreport(self):
        print(f"Name:  {self.name}\t{self.grossrevenue}\tTotalUnits:  {self.totalunits}\tDiscountCost:  {self.discountcost}")


### Main Logic ###

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t","--team-map",help="Path to the team map file", type=str,default=".\\files\\team_map.csv")
parser.add_argument("-p","--product-master",help="Path to the product master file",type=str,default=".\\files\\product_master.csv")
parser.add_argument("-s","--sales",help="Path to the sales file",type=str,default=".\\files\\sales.csv")
parser.add_argument("-tr","--team-report",help="Path to the team report",type=str)
parser.add_argument("-pr","--product-report",help="Path to the product report",type=str)
#parser.add_argument("-h","--help",help="Display help")

args = parser.parse_args()

main(args)




