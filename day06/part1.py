line = input()

for i, char in enumerate(line[14:]):
    marker = line[i:i+14]

    repeating = False
    for c in marker:
        if marker.count(c) > 1:
            repeating = True

    if not repeating:
        print(i+14)
        print(marker)
        exit()
    
