monkeys = []

for i in range(8):
    input()
    items = list(map(int, input()[18:].split(", ")))
    operation = input()[23:]
    test = int(input()[21:])
    iftrue = int(input()[29:])
    iffalse = int(input()[29:])
    input()

    monkeys.append({"items": items, "operation": operation, "test": test, "iftrue": iftrue, "iffalse": iffalse, "inspections": 0})


for r in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]

        while len(monkey["items"]) != 0:
            item = monkey["items"][0]
            old = item
            worry = int(eval(str(item)+monkey["operation"]))//3
            monkey["inspections"] += 1

            if worry % monkey["test"] == 0: monkeys[monkey["iftrue"]]["items"].append(worry)
            else: monkeys[monkey["iffalse"]]["items"].append(worry)

            monkey["items"].pop(0)


inspections = [monkey["inspections"] for monkey in monkeys]
max1 = max(inspections)
inspections.remove(max1)
max2 = max(inspections)
print("level of monkey business: ", end="")
print(max1*max2)