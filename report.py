import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t","--team-map",help="Path to the team map file", type=str)
parser.add_argument("-p","--product-master",help="Path to the product master file",type=str)
parser.add_argument("-s","--sales",help="Path to the sales file",type=str)
parser.add_argument("-tr","--team-report",help="Path to the team report",type=str)
parser.add_argument("-pr","--product-report",help="Path to the product report",type=str)
parser.add_argument("-h","--help",help="Display help",type=str)

args = parser.parse_args()

def main(args):
    team_map_file = ''
    product_master_file = ''
    sales_file = ''

    print(args)