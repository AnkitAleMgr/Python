import argparse

parser = argparse.ArgumentParser(description="Square of number.")

parser.add_argument("-s", "--square", help="square of given number", type= int, required= True, choices=[0,1,2,3,4,5,6,7,8,9])
parser.add_argument("-v", "--verbose", help="give more detail", action="store_true")

args = parser.parse_args()

if args.verbose:
    print(f"{args.square} square is {args.square**2}")
else:
    print(args.square**2)