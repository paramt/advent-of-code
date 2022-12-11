
sack = input()
priority_sum = 0

while sack != "0":
    first_half = sack[:len(sack)//2]
    second_half = sack[len(sack)//2:] # make this a set

    for item in first_half:
        if item in second_half:
            priority = ord(item) - 96
            if priority <= 0: priority += 58
            priority_sum += priority
            break

    sack = input()



print(priority_sum)