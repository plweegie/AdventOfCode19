# Original puzzle:
# https://adventofcode.com/2019/day/3


def get_wire_breakpoints(input):
    wire_pos = 0
    direction_dict = {
        "D": (0, -1),
        "U": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }
    for i in input:



def main():
    wire1_pos = 0
    wire2_pos = 0
    line1 = []
    line2 = []

    with open("puzzle3.txt", "r") as file:
        content = file.readlines()
        line1 = [ x for x in content[0].split(',') ]
        line2 = [ x for x in content[1].split(',') ]
    
    wire1 = get_wire_breakpoints(line1)
    wire2 = get_wire_breakpoints(line2)

if __name__ == "__main__":
    main() 