input_string = "2 T18 WELDER 77 WAYNE WELD BROKE ON CART - UNABLE TO MOVE"
parts = input_string.split(' ')
part_1 = parts[0]
part_2 = parts[1]
part_3 = parts[3]
part_4 = parts[4]
part_5 = ' '.join(parts[5:])

output_string = "{}@{} {} {} {}".format(part_1, part_2, part_3, part_5, "SEE " + part_4)
