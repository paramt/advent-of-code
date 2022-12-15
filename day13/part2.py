from functools import cmp_to_key

def correct_order(left, right):
    if type(left) == list and type(right) == list: 
        for i in range(max(len(right), len(left))):
            if i >= len(left): return 1
            if i >= len(right): return -1 

            if correct_order(left[i], right[i]) == None: continue
            else: return correct_order(left[i], right[i])

    elif type(left) == list: 
        return correct_order(left, [right])

    elif type(right) == list: 
        return correct_order([left], right)
    
    elif left > right: return -1

    elif left < right: return 1

    return None

packets = []

while True:
    packet1 = eval(input())
    packet2 = eval(input())
    blank = input()

    packets.append(packet1)
    packets.append(packet2)

    if blank == "0": break 

packets.append([[2]])
packets.append([[6]])

packets.sort(key=cmp_to_key(correct_order), reverse=True)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))