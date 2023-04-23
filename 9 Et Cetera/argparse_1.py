import argparse

parser = argparse.ArgumentParser(description="Print 'Meow' a number of times")
parser.add_argument("-n", help="Number of times to print 'Meow' (default: 1)", default=1, type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("Meow")