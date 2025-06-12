import argparse

parse = argparse.ArgumentParser(description="Positional argparse")

parse.add_argument("echo", help="echos the given string.")

args = parse.parse_args()

print(args.echo)