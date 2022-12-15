def correct_order(left, right):
    if type(left) == list and type(right) == list: 
        for i in range(max(len(right), len(left))):
            if i >= len(left): return True
            if i >= len(right): return False 

            if correct_order(left[i], right[i]) == None: continue
            else: return correct_order(left[i], right[i])

    elif type(left) == list: 
        return correct_order(left, [right])

    elif type(right) == list: 
        return correct_order([left], right)
    
    elif left > right: return False

    elif left < right: return True

    return None

x = 1
total = 0

while True:
    packet1 = eval(input())
    packet2 = eval(input())
    blank = input()

    if blank == "0": break 

    print(x, end=": ")
    print(correct_order(packet1, packet2))

    if correct_order(packet1, packet2): total += x
    
    x+= 1

print("\nTotal: ", end="")
print(total)