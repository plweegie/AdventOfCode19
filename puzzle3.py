# Original puzzle:
# https://adventofcode.com/2019/day/3


def get_wire_breakpoints(input):
    wire_pos = (0, 0)
    result = [wire_pos]

    for i in input:
        wire_pos = (get_step_in_direction(wire_pos, 0, i), get_step_in_direction(wire_pos, 1, i))
        result.append(wire_pos)
    
    return result


def get_step_in_direction(wire_position, direction, directive):
    direction_dict = {
        "D": (0, -1),
        "U": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }
    return wire_position[direction] + (int(directive[1:]) * direction_dict[directive[0]][direction])


def get_line_segments(breakpoints):

    result = []

    for i in range(len(breakpoints) - 1):
        segment_startx = breakpoints[i][0]
        segment_starty = breakpoints[i][1]
        segment_endx = breakpoints[i+1][0]
        segment_endy = breakpoints[i+1][1]

        if segment_startx == segment_endx and segment_starty > segment_endy:
            segment_starty = breakpoints[i+1][1]
            segment_endy = breakpoints[i][1]
        
        if segment_starty == segment_endy and segment_startx > segment_endx:
            segment_startx = breakpoints[i+1][0]
            segment_endx = breakpoints[i][0]

        result.append((segment_startx, segment_starty, segment_endx, segment_endy))
    
    return result


def is_intersect(segment1, segment2):
    return segment1[0] <= segment2[2] and segment1[2] >= segment2[0] and segment1[1] <= segment2[3] and segment1[3] >= segment2[1]


def get_intersection_point_distance(segment1, segment2):
    intersect_x = 0
    intersect_y = 0

    if segment1[0] == segment1[2]:
        intersect_x = segment1[0]
    else:
        intersect_y = segment1[1]

    if segment2[0] == segment2[2]:
        intersect_x = segment2[0]
    else:
        intersect_y = segment2[1]

    return abs(intersect_x) + abs(intersect_y)


def main():
    line1 = []
    line2 = []
    intersections = []

    with open("puzzle3.txt", "r") as file:
        content = file.readlines()
        line1 = [ x for x in content[0].split(',') ]
        line2 = [ x for x in content[1].split(',') ]
    
    wire1 = get_wire_breakpoints(line1)
    wire2 = get_wire_breakpoints(line2)
    segments1 = get_line_segments(wire1)
    segments2 = get_line_segments(wire2)
    
    for s1 in segments1:
        for s2 in segments2:
            if is_intersect(s1, s2):
                intersections.append(get_intersection_point_distance(s1, s2))

    filtered_intersects = list(filter(lambda x: x > 0, intersections))
    filtered_intersects.sort()
    print(filtered_intersects[0])


if __name__ == "__main__":
    main() 