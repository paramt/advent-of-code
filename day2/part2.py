turn = input()
total_score = 0

while turn != "0":
    opponent, me = turn.split(" ")

    score = 0

    # rock
    if opponent == "A":
        if me == "X":
            score += 3 + 0
        elif me == "Y":
            score += 1 + 3
        elif me == "Z":
            score += 2 + 6

    elif opponent == "B":
        if me == "X":
            score += 1 + 0
        elif me == "Y":
            score += 2 + 3
        elif me == "Z":
            score += 3 + 6

    elif opponent == "C":
        if me == "X":
            score += 2 + 0
        elif me == "Y":
            score += 3 + 3
        elif me == "Z":
            score += 1 + 6

    total_score += score


    turn = input()

print(total_score)