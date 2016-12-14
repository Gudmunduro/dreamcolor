import argparse
from dreamcolor import Light

# Args
parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("--port", type=int)
parser.add_argument("--broadcast", action="store_true")
parser.add_argument("action", choices=["on", "off", "dim", "rgb"])
parser.add_argument("values", nargs=argparse.REMAINDER, type=int)
args = parser.parse_args()

# Create
light = Light(args.ip, args.port or 5000, args.broadcast)

# On/Off
if args.action == "on":
    light.on()
elif args.action == "off":
    light.off()

# Dim
elif args.action == "dim":
    if len(args.values) != 1 or not 0 <= args.values[0] <= 10:
        print("Error: You need to supply a value 0-10")
        exit()

    light.dim(args.values[0])

# RGB
elif args.action == "rgb":
    if len(args.values) != 3 or not all(0 <= v <= 255 for v in args.values):
        print("Error: You need to supply three values 0-255")
        exit()

    light.rgb(args.values[0], args.values[1], args.values[2])
