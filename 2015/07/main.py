import sys

if len(sys.argv) != 2:
    print("You must provide input file as argument!")
    exit()

with open(sys.argv[1]) as file:
    content = file.read().strip()
    lines = content.splitlines()

# All connections
cons = {}

# Hacky, since python by default uses signed negation
def not_16bit(num):
    return num ^ 0xFFFF

# Store each connection as object, with its own cached output (once computed)
class Connection():
    def __init__(self, in1=None, in2=None, op=None):
        self.in1 = in1
        self.in2 = in2
        self.op = op
        self.out_cache = None

    def read_out(self):
        if self.out_cache: return self.out_cache

        # Direct signal
        if not self.op:
            self.out_cache = int(self.in1) if self.in1.isdigit() else cons[self.in1].read_out()
        
        # If operation is negation then we have only in1
        elif self.op == "NOT":
            self.out_cache = not_16bit(int(self.in1) if self.in1.isdigit() else cons[self.in1].read_out()) 

        # Other operations
        elif self.op == "AND":
            in1 = int(self.in1) if self.in1.isdigit() else cons[self.in1].read_out()
            in2 = int(self.in2) if self.in2.isdigit() else cons[self.in2].read_out()
            self.out_cache = in1 & in2

        elif self.op == "OR":
            in1 = int(self.in1) if self.in1.isdigit() else cons[self.in1].read_out()
            in2 = int(self.in2) if self.in2.isdigit() else cons[self.in2].read_out()
            self.out_cache = in1 | in2

        elif self.op == "LSHIFT":
            in1 = int(self.in1) if self.in1.isdigit() else cons[self.in1].read_out()
            in2 = int(self.in2) if self.in2.isdigit() else cons[self.in2].read_out()
            self.out_cache = in1 << in2

        elif self.op == "RSHIFT":
            in1 = int(self.in1) if self.in1.isdigit() else cons[self.in1].read_out()
            in2 = int(self.in2) if self.in2.isdigit() else cons[self.in2].read_out()
            self.out_cache = in1 >> in2
        
        return self.out_cache


def reset_all_connections():
    for c in cons.values():
        c.out_cache = None

def parse_connections(lines):
    for line in lines:
        first, name = line.split(" -> ")
        first = first.strip().split()
        in1, op, in2 = None, None, None
        if len(first) == 1:
            in1 = first[0]        # input is either connection name or signal value(digit)
        elif len(first) == 2:
            op, in1 = first       # in 2-arg input, its always NOT operation of input
        elif len(first) == 3:
            in1, op, in2 = first  # in 3-arg input, its always operation between two inputs

        cons[name] = Connection(in1, in2, op)


# Run initial line parser and create all connections
parse_connections(lines)

# PART 1:
# What signal is ultimately provided to wire a?
a_out = cons["a"].read_out()
print(f"Part1: {a_out}")

# PART 2:
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other
# wires (including wire a). What new signal is ultimately provided to wire a?
reset_all_connections()
cons["b"].in1 = str(a_out)
print(f"Part2: {cons['a'].read_out()}")
