import time

start = time.time()

first = input()

priority_sum = 0

while first != "0":
    second = set(input()) # make these sets
    third = set(input())

    for item in first:
        if item in second and item in third:
            priority = ord(item) - 96
            if priority <= 0: priority += 58
            priority_sum += priority
            break

    first = input()
    

print(priority_sum)

end = time.time()

print(end - start)