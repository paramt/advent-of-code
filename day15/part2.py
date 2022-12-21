SIZE = 4*1000*1000

class Pos: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


# Parse input and store sensor info
sensors = [] # list of (sensor Pos, radius)
line = input()

while line != "0":
    sensor = Pos(int(line.split("=")[1].split(",")[0]), int(line.split("=")[2].split(":")[0]))
    beacon = Pos(int(line.split("=")[3].split(",")[0]), int(line.split("=")[4]))

    d1 = sensor.distance(beacon)
    sensors.append((sensor, d1))

    line = input()

# Check every row for gap in sensor coverage
for y in range(SIZE):

    # Add covered ranges to a list
    covered = []

    for sensor in sensors: 
        s, d1 = sensor
        d2 = abs(y - s.y)
        spread = d1-d2

        if spread >= 0: covered.append((s.x - spread, s.x + spread))

    covered.sort(key=lambda x: x[0])

    # Check if there's a gap in the covered ranges
    prev = covered[0]

    if prev[0] > 0: 
        print(f"x: 0, y: {y}")
        print("Tuning frequency: ", y)

    for i in range(len(covered)-1):
        if prev[1] < covered[i][1]:
            prev = covered[i]

        curr = covered[i+1]

        if curr[0] >= prev[1] + 1:
            x = prev[1]+1
            print(f"x: {x}, y: {y}")
            print("Tuning frequency: ", x*SIZE + y)
            exit()

    # Print progress
    if y % 10000 == 0:
        print(f"Checking row {y}/{SIZE}", end="\r")


