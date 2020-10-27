import argparse
import os
import contextlib
from src.core import run

parser = argparse.ArgumentParser(description="Reads file data and outputs stats")
parser.add_argument("-v", "--verbose", action="store_true",help="increase output verbosity")
parser.add_argument("filepath")
args = parser.parse_args()

if __name__ == '__main__':
    if args.verbose:
        run(args)
    else:
        with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
            run(args)
