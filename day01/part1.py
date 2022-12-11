line = input()
highest = [0, 0, 0]

while line != "0":
    total = int(line)
    calories = input()

    while calories != "":
        total += int(calories)
        calories = input()

    if total > min(highest):
        highest.sort(reverse=True)
        highest.pop()
        highest.append(total)

    line = input()

print(highest)
print(sum(highest))