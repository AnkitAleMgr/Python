import argparse

parse = argparse.ArgumentParser()
parse.add_argument("number1", help="first number", type= int)
parse.add_argument("number2", help="second number", type= int)
parse.add_argument("operation", help="operation", choices=["add", "subtract", "multiply"])

args = parse.parse_args()

result = None

result= args.number1 + args.number2 if args.operation == "add" else args.number1 - args.number2 if args.operation == "subtract" else args.number1 * args.number1

print("Result:",result)