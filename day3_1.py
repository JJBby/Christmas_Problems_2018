import re

path = 'day3.txt' # This needs to be the file you want to run REGEX on.


def file_parser(file):
    with open(file, 'r') as data:
        claim = list(map(lambda s: map(int, re.findall(r'-?\d+', s)), data))
    return claim


def parse(string):
    data = string
    claim = list(map(lambda s: map(int, re.findall(r'-?\d+', s)), data))
    return claim

def make_dic(grid):
    xy = dict()

    for i in range(len(grid)):
        for y in range(grid[i][3]):
            for x in range(grid[i][4]):
                h = grid[i][1] + 1
                w = grid[i][2] + 1
                try:
                    xy[str(h + y) + 'x' + str( w + x)] += 1 
                except KeyError:
                    xy[str(h + y) + 'x' + str(w + x)] = 1 
    count = 0
    for key, val in xy.items():
        if val > 1:
            count+=1
    return count


full = file_parser(path)
print(make_dic(full))


