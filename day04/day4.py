line = input()
total = 0

while line != "0":
    pair = line.split(",")

    if int(pair[0].split("-")[1]) >= int(pair[1].split("-")[0]) and int(pair[0].split("-")[0]) <= int(pair[1].split("-")[1]):
        total += 1
    elif int(pair[1].split("-")[1]) >= int(pair[0].split("-")[0]) and int(pair[1].split("-")[0]) <= int(pair[0].split("-")[1]):
        total += 1

    line = input()

print(total)

