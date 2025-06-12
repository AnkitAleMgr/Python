import argparse

parser = argparse.ArgumentParser(description="Square of one digit number.")

parser.add_argument("-s", "--square", help="square of given number", type= int, choices=[0,1,2,3,4,5,6,7,8,9], default= 5, nargs = "?") #required = True
parser.add_argument("-v", "--verbose", help="give more detail", action="count", required = True, )

args = parser.parse_args()

if args.verbose == 0:
    print(args.square ** 2)
elif args.verbose == 1:
    print(f"{args.square} square is {args.square**2}")
elif args.verbose == 2:
    print(f"{args.square} square is : {args.square**2}")
else:
    print("Invalid varbose")
    