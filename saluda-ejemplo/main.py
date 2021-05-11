import argparse
import sys
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Create the parser
parser = argparse.ArgumentParser(
    prog="Welcome CLI", description="A simple CLI welcome you"
)
# Add the flag
parser.add_argument("--name", type=str, help="Get the name to say hello")
# Parse the args
args = parser.parse_args()

# Validate the args
if args.name:
    # Print if exists
    print(Fore.GREEN + f"Welcome {args.name} to Sendero Tecnológico")
else:
    # Exit output
    print(Fore.RED + "Error need a argument")
    sys.exit(1)
