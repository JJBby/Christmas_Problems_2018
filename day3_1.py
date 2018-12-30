import re

path = '/home/j/Desktop/Code_Projects/adventofcode/day3.txt' # This needs to be the file you want to run REGEX on.


def file_parser(file):
    with open(file, 'r') as data:
        claim = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
    return claim


def parse(string):
    data = string
    claim = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
    return claim

def make_dic(grid):
    xy = dict()
    
    for i in range(len(grid)):
        for y in range(grid[i][3]):
            for x in range(grid[i][4]):
                h = grid[i][1]
                w = grid[i][2]
                try:
                    xy[str(h + y) + 'x' + str( w + x)] += 1 
                except KeyError:
                    xy[str(h + y) + 'x' + str(w + x)] = 1 
    good = []
    for i in range(len(grid)):

        claim = grid[i][0]
        needed = grid[i][4] * grid[i][3]
        count = 0

        for y in range(grid[i][3]):
            for x in range(grid[i][4]):
                h = grid[i][1]
                w = grid[i][2]
                count += xy[str(h + y) + 'x' + str( w + x)]
        if count == needed:
            good.append(claim)


    # count = 0                # Code used for prob 1 of the day
    # for _, val in xy.items():
    #     if val > 1:
    #         count+=1


    return good


full = file_parser(path)
print(make_dic(full))