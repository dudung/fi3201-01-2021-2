# visiting_cities.py
# Search order of visited cities using genetic algorithm
# 
# Sparisoma Viridi | https://github.com/dudung/cookbook
# 
# 20220412 Create this program.
#     1706 Finish a dictionary named City and print it.
#     1721 Finish a matrix named Road and print it.
#     1735 Add some references for future use.
#     2021 Finish distance function and print it.
#     2040 Finish isconnected function and print it.
#     2133 Finish getfenotype function and print it.
#     2155 Finish getgenotype function and print it.
#     2225 Finish getconnectionstr function and print it.
#     2234 Finish isvalidsolution function and print it.
#     2255 Finish crossover function and print it.
#     2311 Pause after try crossover for n = 0, .. 23.
# 20220413 Make it public.
#     0354 Test in OneCompiler.
#     0357 Share it to group of FI3201-01.
# 
# Refs
# 1. https://stackoverflow.com/a/3294899/9475509 dictionary for
# 2. https://stackoverflow.com/a/19084485/9475509 print matrix
# 3. https://stackoverflow.com/a/11266091/9475509 end of line
# 4. https://stackoverflow.com/a/8951047/9475509 circular index
# 5. https://stackoverflow.com/a/8928256/9475509 binary string
# 6. https://stackoverflow.com/a/10411108/9475509 int to binary
# 7. https://stackoverflow.com/a/2294502/9475509 chr pos in str


# Import necessary packages
import math


# City dictionary
City = {
  'A': {'id': 0, 'x': 2, 'y': 2},
  'B': {'id': 1, 'x': 4, 'y': 1},
  'C': {'id': 2, 'x': 7, 'y': 2},
  'D': {'id': 3, 'x': 6, 'y': 5},
  'E': {'id': 4, 'x': 4, 'y': 6},
  'F': {'id': 5, 'x': 5, 'y': 3},
  'G': {'id': 6, 'x': 2, 'y': 6},
  'H': {'id': 7, 'x': 1, 'y': 5},
}

print('City')
for key in City:
  c = City[key]
  i = c['id']
  x = c['x']
  y = c['y']
  print(key, '  ', i, '  ', x, '  ', y, sep='')
print()


# Road matrix
Road = [
  [0, 1, 0, 0, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 1, 0, 0],
  [1, 0, 0, 1, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0],  
]

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

print('distance')
print("AB", distance('A', 'D'))
print()


# Check connection of two cities
def isconnected(c1, c2):
  id1 = City[c1]['id']
  id2 = City[c2]['id']
  
  road = Road[id1][id2]
  connected = bool(road)
  
  return connected
 
print('isconnected')
print("AB", isconnected('A', 'B'))
print("AC", isconnected('A', 'C'))
print()


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

print('getfenotype')
chromose0 = '000001010011100101110111'
print('chromose', chromose0)
print('fenotype', getfenotype(chromose0))
chromose1 = '110111000100101011010001'
print('chromose', chromose1)
print('fenotype', getfenotype(chromose1))
print()


# Get genotype from a solution
def getgenotype(sol):
  geno = ''
  for key in sol:
    id = City[key]['id']
    idbin = '{0:03b}'.format(id)
    geno = geno + idbin
  
  return geno

print('getgenotype')
solution0 = 'GHAEFDCB'
print('solution', solution0)
print('genotype', getgenotype(solution0))
solution1 = 'ABCDHGFE'
print('solution', solution1)
print('genotype', getgenotype(solution1))
print()


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

print('getconnectionstr')
solution0 = 'BHAEFDCG'
print('solution', solution0)
print('connection ', getconnectionstr(solution0))
solution1 = 'GHAEFDCB'
print('solution', solution1)
print('connection ', getconnectionstr(solution1))
print()


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

print('isvalidsolution')
solution0 = 'BHAEFDCG'
print('solution', solution0)
print('valid ', isvalidsolution(solution0))
solution1 = 'GHAEFDCB'
print('solution', solution1)
print('valid ', isvalidsolution(solution1))
print()


# Do crossover two chromosomes
def crossover(ch1, ch2, n):
  ch3a = ch1[0:n]
  ch4b = ch1[n:]
  
  ch4a = ch2[0:n]
  ch3b = ch2[n:]
  
  ch3 = ch3a + ch3b
  ch4 = ch4a + ch4b
  
  return [ch3, ch4]


print('crossover')
chro0 = '111110000001010011100101'
chro1 = '110111000100101011010001'

feno0 = getfenotype(chro0)
print('fenotype0', feno0)
print('connection ', getconnectionstr(feno0))
print('valid ', isvalidsolution(feno0))
print()

feno1 = getfenotype(chro1)
print('fenotype1', feno1)
print('connection ', getconnectionstr(feno1))
print('valid ', isvalidsolution(feno1))
print()

print('chromosome0', chro0)
print('chromosome1', chro1)

# ok: n = 0-2, 6-8, 9, 22, 23
# problem: n = 19, 3-5, 10-12, 13-14, (15), (16, 17, 18), (19, 20, 21)
n = 5

print('crossover at', n)
[chro2, chro3] = crossover(chro0, chro1, n)
print('chromosome2', chro2)
print('chromosome3', chro3)
print()

feno2 = getfenotype(chro2)
print('fenotype2', feno2)
print('connection ', getconnectionstr(feno2))
print('valid ', isvalidsolution(feno2))
print()

feno3 = getfenotype(chro3)
print('fenotype2', feno3)
print('connection ', getconnectionstr(feno3))
print('valid ', isvalidsolution(feno3))
print()