filesystem = {"ok": {}}
cd = []


def add_dir(cd, dir):
    if len(cd) == 0:
        return {dir: {}}

    else:
        first = cd.pop(0)

        return {first: add_dir(cd, dir)}



filesystem.update(add_dir(["test", "two", "three"], "param"))

print(filesystem)

filesystem.update({"test": filesystem.update({"two": filesystem.update({"three": "param"})})})



cd = ["test", "two", "three"]
dir = "param"

filesystem = {'test': {'two': {'three': {'param': {}}}, "teee": {}} }