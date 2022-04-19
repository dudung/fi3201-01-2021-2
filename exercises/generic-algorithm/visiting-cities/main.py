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
#import math    #imported in function.py
import my_function as f

print("AB", f.isconnected('A', 'B'))
print("AC", f.isconnected('A', 'C'))

a = f.distance('A', 'B')
b = f.distance('B', 'C')
print(a)

solution0 = 'ABA'
tot = f.totaldistance(solution0)
print(tot)