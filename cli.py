import argparse
from dreamcolor import Light

# Args
parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("--port", type=int)
parser.add_argument("--dim",  type=int, choices=range(0, 11),  metavar="0-10")
parser.add_argument("-r",     type=int, choices=range(0, 256), metavar="0-255")
parser.add_argument("-g",     type=int, choices=range(0, 256), metavar="0-255")
parser.add_argument("-b",     type=int, choices=range(0, 256), metavar="0-255")
args = parser.parse_args()

# Create
light = Light(args.ip, args.port or 5000)

# Dim
if args.dim != None:
    light.dim(args.dim)

# RGB
if args.r != None and args.g != None and args.b != None:
    light.rgb(args.r, args.g, args.b)
elif args.r != None or args.g != None or args.b != None:
    print("Error: You need to supply all RGB arguments!")
    exit()
