import sys
# this is a sample python file
print(sys.version)
if 5>2:
    print("5 is greater than 2")

finnian = "Finnian[PC]"
john = "John[PC]"
aubrey = "Aubrey[PS5]"
on = True    
off = False
if on == True:
    print("true")
if off != True:
    print("false")
for x in [finnian, john, aubrey]:
    print("PLAYER:", x)

def greet(player):
    print("Hello,", player)

greet(finnian)