line = input()

filesystem = {}
cd = []

def add_dir(path, fs, dir):
    if len(path) == 0:
        fs.update({dir: {}})

    else:
        first = path.pop(0)
        if first in fs: fs.update({first: add_dir(path, fs[first], dir)})
        else: fs.update({first: add_dir(path, {}, dir)})
    
    return fs

def add_file(path, fs, file, size):
    if len(path) == 0:
        fs.update({file: size})

    else:
        first = path.pop(0)
        if first in fs: fs.update({first: add_file(path, fs[first], file, size)})
        else: fs.update({first: add_file(path, {}, file, size)})
    
    return fs

while line != "0":
    # input
    if line[:1] == "$":
        if line[2:4] == "cd":
            if line[5:] == "..":
                cd.pop()
            elif line[5:] == "/":
                cd = []
            else: 
                cd.append(line[5:])

            # print(cd)
        
        elif line[2:4] == "ls":
            pass

        line = input()


    # output
    else:   
        output = line

        while output[:1] != "$" and output != "0":
            if output[:3] == "dir":
                filesystem.update(add_dir(cd.copy(), filesystem.copy(), output[4:]))

            else: 
                filesystem.update(add_file(cd.copy(), filesystem.copy(), 
                                  output.split(" ")[1], int(output.split(" ")[0])))

            # print(filesystem)

        
            output = input()

        line = output



def get_count(folder):
    s = 0

    for dir in folder: 
        
        if isinstance(folder[dir], int):
            s += folder[dir]
        elif folder[dir] == {}:
            pass
        elif isinstance(folder[dir], dict):
            s += get_count(folder[dir])
        else:
            s += folder[dir]

    return s


folders = []

def backtrack(fs):
    global total 

    if(21309880 + get_count(fs)) >= 30000000:
        folders.append(get_count(fs))

    for dir in fs: 
        if fs[dir] == {}:
            pass
        elif isinstance(fs[dir], dict):
            backtrack(fs[dir])
        else:
            pass

# print(filesystem)

(backtrack(filesystem))

print(min(folders))



