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

WORRY_LIMIT = 1

for monkey in monkeys:
    WORRY_LIMIT *= monkey["test"]

for r in range(10000):
    print(f"{r+1}/10000", end="\r")

    for i in range(len(monkeys)):
        monkey = monkeys[i]

        while len(monkey["items"]) != 0:
            item = monkey["items"][0]
            old = item
            worry = int(eval(str(item)+monkey["operation"]))
            monkey["inspections"] += 1

            if worry % monkey["test"] == 0: monkeys[monkey["iftrue"]]["items"].append(worry%WORRY_LIMIT)
            else: monkeys[monkey["iffalse"]]["items"].append(worry%WORRY_LIMIT)

            monkey["items"].pop(0)

inspections = [monkey["inspections"] for monkey in monkeys]
max1 = max(inspections)
inspections.remove(max1)
max2 = max(inspections)

print("\nlevel of monkey business: ", end="")
print(max1*max2)