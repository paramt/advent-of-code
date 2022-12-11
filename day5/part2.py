line = input().split(" ")
crates = [  ["Z", "V", "T", "B", "J", "G", "R"],
            ["L", "V", "R", "J"],
            ["F", "Q", "S"],
            ["G", "Q", "V", "F", "L", "N", "H", "Z"],
            ["W", "M", "S", "C", "J", "T", "Q", "R"],
            ["F", "H", "C", "T", "W", "S"],
            ["J", "N", "F", "V", "C", "Z", "D"],
            ["Q", "F", "R", "W", "D", "Z", "G", "L"],
            ["P", "V", "W", "B", "J"]]

while line != ['0']:
    num, from_pos, to_pos = int(line[1]), int(line[3]), int(line[5])

    crates[to_pos-1] = crates[from_pos-1][:num] + crates[to_pos-1]
    crates[from_pos-1] = crates[from_pos-1][num:]

    line = input().split(" ")

# for crate in crates:
#     print(crate)


for crate in crates:
    print(crate[0])



"QZFJRWHGS"