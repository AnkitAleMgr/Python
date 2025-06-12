import argparse # importing module name argsparse for CLI(Command Line Interface)

# Initilizing the ArgumentParer
parser = argparse.ArgumentParser(
    # giving discription and proper input structure
    description="A simple calculator that compute : x² + y² of any two user input.",
    usage = "python <path/filename.py> <first number> <second number> [-v | -vv]"
)

# adding arguments
parser.add_argument("first", help="First number", type= int)
parser.add_argument("second", help="second number", type= int)
parser.add_argument(
    "-v", "--verbose",
    help="provide more detail description. Use -v for a summary or -vv for detailed output.",
    action="count",
    default=0,
)

# parsing arguments and computing output
args = parser.parse_args()
output = args.first ** 2 + args.second ** 2

# logical section/ output section
match args.verbose:
    case 1:
        print(f"{args.first}² + {args.second}² = {output}")
    case 2:
        print(f"First number: {args.first}\nSecond number: {args.second}\nFormula: x² + y²\noutput: {output}")
    case _:
        print(output)
