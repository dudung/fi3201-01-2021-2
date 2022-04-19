import math
from my_dict import *

# Print dictionary City
def printCity():
    print('City')
    for key in City:
        c = City[key]
        i = c['id']
        x = c['x']
        y = c['y']
    print(key, '  ', i, '  ', x, '  ', y, sep='')
    print()

# Print matrix Road
def printRoad():
    print('Road')
    for i in Road:
        for j in i:
            print(j, ' ', end='')
        print()
    print()

# Distance between two cities
def distance(c1, c2):
    x1 = City[c1]['x']
    y1 = City[c1]['y']
    x2 = City[c2]['x']
    y2 = City[c2]['y']

    dx = (x1 - x2)
    dy = (y1 - y2)
    dr = math.sqrt(dx * dx + dy * dy)

    return dr

# Check connection of two cities
def isconnected(c1, c2):
    id1 = City[c1]['id']
    id2 = City[c2]['id']

    road = Road[id1][id2]
    connected = bool(road)

    return connected

# Get fenotype from a chromosome
def getfenotype(chro):
    N = int(len(chro)/3)
    feno = ''
    for i in range(N):
        j = 3 * i
        genstr = chro[j:j+3]
        genint = int(genstr, 2)
        
        city = ''
        for key in City:
            id = City[key]['id']
            if genint == id:
                city = key
        
        feno = feno + city
    return feno

# Get genotype from a solution
def getgenotype(sol):
    geno = ''
    for key in sol:
        id = City[key]['id']
        idbin = '{0:03b}'.format(id)
        geno = geno + idbin
    
    return geno

# Get connections information in string
def getconnectionstr(sol):
    constr = ''
    for i in range(len(sol)):
        c1 = sol[i]
        if i < len(sol) - 1:
            c2 = sol[i+1]
            iscon = isconnected(c1, c2)
        
        if iscon:
            constr = constr + c1
            if i < len(sol) - 1:
                constr = constr + '--'
        else:
            constr = constr + c1
            if i < len(sol) - 1:
                constr = constr + '  '
    
    return constr

# Check whether a solution is valid
def isvalidsolution(sol):
    disconnect = 0
    for i in range(len(sol)):
        c1 = sol[i]
        if i < len(sol) - 1:
            c2 = sol[i+1]
            iscon = isconnected(c1, c2)
        
        if not iscon:
            disconnect = disconnect + 1
        
        valid = True
        if disconnect > 0:
            valid = False
        
        return valid

# Do crossover two chromosomes
def crossover(ch1, ch2, n):
    ch3a = ch1[0:n]
    ch4b = ch1[n:]
    
    ch4a = ch2[0:n]
    ch3b = ch2[n:]

    ch3 = ch3a + ch3b
    ch4 = ch4a + ch4b
    
    return [ch3, ch4]

# Calculate total distance from a solution
def totaldistance(sol):
    dist = 0
    num = len(sol)
    for city in range(num-1):
        dist += distance(sol[city], sol[city+1])

    return dist